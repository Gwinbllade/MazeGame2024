import os
import time
from enum import Enum
from tkinter import Canvas, Label

from .game_entities.cell import Cell
from .game_entities.maze import Maze
from .game_entities.player import Player
import subprocess
from typing import Tuple

os.environ["PATH"] += r";C:\msys64\ucrt64\bin"


OUTLINE_COLOR = "black"
PLAYER_COLOR = "red"
MAZE_MAP_FILE = "./app_file/maze_map.txt"
MAZE_CONFIG_MAP = "./app_file/maze_config.txt"
FPS = 60

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
    def __init__(self, width: int, height: int, score_multiplier: int, screen: Canvas):
        self.start_time: int = 0
        self.offset_x: int = 0
        self.offset_y: int = 0
        self.cell_size: int = 0
        self.__maze: Maze = Maze()
        self.__generate_maze(width, height)
        self.__player: Player = Player()
        self.__player.set_coord(self.__maze.coord_start)
        self.__score_multiplier:int = score_multiplier
        self.__screen: Canvas = screen


    def move_player(self, direction: str):
        player_current_x: int
        player_current_y: int

        player_current_x, player_current_y = self.__player.get_coord()
        match direction:
            case 'up'   : new_coord: Tuple[int, int] = (player_current_x, player_current_y+1)
            case 'down' : new_coord: Tuple[int, int] = (player_current_x, player_current_y-1)
            case 'left' : new_coord: Tuple[int, int] = (player_current_x-1, player_current_y)
            case 'right': new_coord: Tuple[int, int] = (player_current_x+1, player_current_y)
            case _      : new_coord: Tuple[int, int] = (player_current_x, player_current_y)

        new_x:int
        new_y:int
        new_x, new_y = new_coord

        if not self.__out_of_bounds(new_coord) and self.__maze.get_cell(new_x, new_y).type != 'w':
            self.__player.move(direction)
            self.__draw_player()


    def __draw_player(self):
        # Render new player`s position

        current_player_x: int
        current_player_y: int

        current_player_x, current_player_y = self.__player.get_coord()
        self.__draw_rect(current_player_x, current_player_y, PLAYER_COLOR)

        # Clear old player's position
        old_player_x: int | None
        old_player_y: int | None

        old_player_x, old_player_y = self.__player.get_old_coord()
        if old_player_x is not None:
            self.__draw_rect(old_player_x, old_player_y, CellColor.PASS.value)


    def __out_of_bounds(self, coord: Tuple[int, int]) -> bool:
        if coord[0]<0 or coord[0]>self.__maze.width-1 or coord[1]<0 or coord[1]>self.__maze.height-1:
            return True
        return False

    def __draw_maze(self):
        self.__screen.delete("all")
        # Render maze cells
        for x in range(self.__maze.width):
            for y in range(self.__maze.width):
                cell: Cell = self.__maze.get_cell(x, y)

                match cell.type:
                    case CellType.PASS.value:
                        color:str = CellColor.PASS.value
                    case CellType.WALL.value:
                        color:str = CellColor.WALL.value
                    case CellType.FINISH.value:
                        color:str = CellColor.FINISH.value
                    case _:
                        color:str = CellColor.DEFAULT.value
                self.__draw_rect(x, y, color)
        self.__screen.update()


    def render(self, time_label: Label):
        self.__update_time(time_label)
        self.__screen.update()

    def __draw_rect(self, x: int, y: int, bg_color: str):
        x1: int = self.offset_x + x * self.cell_size
        y1: int = self.offset_y + (self.__maze.width - 1 - y) * self.cell_size  # Invert y-coordinate
        x2: int = x1 + self.cell_size
        y2: int = y1 + self.cell_size
        self.__screen.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=OUTLINE_COLOR)

    def check_win(self):
        x, y = self.__player.get_coord()
        if self.__maze.get_cell(x,y).type == "e":
            return True


    def __calc_game_session_values(self):
        self.__screen.update()
        canvas_width: int = self.__screen.winfo_width()
        canvas_height: int = self.__screen.winfo_height() - 70

        self.cell_size: float = min(canvas_width / self.__maze.width, canvas_height / self.__maze.width)

        # Calculate total maze render size
        total_maze_width: float = self.cell_size * self.__maze.width
        total_maze_height: float = self.cell_size * self.__maze.width

        # Calculate offset to center the maze
        self.offset_x:float = (canvas_width - total_maze_width) / 2
        self.offset_y:float = (canvas_height - total_maze_height) / 2



    def __generate_maze(self, width: int, height: int):
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



    def game_loop(self, time_label: Label) -> Tuple[str, int]:
        is_win: bool = False
        self.start_time: float = time.time()
        self.__calc_game_session_values()
        self.__draw_maze()
        self.__draw_player()
        while not is_win:
            time.sleep(1 / FPS)
            self.render(time_label)
            is_win = self.check_win()


        elapsed_time:int = int(time.time() - self.start_time)
        game_time:str = self.__format_time(elapsed_time)
        score:int = int((self.__score_multiplier*self.__maze.width*self.__maze.height) / elapsed_time if elapsed_time > 0 else 1)
        return game_time, score

    @staticmethod
    def __format_time(seconds: int) -> str:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"


    def __update_time(self, time_label: Label):
        elapsed_time: int = int(time.time() - self.start_time)
        time_label.config(text=self.__format_time(elapsed_time))
