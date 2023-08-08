#!/usr/bin/python3
"""defines the number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers={'User-Agent': '0-subs'}).json()
    try:
        return res['data']['subscribers']
    except Exception:
        return 0
