from user_interface.windows_class.window import Window
import tkinter as tk

from user_record.user_result_record import UserResultRecord
from user_record.user_results import UserResults


class WinWindow(Window):
    def show_window(self, game_time,  score):
        self._clear_current_view()
        tk.Label(self._current_window_frame,
                             text=f"Ви виграли.\n Ваша кількість очок: {score}.\n Час:{game_time}\nВведіть своє ім'я",
                             font=("Helvetica", 40), wraplength=800, justify="center").pack(pady=20)

        # Поле для введення імені
        name_entry = tk.Entry(self._current_window_frame, font=("Helvetica", 16), justify="center")
        name_entry.pack(pady=20)


        tk.Button(self._current_window_frame, text="Зберегти", font=("Helvetica", 16),
                                command=lambda: (
                                UserResults.save_result(name_entry.get(),
                                game_time, score),
                                self._windows["Menu"].show_window())).pack(pady=20)
