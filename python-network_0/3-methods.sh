#!/bin/bash
# displays all methods that a url server can accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
