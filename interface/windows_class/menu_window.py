from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk
class MenuWindow(Window):
    def _show_window(self, *args):
        self._clear_current_view()


        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game", font=(MAIN_FONT, 100, "bold"))


        buttons = [
            ("Start Game", lambda: self._windows["Game setting"]._show_window()),
            ("Leaderboard", lambda: self._windows["Leader board"]._show_window()),
            ("About", lambda: None),
            ("Quit", lambda: self._root.quit())
        ]


        start_y = 300
        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self._bg_canvas,
                               text=text,
                               width=20,
                               font=(MAIN_FONT, 16),
                               command=command)

            self._bg_canvas.create_window(
                self._root.winfo_screenwidth() // 2,  #
                start_y + i * 100,
                window=button
            )