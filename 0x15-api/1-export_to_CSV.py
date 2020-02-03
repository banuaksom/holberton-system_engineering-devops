#!/usr/bin/python3
"""  exports data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)).json()
    USERNAME = req.get("username")
    print(USERNAME)
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(USER_ID)).json()
    print(req2)
    with open(USER_ID + ".csv", "w") as csvfile:
        f = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in req2:
            f.writerow([argv[1], USERNAME, i.get("completed"), i.get("title")])
