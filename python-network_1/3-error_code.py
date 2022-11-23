#!/usr/bin/python3
'''sends a request to a url, displays the response and catches errors'''
import sys
import urllib.request
import urllib.error
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
