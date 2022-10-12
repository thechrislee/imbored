"""
Event information
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Address:
    """class for addresses"""

    """
    content: str
    locality: str
    region: str
    postal_code: str
    street: str
    """
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
class Event:
    """Class for tracking event information"""

    name: str
    location: Location
    offers: dict
    start_date: datetime
    end_date: datetime


@dataclass
class Offer:
    """class for offers"""

    content: str
    price: str
    priceCurrency: str
    url: str
