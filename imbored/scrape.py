"""
"""

import requests
from bs4 import BeautifulSoup
import json
from .event import Event, Address, Offer


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

        for event in event_data:
            event["location"]["address"]["type"] = event["location"]["address"].pop(
                "@type"
            )
            event["offers"]["type"] = event["offers"].pop("@type")
            print(json.dumps(event, indent=4))

    def print_events(
        self,
    ) -> None:
        """Print the events"""
        pass
