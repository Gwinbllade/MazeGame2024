from src.const import GAME_DIFFICULTY, GAME_NAME_FONT, GAME_NAME
from src.interface.widgets.custom_button import CustomButton
from src.interface.windows.window import Window




class GameSettingWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()

        self._bg_canvas.create_text(self._root.winfo_screenwidth() // 2, 100, text=GAME_NAME,
                                    font=GAME_NAME_FONT)

        start_y = 300

        for i, (difficulty_name, values) in enumerate(GAME_DIFFICULTY.items()):
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
                                   y=start_y + len(GAME_DIFFICULTY) * 80 + 40,
                                   master=self._bg_canvas,
                                   callback=lambda: self._windows["Menu"].show_window())