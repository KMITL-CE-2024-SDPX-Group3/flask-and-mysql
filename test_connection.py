# minimal_http_server.py
import http.server
import socketserver

PORT = 5001  # Use a different port to avoid conflicts

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
