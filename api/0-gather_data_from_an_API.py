#!/usr/bin/python3
"""
Fetch and display TODO list progress for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(user_id)
    )
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos"
        "?userId={}".format(user_id)
    )

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todos = todo_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos)

    done_tasks = [
        task for task in todos
        if task.get("completed")
    ]

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee_name,
                len(done_tasks),
                total_tasks)
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
        
