#!/usr/bin/python3
"""export data as json"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user = requests.get(user_url).json()
    tasks = requests.get(tasks_url).json()

    data = {}
    data[f'{user_id}'] = [{'task': task['title'],
                          'completed': task['completed'],
                           'username': user['username']} for task in tasks]

    with open(f'{user_id}.json', 'w') as f:
        json.dump(data, f)
