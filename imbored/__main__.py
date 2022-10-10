""""""
from .scrape import Scrape

def run():
    """ """
    url = "https://www.thisiscleveland.com/things-to-do/event-calendar"
    scraper = Scrape(url)
    print(scraper.get_events())

if __name__ == "__main__":
    print(run())
