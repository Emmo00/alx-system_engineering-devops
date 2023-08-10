#!/usr/bin/python3
"""defines the recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of hot topics of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    res = requests.get(url, allow_redirects=False, params=params,
                       headers={'User-Agent': '2-recurse'}).json()
    err = res.get('error')
    if err or not res.get('data') or not res.get('data').get('children'):
        return None
    if not res.get('data').get('after'):
        return []
    hot_list = [*hot_list, *res.get('data').get('children'),
                *recurse(subreddit, hot_list, res.get('data').get('after'))]
    return hot_list
