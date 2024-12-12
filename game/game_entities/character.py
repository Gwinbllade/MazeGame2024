class Character:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._move_spead = 1


    def get_coord(self):
        return self._x, self._y

    def set_coord(self, coord):
        self._x = coord[0]
        self._y = coord[1]

    def move(self, direction):
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