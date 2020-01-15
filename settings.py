"""Global settings file."""

# Used for importing secrety keys from local file.
import json


class Settings(object):
    """Stores all the settings for the script."""

    def __init__(self):
        self.headers = {
            # Sets the HTTP headers for the requests.
            'USER-AGENT': 'Python:rf_gatherer:v0.1 (by /u/0xMii)',
        }

        # Configure how the output is returned
        self.save_to_file = False
        self.output_file = 'sample_output.txt'
        self.allow_duplicates = False

        # Load keys from local json file.
        # with open("keys.json") as f_obj:
        #     __keys = json.load(f_obj)

        self.app = {
            # Secret app settings. Do not share!!
            # Remove before committing if provided directly.
            'APP-ID': 'AO_DNY4B6vaTcg', #__keys['APP-ID'],
            'APP-SECRET': 'tT4FR6ZhWWky2ba7_lLDG7-wEyY' #__keys['APP-SECRET']
        }

        # Misc settings. Don't change these!
        self.match_pattern = 'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    