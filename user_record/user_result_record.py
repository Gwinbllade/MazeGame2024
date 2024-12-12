
class UserResultRecord:
    def __init__(self, data):
        data = data.split('#')
        self.__name = data[0]
        self.__time = data[1]
        self.__score = int(data[2])

    def __str__(self):
        return f"{self.__name}#{self.__time}#{self.__score}"

    @property
    def score(self):
        return self.__score

    @property
    def name(self):
        return self.__name

    @property
    def time(self):
        return self.__time

    def __lt__(self, other):
        return self.score > other.score


