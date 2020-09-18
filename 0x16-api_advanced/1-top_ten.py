#!/usr/bin/python3
"""
    Request from a API of reddit number of subscriber to a subreddit.
"""
import requests


def top_ten(subreddit):
    """ Function that request the number of subscribers """
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Python3"}).json()
    if str(response) != "<Response [200]>":
        print(None)
        return
    # top_10 = response["data"]["children"]
    return 0  # response["data"]["subscribers"]
