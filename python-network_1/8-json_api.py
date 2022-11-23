#!/usr/bin/python3
'''sends a letter as a parameter in a post request'''
import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jresponse = response.json()
        if jresponse == {}:
            print("No result")
        else:
            print("[{}] {}".format(jresponse.get("id"), jresponse.get("name")))
    except ValueError:
        print("Not a valid JSON")
