#!/usr/bin/python3
"""display_body_response_or_error
Sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than 400 print Error code:
followed by the value of the HTTP status code.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code > 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
