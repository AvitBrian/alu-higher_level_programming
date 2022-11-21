#!/bin/bash
#sends a get request to a provided URL with a header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
