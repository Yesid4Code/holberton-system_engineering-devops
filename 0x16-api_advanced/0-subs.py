#!/usr/bin/python3
"""
    Request from a API of reddit number of subscriber to a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Function that request the number of subscribers """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Python3"})
    if response:
        response = response.json()
        return response["data"]["subscribers"]
    return 0
