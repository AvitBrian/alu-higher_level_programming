#!/usr/bin/python3
''' takes url and email and sends post request '''
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
