import os
import requests
from dotenv import load_dotenv

def get_rate_limit(token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}" # if token is provided, add it to the header. This is used to authenticate the request.

    response = requests.get("https://api.github.com/rate_limit", headers=headers)
    response.raise_for_status()
    return response.headers["x-RateLimit-Limit"]

def main():
    load_dotenv()
    token = os.environ["GITHUB_TOKEN"]
    print("Anonymous:", get_rate_limit())
    print("With token:", get_rate_limit(token))

if __name__ == "__main__":
    main()