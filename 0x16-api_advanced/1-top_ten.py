#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests


def top_ten(subreddit):
    # Reddit API endpoint to get the top posts in a subreddit
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    # Set a custom User-Agent header to avoid issues with too many requests
    users = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Define query parameters, limit to retrieve 10 posts
    params = {
        "limit": 10
    }
    # Send a GET req to the Reddit API with the spec headers and parameters
    # Disallow redirects for invalid subreddits (404 responses)
    response = requests.get(url, headers=users, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
