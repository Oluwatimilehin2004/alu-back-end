#!/usr/bin/python3

"""
Fetch an employee's TODO list progress from JSONPlaceholder API
and display completed tasks in the specified format.
"""

import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee info
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_url = f"{BASE_URL}/users/{employee_id}"
    todos_url = f"{BASE_URL}/todos?userId={employee_id}"

    try:
        user_resp = requests.get(user_url)
        todos_resp = requests.get(todos_url)
        user_resp.raise_for_status()
        todos_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    user_data = user_resp.json()
    todos_data = todos_resp.json()

    EMPLOYEE_NAME = user_data.get("name", "Unknown")
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = [task for task in todos_data if task["completed"]]
    num_done = len(NUMBER_OF_DONE_TASKS)

    # Print summary line
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({num_done}/{TOTAL_NUMBER_OF_TASKS}):")
    print(f"{EMPLOYEE_NAME} has completed the following tasks:")
    for task in NUMBER_OF_DONE_TASKS:
        print(f"  {task['title']}")
    print(f"{num_done} tasks completed")
    print(f"{TOTAL_NUMBER_OF_TASKS} tasks in total")

if __name__ == "__main__":
    main()
