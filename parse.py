"""Functions that parse URL objects."""

import re


def get_data(u_obj, setting="thread"):
    """Parent function. Calls the correct function for either thread or comment parsing."""

    if setting == "thread":
        return _get_data_thread(u_obj)
    elif setting == "comments":
        return _get_data_comments(u_obj)
    else:
        raise AttributeError("Invalid attribute for 'setting'")


def _get_data_thread(u_obj):
    """Child function. Parses URL objects for threads."""

    result = {
        'subreddit': u_obj['subreddit'],
        'author': u_obj['author'],
        'body': u_obj['selftext']
    }
    return result


def _get_data_comments(u_obj):
    """Child function. Parses URL objects for comments."""

    result = list()
    for comment in u_obj:
        next_comment = {
            'subreddit': comment['data']['subreddit'],
            'author': comment['data']['author'],
            'body': comment['data']['body']
        }
        result.append(next_comment)
    return result


def extract_links(data, settings):
    """Returns a list of links from a data object."""

    r = re.findall(settings.match_pattern, data['body'])
    results = list()
    for link in r:
        results.append(re.sub("[]):]+?$", '', link))
    return results
