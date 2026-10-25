from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"<h1>DevOps Assignment 8</h1><p>Docker container is running!</p>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

print("Application running on port 8000", flush=True)
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()