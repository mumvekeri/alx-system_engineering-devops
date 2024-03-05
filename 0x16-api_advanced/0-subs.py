#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Set the base URL and the custom User-Agent
    base_url = "https://www.reddit.com/r/"
    user_agent = "python:0x16.api.advanced:v1.0.0 (by /u/Copilot)"
    # Construct the full URL with the subreddit name
    url = base_url + subreddit + "/about.json"
    # Make a GET request with the headers and no redirects
    response = requests.get(url, headers={"User-Agent": user_agent}, allow_redirects=False)
    # Check the status code
    if response.status_code == 200:
        # Parse the JSON response and get the data
        data = response.json().get("data")
        # Check if the data is valid
        if data:
            # Return the number of subscribers
            return data.get("subscribers")
    # If the status code is not 200 or the data is invalid, return 0
    return 0
