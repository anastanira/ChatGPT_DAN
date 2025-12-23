import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

class EvidenceDatabase:
    def __init__(self):
        self.conn_string = os.environ.get('DATABASE_URL')
        if not self.conn_string:
            raise ValueError("DATABASE_URL environment variable not set")
    
    def get_connection(self):
        return psycopg2.connect(self.conn_string)
    
    def init_database(self):
        """Initialize database schema"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            # Create categories table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL,
                    description TEXT,
                    category_type VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create incidents table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS incidents (
                    id SERIAL PRIMARY KEY,
                    incident_date DATE NOT NULL,
                    category_id INTEGER REFERENCES categories(id),
                    incident_type VARCHAR(50) NOT NULL,
                    title VARCHAR(255) NOT NULL,
                    description TEXT NOT NULL,
                    ip_address VARCHAR(45),
                    witnesses TEXT,
                    evidence_notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create evidence files table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS evidence_files (
                    id SERIAL PRIMARY KEY,
                    incident_id INTEGER REFERENCES incidents(id) ON DELETE CASCADE,
                    file_name VARCHAR(255) NOT NULL,
                    file_type VARCHAR(50),
                    file_path TEXT,
                    description TEXT,
                    uploaded_date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create timeline events table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS timeline_events (
                    id SERIAL PRIMARY KEY,
                    event_date TIMESTAMP NOT NULL,
                    incident_id INTEGER REFERENCES incidents(id) ON DELETE CASCADE,
                    event_title VARCHAR(255) NOT NULL,
                    event_description TEXT,
                    event_type VARCHAR(50) NOT NULL,
                    severity VARCHAR(20),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create connections/relationships table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS incident_connections (
                    id SERIAL PRIMARY KEY,
                    incident_id_1 INTEGER REFERENCES incidents(id) ON DELETE CASCADE,
                    incident_id_2 INTEGER REFERENCES incidents(id) ON DELETE CASCADE,
                    relationship_type VARCHAR(100),
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(incident_id_1, incident_id_2)
                )
            ''')
            
            # Create indexes for faster queries
            cur.execute('CREATE INDEX IF NOT EXISTS idx_incidents_date ON incidents(incident_date)')
            cur.execute('CREATE INDEX IF NOT EXISTS idx_incidents_type ON incidents(incident_type)')
            cur.execute('CREATE INDEX IF NOT EXISTS idx_incidents_category ON incidents(category_id)')
            cur.execute('CREATE INDEX IF NOT EXISTS idx_timeline_date ON timeline_events(event_date)')
            
            conn.commit()
            print("Database initialized successfully")
            
        except Exception as e:
            conn.rollback()
            print(f"Error initializing database: {e}")
            raise
        finally:
            cur.close()
            conn.close()
    
    def add_incident(self, incident_date, category_id, incident_type, title, description, ip_address=None, witnesses=None, evidence_notes=None):
        """Add a new incident"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute('''
                INSERT INTO incidents (incident_date, category_id, incident_type, title, description, ip_address, witnesses, evidence_notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            ''', (incident_date, category_id, incident_type, title, description, ip_address, witnesses, evidence_notes))
            
            incident_id = cur.fetchone()[0]
            conn.commit()
            return incident_id
            
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
    
    def add_timeline_event(self, event_date, incident_id, event_title, event_description, event_type, severity=None):
        """Add timeline event"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute('''
                INSERT INTO timeline_events (event_date, incident_id, event_title, event_description, event_type, severity)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            ''', (event_date, incident_id, event_title, event_description, event_type, severity))
            
            event_id = cur.fetchone()[0]
            conn.commit()
            return event_id
            
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
    
    def add_evidence_file(self, incident_id, file_name, file_type, file_path, description, uploaded_date):
        """Add evidence file record"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute('''
                INSERT INTO evidence_files (incident_id, file_name, file_type, file_path, description, uploaded_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            ''', (incident_id, file_name, file_type, file_path, description, uploaded_date))
            
            file_id = cur.fetchone()[0]
            conn.commit()
            return file_id
            
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
    
    def get_timeline(self, start_date=None, end_date=None, incident_type=None):
        """Get timeline events sorted by date"""
        conn = self.get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = '''
                SELECT t.*, i.title as incident_title, i.incident_type, c.name as category_name
                FROM timeline_events t
                JOIN incidents i ON t.incident_id = i.id
                LEFT JOIN categories c ON i.category_id = c.id
                WHERE 1=1
            '''
            params = []
            
            if start_date:
                query += ' AND t.event_date >= %s'
                params.append(start_date)
            
            if end_date:
                query += ' AND t.event_date <= %s'
                params.append(end_date)
            
            if incident_type:
                query += ' AND i.incident_type = %s'
                params.append(incident_type)
            
            query += ' ORDER BY t.event_date ASC'
            
            cur.execute(query, params)
            return cur.fetchall()
            
        finally:
            cur.close()
            conn.close()
    
    def get_incidents_by_category(self, category_id=None, incident_type=None):
        """Get incidents filtered by category or type"""
        conn = self.get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = '''
                SELECT i.*, c.name as category_name
                FROM incidents i
                LEFT JOIN categories c ON i.category_id = c.id
                WHERE 1=1
            '''
            params = []
            
            if category_id:
                query += ' AND i.category_id = %s'
                params.append(category_id)
            
            if incident_type:
                query += ' AND i.incident_type = %s'
                params.append(incident_type)
            
            query += ' ORDER BY i.incident_date DESC'
            
            cur.execute(query, params)
            return cur.fetchall()
            
        finally:
            cur.close()
            conn.close()
    
    def get_incident_with_details(self, incident_id):
        """Get full incident details with timeline, evidence, and connections"""
        conn = self.get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            # Get incident
            cur.execute('''
                SELECT i.*, c.name as category_name
                FROM incidents i
                LEFT JOIN categories c ON i.category_id = c.id
                WHERE i.id = %s
            ''', (incident_id,))
            incident = cur.fetchone()
            
            if not incident:
                return None
            
            # Get timeline events
            cur.execute('''
                SELECT * FROM timeline_events
                WHERE incident_id = %s
                ORDER BY event_date ASC
            ''', (incident_id,))
            timeline = cur.fetchall()
            
            # Get evidence files
            cur.execute('''
                SELECT * FROM evidence_files
                WHERE incident_id = %s
                ORDER BY uploaded_date DESC
            ''', (incident_id,))
            evidence = cur.fetchall()
            
            # Get connected incidents
            cur.execute('''
                SELECT ic.*, i2.title as connected_incident_title
                FROM incident_connections ic
                JOIN incidents i2 ON (
                    (ic.incident_id_1 = %s AND ic.incident_id_2 = i2.id) OR
                    (ic.incident_id_2 = %s AND ic.incident_id_1 = i2.id)
                )
            ''', (incident_id, incident_id))
            connections = cur.fetchall()
            
            return {
                'incident': incident,
                'timeline': timeline,
                'evidence': evidence,
                'connections': connections
            }
            
        finally:
            cur.close()
            conn.close()
    
    def add_connection(self, incident_id_1, incident_id_2, relationship_type, description=None):
        """Create connection between incidents"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            # Ensure incident_id_1 < incident_id_2 for unique constraint
            if incident_id_1 > incident_id_2:
                incident_id_1, incident_id_2 = incident_id_2, incident_id_1
            
            cur.execute('''
                INSERT INTO incident_connections (incident_id_1, incident_id_2, relationship_type, description)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (incident_id_1, incident_id_2) DO UPDATE
                SET relationship_type = %s, description = %s
                RETURNING id
            ''', (incident_id_1, incident_id_2, relationship_type, description, relationship_type, description))
            
            connection_id = cur.fetchone()[0]
            conn.commit()
            return connection_id
            
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
    
    def get_category_id(self, name, category_type):
        """Get or create category"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute('SELECT id FROM categories WHERE name = %s', (name,))
            result = cur.fetchone()
            
            if result:
                return result[0]
            
            # Create new category
            cur.execute('''
                INSERT INTO categories (name, category_type)
                VALUES (%s, %s)
                RETURNING id
            ''', (name, category_type))
            
            category_id = cur.fetchone()[0]
            conn.commit()
            return category_id
            
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
