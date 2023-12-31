import argparse
from urllib.parse import urlparse
from actions.actions import ValidateUrl


parser = argparse.ArgumentParser(prog="RESTful APIs test utility")
sub_parsers = parser.add_subparsers()

curl_parser = sub_parsers.add_parser('ccurl')
curl_parser.add_argument('url', nargs=1, action=ValidateUrl, help='request URL', metavar='URL')
args = parser.parse_args()


if __name__ == '__main__':
    pass
