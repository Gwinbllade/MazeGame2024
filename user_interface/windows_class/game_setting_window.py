from user_interface.windows_class.window import Window
import tkinter as tk

class GameSettingWindow(Window):
    def show_window(self, *args):
        self._clear_current_view()
        title_label = tk.Label(self._current_window_frame, text="Maze Game", font=("Helvetica", 100, "bold"))
        title_label.pack(pady=50)

        difficulty = {
            "Hard": [45, 45, 300],
            "Medium": [25, 25, 200],
            "Easy": [15, 15, 50],
        }


        for difficulty_name in difficulty:
            difficulty_value = difficulty[difficulty_name]
            width = difficulty_value[0]
            height = difficulty_value[1]
            score_multiplier = difficulty_value[2]

            tk.Button(self._current_window_frame, text=difficulty_name, width="20", font=("Helvetica", 16),
                      command = lambda w=width, h=height: self._windows["Game window"].show_window(w, h, score_multiplier)) .pack(pady=10)


        menu_button = tk.Button(self._current_window_frame, text="Menu", width="20", font=("Helvetica", 16),
                                command=self._windows["Menu"].show_window)
        menu_button.pack(pady=40)