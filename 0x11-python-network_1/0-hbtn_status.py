#!/usr/bin/python3
"""fetch_body-response_url
Fetch the body response of a url
"""

if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    output = ("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}\n\t- utf8 content: {}")
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(output.format(type(content), content, content.decode('utf-8')))
