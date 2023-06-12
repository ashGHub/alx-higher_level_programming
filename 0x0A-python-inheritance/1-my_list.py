#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """
    Custom List class that extends from list
    """

    def print_sorted(self):
        """
        prints the current list in sorted
        """
        print(sorted(self))
