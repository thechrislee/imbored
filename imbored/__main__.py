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
        e = Event.from_json(event)
        print(e)


if __name__ == "__main__":
    exit(run())
