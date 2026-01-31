import requests
response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print("Username:", data["login"])
print("Public Repositories:", data["public_repos"])
