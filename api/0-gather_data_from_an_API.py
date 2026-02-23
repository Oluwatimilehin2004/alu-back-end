#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress
using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos"
        "?userId={}".format(employee_id)
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos = todos_response.json()

    employee_name = user_data.get("name")
    total_number_of_tasks = len(todos)

    number_of_done_tasks = 0
    for task in todos:
        if task.get("completed") is True:
            number_of_done_tasks += 1

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(
            employee_name,
            number_of_done_tasks,
            total_number_of_tasks
        )
    )

    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
