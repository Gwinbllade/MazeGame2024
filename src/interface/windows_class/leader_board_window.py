from src.interface.custom_button import CustomButton
from src.interface.table import Table
from src.interface.windows_class.window import Window
import tkinter as tk

from src.user_record.user_results import UserResults


class LeaderBoardWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()


        table_frame = tk.Frame(self._bg_canvas)
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            250,
            window=table_frame
        )


        table = Table(table_frame)
        table.create_table(("N", "Name", "Time", "Score"), None).pack(pady=20, anchor="center")


        user_results = UserResults()
        table.insert_data(user_results.get_top_10())

        CustomButton.create_button(
            button_name="Back to Menu",
            x=self._root.winfo_screenwidth() // 2,
            y=500,
            master=self._bg_canvas,
            callback= lambda: self._windows["Menu"].show_window()
        )