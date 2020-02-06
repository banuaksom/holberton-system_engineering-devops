#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ queries the Reddit API, prints titles of first 10 hot posts """
    req = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                       format(subreddit), headers={"User-Agent": "custom"})

    if (req.status_code == 200):
        for i in req.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
