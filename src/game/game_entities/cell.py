from enum import Enum
from typing import Tuple


class CellColor(Enum):
    WALL = "black"
    PASS = "white"
    FINISH = "blue"
    DEFAULT = "green"

class CellType(Enum):
    WALL = "w"
    PASS = "p"
    FINISH = "e"


class Cell:
    def __init__(self, x: int, y: int, cell_type: str = "p"):

        self.__x: int = x
        self.__y: int = y
        self.__type: str = cell_type


    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    def get_coord(self) -> Tuple[int, int]:
        return self.__x, self.__y


