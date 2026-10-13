import os
import requests
from dotenv import load_dotenv

def get_all_repos(org, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"https://api.github.com/orgs/{org}/repos?per_page=100"
    repos = []

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repos.extend(response.json())

        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            url = None

    return repos

def main():
    load_dotenv()
    token = os.environ["GITHUB_TOKEN"]
    repos = get_all_repos("equinor", token)
    print(f"Fetched {len(repos)} repos")
    print(repos[0]["name"])


if __name__ == "__main__":
    main()