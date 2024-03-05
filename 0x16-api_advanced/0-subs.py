import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'YourBotName/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subreddit_info = response.json()
        return subreddit_info['data']['subscribers']
    else:
        return 0

subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers for r/{subreddit_name} is: {subscribers_count}")

