from game.game_entities.character import Character

class Player(Character):
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
