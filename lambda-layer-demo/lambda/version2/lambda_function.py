import requests
from layer_helper import get_layer_message

def lambda_handler(event, context):
    username = "octocat"
    repo_url = "https://github.com/octocat/Spoon-Knife"

    r = requests.get(f"https://api.github.com/repos/octocat/Spoon-Knife")
    repo_info = r.json()

    return {
        "statusCode": 200,
        "lambda_version": "Version 2",
        "layer_message": get_layer_message(),
        "repo_name": repo_info.get("name"),
        "forks": repo_info.get("forks_count"),
        "url": repo_url
    }
