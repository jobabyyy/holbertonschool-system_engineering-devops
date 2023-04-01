#!/usr/bin/python3
"""
Python script that, using this REST API,
TODO list progress and exports data
in CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]
    employee = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    employee_name = employee.get('name')

    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

    with open('{}.csv'.format(employee_id), mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()

        for task in todos:
            completed_status = "True" if task["completed"] else "False"
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task.get("completed"),
                'TASK_TITLE': task.get('title')
            })
