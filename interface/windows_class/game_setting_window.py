from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk

class GameSettingWindow(Window):
    def _show_window(self, *args):
        self._clear_current_view()

        difficulty = {
            "Hard": [105, 105, 300],
            "Medium": [75, 75, 200],
            "Easy": [25, 25, 50],
        }

        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game",
                                    font=(MAIN_FONT, 100, "bold"))




        start_y = 300
        for i, (difficulty_name, values) in enumerate(difficulty.items()):
            width, height, score_multiplier = values

            button = tk.Button(
                self._bg_canvas,
                text=difficulty_name,
                width=20,
                font=(MAIN_FONT, 16),
                command=lambda w=width, h=height, s=score_multiplier:
                self._windows["Game window"]._show_window(w, h, s)
            )

            self._bg_canvas.create_window(
                self._root.winfo_screenwidth() // 2,
                start_y + i * 80,
                window=button
            )


        menu_button = tk.Button(
            self._bg_canvas,
            text="Menu",
            width=20,
            font=(MAIN_FONT, 16),
            command=self._windows["Menu"]._show_window
        )

        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            start_y + len(difficulty) * 80 + 40,
            window=menu_button
        )