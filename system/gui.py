from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pathlib import Path
import backend
import os
import sys

# Order creation
order = backend.Order()
# test
item = backend.Item()
order.user.fname = "John"
order.user.lname = "Smith"
order.user.phone = 1234567890
order.user.email = "username@gmail.com"
order.user.address = "12345 Street Name Blvd."

def getItemFromText(event=None):
    id = ent_search.get()
    order.addItemToCart(id)
    txt_itemsDisplay.configure(state="normal")
    for i in range(len(order.items)):
        txt_itemsDisplay.delete(str(float(i + 1)), END)
    txt_itemsDisplay.insert("1.0", order.displayCartItems())
    txt_itemsDisplay.configure(state="disabled")
    lbl_totalsDisplay.config(text=order.displayCartTotals())
    ent_search.delete(0, END)
    txt_itemInfo.insert("1.0", "Item Info:\n" + order.items[len(order.items) - 1].displayItem())
    img = ImageTk.PhotoImage(Image.open(order.items[len(order.items)-1].displayImage()))
    cnv_itemPic.create_image(0,0,image=img)
    return

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

# Window
window  = Tk()
# window.attributes('-fullscreen', True)
window.title("Best Buy POS System")
window.option_add("*Font", 'Verdana 14')
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, minsize = 250, weight = 1)
window.columnconfigure(1, minsize = 350)
window.columnconfigure(2, minsize = 300, weight = 1)
window.columnconfigure(3, minsize = 300, weight = 1)

# Logo
root_dir = Path(__file__).resolve().parent.parent
fileName = root_dir / "system" / "bestbuy.png"
# img = Image.open(get_path("bestbuy.png"))
img = Image.open(fileName)
photo = ImageTk.PhotoImage(img)
window.wm_iconphoto(False, photo)

# Admin panel
frm_admin = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
cnv_logo = Canvas(frm_admin, background = "#1072e3", width = photo.width(), height = photo.height(), highlightthickness = 0)
cnv_logo.create_image(0, 0, anchor = "nw", image = photo)

# Middle panel (cart, totals, search)
frm_middle = Frame(window)
lbl_search = Label(frm_middle, text = "Search:", justify = "left", anchor = "w")
ent_search = Entry(frm_middle)
ent_search.bind('<Return>', getItemFromText)
lbl_categories = Label(frm_middle, text = "ID             Name                  Price  ", 
                       font = "Courier 17", anchor = "w")
txt_itemsDisplay = Text(frm_middle, width = 1, background = "#cccccc", font = "Courier 17")
txt_itemsDisplay.insert("1.0", order.displayCartItems())
txt_itemsDisplay.configure(state = "disabled")
lbl_totalsDisplay = Label(frm_middle, text = order.displayCartTotals(), foreground = "red", 
                          justify = "right", anchor = "e", font = "Verdana 20 bold", relief = SUNKEN, borderwidth = 5)
btn_total = Button(frm_middle, text = "Total")

# Item panel
frm_itemInfo = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
txt_itemInfo = Text(frm_itemInfo, width = 28)
cnv_itemPic = Canvas(frm_itemInfo)
nbk_itemOptions = ttk.Notebook(frm_itemInfo)
frm_protection = Frame(nbk_itemOptions)
frm_services = Frame(nbk_itemOptions)
frm_accessories = Frame(nbk_itemOptions)
frm_other = Frame(nbk_itemOptions)
nbk_itemOptions.add(frm_protection, sticky = "nsew", text = "Protection Plans")
nbk_itemOptions.add(frm_services, sticky = "nsew", text = "Services")
nbk_itemOptions.add(frm_accessories, sticky = "nsew", text = "Accessories")
nbk_itemOptions.add(frm_other, sticky = "nsew", text = "Other")

# Customer info panel
frm_customerInfo = Frame(window, relief = RAISED, borderwidth = 2, background = "#1072e3")
txt_customerInfo = Text(frm_customerInfo, width = 28)
txt_customerInfo.insert("1.0", "Customer Info:\n" + order.user.displayUser())
txt_customerInfo.configure(state = "disabled")
btn_quit = Button(frm_customerInfo, text = "Quit", command = window.destroy)

# Grid
cnv_logo.grid(row = 0, column = 0)
frm_admin.grid(row = 0, column = 0, sticky = "nsew")
frm_admin.grid_columnconfigure(0, weight = 1)
lbl_search.grid(row = 0, column = 0, sticky = "ew")
ent_search.grid(row = 1, column = 0, sticky = "ew")
lbl_categories.grid(row = 2, column = 0, sticky = "ew")
txt_itemsDisplay.grid(row = 3, column = 0, sticky = "nsew")
btn_total.grid(row = 4, column = 0, sticky = "ew")
lbl_totalsDisplay.grid(row = 5, column = 0, sticky = "ew")
frm_middle.grid(row = 0 , column = 1, sticky = "nsew")
frm_middle.grid_rowconfigure(3, weight = 1)
txt_itemInfo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")
cnv_itemPic.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")
nbk_itemOptions.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")
frm_itemInfo.grid(row = 0, column = 2, sticky = "nsew")
frm_itemInfo.grid_columnconfigure(0, weight = 1)
txt_customerInfo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")
btn_quit.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")
frm_customerInfo.grid(row = 0, column = 3, sticky = "nsew")
frm_customerInfo.grid_columnconfigure(0, weight = 1)

window.mainloop()