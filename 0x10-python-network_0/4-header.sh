#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL and display the body of the response
curl -sGH "X-School-User-Id: 98" "$1"