from interface.custom_button import CustomButton
from interface.interface_const import MAIN_FONT
from interface.windows_class.window import Window


DIFFICULTY = {
    "Hard": [105, 105, 300],
    "Medium": [75, 75, 200],
    "Easy": [25, 25, 50],
}

class GameSettingWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()



        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text="Maze Game",
                                    font=(MAIN_FONT, 100, "bold"))


        start_y = 300
        for i, (difficulty_name, values) in enumerate(DIFFICULTY.items()):
            width, height, score_multiplier = values

            CustomButton.create_button(button_name=difficulty_name,
                                       x=self._root.winfo_screenwidth() // 2,
                                       y=start_y + i * 80,
                                       master=self._bg_canvas,
                                       callback=lambda  w=width, h=height, s=score_multiplier:
                                            self._windows["Game window"].show_window(width=w, height=h, score_multiplier=s)
                                       )

        CustomButton.create_button(button_name="Meny",
                                   x=self._root.winfo_screenwidth() // 2,
                                   y=start_y + len(DIFFICULTY) * 80 + 40,
                                   master=self._bg_canvas,
                                   callback=lambda: self._windows["Menu"].show_window())
