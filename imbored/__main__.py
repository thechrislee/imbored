""""""
from .scrape import Scrape
from .event import Event
import json


from rich.table import Table
from rich.markdown import Markdown

from textual import events
from textual.app import App
from textual.reactive import Reactive

from textual.widgets import (
    ScrollView,
    Header,
    Footer,
    Placeholder,
    TreeControl,
    TreeClick,
)
from textual.views import DockView, GridView


class ImboredApp(App):

    update = Reactive(False)

    def watch_update(self, update: bool) -> None:
        pass

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:

        self.description = Markdown(
            f"## Welcome to `imbored`. Click an event on the left to view the details of it."
        )
        self.body = ScrollView(self.description)

        tree = TreeControl("Events", {})

        scraper = Scrape()
        event_data = scraper.get_events()
        events = {}
        for event in event_data:
            e = Event.from_json(event)
            name = e.name
            start_date = (str(e.startDate).split()[0]).strip()
            description = str(e)
            await tree.add(
                tree.root.id, name, {"event": name, "description": description}
            )
        await tree.root.expand()

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(ScrollView(tree), size=50, edge="left")
        await self.view.dock(self.body)

    async def handle_tree_click(self, message: TreeClick[dict]) -> None:
        ID = message.node.id
        label = message.node.label
        event = message.node.data.get("event")

        if ID == 0:
            self.description = Markdown(
                f"## Welcome to `imbored`. Click an event on the left to view the details of it."
            )
            await self.body.update(self.description)
        else:
            self.description = Markdown(message.node.data.get("description"))
            await self.body.update(self.description)


def run():
    """ """

    ImboredApp.run(title="imbored", log="textual.log")


if __name__ == "__main__":
    exit(run())
