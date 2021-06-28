from enum import Enum


class ProductType(Enum):
    JEWEL = '000'
    BOOK = '111'
    ELETRONIC = '333'
    DRINK = '555'
    TOY = '888'


class Region(Enum):
    SOUTH = '000'
    MIDWEST = '111'
    NORTH_EAST = '333'
    NORTH = '555'
    SOUTH_EAST = '888'
