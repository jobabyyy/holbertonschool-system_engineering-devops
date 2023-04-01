#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import urllib

if __name__ == "__main__":
    "defining base Url for API"
    url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]
    employee = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    "counts total # of tasks and tasks completed"
    total_tasks = len(todos)
    done_tasks = sum(1 for t in todos if t['completed'])
    employee_name = employee.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    for task in todos:
        if task.get('completed'):
            print("\t {} {}".format('\t', task.get('title')))
