"""Functions that get and return input from the user."""

import re

from errors import IDError

def get_id(id=None):
    """Prompts the user to enter a submission ID."""
    prompt = "Please enter a Reddit submission ID.\n-> "

    id_format = "^([a-z0-9]{6})$"
    if not id:
        id = input(prompt)

    if re.search(id_format, id) is None:
        # Raise exception is not valid.
        raise IDError("ID not in required format.")

    return id


def get_output_format():
    """Asks the user how he wants the data presented."""
    pass