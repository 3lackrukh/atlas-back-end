#!/usr/bin/python3
""" This defines the module for exporting employee task data to json file"""
import json
import requests
import sys


def all_employee_todo():
    """ Method exports all employee usernames and todo data to json file """

    # base URL dor the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # fetch all todos and usernames
    todo_url = f'{base_url}/todos'
    users_url = f'{base_url}/users'
    response1 = requests.get(todo_url)
    response2 = requests.get(users_url)

    if response1.status_code != 200:
        print('Failed to fetch todos')
        return

    if response2.status_code != 200:
        print('Failed to fetch usernames')
        return

    # construct JSON file name
    file_name = 'todo_all_employees.json'

    # compile data for master list
    master_list = {}
    for employee in response2.json():
        employee_id = employee['id']
        user_name = employee['username']
        todos = [t for t in response1.json() if t['userId'] == employee_id]
        data = [{
            "username": user_name,
            "task": t['title'],
            "completed": t['completed']
        } for t in todos]

        master_list[str(employee_id)] = data

    # create file and write formatted data
    with open(file_name, 'w') as f:
        json.dump(master_list, f)


if __name__ == '__main__':
    all_employee_todo()
