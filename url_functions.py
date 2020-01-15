"""Functions that process URLs and links."""

import re


class Submission(object):
    """
        Class for Submission Object which stores links.
        Every instance must have one fixed ID.
    """

    def __init__(self, reddit, settings, id):
        self.reddit = reddit
        self.settings = settings
        self.id = id
        self.links = self.__generate_links()
        self.allow_duplicates = self.settings.allow_duplicates

    def __generate_links(self):
        """Generates a link list to be stored in the self.links variable."""

        sub = self.reddit.submission(id=self.id)
        links = list()
        for comment in sub.comments:
            for link in re.findall(self.settings.match_pattern, comment.body):
                links.append((self.__clean_url(link), comment.author.name))
        return links

    def __clean_url(self, link):
        """Cleans a link according to the default URL pattern."""
        c_link = re.sub("[]):,.]+?$", '', link).split(']')
        return c_link[0]

    def tgl_duplicates(self):
        """Toggles the local allow_duplicates setting."""

        if self.allow_duplicates:
            self.allow_duplicates = False
            print("Show duplicate links: OFF")
        else:
            self.allow_duplicates = True
            print("Show duplicate links: ON")

    def print_links(self, show_user=False):
        """Prints extraced links to the CLI."""

        print("Links found:\n------------")
        c = 1
        for link_tuple in self.links:
            if show_user:
                print(f"{c}. <{link_tuple[1]}> {link_tuple[0]}")
            else:
                print(f"{c}. {link_tuple[0]}")
            c += 1