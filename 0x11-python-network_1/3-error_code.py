#!/usr/bin/python3
"""display_response_or_code
sends a request to the URL and display the body of the response
decode in utf-8. If exception occurs print `Error code:` followed
by the HTTP status code
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read()
            print(result.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
