"""Functions that get and return input from the user."""

import re


def get_id(id=None):
    """Prompts the user to enter a submission ID."""
    prompt = "Please enter a Reddit submission ID.\n-> "

    id_format = "^([a-z0-9]{6})$"
    if not id:
        id = input(prompt)

    if re.search(id_format, id) is None:
        # Raise exception is not valid.
        raise ValueError("ID not in required format.")

    return id
