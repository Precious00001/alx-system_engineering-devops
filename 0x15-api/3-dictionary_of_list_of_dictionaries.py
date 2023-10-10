#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Define the output file where the JSON data will be stored
    employees = "todo_all_employees.json"
    # Make an HTTP GET request to fetch all to-do list items
    users = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    # Make an HTTP GET request to fetch user information
    use_id = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    # Open the output file for writing
    with open(employees, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
             'completed': i.get('completed'),
                            'username': j.get('username')} for i in users
                           if j.get("id") == i.get('userId')]
             for j in use_id}
        json.dump(d, f)
