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

## Notes
This library documents jailbreak attempts and safety measures for research and educational purposes. Understanding these techniques helps organizations better protect their AI systems and implement workplace policies.
