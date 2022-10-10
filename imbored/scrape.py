"""
"""

import requests
from bs4 import BeautifulSoup


class Scrape:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_events(self):
        """
        get the events
        """
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        return r.status_code
