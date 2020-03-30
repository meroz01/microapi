from json import loads, dumps

from http.server import BaseHTTPRequestHandler, HTTPServer
from microapi.args_parser import args_parser


class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        args = args_parser()

        self.response_code = args.c
        self.data = args.d
        self.api_path = args.e if hasattr(args, 'e') else ''
        self.response_file_path = args.f

        super().__init__(request, client_address, server)

    def get_response_data_from_file(self):
        if not self.response_file_path:
            return None

        with open(self.response_file_path, 'r') as file:
            return loads(file.read())

    def response(self):
        self.send_response(self.response_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        file_data = self.get_response_data_from_file()

        if self.path == f'/{self.api_path}':
            if file_data:
                self.send(dumps(file_data))
            else:
                self.send(self.data)
        else:
            self.send('No endpoint')

    def send(self, data):
        self.wfile.write(data.encode('utf-8'))

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


def run_server(port):
    return HTTPServer(('localhost', port), Server)
