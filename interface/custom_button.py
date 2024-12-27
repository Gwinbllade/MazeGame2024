import tkinter as tk

from interface.interface_const import MAIN_FONT

FILL: str = "black"
FONT: tuple[str, int] = (MAIN_FONT, 25)
COVER_FILL = "purple"
TAGS: str = 'button'

class CustomButton:


   @staticmethod
   def create_button(button_name:str, x:float, y:float, master: tk.Canvas, callback:callable ):
       button_text = master.create_text(x, y, text = button_name, font = FONT, fill=FILL, tags=TAGS)
       master.tag_bind(button_text, "<Button-1>", lambda e, cmd=callback: cmd())
       master.tag_bind(button_text, "<Enter>",
                                lambda e, t=button_text: master.itemconfig(t, fill=COVER_FILL))

       master.tag_bind(button_text, "<Leave>",
                                lambda e, t=button_text: master.itemconfig(t, fill=FILL))
