class Cell:
    def __init__(self, x, y, type ="p"):
        self.__x = x
        self.__y = y
        self.__type = type


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def get_coord(self):
        return self.__x, self.__y


