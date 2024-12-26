from interface.interface_const import MAIN_FONT, BG_PATH
from interface.table import Table
from interface.windows_class.window import Window
import tkinter as tk

from user_record.user_results import UserResults


class LeaderBoardWindow(Window):
    def _show_window(self, *args):
        self._clear_current_view()


        table_frame = tk.Frame(self._bg_canvas)
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            250,
            window=table_frame
        )

        # Створюємо таблицю
        table = Table(table_frame)
        table.create_table(("N", "Name", "Time", "Score"), None).pack(pady=20, anchor="center")


        user_results = UserResults()
        table.insert_data(user_results.get_top_10())

        # Кнопка повернення до меню
        menu_button = tk.Button(
            self._bg_canvas,
            text="Back to Menu",
            font=(MAIN_FONT, 16),
            command=self._windows["Menu"]._show_window
        )
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            500,  # Позиція Y для кнопки
            window=menu_button
        )