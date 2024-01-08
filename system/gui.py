import tkinter as tk
# from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import backend

# root = tk.Tk()
# root.attributes('-fullscreen', True)
# root.option_add("*Font", 'Verdana 20')
# root.rowconfigure(10, minsize = 800, weight = 1)
# root.columnconfigure(10, minsize = 800, weight = 1)
# logoFrame = tk.Frame(root, relief = tk.RIDGE, borderwidth = 7)
# dispFrame = tk.Frame(root, relief = tk.GROOVE, borderwidth = 5)
# quitFrame = tk.Frame(root)

# # Menu bar
# menu = Menu(root)
# root.config(menu = menu)

# # Transaction dropdown
# transaction = Menu(root)
# transaction.add_command(label = "Void Transaction", command = backend.Order().voidOrder())
# menu.add_cascade(label = "Transaction", menu = transaction, font = "Verdana 20")

# # Customer dropdown
# customer = Menu(menu)
# customer.add_command(label = "Search Customer")
# menu.add_cascade(label = "Customer", menu = customer)

# # Main window text
# root_dir = Path(__file__).resolve().parent.parent
# fileName = root_dir / "system" / "bestbuy.jpg"
# image1 = Image.open(fileName)
# photo = ImageTk.PhotoImage(image1)
# title = Label(logoFrame, image = photo)
# cart = backend.Cart()
# dispCart = Label(dispFrame, text = cart.displayCart(), justify = "left")
# quit = Button(quitFrame, text = "Quit", command = root.destroy)

# # Grid
# title.grid(row = 0, column = 0)
# logoFrame.grid(row = 0, column = 0)
# dispCart.grid(row = 1, column = 0)
# dispFrame.grid(row = 1, column = 0, sticky = "w")
# quit.grid(row = 2, column = 0)
# quitFrame.grid(row = 2, column = 0, sticky = "w")

# root.mainloop()


# Window
window  = Tk()
window.attributes('-fullscreen', True)
window.option_add("*Font", 'Verdana 14')
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, minsize = 180, weight = 2)
window.columnconfigure(1, minsize = 900)
window.columnconfigure(2, minsize = 800)

# Logo
root_dir = Path(__file__).resolve().parent.parent
fileName = root_dir / "system" / "bestbuy.png"
img = Image.open(fileName)
photo = ImageTk.PhotoImage(img)
window.wm_iconphoto(False, photo)

# Admin panel
frm_admin = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
canvas = Canvas(frm_admin, background = "#1072e3", width = photo.width(), height = photo.height(), highlightthickness = 0)
canvas.create_image(0, 0, anchor = "nw", image = photo)
# lbl_logo = tk.Label(frm_admin, image = photo)

# Middle panel (cart, totals, search)
frm_middle = Frame(window)
lbl_search = Label(frm_middle, text = "Search:", justify = "left", anchor = "w")
ent_search = Entry(frm_middle)
lbl_categories = Label(frm_middle, text = "ID              Name                                       Price", font = "Courier 17")
txt_itemsDisplay = Text(frm_middle, background = "#cccccc", font = "Courier 17")
cart = backend.Cart()
txt_itemsDisplay.insert("1.0", cart.displayCartItems())
lbl_totalsDisplay = Label(frm_middle, text = cart.displayCartTotals(), foreground = "red", 
                          justify = "right", anchor = "e", font = "Verdana 20 bold", relief = SUNKEN, borderwidth = 5)

# Customer info panel
frm_customerInfo = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
lbl_customer = Label(frm_customerInfo, text = "Customer Info:", width = 17)
btn_quit = Button(frm_customerInfo, text = "Quit", command = window.destroy)

# Grid
canvas.grid(row = 0, column = 0)
frm_admin.grid(row = 0, column = 0, sticky = "nsew")
lbl_search.grid(row = 0, column = 0, sticky = "ew")
ent_search.grid(row = 1, column = 0, sticky = "ew")
lbl_categories.grid(row = 2, column = 0, sticky = "w")
txt_itemsDisplay.grid(row = 3, column = 0, sticky = "nsew")
lbl_totalsDisplay.grid(row = 4, column = 0, sticky = "ew")
frm_middle.grid(row = 0 , column = 1, sticky = "nsew")
lbl_customer.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = "ew")
btn_quit.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = "ew")
frm_customerInfo.grid(row = 0, column = 2, sticky = "nsew")

window.mainloop()