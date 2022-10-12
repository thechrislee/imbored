"""
Event information
"""
from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    """"""

    name: str
    location: Location
    offers: Offer
    start_date: datetime
    end_date: datetime


class Location(BaseModel):
    """"""

    address: Address
    name: str


class Address(BaseModel):
    """class for addresses"""

    content: str
    locality: str
    region: str
    postal_code: str
    street: str


class Offer(BaseModel):
    """class for offers"""

    content: str
    price: str
    currency: str
    url: str
