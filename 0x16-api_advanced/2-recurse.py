#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieve the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {'limit': 100, 'after': hot_list[-1]['data']['name']} if hot_list else {'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Check if the subreddit is invalid
        if response.status_code == 404:
            return None
        
        # Parse the JSON response
        data = response.json().get('data', {}).get('children', [])
        
        # Append current page's hot posts to the list
        hot_list.extend(data)
        
        # Check if there are more pages and recursively call the function
        if data and data[-1]['data']['name'] != hot_list[-1]['data']['name']:
            recurse(subreddit, hot_list)
        
        return hot_list
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
subreddit_name = "python"
result = recurse(subreddit_name)
if result is not None:
    for post in result:
        print(post['data']['title'])
