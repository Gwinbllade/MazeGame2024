import tkinter as tk
from tkinter import Frame, ttk


class Table:
    def __init__(self, root):
        self.__root = root
        self.__table = None



    def create_table(self, columns, cell_width = 100):
        table_frame = Frame(self.__root, bg='white')

        self.__table = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.__table.pack(fill=tk.BOTH, expand=True)


        for column in columns:
            self.__table.heading(column, text=column)
            self.__table.column(column, width=cell_width)


        return table_frame


    def insert_data(self, data):
        self.__table.delete(*self.__table.get_children())

        for record in data:
            self.__table.insert("", "end", values=record)









