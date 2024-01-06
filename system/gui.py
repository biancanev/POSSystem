from tkinter import *
from tkinter import ttk
import backend

root = Tk()
root.attributes('-fullscreen', True)
root.option_add("*Font", 'Verdana 20')
frame = ttk.Frame(root, padding = 10)
frame.grid()
#Menubar
menu = Menu(root)
root.config(menu=menu)
#Transaction Dropdown
transaction = Menu(root)
transaction.add_command(label="Void Transaction", command=backend.Order().voidOrder())
menu.add_cascade(label="Transaction", menu=transaction, font="Verdana 20")
#Customer dropdown
customer = Menu(menu)
customer.add_command(label="Search Customer")
menu.add_cascade(label="Customer", menu=customer)
#Main window text
title = Label(frame, text = "Best Buy", fg = "blue").grid(column = 0, row = 0)
cart = backend.Cart()
dispCart = Label(frame, text = cart.displayCart(), justify = "left").grid(column = 0, row = 1)
quit = Button(frame, text = "Quit", command = root.destroy).grid(column = 1000, row = 1000)

root.mainloop()
