#!/usr/bin/python3
"""
    Python script that get data for an employee using a REST API.
    Returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_request = "{}users/".format(url)
    users = requests.get(users_request).json()

    jsonfile = "todo_all_employees.json"
    user_dic = {}
    for user in users:
        list_tasks = []
        tasks = requests.get("{}todos?userId={}".
                             format(url, user["id"])).json()
        name_user = user["username"]
        for task in tasks:
            dics_tasks = {}
            dics_tasks["task"] = task["title"]
            dics_tasks["completed"] = task["completed"]
            dics_tasks["username"] = name_user
            list_tasks.append(dics_tasks)
        user_dic[task["userId"]] = list_tasks

    with open(jsonfile, mode="w") as file:
        file_w = json.dumps(user_dic)
        file.write(file_w)
