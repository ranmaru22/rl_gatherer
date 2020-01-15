#!/usr/bin/python
"""This is the main file which you want to run to get some data."""

import praw

from settings import Settings
import get_input as gi
import url_functions as uf


class RL_Gatherer(object):
    """Overall class to run the script."""

    def __init__(self):
        self.settings = Settings()
        self.reddit = praw.Reddit(
            user_agent=self.settings.headers['USER-AGENT'],
            client_id=self.settings.app['APP-ID'],
            client_secret=self.settings.app['APP-SECRET'])

    def run(self):
        """The main cycle for the script."""

        demo = 'eojk97'
        id = gi.get_id(demo)
        test_sub = uf.Submission(self.reddit, self.settings, id)
        test_sub.print_links(show_user=True)


if __name__ == '__main__':
    # Create an instance and run the script.
    rl_g = RL_Gatherer()
    rl_g.run()
