from src.const import MAIN_FONT_NAME, MAIN_FONT
from src.interface.widgets.custom_button import CustomButton
from src.interface.windows.window import Window
import tkinter as tk
from src.user_record.user_results import UserResults


class WinWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()
        game_time: str = kwargs['game_time']
        score: int = kwargs['score']


        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 150,
                                    text=f"You win.\n  Your number of points: {score}.\n Time: {game_time}\nEnter your name",
                                    font=(MAIN_FONT_NAME, 50, "bold"), justify="center", fill="white")


        name_entry = tk.Entry(
            self._bg_canvas,
            font=MAIN_FONT,
            justify="center"
        )
        self._bg_canvas.create_window(
            self._root.winfo_screenwidth() // 2,
            350,
            window=name_entry
        )

        CustomButton.create_button(
            button_name="Save",
            x=self._root.winfo_screenwidth() // 2,
            y=450,
            master=self._bg_canvas,
            callback=lambda : (
                            UserResults.save_result(name_entry.get(), game_time, score),
                            self._windows["Menu"].show_window())
        )