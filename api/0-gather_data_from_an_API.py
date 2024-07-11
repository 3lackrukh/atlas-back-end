#!/usr/bin/python3
import json
import sys
import requests

""" This defines the module for gathering data from an api"""


def get_employee_todo(employee_id):
    """ This method displays an employee's todo list progress"""

    # check that employee_id is an integer
    if not isinstance(employee_id, int):
        raise TypeError("employee_id must be an integer")
    
    # base URL dor the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # fetch todos for the given employee
    todo_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users?id={employee_id}'
    response1 = requests.get(todo_url)
    response2 = requests.get(user_url)

    if response1.status_code != 200:
        print(f'Failed to fetch todos for employee ID {employee_id}.')
        return
    
    if response2.status_code != 200:
        print(f'Failed to fetch name for employee ID {employee_id}.')
        return
    
    # retrieve todos and employee name
    todos = response1.json()
    emp_name = response2.json()[0]['name']
    #calculate the number of completed and total tasks
    num_tasks = len(todos)
    done_tasks = len([task for task in todos if task['completed']])

    # display employee progress
    print(f'Employee {emp_name} is done with tasks({done_tasks}/{num_tasks}):')

    # display titles of completed tasks
    for task in todos:
        if task['completed']:
            print('\t' + task['title'])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo(employee_id)