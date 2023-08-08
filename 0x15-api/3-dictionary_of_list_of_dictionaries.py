#!/usr/bin/python3
"""export all data as json"""
import json
import requests

if __name__ == '__main__':
    users_url = f'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url).json()

    data = {}
    for user in users:
        user_id = user['id']
        tasks_url = f'https://jsonplaceholder.typicode.com/todos'\
                    f'?userId={user_id}'
        tasks = requests.get(tasks_url).json()
        data[f'{user_id}'] = [{'username': user['username'],
                               'task': task['title'],
                               'completed': task['completed']}
                              for task in tasks]
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
