"""Functions that get and return input from the user."""

import re


def get_url(url=None):
    """
    Prompts the user to enter link to a Reddit thread.
    Format should be either:
        r/<Subreddit>/comments/<hash>
        /r/<Subreddit>/comments/<hash>/
    """
    prompt = "Please enter a valid Reddit link starting with /r/ and the name of the Subreddit, followed by the link to the comments.\n-> "

    url_format = "^\/?(r\/(\S+)\/comments\/([a-z0-9]{6}))\/?.*$"
    if not url:
        url = input(prompt)

    if re.search(url_format, url) is None:
        # Raise exception is not valid.
        raise ValueError("URL not in required format.")
    
    # Store useful information contained in the URL in a dict for easy access.
    url_items = re.findall(url_format, url)
    url_dict = {
        'link': url_items[0][0],
        'subreddit': url_items[0][1],
        'thread': url_items[0][2]
    }

    return url_dict
