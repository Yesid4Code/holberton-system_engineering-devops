#!/usr/bin/python3
"""
    Request from a API of reddit Top 10 number of subscriber to a subreddit.
"""
import requests


def top_ten(subreddit):
    """ Function that request the number of subscribers """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Python3"})
    if str(response) != "<Response [200]>":  # response.status_code != 200
        print(None)
        return
    response = response.json()
    child = response["data"]["children"]
    for tittle in child:
        print(tittle["data"]["title"])
