from src.const import MAIN_FONT_NAME
from src.interface.widgets.custom_button import CustomButton
from src.interface.windows.window import Window


class MenuWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()


        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game",
                                    font=(MAIN_FONT_NAME, 100, "bold"))


        buttons_config = [
            ("Start Game", lambda: self._windows["Game setting"].show_window()),
            ("Leaderboard", lambda: self._windows["Leader board"].show_window()),
            ("About", lambda: None), #todo
            ("Quit", lambda: self._root.quit())
        ]


        start_y = 300
        for i, (button_name, callback) in enumerate(buttons_config):
            CustomButton.create_button(button_name, self._root.winfo_screenwidth() // 2, start_y + i * 100, self._bg_canvas, callback)
