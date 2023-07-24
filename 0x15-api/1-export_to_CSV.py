#!/usr/bin/python3
"""export data as csv"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user = requests.get(user_url)
    user = user.json()

    tasks = requests.get(tasks_url)
    tasks = tasks.json()

    with open(f'{user["id"]}.csv', 'w') as f:
        for task in tasks:
            f.write(f"\"{user['id']}\",\"{user['username']}\","
                    f"\"{task['completed']}\",\"{task['title']}\"\n")
