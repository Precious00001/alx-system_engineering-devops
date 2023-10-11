#!/usr/bin/python3
'''Get ALL articles for a given subreddit'''
import pprint
import requests

# Define the base URL for Reddit's API
url = 'http://reddit.com/r/{}/hot.json'


# Define a recursive function to get all hot posts from a subreddit
def recurse(subreddit, hot_list=[], after=None):
    ''' function recurse :Get ALL hot posts'''
    # Define custom headers for the request
    headers = {'User-agent': 'Unix:0-subs:v1'}
    # Define parameters for the request, including the 'limit' for the number of posts
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(url.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    # Parse the JSON response and extract relevant data
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    # Extract and append the titles of hot posts to the hot_list
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
