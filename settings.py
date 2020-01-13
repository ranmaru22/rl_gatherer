"""Global settings file."""

class Settings():
    """Stores all the settings for the script."""

    def __init__(self):
        self.headers = {
            # Sets the HTTP headers for the requests.
            'User-Agent': 'Python:rf_gatherer:v0.1 (by /u/0xMii)'
        }

        # Configure how the output is returned
        save_to_file: False
        output_file: 'sample_output.txt'
        allow_duplicates: False

        self.app = {
            # Secret app settings. Do not share!!
            # Remove before committing.
            'APP-ID': '',
            'APP-SECRET': ''
        }

        # Misc settings. Don't change these!
        self.match_pattern = 'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
