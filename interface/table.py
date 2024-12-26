import tkinter as tk
from tkinter import Frame, ttk
from typing import Tuple, Optional

from user_record.user_result_record import UserResultRecord


class Table:
    def __init__(self, root: tk.Frame):
        self.__root: tk.Frame = root
        self.__table: ttk.Treeview | None  = None



    def create_table(self, columns:  Tuple[str, ...], cell_width: Optional[int] = 100) -> Frame:
        table_frame: Frame = Frame(self.__root, bg='white')

        self.__table:ttk.Treeview = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.__table.pack(fill=tk.BOTH, expand=True)


        for column in columns:
            self.__table.heading(column, text=column)
            self.__table.column(column, width=cell_width)


        return table_frame


    def insert_data(self, data: [UserResultRecord]):
        self.__table.delete(*self.__table.get_children())

        for record in data:
            self.__table.insert("", "end", values=record)









