from src.const import TABLE_LEFT_MARGIN, TABLE_TOP_MARGIN, TABLE_RIGHT_MARGIN, TABLE_BOTTOM_MARGIN
from src.interface.widgets.custom_button import CustomButton
from src.interface.widgets.custom_table import CustomTable
from src.interface.windows.window import Window
from src.user_record.user_results import UserResults




class LeaderBoardWindow(Window):
    def show_window(self, **kwargs):
        self._clear_current_view()
        user_results = UserResults()
        table = CustomTable(screen=self._bg_canvas,
                            x1 = TABLE_LEFT_MARGIN,
                            y1 = TABLE_TOP_MARGIN,
                            x2 = self._bg_canvas.winfo_screenwidth() - TABLE_RIGHT_MARGIN,
                            y2 = self._bg_canvas.winfo_screenheight() - TABLE_BOTTOM_MARGIN,
                            columns = {
                                "N" : 0.1,
                                "Name" : 0.4,
                                "Time": 0.2,
                                "Score": 0.3,
                            },
                            data = user_results.get_top_10(),
                            is_line=False)


        table.draw()

        CustomButton.create_button(
            button_name="Back to Menu",
            x=self._root.winfo_screenwidth() // 2,
            y=self._root.winfo_screenheight() - TABLE_BOTTOM_MARGIN / 2,
            master=self._bg_canvas,
            callback= lambda: self._windows["Menu"].show_window()
        )