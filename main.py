from github import Github
from github import Auth
import requests

username_to_check = input("Enter the username to check through commits: ").strip()
github_access_token = input("Enter your access token: ").strip()

auth = Auth.Token(github_access_token)
g = Github(auth=auth)

user = g.get_user(username_to_check)
repos = user.get_repos()

false = False
true = True
null = None

pairs = []

headers = {"Authorization" : f"Bearer {github_access_token}"}
for repo in user.get_repos():
    if repo.fork is False:
        r = requests.get(f"https://api.github.com/repos/{username_to_check}/{repo.name}/commits" , headers = headers)
        response = eval(r.text)
        for commit in response:
            pair = (commit["commit"]["author"]["name"] , commit["commit"]["author"]["email"])
            if pair in pairs:
                pass 
            else:
                pairs.append(pair)
                print(f'{commit["commit"]["author"]["name"]} --> {commit["commit"]["author"]["email"]}')

