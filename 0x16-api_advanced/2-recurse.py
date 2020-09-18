#!/usr/bin/python3
"""
    Request from a API of reddit the titles of all hot articles
    for a given subreddit.
    Recursively.
"""
import requests


def recurse(subreddit, hot_list=[], next=""):
    """ Function that request a list of articles. """
    if next is None:
        return []

    url = "https://api.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, next)

    response = requests.get(url, headers={"User-Agent": "Python3"})
    if str(response) != "<Response [200]>":  # response.status_code != 200
        return None
    response = response.json()
    child = response["data"]["children"]
    next = response["data"]["after"]
    for tittle in child:
        hot_list.append(tittle["data"]["title"])
    return hot_list + recurse(subreddit, [], next)
