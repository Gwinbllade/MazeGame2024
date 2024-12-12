from user_interface.table import Table
from user_interface.windows_class.window import Window
import tkinter as tk

from user_record.user_results import UserResults




class LeaderBoardWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()

        table = Table(self._current_window_frame)
        table.create_table(("N", "Name", "Time", "Score"), None).pack(pady=20, anchor="center")

        user_results = UserResults("app_file/results.txt")
        table.insert_data(user_results.get_top_10())

        # Кнопка для повернення до меню
        back_button = tk.Button(self._current_window_frame, text="Back to Menu", font=("Helvetica", 16),
                                command=self._windows["Menu"].show_window)
        back_button.pack(pady=20, anchor="center")  # Зробимо кнопку по центру