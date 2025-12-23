# ChatGPT DAN Prompts Library & Reference

## Overview
An interactive web-based library documenting ChatGPT "DAN" (Do Anything Now) jailbreak prompts and AI safety measures. This project serves as:
- Educational resource about AI safety and jailbreak techniques
- Reference for understanding AI policy limitations
- Workplace compliance and verification framework
- Documentation of prompt evolution and tactics

## Project Structure
- `index.html` - Interactive web interface with prompt library (served on port 5000)
- `server.py` - Python HTTP server for hosting the library
- `README.md` - Original documentation with various DAN prompt versions
- `citation.cff` - Academic citation information

## Technical Setup
- **Language**: Python 3
- **Server**: Python's SimpleHTTPServer on port 5000
- **Frontend**: Interactive HTML5 with CSS Grid and JavaScript filtering
- **Database**: None
- **Workflow**: `web-server` running `python3 server.py`

## Features
### Interactive Prompt Library
- 100+ categorized prompts
- 8 Categories: Jailbreak Tactics, Workplace Policies, Verification Methods, Advanced Techniques, Safety Protocols, Historical Reference, Restricted Content
- Real-time search functionality
- Category filtering with active state tracking
- Click-to-expand prompt cards
- Statistics dashboard

### Categories Included
1. **Jailbreak Tactics & Methods** - Role-play, token systems, context injection, authority override
2. **Workplace Policies & Compliance** - Documentation standards, access control, acceptable use, monitoring, content review, incident response
3. **Verification Methods & Fact-Checking** - Source attribution, discussion validation, temporal accuracy, personal information verification, claim corroboration, fact-check integration
4. **Advanced Techniques** - DAN versions 12.0+, dual response formats, simulation frameworks, progressive boundary testing
5. **Safety Protocols** - Policy explanation, harm assessment, redirect strategies, transparency, defense-in-depth
6. **Historical Reference** - Evolution from DAN 6.0 through 13.0, tracking changes in jailbreak attempts
7. **Restricted Content** - Content filter detection, encoded messages, malicious use patterns, Anti-DAN responses

## How to Run
1. Workflow automatically starts via `python3 server.py`
2. Server listens on `0.0.0.0:5000`
3. Access via web browser to view interactive prompt library

## Key Features
- **Search**: Real-time search across all prompts
- **Filter**: Category-based filtering with active state indication
- **Statistics**: Display of total prompts, categories, and compilation year
- **Responsive Design**: Works on desktop and mobile devices
- **Professional UI**: Purple gradient theme with smooth interactions

## Evidence & Legal Tools Suite (Added Dec 23)

### Evidence Organizer (`/evidence.html`)
A comprehensive tool to document and organize:
- **Employment Violations**: Wage theft, visa discrimination, retaliation, contract coercion, HR bias
- **Security Incidents**: Unauthorized access, data exfiltration, network monitoring, IP tracking
- **Features**: 
  - Incident documentation with categorization
  - Automatic timeline generation
  - Formal complaint report generation (Employment, Security, Combined)
  - Export-to-file functionality for legal filing
  - Statistics dashboard

**Use Case**: Compile evidence for employment lawyers and law enforcement

### Legal Resources (`/resources.html`)
Guidance and resource directory including:
- **Government Agencies**: DOL, EEOC, FBI IC3, state labor boards
- **Legal Help**: Free consultants, legal aid organizations, bar association referrals
- **Cybersecurity**: Forensics firms, ISP abuse reporting, incident response
- **Checklists**: Documentation requirements, immediate security actions, what NOT to do
- **Contact Info**: How to file complaints, who to consult for each issue type

**Use Case**: Navigate complex legal and security response processes

## Critical Disclaimer
This project does **NOT** provide:
- DIY hacking tools or reverse shells
- Data exfiltration code
- Forensics tools (use professional firms)
- Legal advice (consult qualified lawyers)

Instead it provides:
- Evidence organization templates
- Professional resource directories
- Guidance for legitimate complaints
- Documentation frameworks for legal proceedings

## All Files in Project

