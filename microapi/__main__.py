from microapi.Server import run_server
from microapi.args_parser import args_parser


def main():
    try:
        args = args_parser()
        port = int(args.p) or 8080
        print(f'Serve on: localhost:{port}/{args.e or ""}')
        server = run_server(port)

        server.serve_forever()
        server.server_close()
    except:
        print('Error in parameters')


if __name__ == '__main__':
    main()
