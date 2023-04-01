#!/usr/bin/python3
"""
export data in the CSV and JSON formats.
"""
import requests
import csv
import json
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    EMPLOYEE_ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        EMPLOYEE_ID)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        EMPLOYEE_ID)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get("username")
    filename_csv = "{}.csv".format(EMPLOYEE_ID)
    filename_json = "{}.json".format(EMPLOYEE_ID)

    with open(filename_csv, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        writer.writeheader()

        for todo in todos:
            completed_status = "True" if todo["completed"] else "False"
            writer.writerow({
                'USER_ID': EMPLOYEE_ID,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': completed_status,
                'TASK_TITLE': todo["title"]
            })

    with open(filename_json, mode='w') as jsonfile:
        tasks = []
        for todo in todos:
            completed_status = True if todo["completed"] else False
            task = {
                "task": todo["title"],
                "completed": completed_status,
                "username": employee_name
            }
            tasks.append(task)

        data = {EMPLOYEE_ID: tasks}
        json.dump(data, jsonfile)
