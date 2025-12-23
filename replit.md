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

## NEW: Evidence & Legal Tools (Added Dec 23)

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

## Notes
- Main library documents jailbreak attempts for research/educational purposes
- New tools help affected employees protect themselves through legitimate legal channels
- All information is for lawful use only
