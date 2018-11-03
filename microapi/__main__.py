import sys, argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


args = ''

class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.response_code = args.c
        self.data = args.d
        self.api_path = args.e if hasattr(args, 'e') else ''

        super().__init__(request, client_address, server)

    def response(self):
        self.send_response(self.response_code);
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        if self.path == f'/{self.api_path}':
            self.send(self.data)
        else:
            self.send('No endpoint')

    def do_GET(self):
        self.response()

    def do_POST(self):
        self.response()

    def do_PATCH(self):
        self.response()

    def do_TRACE(self):
        self.response()

    def do_DELETE(self):
        self.response()

    def do_HEAD(self):
        self.response()

    def send(self, data):
        self.wfile.write(data.encode('utf-8'))


def main():
    port = int(args.p) or 8080
    print(f'Serve on: localhost:{port}/{args.e or ""}')
    server = HTTPServer(('localhost', port), Server)
    server.serve_forever()
    server.server_close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fast api')
    parser.add_argument('-p', help='port number', type=int)
    parser.add_argument('-e', help='enpoint path', type=str)
    parser.add_argument('-d', help='data in string e.g. "api/hello"', type=str, default='{}')
    parser.add_argument('-c', help='response code, default 200', type=int, default=200)
    args = parser.parse_args()
    
    main()
