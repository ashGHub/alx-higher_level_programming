#!/bin/bash
# Sends a POST request to the URL, and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
