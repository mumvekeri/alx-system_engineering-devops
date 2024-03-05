#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Check for both status codes 200 and 404
        if response.status_code == 200:
            results = response.json().get("data")
            if results is not None:
                return results.get("subscribers", 0)
        elif response.status_code == 404:
            return 0
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError occurred: {e}")
    
    return 0

# Example usage:
subreddit_name = "existingSubreddit"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers for r/{subreddit_name} is: {subscribers_count}")
