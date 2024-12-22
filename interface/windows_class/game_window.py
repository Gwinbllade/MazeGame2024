from game.game_logic import GameLogic
from game.game_render import GameRender
from interface.windows_class.window import Window

class GameWindow(Window):
    def show_window(self, width, height, score_multiplier):
        self._clear_current_view()

        game_logic:GameLogic = GameLogic(width, height, score_multiplier)
        game_render: GameRender = GameRender(game_logic, self._current_window_frame, self._root)


        game_time:str
        score:int

        game_time, score = game_render.loop()
        self._windows["Win window"].show_window(game_time, score)

