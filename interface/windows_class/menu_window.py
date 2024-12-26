from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window


class MenuWindow(Window):
    def _show_window(self, **kwargs):
        self._clear_current_view()


        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game",
                                    font=(MAIN_FONT, 100, "bold"))


        buttons_config = [
            ("Start Game", lambda: self._windows["Game setting"]._show_window()),
            ("Leaderboard", lambda: self._windows["Leader board"]._show_window()),
            ("About", lambda: None),
            ("Quit", lambda: self._root.quit())
        ]


        start_y = 300
        for i, (text, command) in enumerate(buttons_config):
            button_text = self._bg_canvas.create_text(
                self._root.winfo_screenwidth() // 2,
                start_y + i * 100,
                text=text,
                font=(MAIN_FONT, 25),
                fill="black",
                tags="button"
            )


            self._bg_canvas.tag_bind(button_text, "<Button-1>", lambda e, cmd=command: cmd())

            # Додаємо ефекти наведення
            self._bg_canvas.tag_bind(button_text, "<Enter>", lambda e, t=button_text: self._bg_canvas.itemconfig(t, fill="purple"))
            self._bg_canvas.tag_bind(button_text, "<Leave>", lambda e, t=button_text: self._bg_canvas.itemconfig(t, fill="black"))
