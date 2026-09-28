import os
import requests


def get_zen():
    response = requests.get("https://api.github.com/zen")
    response.raise_for_status()
    return response.text


def get_repos(username):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        params={"per_page": 5}
    )

    response.raise_for_status()
    return response.json()


def post_well(well_name):
    response = requests.post(
        "https://httpbin.org/post",
        json={"well": well_name}
    )

    response.raise_for_status()
    return response.json()

def get_bearer(token):
    response = requests.get(
        "https://httpbin.org/bearer",
        headers={"Authorization": f"Bearer {token}"}
    )

    response.raise_for_status()
    return response.json()

def main():
    token = os.environ["HTTPBIN_TOKEN"]

    quote = get_zen()
    print(quote)

    repos = get_repos("nostraoil")
    for repo in repos:
        print(repo["name"])

    data = post_well("LWX20")
    print(data["json"]["well"])

    bearer_data = get_bearer(token)
    print(bearer_data)


if __name__ == "__main__":
    main()