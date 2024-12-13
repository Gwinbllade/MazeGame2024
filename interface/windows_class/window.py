import tkinter as tk
from typing import Optional


class Window:
    def __init__(self, root: tk.Tk):
        self._current_window_frame: Optional[tk.Frame]  = None
        self._root: tk.Tk = root
        self._windows: Optional['Window'] = None

    @property
    def windows(self) -> ['Window']:
        return self._windows

    @windows.setter
    def windows(self, windows: ['Window']):
        self._windows = windows


    @property
    def current_window_frame(self) -> tk.Frame:
        return self._current_window_frame

    @current_window_frame.setter
    def current_window_frame(self, current_window_frame: tk.Frame):
        self._current_window_frame = current_window_frame

    def _clear_current_view(self):
        for widget in self._current_window_frame.winfo_children():
            widget.destroy()

    def show_window(self, *args):
        pass