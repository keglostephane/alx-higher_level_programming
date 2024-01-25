#!/bin/bash
# Takes in a URL and displays all HTTP methods the server accept
curl -sIX OPTIONS "$1" | grep -Po "(?<=Allow: ).*" | cat
