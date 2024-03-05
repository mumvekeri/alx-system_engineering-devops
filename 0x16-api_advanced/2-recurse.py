#!/usr/bin/python3
import requests

def add_title(hot_list, hot_posts):
    """ Add item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)

def recurse(subreddit, hot_list=[], after=None):
    """ Query Reddit API """
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
    }
    params = {
        'after': after
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code != 200:
        return None

    body = res.json()
    hot_posts = body['data']['children']
    add_title(hot_list, hot_posts)
    after = body['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)

# Example usage:
subreddit_name = "python"
result = recurse(subreddit_name)
if result is not None:
    for post_title in result:
        print(post_title)
