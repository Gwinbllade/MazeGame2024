from game.game_entities.character import Character

class Player(Character):
    def __init__(self):
        super().__init__()
        self.__old_x = None
        self.__old_y = None

    def get_old_coord(self):
        return self.__old_x, self.__old_y

    def move(self, direction):
        self.__old_x = self._x
        self.__old_y = self._y
        match direction:
            case "up":
                self._y+=1
            case "down":
                self._y-=1
            case "left":
                self._x-=1
            case "right":
                self._x+=1
            case _:
                pass
