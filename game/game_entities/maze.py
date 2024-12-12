from game.game_entities.cell import Cell


class Maze:
    def __init__(self):
        self.__game_map = []
        self.__width = 0
        self.__height = 0
        self.__coord_start = (0, 0)


    def load_game_map(self, file_name):
        with open(file_name, "r") as file:
            data = file.read().split("\n")
            self.__height = int(data.pop(0))
            self.__width = int(data.pop(0))
            for i in range(0, self.__height):
                self.__game_map.append([])
                for j in range(0, self.__width):

                    if len(data) == 0:
                        self.__game_map[i].append(Cell(0, 0, "p"))
                        continue


                    cell_entry = data.pop(0).split(" ")

                    x = int(cell_entry[0])
                    y = int(cell_entry[1])
                    cell_type = cell_entry[2][0]
                    self.__game_map[i].append(Cell(x, y, cell_type))
                    if cell_type == "s":
                        self.__coord_start = (x, y)


    @property
    def coord_start(self):
        return self.__coord_start

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def get_cell(self, x, y):
        return self.__game_map[x][y]