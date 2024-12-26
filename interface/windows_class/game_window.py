from game.game_logic import GameLogic
from game.game_render import GameRender
from interface.windows_class.window import Window


class GameWindow(Window):
    def _show_window(self, width, height, score_multiplier):
        self._clear_current_view()

        game_logic:GameLogic = GameLogic(width, height, score_multiplier)
        game_render: GameRender = GameRender(game_logic, self._current_window_frame, self._root, self._bg_canvas)

        game_render.start_loop()

        game_time:str = game_logic.get_format_time()
        score:int = game_logic.get_score()

        self._windows["Win window"]._show_window(game_time, score)

