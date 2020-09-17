#!/usr/bin/python3
"""
    API
"""
import requests


def number_of_subscribers(subreddit):
    """ . """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Python3"})
    if response:
        response = response.json()
        return response["data"]["subscribers"]
    return 0
