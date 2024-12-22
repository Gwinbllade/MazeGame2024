import time
from enum import Enum
from game.game_entities.cell import Cell
from game.game_logic import GameLogic, CellType
import tkinter as tk


OUTLINE_COLOR = "black"
PLAYER_COLOR = "red"
FPS = 144


class CellColor(Enum):
    WALL = "black"
    PASS = "white"
    FINISH = "blue"
    DEFAULT = "green"




class GameRender:
    def __init__(self, game_logic: GameLogic, window: tk.Frame, root: tk.Tk):
        self.__window = window
        self.__game_logic = game_logic
        self.__offset_x: int = 0
        self.__offset_y: int = 0
        self.__cell_size: int = 0
        self.__root = root

        self.__screen = tk.Canvas(self.__window)
        self.__screen.pack(fill=tk.BOTH, expand=True)

        self.__time_label: tk.Label = tk.Label(self.__window, text="00:00:00", font=("Helvetica", 30), bg="white")
        self.__time_label.place(x=10, y=10)


    def __add_event_handle(self):
        up_button_move: [str] = ["w", "up"]
        left_button_move: [str] = ["a", "left"]
        right_button_move: [str] = ["d", "right"]
        down_button_move: [str] = ["s", "down", ]

        def handle_key_press(event):
            key:str = event.keysym.lower()
            if key in up_button_move:
                self.__game_logic.move_player('up')
            elif key in left_button_move:
                self.__game_logic.move_player('left')
            elif key in down_button_move:
                self.__game_logic.move_player('down')
            elif key in right_button_move:
                self.__game_logic.move_player('right')
            self.__draw_player() #todo make better


        self.__root.bind("<KeyPress>", handle_key_press)


    def __draw_player(self):
        # Render new player`s position

        current_player_x: int
        current_player_y: int

        current_player_x, current_player_y = self.__game_logic.player.get_coord()
        self.__draw_rect(current_player_x, current_player_y, PLAYER_COLOR)

        # Clear old player's position
        old_player_x: int | None
        old_player_y: int | None

        old_player_x, old_player_y = self.__game_logic.player.get_old_coord()
        if old_player_x is not None:
            self.__draw_rect(old_player_x, old_player_y, CellColor.PASS.value)


    def __draw_maze(self):
        self.__screen.delete("all")
        # Render maze cells
        for x in range(self.__game_logic.maze.width):
            for y in range(self.__game_logic.maze.width):
                cell: Cell = self.__game_logic.maze.get_cell(x, y)
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


    def __calc_game_session_values(self):
        self.__screen.update()
        canvas_width: int = self.__screen.winfo_width()
        canvas_height: int = self.__screen.winfo_height() - 70

        self.__cell_size: float = min(canvas_width / self.__game_logic.maze.width, canvas_height / self.__game_logic.maze.height)

        # Calculate total maze render size
        total_maze_width: float = self.__cell_size * self.__game_logic.maze.width
        total_maze_height: float = self.__cell_size * self.__game_logic.maze.height

        # Calculate offset to center the maze
        self.__offset_x:float = (canvas_width - total_maze_width) / 2
        self.__offset_y:float = (canvas_height - total_maze_height) / 2


    def render(self):
        self.__update_time_label()
        self.__screen.update()


    def start_loop(self):
        self.__calc_game_session_values()
        self.__add_event_handle()
        self.__draw_maze()
        self.__draw_player()
        sleep_time:float = 1 / FPS
        while not self.__game_logic.is_win():
            time.sleep(sleep_time)
            self.render()


        self.__root.unbind("<KeyPress>")


    def __draw_rect(self, x: int, y: int, bg_color: str):
        x1: int = self.__offset_x + x * self.__cell_size
        y1: int = self.__offset_y + (self.__game_logic.maze.width - 1 - y) * self.__cell_size  # Invert y-coordinate
        x2: int = x1 + self.__cell_size
        y2: int = y1 + self.__cell_size
        self.__screen.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=OUTLINE_COLOR)


    def __update_time_label(self):
        self.__time_label.config(text=self.__game_logic.get_format_time())