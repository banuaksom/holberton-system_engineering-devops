#!/usr/bin/python3
"""Exports tasks owned by specified USER_ID in JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    dicti = {}
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(argv[1])).json()
    print(req)
    USERNAME = req.get("username")
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1])).json()
    dicti[USER_ID] = [{"task": i.get("title"),
                           "completed": i.get("completed"),
                           "username": USERNAME} for i in req2]
    with open('{}.json'.format(argv[1]), "w") as f:
        json.dump(dicti, f)

