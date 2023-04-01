#!/usr/bin/python3
"""
export data in
JSON format.
"""

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()

    todos_dict = {}
    for user in users:
        employee_id = user.get('id')
        employee_name = user.get('username')
        todos = requests.get(url + "{}/todos".format(employee_id)).json()

        todo_list = []
        for todo in todos:
            task = todo.get('title')
            status = todo.get('completed')
            todo_dict = {
                "username": employee_name,
                "task": task,
                "completed": status
            }
            todo_list.append(todo_dict)

        todos_dict[str(employee_id)] = todo_list

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(todos_dict, json_file)
