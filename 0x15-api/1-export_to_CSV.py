#!/usr/bin/python3
"""  exports data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                       format(argv[1])).json()
    USERNAME = req.get("username")
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(argv[1])).json()
    with open(argv[1] + ".csv", "w") as csvfile:
        f = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in req2:
            f.writerow([argv[1], USERNAME, i.get("completed"), i.get("title")])
