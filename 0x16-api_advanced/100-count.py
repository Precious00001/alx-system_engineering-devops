#!/usr/bin/python3
"""Function to count words."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    function count_words : Get ALL hot posts
    """
    # Define the Reddit API URL for the specified subreddit
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define the User-Agent header for the API request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the API request
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send an API request to Reddit
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        # Try to parse the API response as JSON
        results = response.json()

        # Check if the response indicates a 404 error
        if response.status_code == 404:
            raise Exception
    except Exception:
        # Handle exceptions (e.g., invalid subreddit or request error)
        print("")
        return

    # Extract data from the API response
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    # Iterate through the posts in the response
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()

        # Iterate through the words in the word list
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])

                # Update the word count in the 'instances' dictionary
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    # Check if there are more pages of results
    if after is None:
        # If no more pages, sort and print word counts
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        # If more pages, recursively call the function for the next page
        count_words(subreddit, word_list, instances, after, count)
