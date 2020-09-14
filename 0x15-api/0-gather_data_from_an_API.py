#!/usr/bin/python3
"""
    Python script that get data for an employee using a REST API.
    Returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_req = "{}users/{}".format(url, user_id)
    user_name = requests.get(user_req, verify=False).json().get("name")
    tasks = requests.get("{}todos?userId={}".format(url, user_id), verify=False).json()
    total_tasks = len(tasks)
    tasks_done = requests.get("{}todos?userId={}&&completed=true".
                              format(url, user_id), verify=False).json()
    total_tasks_done = len(total_tasks_done)

    print("Employee {} is done with tasks({}/{})".
          format(user_name, total_tasks_done, total_tasks))
    for task in tasks_done:
        print("\t {}".format(task["title"]))
