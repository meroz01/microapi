import sys, argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.default_response_code = 200
        self.data = args.d
        self.api_path = args.e

        super().__init__(request, client_address, server)

    def response(self):
        response_code = args.c or self.default_response_code
        self.send_response(response_code);
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

    def send(self, data):
        self.wfile.write(data.encode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fast api')
    parser.add_argument('-p', help='port number', type=int)
    parser.add_argument('-e', help='enpoint path', type=str)
    parser.add_argument('-d', help='data in string e.g. "api/hello"', type=str)
    parser.add_argument('-c', help='optional, default 200', type=int)
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()

    Server = HTTPServer(('localhost', args.p), Server)
    Server.serve_forever()

    print(f'Serve on: localhost:{port}')

    Server.server_close()
