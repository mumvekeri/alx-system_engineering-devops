#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Check if the subreddit is invalid
        if response.status_code == 404:
            print(None)
            return
        
        # Parse the JSON response
        data = response.json().get('data', {}).get('children', [])
        
        # Print titles of the first 10 hot posts
        for post in data[:10]:
            print(post.get('data', {}).get('title'))
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
subreddit_name = "python"
top_ten(subreddit_name)
