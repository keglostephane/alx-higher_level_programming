#!/bin/bash
# Take an URL, send a request to it, and display the size of the body response
curl -Is "$1" | grep -Po "(?<=Content-Length: )\d+"
