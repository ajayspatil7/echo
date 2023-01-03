import http.server


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # read the input value from the POST request
        input_value = self.rfile.read(int(self.headers.get('Content-Length')))

        # print the input value on the Python terminal
        print(input_value)

        # send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Input received')
