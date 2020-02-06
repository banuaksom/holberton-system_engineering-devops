#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers """
    req = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                       headers={"User-Agent": "custom"})
    if(req.status_code == 200):
        return req.json().get("data").get("subscribers")
    return 0
