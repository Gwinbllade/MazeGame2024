from interface.interface_const import MAIN_FONT, BG_PATH
from interface.table import Table
from interface.windows_class.window import Window
import tkinter as tk

from user_record.user_results import UserResults


class LeaderBoardWindow(Window):
    def _show_window(self, **kwargs):
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


        back_button_text = self._bg_canvas.create_text(
            self._root.winfo_screenwidth() // 2,
            500,
            text="Back to Menu",
            font=(MAIN_FONT, 25),
            fill="black",
            tags="back_button"
        )


        self._bg_canvas.tag_bind(back_button_text, "<Button-1>", lambda e: self._windows["Menu"]._show_window())


        self._bg_canvas.tag_bind(back_button_text, "<Enter>",
                                  lambda e, t=back_button_text: self._bg_canvas.itemconfig(t, fill="purple"))
        self._bg_canvas.tag_bind(back_button_text, "<Leave>",
                                  lambda e, t=back_button_text: self._bg_canvas.itemconfig(t, fill="black"))
