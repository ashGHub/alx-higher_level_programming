#!/bin/bash
# Sends a OPTIONS request to the URL, and displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
