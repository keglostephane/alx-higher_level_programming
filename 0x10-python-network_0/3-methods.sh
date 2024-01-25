#!/bin/bash
# Takes in a URL and displays all HTTP methods the server accept
curl -sIX OPTIONS 0.0.0.0:5000/route_4 | grep "Allow" | grep -Po "(?<=Allow: ).*" | cat
