import tkinter as tk
# from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import backend

# Order creation
order = backend.Order()
# test
item = backend.Item()
item.id, item.name, item.price = 123456789012, "Laptop", 700
order.items.append(item)
order.user.fname = "John"
order.user.lname = "Smith"
order.user.phone = 1234567890
order.user.email = "username@gmail.com"
order.user.address = "12345 Street Name Blvd."

def getItemFromText(event=None):
    id = ent_search.get()
    order.addItemToCart(id)
    #update item display text
    #update totals text
    return

# Window
window  = Tk()
# window.attributes('-fullscreen', True)
window.option_add("*Font", 'Verdana 14')
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, minsize = 250, weight = 1)
window.columnconfigure(1, minsize = 900, weight = 1)
window.columnconfigure(2, minsize = 300, weight = 1)

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

# Middle panel (cart, totals, search)
frm_middle = Frame(window)
lbl_search = Label(frm_middle, text = "Search:", justify = "left", anchor = "w")
ent_search = Entry(frm_middle)
ent_search.bind('<Return>', getItemFromText)
lbl_categories = Label(frm_middle, text = "ID              Name                                      Price  ", 
                       font = "Courier 17", anchor = "w")
txt_itemsDisplay = Text(frm_middle, width = 60, background = "#cccccc", font = "Courier 17")
txt_itemsDisplay.insert("1.0", order.displayCartItems())
txt_itemsDisplay.configure(state = "disabled")
lbl_totalsDisplay = Label(frm_middle, text = order.displayCartTotals(), foreground = "red", 
                          justify = "right", anchor = "e", font = "Verdana 20 bold", relief = SUNKEN, borderwidth = 5)

# Customer info panel
frm_customerInfo = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
txt_customerInfo = Text(frm_customerInfo, width = 28)
txt_customerInfo.insert("1.0", "Customer Info:\n" + order.user.displayUser())
txt_customerInfo.configure(state = "disabled")
btn_quit = Button(frm_customerInfo, text = "Quit", command = window.destroy)

# Grid
canvas.grid(row = 0, column = 0)
frm_admin.grid(row = 0, column = 0, sticky = "nsew")
frm_admin.grid_columnconfigure(0, weight = 1)
lbl_search.grid(row = 0, column = 0, sticky = "ew")
ent_search.grid(row = 1, column = 0, sticky = "ew")
lbl_categories.grid(row = 2, column = 0, sticky = "ew")
txt_itemsDisplay.grid(row = 3, column = 0, sticky = "nsew")
lbl_totalsDisplay.grid(row = 4, column = 0, sticky = "ew")
frm_middle.grid(row = 0 , column = 1, sticky = "nsew")
frm_middle.grid_rowconfigure(3, weight = 1)
frm_middle.grid_columnconfigure(0, weight = 1)
txt_customerInfo.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "ew")
btn_quit.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "ew")
frm_customerInfo.grid(row = 0, column = 2, sticky = "nsew")
frm_customerInfo.grid_columnconfigure(0, weight = 1)

window.mainloop()