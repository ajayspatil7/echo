import http.server


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # handle POST requests
        input_value = self.rfile.read(int(self.headers.get('Content-Length')))
        print(input_value)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Input received')


    def do_GET(self):
        # handle GET requests
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())
