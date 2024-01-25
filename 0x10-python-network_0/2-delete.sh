#!/bin/bash
# Sends a DELETE request to the url passed as first argument and display the body of the response
curl -Xs DELETE "$1"
