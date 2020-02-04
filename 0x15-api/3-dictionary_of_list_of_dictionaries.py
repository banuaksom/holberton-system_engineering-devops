#!/usr/bin/python3
""" export data in the JSON format """
import json
import requests


if __name__ == "__main__":
    dicti = {}
    req = requests.get("https://jsonplaceholder.typicode.com/users").json()
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    dicti = {i.get("id"): [{"task": j.get("title"),
                            "completed": j.get("completed"),
                            "username": i.get("username")} for j in req2
                           if j.get("userId") == i.get("id")]
             for i in req}

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(dicti, json_file)
