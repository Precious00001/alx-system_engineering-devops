#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests


def add_title(dictionary, popular_post):
    """
    Adds item into a list

    Args:
        dictionary: Dictionary to store word counts
        popular_post: List of hot posts from Reddit
    """
    if len(popular_post) == 0:
        return

    title = popular_post[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    popular_post.pop(0)
    add_title(dictionary, popular_post)


def recurse(subreddit, dictionary, after=None):
    """
    Queries the Reddit API

    Args:
        subreddit: Subreddit to query
        dictionary: Dictionary to store word counts
        after: Identifier for the next page of posts
    """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    popular_post = dic['data']['children']
    add_title(dictionary, popular_post)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """
    Init function to count words in subreddit posts

    Args:
        subreddit: Subreddit to query
        word_list: List of words to count
        dictionary: Dictionary to store word counts
    """
    if dictionary is None:
        dictionary = {}

    for word in word_list:
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}: {}".format(item[0], item[1]))
