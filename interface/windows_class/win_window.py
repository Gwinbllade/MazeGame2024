from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk
from user_record.user_results import UserResults


class WinWindow(Window):
    def _show_window(self, **kwargs):
        self._clear_current_view()
        game_time: str = kwargs['game_time']
        score: int = kwargs['score']




        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 150, text=f"You win.\n  Your number of points: {score}.\n Time:{game_time}\nEnter your name",
                                   font=(MAIN_FONT, 50, "bold"), justify="center", fill="white")



        name_entry = tk.Entry(
            self._bg_canvas,
            font=(MAIN_FONT, 30),
            justify="center"
        )
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            350,
            window=name_entry
        )


        save_button = tk.Button(
            self._bg_canvas,
            text="Save",
            font=(MAIN_FONT, 16),
            command=lambda: (
                UserResults.save_result(name_entry.get(), game_time, score),
                self._windows["Menu"]._show_window()
            )
        )
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            450,
            window=save_button
        )