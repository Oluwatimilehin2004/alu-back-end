#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]

    USER_URL = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(EMPLOYEE_ID)
    )
    TODO_URL = (
        "https://jsonplaceholder.typicode.com/todos"
        "?userId={}".format(EMPLOYEE_ID)
    )

    USER_RESPONSE = requests.get(USER_URL)
    TODO_RESPONSE = requests.get(TODO_URL)

    USER_DATA = USER_RESPONSE.json()
    TODOS = TODO_RESPONSE.json()

    EMPLOYEE_NAME = USER_DATA.get("name")
    TOTAL_NUMBER_OF_TASKS = len(TODOS)

    NUMBER_OF_DONE_TASKS = 0
    for TASK in TODOS:
        if TASK.get("completed"):
            NUMBER_OF_DONE_TASKS += 1

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS
        )
    )

    for TASK in TODOS:
        if TASK.get("completed"):
            TASK_TITLE = TASK.get("title")
            print("\t {}".format(TASK_TITLE))
