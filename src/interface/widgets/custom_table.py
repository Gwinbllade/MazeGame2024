import tkinter

from src.const import MAIN_FONT, TABLE_LINE_COLOR, TABLE_HEADER_NAME_COLOR, TABLE_ENTRY_COLOR, TABLE_LINE_WIDTH


class CustomTable:
    def __init__(self, screen, x1, y1, x2, y2, columns, data, is_line = True):
        self.__screen: tkinter.Canvas = screen
        self.__data = data
        self.__width = x2 - x1
        self.__height = y2 - y1
        self.__start_x = x1
        self.__start_y = y1
        self.__columns = columns
        self.__is_line = is_line
        self.__cell_height = self.__height / (len(data) + 1)  # +1 for header

        # Calculate column widths based on proportions
        self.__column_widths = {}
        for col, proportion in columns.items():
            self.__column_widths[col] = self.__width * proportion

    def draw(self):
        # Draw outer rectangle
        if self.__is_line:

            self.__screen.create_rectangle(
                self.__start_x,
                self.__start_y,
                self.__start_x + self.__width,
                self.__start_y + self.__height,
                fill="",
                width=TABLE_LINE_WIDTH
            )
            self.__draw_horizontal_lines()
            self.__draw_vertical_lines()

        self.__draw_headers()
        self.__fill_data()

    def __draw_horizontal_lines(self):
        for i in range(len(self.__data) + 2):  # +2 for header and bottom line
            y = self.__start_y + self.__cell_height * i
            self.__screen.create_line(
                self.__start_x,
                y,
                self.__start_x + self.__width,
                y,
                fill=TABLE_LINE_COLOR,
                width=TABLE_LINE_WIDTH
            )

    def __draw_vertical_lines(self):
        current_x = self.__start_x
        for col, width in self.__column_widths.items():
            self.__screen.create_line(
                current_x,
                self.__start_y,
                current_x,
                self.__start_y + self.__height,
                fill=TABLE_LINE_COLOR,
                width=TABLE_LINE_WIDTH
            )
            current_x += width


        self.__screen.create_line(
            self.__start_x + self.__width,
            self.__start_y,
            self.__start_x + self.__width,
            self.__start_y + self.__height,
            fill=TABLE_LINE_COLOR,
            width=TABLE_LINE_WIDTH
        )

    def __draw_headers(self):
        current_x = self.__start_x
        for col in self.__columns.keys():
            x = current_x + self.__column_widths[col] / 2
            self.__screen.create_text(
                x,
                self.__start_y + self.__cell_height / 2,
                text=col,
                font=MAIN_FONT,
                fill = TABLE_HEADER_NAME_COLOR
            )
            current_x += self.__column_widths[col]

    def __fill_data(self):
        for row_idx, row_data in enumerate(self.__data):
            current_x = self.__start_x
            for col_idx, cell_data in enumerate(row_data):
                x = current_x + list(self.__column_widths.values())[col_idx] / 2
                y = self.__start_y + self.__cell_height * (row_idx + 1.5)
                self.__screen.create_text(
                    x,
                    y,
                    text=str(cell_data),
                    fill = TABLE_ENTRY_COLOR,
                    font=MAIN_FONT
                )
                current_x += list(self.__column_widths.values())[col_idx]