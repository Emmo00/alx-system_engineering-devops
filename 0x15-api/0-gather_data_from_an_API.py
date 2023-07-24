#!/usr/bin/python3
"""returns info about an employee by ID passed as argument"""
import requests
import sys


def get_completed_tasks(tasks):
    """get the number of completed tasks"""
    completed = 0
    for task in tasks:
        if task['completed']:
            completed += 1
    return completed


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user = requests.get(user_url)
    user = user.json()

    tasks = requests.get(tasks_url)
    tasks = tasks.json()

    print(f'Employee {user["name"]} is done with '
          f'tasks({get_completed_tasks(tasks)}/{len(tasks)}):')

    for task in tasks:
        if task['completed']:
            print(f'\t {task["title"]}')
