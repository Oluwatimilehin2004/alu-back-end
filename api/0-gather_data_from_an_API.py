#!/usr/bin/bash/python3

"""
Fetch an employee's TODO list progress from JSONPlaceholder API
and display completed tasks in the specified format.
"""

import requests
import sys

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
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

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

    employee_name = user_data.get("name", "Unknown")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_done = len(completed_tasks)

    # Print summary line
    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    print(f"{employee_name}")
    print(f"{num_done} tasks completed")
    print(f"{total_tasks} tasks in total")

if __name__ == "__main__":
    main()
