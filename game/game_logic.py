import os
import time
from .game_entities.maze import Maze
from .game_entities.player import Player
import subprocess

os.environ["PATH"] += r";C:\msys64\ucrt64\bin"

WALL_COLOR = "black"
PASS_COLOR = "white"
FINISH_COLOR = "blue"
OUTLINE_COLOR = "gray"
PLAYER_COLOR = "red"
MAZE_MAP_FILE = "./app_file/maze_map.txt"
MAZE_CONFIG_MAP = "./app_file/maze_config.txt"

class GameLogic:
    def __init__(self, width, height, score_multiplier):
        self.start_time = None
        self.offset_x = None
        self.offset_y = None
        self.cell_size = None
        self.__maze = Maze()
        self.__generate_maze(width, height)
        self.__player = Player()
        self.__player.set_coord(self.__maze.coord_start)
        self.__score_multiplier = score_multiplier

    def move_player(self, direction):
        player_current_coord = self.__player.get_coord()
        match direction:
            case 'up'   : new_coord = (player_current_coord[0], player_current_coord[1]+1)
            case 'down' : new_coord = (player_current_coord[0], player_current_coord[1]-1)
            case 'left' : new_coord = (player_current_coord[0]-1, player_current_coord[1])
            case 'right': new_coord = (player_current_coord[0]+1, player_current_coord[1])
            case _      : new_coord = (player_current_coord[0], player_current_coord[1])

        if not self.out_of_bounds(new_coord) and self.__maze.get_cell(new_coord[0],new_coord[1]).type != 'w':
            self.__player.move(direction)


    def out_of_bounds(self, coord):
        if coord[0]<0 or coord[0]>self.__maze.width-1 or coord[1]<0 or coord[1]>self.__maze.height-1:
            return True
        return False

    def render(self, screen, time_label):
        self.__update_time(time_label)
        # Wait for screen to be fully sized
        screen.update()
        self.calc_game_session_values(screen)
        screen.delete("all")

        # Render maze cells
        for x in range(self.__maze.width):
            for y in range(self.__maze.width):
                cell = self.__maze.get_cell(x,y)

                match cell.type:
                    case "p": color = PASS_COLOR
                    case "w": color = WALL_COLOR
                    case "e": color = FINISH_COLOR
                    case _  : color = "green"


                self.__draw_rect(screen, x, y, color)

        # Render player
        player_x = self.__player.get_coord()[0]
        player_y = self.__player.get_coord()[1]
        self.__draw_rect(screen, player_x, player_y, PLAYER_COLOR)



    def __draw_rect(self, screen, x, y, bg_color):
        x1 = self.offset_x + x * self.cell_size
        y1 = self.offset_y + (self.__maze.width - 1 - y) * self.cell_size  # Invert y-coordinate
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        screen.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=OUTLINE_COLOR)

    def check_win(self):
        player_coord = self.__player.get_coord()
        x = player_coord[0]
        y = player_coord[1]
        if self.__maze.get_cell(x,y).type == "e":
            return True


    def calc_game_session_values(self, screen):
        canvas_width = screen.winfo_width()
        canvas_height = screen.winfo_height() - 70

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



    def game_loop(self, canvas, time_label):
        is_win = False
        self.start_time = time.time()

        while not is_win:
            self.render(canvas, time_label)
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
