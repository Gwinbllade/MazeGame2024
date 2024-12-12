from user_interface.windows_class.window import Window
import tkinter as tk

class MenuWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()
        title_label = tk.Label(self._current_window_frame, text="Maze Game", font=("Helvetica", 100, "bold"))
        title_label.pack(pady=50)

        start_button = tk.Button(self._current_window_frame, text="Start Game", width="20", font=("Helvetica", 16),
                                 command=self._windows["Game setting"].show_window)
        start_button.pack(pady=20)

        leaderboard_button = tk.Button(self._current_window_frame, text="Leaderboard", width="20",
                                       font=("Helvetica", 16), command=self._windows["Leader board"].show_window)
        leaderboard_button.pack(pady=20)

        settings_button = tk.Button(self._current_window_frame, text="About ", width="20", font=("Helvetica", 16))
        settings_button.pack(pady=20)

        quit_button = tk.Button(self._current_window_frame, text="Quit", width="20", font=("Helvetica", 16),
                                command=lambda: self._root.quit())
        quit_button.pack(pady=20)