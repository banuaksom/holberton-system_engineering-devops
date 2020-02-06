#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries Reddit API and returns list of titles of hot articles"""
    try:
        req = requests.get("https://www.reddit.com/r/{}/hot.json".
                           format(subreddit),
                           headers={'User-Agent': 'custom'},
                           params={"after": after},
                           allow_redirects=False).json()
    except:
        return None
    if ("data" in req and "children" in req.get("data")):
        for i in req.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in req.get("data") and req.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           req.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
