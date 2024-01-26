#!/usr/bin/python3
"""display_user_github_id
Takes your GitHub credentials (username and password) and use the GitHub API
to display your id. Use Basic Authentication with personal access token as
password to access your information.
"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1] if len(sys.argv) >= 2 else ''
    token = sys.argv[2] if len(sys.argv) == 3 else ''
    url = "https://api.github.com/users/{}".format(username)
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + token,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
