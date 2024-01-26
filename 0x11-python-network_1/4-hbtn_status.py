#!/usr/bin/python3
"""fetch_body_response
Fetch and display body response from a URL
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    resp = "Body response:\n\t- type: {}\n\t- content: {}"
    req = requests.get(url)
    print(resp.format(type(req.text), req.text))
