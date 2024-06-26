#!/usr/bin/python3
'''
 function that queries the Reddit API and
 prints the titles of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts listed for a given
    subreddit'''

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {
        "limit": 10
    }

    response = requests.get(url, allow_redirects=False, params=params)

    if response.status_code != 200:
        print("None")
        return
    results = response.json().get('data')
    [print(c.get("data").get("title")) for c in results.get("children")]
