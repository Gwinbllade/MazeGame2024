class Window:
    def __init__(self, root):
        self._current_window_frame = None
        self._root = root
        self._windows = None

    @property
    def windows(self):
        return self._windows

    @windows.setter
    def windows(self, windows):
        self._windows = windows


    @property
    def current_window_frame(self):
        return self._current_window_frame

    @current_window_frame.setter
    def current_window_frame(self, current_window_frame):
        self._current_window_frame = current_window_frame

    def _clear_current_view(self):
        for widget in self._current_window_frame.winfo_children():
            widget.destroy()

    def show_window(self, *args):
        pass