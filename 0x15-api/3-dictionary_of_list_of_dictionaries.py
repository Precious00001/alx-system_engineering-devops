#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    import json
    import requests
    import sys

    # Make an HTTP GET request to fetch a list of users
    users_list = requests.get("https://jsonplaceholder.typicode.com/users")
    
    # Convert the JSON response to a Python list of user objects
    users = users_list.json()

    # Make an HTTP GET request to fetch a list of TODOs
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    
    # Convert the JSON response to a Python list of TODO objects
    todos = todo_list.json()

    # Create an empty dictionary to store TODO information for all employees
    todoAll = {}

# Loop through each user
    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

# Write the 'todoAll' dictionary to a JSON file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
