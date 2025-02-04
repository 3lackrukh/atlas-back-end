#!/usr/bin/python3
""" This defines the module for exporting employee task data to CSV"""
import csv
import requests
import sys


def get_employee_todo(employee_id):
    """ This method reports an employee's todo list progress in CSV format"""

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
    user_name = response2.json()[0]['username']

    # construct CSV file name
    file_name = f'{employee_id}.csv'

    # create and write formatted data to file
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id, user_name,
                task['completed'], task['title']])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo(employee_id)
