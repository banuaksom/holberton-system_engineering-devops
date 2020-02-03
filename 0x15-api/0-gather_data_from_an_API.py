#!/usr/bin/python3
""" returns information about TODO list progress """
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    EMPLOYEE_NAME = req.get("name")
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                                             format(argv[1])).json()


