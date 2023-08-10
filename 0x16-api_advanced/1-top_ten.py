#!/usr/bin/python3
"""defines the top ten function"""
import requests


def top_ten(subreddit):
    """get the titles of top ten posts of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(url, params={'limit': 10}, allow_redirects=False,
                       headers={'User-Agent': '1-top_ten'}).json()
    err = res.get('error')
    if err or not res.get('data') or not res.get('data').get('children'):
        print("None")
        return
    for post in res['data']['children']:
        print(post['data']['title'])
