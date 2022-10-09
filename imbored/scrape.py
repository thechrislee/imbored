"""
"""

import requests
from bs4 import beautifulsoup

def Scraper():
    
    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def url(self) -> str:
        return getattr(self, "_url", "https://www.thisiscleveland.com/things-to-do/event-calendar")

    def get_events(self) -> str:
        """
        get the events
        """
        r = requests.get(self.url)
        soup = beautifulsoup(r.text, "html.parser")
        return soup.prettify()

