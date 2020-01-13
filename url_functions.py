"""Functions that process URLs and links."""

import requests
from errors import ResponseError, TokenError

def create_web_object(thread, settings):
    """Takes a link to a Reddit thread as input and returns a parsable object as a result."""

    url = f"https://www.reddit.com/{thread}/.json"
    url = url.encode()

    # Set the auth tokens for Reddit so we're not rate limited
    auth = requests.auth.HTTPBasicAuth(settings.app['APP-ID'], settings.app['APP-SECRET'])

    r = requests.get(url, headers=settings.headers, auth=auth)
    if r.status_code == 401:
        raise TokenError("401: Please refresh auth token.")
    elif r.status_code != 200:
        raise ResponseError("Returned web object does not have status code 200.")

    return r


# This is a debug/legacy function. We don't need to use bs4
# if we work with the Reddit API.
# def _make_soup(w_obj):
#     """Takes a request object and turns it into a bs4 Soup."""
#     soup = BeautifulSoup(w_obj, 'html.parser')
#     return soup