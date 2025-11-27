import http.server
import socketserver
import sys

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Check the path and send appropriate status code
        if self.path == '/':
            # Send 200 OK
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'200 OK')
        
        elif self.path == '/notfound':
            # Send 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')
        
        elif self.path == '/error':
            # Send 500 Internal Server Error
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'500 Internal Server Error')
        
        elif self.path == '/redirect':
            # Send 301 Moved Permanently
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
        
        else:
            # Default: send 404 for any other path
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')
    
    def log_message(self, format, *args):
        # Custom log format to show status codes clearly
        sys.stdout.write("%s - - [%s] %s\n" %
                        (self.address_string(),
                         self.log_date_time_string(),
                         format % args))

# Create and start the web server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    print("Available endpoints:")
    print(f"  http://localhost:{PORT}/          -> 200 OK")
    print(f"  http://localhost:{PORT}/notfound  -> 404 Not Found")
    print(f"  http://localhost:{PORT}/error     -> 500 Internal Server Error")
    print(f"  http://localhost:{PORT}/redirect  -> 301 Redirect")
    print(f"  Any other path                     -> 404 Not Found")
    httpd.serve_forever()
