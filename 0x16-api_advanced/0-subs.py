#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'YourBotName/1.0'}  # Update with your desired User-Agent
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = get(url, headers=user_agent)
        all_data = response.json()
        return all_data.get('data').get('subscribers')
    except:
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers for r/{subreddit_name} is: {subscribers_count}")
