#!/usr/bin/python3
""" returns information about TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                       format(argv[1])).json()
    EMPLOYEE_NAME = req.get("name")
    req2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(argv[1])).json()
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    for i in req2:
        if i.get("completed") is True:
            TASK_TITLE.append(i.get("title"))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(req2)
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
