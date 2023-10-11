#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests


def number_of_subscribers(subreddit):
    # Set a custom User-Agent header to avoid issues with too many requests
    user = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    # Reddit API endpoint to get subreddit information
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
