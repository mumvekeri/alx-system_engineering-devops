#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers for a given subreddit"""
import requests
from json.decoder import JSONDecodeError  # Import JSONDecodeError

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        results = response.json().get("data")
        return results.get("subscribers")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers for r/{subreddit_name} is: {subscribers_count}")
