#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    EMPLOYEE_ID = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        EMPLOYEE_ID)
    response = requests.get(URL)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        sys.exit(1)

    TODOS = response.json()
    EMPLOYEE_NAME_URL = "https://jsonplaceholder.typicode.com/users/{}".format(
        EMPLOYEE_ID)
    response_name = requests.get(EMPLOYEE_NAME_URL)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        sys.exit(1)

    EMPLOYEE_NAME = response_name.json().get("username")
    FILENAME = "{}.csv".format(EMPLOYEE_ID)

    with open(FILENAME, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in TODOS:
            completed_status = "True" if todo["completed"] else "False"
            writer.writerow({
                'USER_ID': EMPLOYEE_ID,
                'USERNAME': EMPLOYEE_NAME,
                'TASK_COMPLETED_STATUS': completed_status,
                'TASK_TITLE': todo["title"]
            })
