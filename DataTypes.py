from enum import Enum
from typing import List, TypedDict

class ItemType(str, Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    TECH = "tech"

class Item(TypedDict):
    # id: int # TODO: Find a way to get the id
    name: str
    localization: str
    image: str
    tier: int
    type: ItemType

class Ability(TypedDict):
    # id: int # TODO: Find a way to get the id
    name: str
    image: str
    localization: str
    hero: str

class Hero(TypedDict):
    id: int
    name: str
    localization: str
    image: str
    abilities: List[{str, Ability}]
