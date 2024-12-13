import os
import time
from enum import Enum

from .game_entities.maze import Maze
from .game_entities.player import Player
import subprocess

os.environ["PATH"] += r";C:\msys64\ucrt64\bin"


OUTLINE_COLOR = "black"
PLAYER_COLOR = "red"
MAZE_MAP_FILE = "./app_file/maze_map.txt"
MAZE_CONFIG_MAP = "./app_file/maze_config.txt"

class CellType(Enum):
    WALL = "w"
    PASS = "p"
    FINISH = "e"

class CellColor(Enum):
    WALL = "black"
    PASS = "white"
    FINISH = "blue"
    DEFAULT = "green"


class GameLogic:
    def __init__(self, width, height, score_multiplier, screen):
        self.start_time = None
        self.offset_x = None
        self.offset_y = None
        self.cell_size = None
        self.__maze = Maze()
        self.__generate_maze(width, height)
        self.__player = Player()
        self.__player.set_coord(self.__maze.coord_start)
        self.__score_multiplier = score_multiplier
        self.__screen = screen


    def move_player(self, direction):
        player_current_coord = self.__player.get_coord()
        match direction:
            case 'up'   : new_coord = (player_current_coord[0], player_current_coord[1]+1)
            case 'down' : new_coord = (player_current_coord[0], player_current_coord[1]-1)
            case 'left' : new_coord = (player_current_coord[0]-1, player_current_coord[1])
            case 'right': new_coord = (player_current_coord[0]+1, player_current_coord[1])
            case _      : new_coord = (player_current_coord[0], player_current_coord[1])

        new_x, new_y = new_coord

        if not self.__out_of_bounds(new_coord) and self.__maze.get_cell(new_x, new_y).type != 'w':
            self.__player.move(direction)


    def __out_of_bounds(self, coord):
        if coord[0]<0 or coord[0]>self.__maze.width-1 or coord[1]<0 or coord[1]>self.__maze.height-1:
            return True
        return False

    def __draw_maze(self):
        self.__screen.delete("all")
        # Render maze cells
        for x in range(self.__maze.width):
            for y in range(self.__maze.width):
                cell = self.__maze.get_cell(x, y)

                match cell.type:
                    case CellType.PASS.value:
                        color = CellColor.PASS.value
                    case CellType.WALL.value:
                        color = CellColor.WALL.value
                    case CellType.FINISH.value:
                        color = CellColor.FINISH.value
                    case _:
                        color = CellColor.DEFAULT.value

                self.__draw_rect(x, y, color)
        self.__screen.update()


    def render(self, time_label):
        self.__update_time(time_label)
        self.__screen.update()

        # Render new player`s position
        current_player_x, current_player_y = self.__player.get_coord()
        self.__draw_rect(current_player_x, current_player_y, PLAYER_COLOR)

        # Clear old player's position
        old_player_x, old_player_y = self.__player.get_old_coord()
        if old_player_x is not None:
            self.__draw_rect(old_player_x, old_player_y, CellColor.PASS.value)




    def __draw_rect(self, x, y, bg_color):
        x1 = self.offset_x + x * self.cell_size
        y1 = self.offset_y + (self.__maze.width - 1 - y) * self.cell_size  # Invert y-coordinate
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.__screen.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=OUTLINE_COLOR)

    def check_win(self):
        x, y = self.__player.get_coord()
        if self.__maze.get_cell(x,y).type == "e":
            return True


    def __calc_game_session_values(self):
        self.__screen.update()
        canvas_width = self.__screen.winfo_width()
        canvas_height = self.__screen.winfo_height() - 70

        self.cell_size = min(canvas_width / self.__maze.width, canvas_height / self.__maze.width)

        # Calculate total maze render size
        total_maze_width = self.cell_size * self.__maze.width
        total_maze_height = self.cell_size * self.__maze.width

        # Calculate offset to center the maze
        self.offset_x = (canvas_width - total_maze_width) / 2
        self.offset_y = (canvas_height - total_maze_height) / 2



    def __generate_maze(self, width, height):
        with open(MAZE_CONFIG_MAP, "w") as f:
            f.write(str(width) + " " + str(height))

        command = [
            "cd", r"d:\Проекти\MazeGame\maze_generator",
            "&&", "g++", "MazeGenerator.cpp", "-o", "MazeGenerator",
            "&&", r"d:\Проекти\MazeGame\maze_generator\MazeGenerator"
        ]
        subprocess.run(
            " ".join(command),
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        self.__maze.load_game_map(MAZE_MAP_FILE)



    def game_loop(self, time_label):
        is_win = False
        self.start_time = time.time()
        self.__calc_game_session_values()
        self.__draw_maze()
        while not is_win:
            self.render(time_label)
            is_win = self.check_win()


        elapsed_time = int(time.time() - self.start_time)
        game_time = self.__format_time(elapsed_time)
        score = int((self.__score_multiplier*self.__maze.width*self.__maze.height) / elapsed_time if elapsed_time > 0 else 1)
        return game_time, score

    @staticmethod
    def __format_time(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"


    def __update_time(self, time_label):
        elapsed_time = int(time.time() - self.start_time)
        time_label.config(text=self.__format_time(elapsed_time))
