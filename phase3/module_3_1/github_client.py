import requests

response = requests.get("https://api.github.com/zen")

print(response.status_code)
print(response.text)
print(response.headers['Content-Type'])

response = requests.get("https://api.github.com/users/nostraoil/repos", params={"per_page": 5})

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo["name"])
else:
    print(f"Request failed: {response.status_code}")

response = requests.post("https://httpbin.org/post", json={"well": "LWX20"})

print(response.status_code)
print(response.headers['Content-Type'])
print(response.json())

data = response.json()
print(data["json"]["well"])
