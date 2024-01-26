#!/usr/bin/python3
"""send_POST_request
Takes a URL and an email address, send a POST request to the URL with
the email as parameter, and display the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    req = requests.post(url, data=payload)
    print(req.text)
