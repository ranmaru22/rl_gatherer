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

    # Create a dictionary with the relevant data
    result = {
        'subreddit': u_obj['subreddit'],
        'author': u_obj['author'],
        'body': u_obj['selftext']
    }
    return result


def _get_data_comments(u_obj):
    """Child function. Parses URL objects for comments."""

    # Create a list of dictionaries with data for all replies
    # The individual dicts are fetched by the child function
    result = list()
    result = _get_data_children(u_obj, result)
    return result


def _get_data_children(u_obj, return_lst):
    """Recursive fetching of comment trees."""

    for comment in u_obj:
        # Check whether the node is a comment (t1)
        if comment['kind'] == 't1':
            next_comment = {
                'author': comment['data']['author'],
                'body': comment['data']['body']
            }
            return_lst.append(next_comment)
            # Check whether the node has more children
            if comment['data']['replies']:
                sub_obj = comment['data']['replies']['data']['children']
                _get_data_children(sub_obj, return_lst)
    return return_lst


def extract_links(data, settings):
    """Returns a list of links from a data object."""

    results = list()
    # Find links inside the body text
    for link in re.findall(settings.match_pattern, data['body']):
        r = re.sub("[]):,.]+?$", '', link)
        results.append(r)
    return results
