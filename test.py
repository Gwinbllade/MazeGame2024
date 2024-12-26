# from tkinter import *
#
# # Create object
# root = Tk()
#
# # Open window maximized (visible taskbar, resizable window)
# root.state('zoomed')
#
# # Add image file
# bg = PhotoImage(file="jungle.ppm")
#
# # Create Canvas
# canvas1 = Canvas(root)
# canvas1.pack(fill="both", expand=True)
#
# # Display image
# image_on_canvas = canvas1.create_image(0, 0, image=bg, anchor="nw")
#
# # Function to resize and stretch image
# def resize_image(event):
#     global bg_resized, stretched_image
#     canvas_width = event.width
#     canvas_height = event.height
#
#     # Scale image exactly to window size
#     stretched_image = bg.subsample(bg.width() // canvas_width, bg.height() // canvas_height) \
#         if bg.width() > canvas_width or bg.height() > canvas_height else \
#         bg.zoom(canvas_width // bg.width(), canvas_height // bg.height())
#
#     # Update canvas image
#     canvas1.itemconfig(image_on_canvas, image=stretched_image)
#     canvas1.config(width=canvas_width, height=canvas_height)
#
# # Bind resize event
# root.bind("<Configure>", resize_image)
#
# # Add Text
# canvas1.create_text(200, 250, text="Welcome")
#
# # Create Buttons
# button1 = Button(root, text="Exit", command=root.destroy)
# button3 = Button(root, text="Start")
# button2 = Button(root, text="Reset")
#
# # Display Buttons
# canvas1.create_window(100, 10, anchor="nw", window=button1)
# canvas1.create_window(100, 40, anchor="nw", window=button2)
# canvas1.create_window(100, 70, anchor="nw", window=button3)
#
# # Execute tkinter
# root.mainloop()
