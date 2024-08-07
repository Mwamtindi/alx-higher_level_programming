#!/usr/bin/python3
"""
A script that lists 10 most recent commits of a GitHub repository by a
specific owner using the GitHub API.
"""

import sys
import requests


def get_commits(repoz_name, owner_name):
    """
    Fetches and prints 10 most recent commits of a repository.

    Args:
        repo_name : (str) Name of the repository.
        owner_name : (str) Name of the repository owner.
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits.
              Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        repoz_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_commits(repoz_name, owner_name)
