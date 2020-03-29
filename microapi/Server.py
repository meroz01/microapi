from http.server import BaseHTTPRequestHandler, HTTPServer
from microapi.args_parser import args_parser


class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        args = args_parser()

        self.response_code = args.c
        self.data = args.d
        self.api_path = args.e if hasattr(args, 'e') else ''

        super().__init__(request, client_address, server)

    def response(self):
        self.send_response(self.response_code)
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


def run_server(port):
    return HTTPServer(('localhost', port), Server)
