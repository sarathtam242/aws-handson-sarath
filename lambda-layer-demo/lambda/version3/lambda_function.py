import os
import json
import requests
from layer_helper import get_layer_message

def lambda_handler(event, context):
    username = "octocat"
    repo_name = os.getenv("GITHUB_REPO", "Hello-World")
    repo_url = f"https://github.com/{username}/{repo_name}"

    try:
        r = requests.get(f"https://api.github.com/repos/{username}/{repo_name}", timeout=5)
        r.raise_for_status()
        repo_info = r.json()

        response_body = {
            "lambda_version": "Version 3",
            "layer_message": get_layer_message(),
            "repo_name": repo_info.get("name"),
            "watchers": repo_info.get("watchers_count"),
            "url": repo_url
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_body)
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
