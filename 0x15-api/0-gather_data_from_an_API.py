#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionRequests = requests.Session()

    id_c = argv[1]
    base_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'
.format(id_c)
    base_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_c)

    # Make a GET request to fetch the employee's information
    employee = sessionRequests.get(base_todos)
    employeeName = sessionRequests.get(base_user)

    # Make a GET request to fetch the user's TODO list
    json_request = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_request:
        if done_tasks['completed']:
            totalTasks += 1

    # Display the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_request)))

    for done_tasks in json_request:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
