from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk

class MenuWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()
        title_label:tk.Label = tk.Label(self._current_window_frame, text="Maze Game", font=(MAIN_FONT, 100, "bold"))
        title_label.pack(pady=50)

        #Start game button
        tk.Button(self._current_window_frame, text="Start Game", width="20", font=(MAIN_FONT, 16),
                                 command=self._windows["Game setting"].show_window).pack(pady=20)

        #Leaderboard button
        tk.Button(self._current_window_frame, text="Leaderboard", width="20",
                                       font=(MAIN_FONT, 16), command=self._windows["Leader board"].show_window).pack(pady=20)

        #About button
        tk.Button(self._current_window_frame, text="About ", width="20", font=(MAIN_FONT, 16)).pack(pady=20)

        #Quit button
        tk.Button(self._current_window_frame, text="Quit", width="20", font=(MAIN_FONT, 16),
                                command=lambda: self._root.quit()).pack(pady=20)
