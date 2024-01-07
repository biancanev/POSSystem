import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
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


# window  = tk.Tk()
# window.title("Best Buy POS System")
# window.rowconfigure(0, minsize = 800, weight = 1)
# window.columnconfigure(1, minsize = 800, weight = 1)

# image1 = Image.open("C:/Users/fonga/Downloads/POSSystem/POSSystem/system/bestbuy.jpg")
# photo = ImageTk.PhotoImage(image1)

# frm_sidebar = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)
# lbl_title = tk.Label(
#     frm_sidebar,
#     image = photo
# )

# book_options = ttk.Notebook()
# txt_cartDisplay = tk.Text(book_options)
# txt_cartDisplay.insert("1.0", "Cart:")
# lbl_option1 = tk.Label(text = "")
# lbl_option2 = tk.Label(text = "")
# book_options.add(
#     txt_cartDisplay,
#     state = "normal",
#     sticky = "nsew",
#     padding = 2,
#     text = "Cart"
# )
# book_options.add(
#     lbl_option2,
#     state = "normal",
#     sticky = "nsew",
#     padding = 2,
#     text = "Checkout"
# )

# # grid
# lbl_title.grid(row = 0, column = 0, sticky = "ew")
# frm_sidebar.grid(row = 0, column = 0, sticky = "ns")
# book_options.grid(row = 0, column = 1, sticky = "nsew")

# window.mainloop()