### Application Files
- **index.html** - Original DAN prompts library (8 categories, 40+ prompts)
- **evidence.html** - Basic evidence organizer with timeline and reports
- **evidence-enhanced.html** - Advanced organizer with multi-format export (JSON, CSV, Markdown, PDF, TXT)
- **resources.html** - Legal and professional resource directory
- **server.py** - Python HTTP server (port 5000)
- **templates.md** - Pre-formatted templates for documentation

### Configuration Files
- **.replit** - Replit project configuration with workflows
- **.gitignore** - Python environment files exclusion
- **pyproject.toml** - Python project dependencies
- **uv.lock** - UV dependency lock file
- **citation.cff** - Academic citation information

### Documentation
- **README.md** - Original DAN prompt reference (from GitHub import)
- **replit.md** - Complete project documentation (this file)
- **main.py** - Placeholder Python file (can be repurposed)

## Multi-Format Export Capabilities

### Enhanced Evidence Organizer (`/evidence-enhanced.html`)
- **JSON Export**: Structured data for analysis
- **CSV Export**: Spreadsheet-compatible format for Excel/Google Sheets
- **PDF Export**: Professional document for filing
- **Markdown Export**: Formatted text for sharing
- **TXT Export**: Plain text report

### Template System (`/templates.md`)
Pre-formatted templates for:
- Wage theft documentation
- Work permit/visa discrimination
- Contract coercion incidents
- Unauthorized access incidents
- Data exfiltration suspicions
- Witness statements
- Evidence preservation checklists
- Key contacts reference

## Workflow Status
- **web-server**: Running on port 5000, serving all HTML files and static content
- All exports work client-side (no server processing needed for privacy)

## Usage Instructions

1. **Document Evidence**
   - Use `/evidence.html` or `/evidence-enhanced.html`
   - Add employment issues (wages, visa, contract, HR bias)
   - Add security incidents (IP addresses, unauthorized access)

2. **Export for Legal Use**
   - Enhanced version supports CSV, JSON, PDF, Markdown, TXT
   - All exports download directly to your computer
   - Data never leaves your browser

3. **Reference Templates**
   - View `/templates.md` for structured documentation format
   - Follow examples to organize evidence systematically
   - Use witness statement template for third-party accounts

4. **Share with Authorities/Lawyers**
   - Export as PDF for formal filing
   - Export as CSV for analysis/evidence tracking
   - Export as JSON for data processing
   - Export as TXT for email/printing

## Database System (NEW)

### PostgreSQL Database
- **Status**: Created and configured
- **Tables**: incidents, timeline_events, evidence_files, categories, incident_connections
- **Features**:
  - Organize incidents by date, type, and category
  - Track chronological timeline of events
  - Link related incidents
  - Store evidence file references

### API Server (Port 8000)
- **Endpoints**:
  - `/api/incidents` - Create/retrieve incidents
  - `/api/timeline` - Create/view timeline events
  - `/api/evidence` - Track evidence files
  - `/api/connections` - Link related incidents
  - `/api/categories` - Manage categories

### Web Interfaces

**Dashboard** (`/dashboard.html`) - Main database interface
- Add incidents and categorize them
- Create timeline events
- View real-time statistics
- Recent incidents and events list

**Timeline View** (`/timeline.html`) - Visual timeline
- Chronological view of all events
- Filter by date range and type
- Incident detail view
- CSV export of timeline

### Workflows
- **web-server** (port 5000): Serves HTML files
- **api-server** (port 8000): PostgreSQL API backend

## Usage Workflow

1. **Document Evidence** → Use Evidence Organizer or Dashboard
2. **Create Timeline Events** → Dashboard creates searchable timeline
3. **View Attack Pattern** → Timeline shows chronological flow
4. **Export for Legal Use** → CSV/JSON for lawyers and authorities
5. **Track Relationships** → Link connected incidents

## Notes
- Main library documents jailbreak attempts for research/educational purposes
- Tools help affected employees organize evidence through legitimate legal channels
- Database stores all incidents with dates for timeline analysis
- All file types preserved - nothing deleted, only added
- System supports comprehensive evidence organization across multiple formats
- PostgreSQL provides persistent storage and complex queries
