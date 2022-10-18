""""""
from .scrape import Scrape
from .event import Event
import json


def run():
    """ """
    url = "https://www.thisiscleveland.com/things-to-do/event-calendar"
    scraper = Scrape()
    event_data = scraper.get_events()
    for event in event_data:
        print(Event.from_json(event))


if __name__ == "__main__":
    exit(run())
