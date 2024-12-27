import tkinter as tk

from src.const import BLURRED_BG_PATH, BG_PATH
from src.interface.windows_class.game_setting_window import GameSettingWindow
from src.interface.windows_class.game_window import GameWindow
from src.interface.windows_class.leader_board_window import LeaderBoardWindow
from src.interface.windows_class.menu_window import MenuWindow
from src.interface.windows_class.win_window import WinWindow
from src.interface.windows_class.window import Window


class UI:
    def __init__(self):
        self.__root: tk.Tk = tk.Tk()
        self.__root.title('Maze Game')
        self.__root.state('zoomed')
        self.__root.overrideredirect(True)
        self.__root.bind("<Escape>", lambda event: self.__windows["Menu"].show_window())


        self._current_window_frame: tk.Frame = tk.Frame(self.__root)
        self._current_window_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.__windows: dict[str, Window] = {
            "Game setting" : GameSettingWindow(self.__root, BLURRED_BG_PATH),
            "Menu": MenuWindow(self.__root, BG_PATH),
            "Leader board": LeaderBoardWindow(self.__root, BLURRED_BG_PATH),
            "Win window": WinWindow(self.__root, BLURRED_BG_PATH),
            "Game window": GameWindow(self.__root, BLURRED_BG_PATH),
        }

        for window_name in self.__windows:
            self.__windows[window_name].windows = self.__windows
            self.__windows[window_name].current_window_frame = self._current_window_frame



    def start(self):
        self.__windows["Menu"].show_window()
        self.__root.mainloop()
