from interface.table import Table
from interface.windows_class.window import Window
import tkinter as tk

from user_record.user_results import UserResults




class LeaderBoardWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()

        table: Table = Table(self._current_window_frame)
        table.create_table(("N", "Name", "Time", "Score"), None).pack(pady=20, anchor="center")

        user_results: UserResults = UserResults("app_file/results.txt")
        table.insert_data(user_results.get_top_10())

        # Menu button
        tk.Button(self._current_window_frame, text="Back to Menu", font=("Helvetica", 16),
                                command=self._windows["Menu"].show_window).pack(pady=20, anchor="center")
