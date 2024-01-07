import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
# import backend

window  = tk.Tk()
window.title("Best Buy POS System")
window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

image1 = Image.open("C:/Users/fonga/Downloads/POSSystem/POSSystem/system/bestbuy.jpg")
photo = ImageTk.PhotoImage(image1)

frm_sidebar = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)
lbl_title = tk.Label(
    frm_sidebar,
    image = photo
)

book_options = ttk.Notebook()
txt_cartDisplay = tk.Text(book_options)
txt_cartDisplay.insert("1.0", "Cart:")
lbl_option1 = tk.Label(text = "")
lbl_option2 = tk.Label(text = "")
book_options.add(
    txt_cartDisplay,
    state = "normal",
    sticky = "nsew",
    padding = 2,
    text = "Cart"
)
book_options.add(
    lbl_option2,
    state = "normal",
    sticky = "nsew",
    padding = 2,
    text = "Checkout"
)

# grid
lbl_title.grid(row = 0, column = 0, sticky = "ew")
frm_sidebar.grid(row = 0, column = 0, sticky = "ns")
book_options.grid(row = 0, column = 1, sticky = "nsew")

# cart = backend.Cart()
# cartDisplay.insert(0, cart.displayCart())

window.mainloop()
