import requests
from layer_helper import get_layer_message

def lambda_handler(event, context):
    username = "octocat"  # Public GitHub test account
    repo_url = "https://github.com/octocat/Hello-World"  # Public repo

    r = requests.get(f"https://api.github.com/repos/octocat/Hello-World")
    repo_info = r.json()

    return {
        "statusCode": 200,
        "lambda_version": "Version 1",
        "layer_message": get_layer_message(),
        "repo_name": repo_info.get("name"),
        "stars": repo_info.get("stargazers_count"),
        "url": repo_url
    }
