import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import backend

root = tk.Tk()
root.attributes('-fullscreen', True)
root.option_add("*Font", 'Verdana 20')
root.rowconfigure(10, minsize = 800, weight = 1)
root.columnconfigure(10, minsize = 800, weight = 1)
logoFrame = tk.Frame(root, relief = tk.RIDGE, borderwidth = 7)
dispFrame = tk.Frame(root, relief = tk.GROOVE, borderwidth = 5)
quitFrame = tk.Frame(root)

# Menu bar
menu = Menu(root)
root.config(menu = menu)

# Transaction dropdown
transaction = Menu(root)
transaction.add_command(label = "Void Transaction", command = backend.Order().voidOrder())
menu.add_cascade(label = "Transaction", menu = transaction, font = "Verdana 20")

# Customer dropdown
customer = Menu(menu)
customer.add_command(label = "Search Customer")
menu.add_cascade(label = "Customer", menu = customer)

# Main window text
root_dir = Path(__file__).resolve().parent.parent
fileName = root_dir / "system" / "bestbuy.jpg"
image1 = Image.open(fileName)
photo = ImageTk.PhotoImage(image1)
title = Label(logoFrame, image = photo)
cart = backend.Cart()
dispCart = Label(dispFrame, text = cart.displayCart(), justify = "left")
quit = Button(quitFrame, text = "Quit", command = root.destroy)

# Grid
title.grid(row = 0, column = 0)
logoFrame.grid(row = 0, column = 0)
dispCart.grid(row = 1, column = 0)
dispFrame.grid(row = 1, column = 0, sticky = "w")
quit.grid(row = 2, column = 0)
quitFrame.grid(row = 2, column = 0, sticky = "w")

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