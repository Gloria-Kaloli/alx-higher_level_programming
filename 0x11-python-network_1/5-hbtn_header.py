#!/usr/bin/python3
"""
 takes url, sends a request to the URL and displays
 the value of variable X-Request-Id in  response header
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
