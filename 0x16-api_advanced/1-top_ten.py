#!/usr/bin/python3
"""defines the top ten function"""
import requests


def top_ten(subreddit):
    """get the titles of top ten posts of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/top.json'
    res = requests.get(url, params={'limit': 10}, allow_redirects=False,
                       headers={'User-Agent': '1-top_ten'}).json()
    error = res.get('error')
    if error:
        print("None")
        return
    for post in res['data']['children']:
        print(post['data']['title'])
