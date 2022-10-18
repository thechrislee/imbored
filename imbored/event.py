"""
Event information
"""
from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class Address:
    """class for addresses"""

    addressLocality: str
    addressRegion: str
    postalCode: str
    streetAddress: str
    type: str

    def __str__(self) -> str:
        return f"{self.streetAddress}, {self.addressLocality}, {self.addressRegion}, {self.postalCode}"

    def __repr__(self) -> str:
        return f"{self.streetAddress}, {self.addressLocality}, {self.addressRegion}, {self.postalCode}"


@dataclass
class Location:
    """Location infomration"""

    address: Address
    name: str


@dataclass
class Offer:
    """class for offers"""

    price: str
    priceCurrency: str
    url: str
    type: str


@dataclass
class Event:
    """Class for tracking event information"""

    name: str
    startDate: str
    endDate: str
    location: Location
    offers: Offer

    @classmethod
    def from_json(cls, data: str) -> "Event":
        """
        Return an event object using the provided json dictionary. Dictionary should be provided as a string. Cleanup is done on the dictionary to remove '@' from object keys.
        """
        event = json.loads(data)
        event["location"]["address"]["type"] = event["location"]["address"].pop("@type")
        event["offers"]["type"] = event["offers"].pop("@type")

        date_format = "%Y-%m-%dT%H:%M"
        name = event["name"]
        startDate = datetime.strptime(event["startDate"], date_format)
        endDate = datetime.strptime(event["endDate"], date_format)
        location = Location(Address(**event["location"]["address"]), event["name"])
        offers = Offer(**event["offers"])
        return cls(name, startDate, endDate, location, offers)
