#!/usr/bin/python3
"""A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":

    # Define the base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Make a GET request to fetch the user's information
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed_tasks") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    [print("\t {}".format(c)) for c in completed_tasks]
