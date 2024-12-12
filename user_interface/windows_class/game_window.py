from game.game_logic import GameLogic
from user_interface.windows_class.window import Window
import tkinter as tk


class GameWindow(Window):
    def show_window(self, width, height, score_multiplier):
        self._clear_current_view()

        up_button_move = ["w", "up"]
        left_button_move = ["a", "left"]
        right_button_move = ["d", "right"]
        down_button_move = ["s", "down",]


        canvas = tk.Canvas(self._current_window_frame)
        canvas.pack(fill=tk.BOTH, expand=True)

        time_label = tk.Label(self._current_window_frame, text="00:00:00", font=("Helvetica", 30), bg="white")
        time_label.place(x=10, y=10)

        game_logic = GameLogic(width, height, score_multiplier)

        def handle_keypress(event):
            key = event.keysym.lower()
            if key in up_button_move:
                game_logic.move_player('up')
            elif key in left_button_move:
                game_logic.move_player('left')
            elif key in down_button_move:
                game_logic.move_player('down')
            elif key in right_button_move:
                game_logic.move_player('right')

        self._root.bind("<KeyPress>", handle_keypress)
        game_time, score = game_logic.game_loop(canvas, time_label)
        self._root.unbind("<KeyPress>")

        self._windows["Win window"].show_window(game_time, score)

