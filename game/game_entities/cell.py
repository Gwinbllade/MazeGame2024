from typing import Tuple


class Cell:
    def __init__(self, x: int, y: int, type: str ="p"):

        self.__x: int = x
        self.__y: int = y
        self.__type: str = type


    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    def get_coord(self) -> Tuple[int, int]:
        return self.__x, self.__y


