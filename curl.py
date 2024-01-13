import argparse
from urllib.parse import urlparse
from actions.actions import ValidateUrl
import requests


parser = argparse.ArgumentParser(prog="RESTful APIs test utility")
sub_parsers = parser.add_subparsers()

curl_parser = sub_parsers.add_parser('ccurl')
curl_parser.add_argument('url', nargs=1, action=ValidateUrl, help='request URL', metavar='URL')
args = parser.parse_args()


def request_message(parsed_request_url, method='GET'):
    print(fr'connecting to {parsed_request_url.netloc}' '\n'
          fr'Sending request {method} /{method.lower()} {parsed_request_url.scheme.upper()}' '\n'
          fr'Host: {parsed_request_url.hostname}' '\n'
          fr'Accept: */*' '\n')


def print_response(response_):
    print(response_.json())


if __name__ == '__main__':
    parsed_request_url = urlparse(args.url)
    request_message(parsed_request_url)
    response = requests.get(args.url)
    print_response(response)
