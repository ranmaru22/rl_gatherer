"""This is the main file which you want to run to get some data."""

import requests
import get_input as gi
import url_functions as uf
import re

from settings import Settings


class RL_Gatherer():
    """Overall class to run the script."""

    def __init__(self):
        self.settings = Settings()

    def run(self):
        """The main cycle for the script."""
        demo = 'r/learnpython/comments/593ox9'

        response = uf.create_web_object(demo, self.settings)
        data = response.json()
        thread = data[0]['data']['children'][0]['data']
        comments = data[1]['data']['children']
            
        for comment in comments:
            s = comment['data']['body']
            link = re.findall(self.settings.match_pattern, s)
            print(link)

if __name__ == '__main__':
    # Create an instance and run the script.
    rl_g = RL_Gatherer()
    rl_g.run()