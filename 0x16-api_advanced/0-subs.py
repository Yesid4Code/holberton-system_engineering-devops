#!/usr/bin/python3
"""
    API
"""
import requests


def number_of_subscribers(subreddit)
    """ . """
    if subreddit is None:
        return 0

    url = "https://www.reddit.com/dev/api/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": ""}).json()["data"]
    if response:
        return response["subscribers"]
