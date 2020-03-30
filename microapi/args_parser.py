import argparse


def args_parser():
    parser = argparse.ArgumentParser(description='fast api')
    parser.add_argument('-p', help='port number, default 8080', type=int, default=8080)
    parser.add_argument('-e', help='endpoint path', type=str)
    parser.add_argument('-d', help='data in string e.g. "api/hello"', type=str, default='{}')
    parser.add_argument('-c', help='response code, default 200', type=int, default=200)
    parser.add_argument('-f', help='file path for json response', type=str)
    args = parser.parse_args()

    return args
