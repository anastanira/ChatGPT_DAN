#!/usr/bin/env python3
import http.server
import socketserver
import os
import socket

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server running on http://0.0.0.0:{PORT}")
    httpd.serve_forever()
