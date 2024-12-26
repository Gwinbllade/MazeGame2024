from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window
import tkinter as tk

class GameSettingWindow(Window):
    def _show_window(self, **kwargs):
        self._clear_current_view()

        difficulty = {
            "Hard": [105, 105, 300],
            "Medium": [75, 75, 200],
            "Easy": [25, 25, 50],
        }

        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game",
                                    font=(MAIN_FONT, 100, "bold"))

        start_y = 300
        for i, (difficulty_name, values) in enumerate(difficulty.items()):
            width, height, score_multiplier = values


            button_text = self._bg_canvas.create_text(
                self._root.winfo_screenwidth() // 2,
                start_y + i * 80,
                text=difficulty_name,
                font=(MAIN_FONT, 25),
                fill="black",
                tags="difficulty_button"
            )


            self._bg_canvas.tag_bind(button_text, "<Button-1>",
                                     lambda e, w=width, h=height, s=score_multiplier:
                                     self._windows["Game window"]._show_window(width=w, height=h, score_multiplier=s))


            self._bg_canvas.tag_bind(button_text, "<Enter>",
                                     lambda e, t=button_text: self._bg_canvas.itemconfig(t, fill="purple"))
            self._bg_canvas.tag_bind(button_text, "<Leave>",
                                     lambda e, t=button_text: self._bg_canvas.itemconfig(t, fill="black"))
  # Меню
        menu_button_text = self._bg_canvas.create_text(
            self._root.winfo_screenwidth() // 2,
            start_y + len(difficulty) * 80 + 40,
            text="Menu",
            font=(MAIN_FONT, 25),
            fill="black",
            tags="menu_button"
        )


        self._bg_canvas.tag_bind(menu_button_text, "<Button-1>", lambda e: self._windows["Menu"]._show_window())


        self._bg_canvas.tag_bind(menu_button_text, "<Enter>",
                                 lambda e, t=menu_button_text: self._bg_canvas.itemconfig(t, fill="purple"))
        self._bg_canvas.tag_bind(menu_button_text, "<Leave>",
                                 lambda e, t=menu_button_text: self._bg_canvas.itemconfig(t, fill="black"))
