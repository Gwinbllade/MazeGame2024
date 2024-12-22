import os
import time
from enum import Enum
from .game_entities.maze import Maze
from .game_entities.player import Player
import subprocess
from typing import Tuple

os.environ["PATH"] += r";C:\msys64\ucrt64\bin"
MAZE_MAP_FILE = "./app_file/maze_map.txt"
MAZE_CONFIG_MAP = "./app_file/maze_config.txt"

class CellType(Enum):
    WALL = "w"
    PASS = "p"
    FINISH = "e"



class GameLogic:
    def __init__(self, width: int, height: int, score_multiplier: int):
        self.__maze: Maze = Maze()
        self.__generate_maze(width, height)
        self.__player: Player = Player()
        self.__player.set_coord(self.__maze.coord_start)
        self.__score_multiplier:int = score_multiplier
        self.__start_time: float = time.time()

    def get_game_time(self):
        return int(time.time() - self.__start_time)

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def maze(self) -> Maze:
        return self.__maze

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
            print("Move")


    def __out_of_bounds(self, coord: Tuple[int, int]) -> bool:
        if coord[0]<0 or coord[0]>self.__maze.width-1 or coord[1]<0 or coord[1]>self.__maze.height-1:
            return True
        return False


    def check_win(self)->bool:
        x, y = self.__player.get_coord()
        if self.__maze.get_cell(x,y).type == "e":
            return True


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


    def get_score(self) ->int:
        elapsed_time:int = self.get_game_time()
        score: int = int((self.__score_multiplier * self.__maze.width * self.__maze.height) / elapsed_time if elapsed_time > 0 else 1)
        return score

