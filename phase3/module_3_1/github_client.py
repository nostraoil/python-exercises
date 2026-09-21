import requests

response = requests.get("https://api.github.com/zen")

print(response.status_code)
print(response.text)
print(response.headers['Content-Type'])

response = requests.get("https://api.github.com/users/nostraoil/repos", params={"per_page": 5})

repos = response.json()

for repo in repos:
    print(repo["name"])
print(type(repos))