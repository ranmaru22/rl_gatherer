"""This is the main file which you want to run to get some data."""

import requests
import re
import json

import praw

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
        """Initialize the Reddit instance, gets ID from user and returns it."""

        self.reddit = praw.Reddit(user_agent=self.settings.headers['User-Agent'],
                                  client_id=self.settings.app['APP-ID'],
                                  client_secret=self.settings.app['APP-SECRET'])
        demo = 'eojk97'
        id = gi.get_id(demo)
        return id

    def run(self):
        """The main cycle for the script."""

        id = self.setup()
        submission = self.reddit.submission(id=id)

        for top_level_comment in submission.comments:
            for link in re.findall(self.settings.match_pattern, top_level_comment.body):
                print(link)


if __name__ == '__main__':
    # Create an instance and run the script.
    rl_g = RL_Gatherer()
    rl_g.run()
