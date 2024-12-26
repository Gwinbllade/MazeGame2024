from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk

class GameSettingWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()
        title_label: tk.Label = tk.Label(self._current_window_frame, text="Maze Game", font=(MAIN_FONT, 100, "bold"))
        title_label.pack(pady=50)

        difficulty: dict[str: [int]] = {
            "Hard": [105, 105, 300],
            "Medium": [75, 75, 200],
            "Easy": [25, 25, 50],
        }


        for difficulty_name in difficulty:
            difficulty_value:[int] = difficulty[difficulty_name]
            width:int = difficulty_value[0]
            height:int = difficulty_value[1]
            score_multiplier:int = difficulty_value[2]

            tk.Button(self._current_window_frame, text=difficulty_name, width="20", font=(MAIN_FONT, 16),
                      command = lambda w=width, h=height: self._windows["Game window"].show_window(w, h, score_multiplier)) .pack(pady=10)


        menu_button: tk.Button = tk.Button(self._current_window_frame, text="Menu", width="20", font=(MAIN_FONT, 16),
                                command=self._windows["Menu"].show_window)
        menu_button.pack(pady=40)