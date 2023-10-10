#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

# Check if the script is being run as the main program
if __name__ == '__main__':

    # Get the employee ID from the command line arguments
    id_c = sys.argv[1]

    # Define the url for the JSONPlaceholder API
    url_user = "https://jsonplaceholder.typicode.com/"

    # Make an HTTP GET request to fetch user data based on the employee ID
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id_c)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

# Open a CSV file for writing, named after the employee ID
    with open("{}.json".format(id_c), "w") as user_id:
        json.dump({id_c: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': users.get('username')
            } for task in todos]}, user_id)
