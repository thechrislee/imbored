"""
Event information
"""
from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime


@dataclass
class Event:
    """Class for tracking event information"""

    name: str
    location: dict
    offers: dict
    start_date: str
    end_date: str


class Event2(BaseModel):
    """"""

    name: str
    location: Location
    offers: dict
    start_date: datetime
    end_date: datetime

class Location(BaseModel):
    """"""
    address: Address
    name: str

@dataclass
class Place:
    """class for places"""

    address: dict
    name: str


@dataclass
class Address:
    """class for addresses"""

    content: str
    locality: str
    region: str
    postal_code: str
    street: str


@dataclass
class Offer:
    """class for offers"""

    content: str
    price: str
    currency: str
    url: str
