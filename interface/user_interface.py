import tkinter as tk

from interface.interface_const import BG_PATH
from interface.windows_class.game_setting_window import GameSettingWindow
from interface.windows_class.game_window import GameWindow
from interface.windows_class.leader_board_window import LeaderBoardWindow
from interface.windows_class.menu_window import MenuWindow
from interface.windows_class.win_window import WinWindow
from interface.windows_class.window import Window


class UI:
    def __init__(self):
        self.__root: tk.Tk = tk.Tk()
        self.__root.title('Maze Game')
        self.__root.state('zoomed')
        self._current_window_frame: tk.Frame = tk.Frame(self.__root)
        self._current_window_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.__windows: dict[str, Window] = {
            "Game setting" : GameSettingWindow(self.__root, BG_PATH),
            "Menu": MenuWindow(self.__root, BG_PATH),
            "Leader board": LeaderBoardWindow(self.__root, BG_PATH),
            "Win window": WinWindow(self.__root, BG_PATH),
            "Game window": GameWindow(self.__root, BG_PATH),
        }

        for window_name in self.__windows:
            self.__windows[window_name].windows = self.__windows
            self.__windows[window_name].current_window_frame = self._current_window_frame


        self.__windows["Menu"]._show_window()


    def start(self):
        self.__root.mainloop()
