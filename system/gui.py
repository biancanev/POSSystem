from tkinter import *
from tkinter import ttk
import backend

root = Tk()
frame = ttk.Frame(root, padding = 10)
frame.grid()
title = Label(frame, text = "Best Buy", fg = "blue").grid(column = 0, row = 0)
cart = backend.Cart()
dispCart = Label(frame, text = cart.displayCart(), justify = "left").grid(column = 0, row = 1)
quit = Button(frame, text = "Quit", command = root.destroy).grid(column = 1000, row = 1000)

root.mainloop()
