#!/usr/bin/python3
"""defines the recurse function"""
import requests


def extract(post_list, word_list, appearance):
    for post in post_list:
        for word in word_list:
            word = word.lower()
            if word in post.get('data').get('title').lower():
                if not appearance.get(word):
                    appearance[word] = 1
                else:
                    appearance[word] += 1
    return appearance


def count_words(subreddit, word_list, word_appearance={}, after=None):
    """parses the title of all hot articles, and prints a
    sorted count of given keywords"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    res = requests.get(url, allow_redirects=False, params=params,
                       headers={'User-Agent': '2-recurse'})
    if res.status_code == 302:
        return None
    res = res.json()
    err = res.get('error')
    if err or not res.get('data') or not res.get('data').get('children'):
        return None
    res_after = res.get('data', {}).get('after')
    if not res_after:
        return extract(res.get('data').get('children'), word_list,
                       word_appearance)
    word_appearance.update(extract(res['data']['children'], word_list,
                           word_appearance))
    word_appearance.update(count_words(subreddit, word_list, word_appearance,
                           res_after))
    if after:
        return word_appearance
    for key, value in sorted(word_appearance.items(),
                             key=lambda x: (-x[1], x[0])):
        print(f'{key}: {value}')
