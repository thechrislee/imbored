"""
"""

import requests
from bs4 import BeautifulSoup
import json


class Scrape:
    def __init__(self, url: str = "events.html") -> None:
        self.url = url

    def get_events(self) -> list:
        """
        get the events
        working with local html file for the moment
        """
        # r = requests.get(self.url)
        soup = BeautifulSoup(open(self.url), "html.parser")
        event_data = [
            json.loads(data.text)
            for data in soup.find_all("script", type="application/ld+json")
        ]
        return event_data
