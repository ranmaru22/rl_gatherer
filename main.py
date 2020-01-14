"""This is the main file which you want to run to get some data."""

import requests
import re

from settings import Settings
import get_input as gi
import url_functions as uf
import parse
import format

class RL_Gatherer():
    """Overall class to run the script."""

    def __init__(self):
        self.settings = Settings()

    def setup(self):
        """Set everyting up for the link gathering."""
        demo = '/r/learnprogramming/comments/eojk97'
        url = gi.get_url(demo)
        response = uf.create_web_object(url['thread'], self.settings)
        return response

    def run(self):
        """The main cycle for the script."""

        # Create the data object
        data = self.setup()

        # Get content dicts for both the thread itself and all the comments.
        ti = uf.get_url_patterns(data)
        ci = uf.get_url_patterns(data, results="comments")

        thread_info = parse.get_data(ti)
        comments_info = parse.get_data(ci, setting="comments")

        links = parse.extract_links(thread_info, self.settings)
        for comment in comments_info:
            new_link = parse.extract_links(comment, self.settings)
            if set(new_link).intersection(links) \
                    and not self.settings.allow_duplicates:
                continue
            links += new_link

        format.print_links(links)


if __name__ == '__main__':
    # Create an instance and run the script.
    rl_g = RL_Gatherer()
    rl_g.run()
