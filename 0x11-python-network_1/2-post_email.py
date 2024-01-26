#!/usr/bin/python3
"""post_request
Send a POST request to the passed URL with the email as a parameter,
and display the body of the response decoded in utf-8
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data)
    payload = data.encode('utf-8')
    req = urllib.request.Request(url, payload, method='POST')
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf-8'))
