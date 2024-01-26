#!/bin/bash
# Send a JSON POST request to a URL passed as the first argument and display the body response
curl -sX POST -H "Content-Type: application/JSON" -d "@$2" "$1"
