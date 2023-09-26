#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":

# Get the employee ID from the command line arguments
    id_c = sys.argv[1]

# Define the base URL for the JSONPlaceholder API
    url_user = "https://jsonplaceholder.typicode.com/users/" + id_c

# Make an HTTP GET request to fetch user data based on the employee ID
    user = requests.get(url_user).json()
    username = user.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id_c) + '/todos')

# Open a CSV file for writing, named after the employee ID
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([id_c, username,
                            task.get("completed"), task.get("title")])
