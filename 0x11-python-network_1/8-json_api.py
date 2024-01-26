#!/usr/bin/python3
"""post_request_to_search_api
Sends a POST request to a URL search api with a the letter as parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    to_search = sys.argv[1] if len(sys.argv) == 2 else ""
    payload = {'q': to_search}
    req = requests.post(url, data=payload)
    try:
        result = req.json()
        if req.headers.get('Content-Type') == 'application/json' and \
           req.status_code == 200:
            if len(result) == 2:
                print("[{}] {}".format(result.get('id'), result.get('name')))
            else:
                print("No result")
    except Exception:
        print("Not a valid JSON")
