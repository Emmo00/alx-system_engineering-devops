#!/usr/bin/python3
"""returns info about an employee by ID passed as argument"""
import sys
import requests

user_id = sys.argv[1]


def get_completed_tasks(tasks):
    completed = 0
    for task in tasks:
        if task['completed']:
            completed += 1
    return completed


user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

user = requests.get(user_url)
user = user.json()

tasks = requests.get(tasks_url)
tasks = tasks.json()

print(f'Employee {user["name"]} is done with \
      tasks({get_completed_tasks(tasks)}/{len(tasks)}):')

for task in tasks:
    if task['completed']:
        print(f'\t {task["title"]}')
