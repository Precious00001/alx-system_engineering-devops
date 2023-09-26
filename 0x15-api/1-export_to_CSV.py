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
    url_user = "https://jsonplaceholder.typicode.com/"

# Make an HTTP GET request to fetch user data based on the employee ID
    user = requests.get(url_user + "users/{}".format(id_c)).json()
    username = user.get("username")
    req = requests.get(url_user + "todos", params={"userId": id_c}).json()

# Open a CSV file for writing, named after the employee ID
    with open("{}.csv".format(id_c), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id_c, username, t.get("completed"), t.get("title")]
         ) for t in url_user]
