""""""
from .scrape import Scrape
import json


def run():
    """ """
    url = "https://www.thisiscleveland.com/things-to-do/event-calendar"
    scraper = Scrape()
    events = scraper.get_events()
    print(json.dumps(events[0], indent=4))
    print(len(events))


if __name__ == "__main__":
    exit(run())
