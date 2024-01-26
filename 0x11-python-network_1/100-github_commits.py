#!/usr/bin/python3
"""list_10_last_commits
List 10 commits (from the most recent to oldest) of a given repository
Print all commits by: `<sha>: <author name>` one by line
"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1] if len(sys.argv) >= 2 else ''
    owner = sys.argv[2] if len(sys.argv) == 3 else ''
    url = "https://api.github.com/repos/{owner}/{repo}/commits".format(
        owner=owner, repo=repo)
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    result = response.json()
    try:
        if (len(result) > 10):
            result = result[0:10]
        for entry in result:
            print("{sha}: {author}".format(
                sha=entry.get('sha'),
                author=entry.get('commit').get('author').get('name')))
    except AttributeError:
        print(result)
