from flask import Flask, request, jsonify
from flask_cors import CORS
from database import EvidenceDatabase
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

db = EvidenceDatabase()

@app.before_request
def init_db():
    """Initialize database on first request"""
    if not hasattr(app, 'db_initialized'):
        try:
            db.init_database()
            app.db_initialized = True
        except:
            pass

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/incidents', methods=['GET'])
def get_incidents():
    """Get all incidents with optional filters"""
    incident_type = request.args.get('type')
    category_id = request.args.get('category')
    
    try:
        incidents = db.get_incidents_by_category(
            category_id=int(category_id) if category_id else None,
            incident_type=incident_type
        )
        return jsonify(incidents)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/incidents', methods=['POST'])
def create_incident():
    """Create new incident"""
    data = request.json
    
    try:
        incident_id = db.add_incident(
            incident_date=data.get('incident_date'),
            category_id=data.get('category_id'),
            incident_type=data.get('incident_type'),
            title=data.get('title'),
            description=data.get('description'),
            ip_address=data.get('ip_address'),
            witnesses=data.get('witnesses'),
            evidence_notes=data.get('evidence_notes')
        )
        
        return jsonify({'id': incident_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    """Get incident with full details"""
    try:
        incident = db.get_incident_with_details(incident_id)
        if not incident:
            return jsonify({'error': 'Incident not found'}), 404
        return jsonify(incident)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    """Get timeline events"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    incident_type = request.args.get('type')
    
    try:
        timeline = db.get_timeline(
            start_date=start_date,
            end_date=end_date,
            incident_type=incident_type
        )
        return jsonify(timeline)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/timeline', methods=['POST'])
def create_timeline_event():
    """Create timeline event"""
    data = request.json
    
    try:
        event_id = db.add_timeline_event(
            event_date=data.get('event_date'),
            incident_id=data.get('incident_id'),
            event_title=data.get('event_title'),
            event_description=data.get('event_description'),
            event_type=data.get('event_type'),
            severity=data.get('severity')
        )
        
        return jsonify({'id': event_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/evidence', methods=['POST'])
def add_evidence():
    """Add evidence file"""
    data = request.json
    
    try:
        file_id = db.add_evidence_file(
            incident_id=data.get('incident_id'),
            file_name=data.get('file_name'),
            file_type=data.get('file_type'),
            file_path=data.get('file_path'),
            description=data.get('description'),
            uploaded_date=data.get('uploaded_date')
        )
        
        return jsonify({'id': file_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/connections', methods=['POST'])
def create_connection():
    """Create connection between incidents"""
    data = request.json
    
    try:
        connection_id = db.add_connection(
            incident_id_1=data.get('incident_id_1'),
            incident_id_2=data.get('incident_id_2'),
            relationship_type=data.get('relationship_type'),
            description=data.get('description')
        )
        
        return jsonify({'id': connection_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get category by name/type"""
    name = request.args.get('name')
    category_type = request.args.get('type', 'employment')
    
    if not name:
        return jsonify({'error': 'Name required'}), 400
    
    try:
        category_id = db.get_category_id(name, category_type)
        return jsonify({'id': category_id, 'name': name, 'type': category_type})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
