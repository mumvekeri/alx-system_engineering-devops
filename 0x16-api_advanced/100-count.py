#!/usr/bin/python3
import requests
from collections import Counter

def count_words(subreddit, word_list, results=None):
    """
    Recursively count the occurrences of given keywords in the titles of hot articles.
    Print the results in descending order by count and ascending order alphabetically.
    """
    if results is None:
        results = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {'limit': 100, 'after': results[-1]['data']['name']} if results else {'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Check if the subreddit is invalid
        if response.status_code == 404:
            return

        # Parse the JSON response
        data = response.json().get('data', {}).get('children', [])

        # Extract titles and update word counts
        titles = [post['data']['title'] for post in data]
        for title in titles:
            for word in word_list:
                lowercase_title = title.lower()
                lowercase_word = word.lower()
                if f"{lowercase_word} " in lowercase_title or f" {lowercase_word}" in lowercase_title:
                    results[lowercase_word] += 1

        # Check if there are more pages and recursively call the function
        if data and data[-1]['data']['name'] != results[-1]['data']['name']:
            count_words(subreddit, word_list, results)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Print the results
    for word, count in sorted(results.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word}: {count}")

# Example usage:
subreddit_name = "python"
keywords = ["python", "javascript", "java"]
count_words(subreddit_name, keywords)
