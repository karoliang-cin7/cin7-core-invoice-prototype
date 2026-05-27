#!/usr/bin/env python3
"""Serve the Cin7 Core HTML preview at http://localhost:8080/preview.html"""
import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.css': 'text/css',
        '.woff': 'font/woff',
        '.woff2': 'font/woff2',
        '.ttf': 'font/ttf',
        '.eot': 'application/vnd.ms-fontobject',
        '.svg': 'image/svg+xml',
        '': 'application/octet-stream',
    }

    def log_message(self, fmt, *args):
        if any(args[0].endswith(ext) for ext in ('.html', '.css', '.js', '.png', '.svg', '.woff2')):
            super().log_message(fmt, *args)

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/preview.html")
    print("Ctrl+C to stop")
    httpd.serve_forever()
