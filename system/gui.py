from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from pathlib import Path
import backend
import os
import sys

bestbuyblue = "#1072e3"

# Order creation
order = backend.Order()

def getItemFromText(event = None):
    id = ent_search.get()
    order.addItemToCart(id)
    txt_itemsDisplay.configure(state = "normal")
    for i in range(len(order.items)):
        txt_itemsDisplay.delete(str(float(i + 1)), END)
    txt_itemsDisplay.insert("1.0", order.displayCartItems())
    txt_itemsDisplay.configure(state = "disabled")
    lbl_totalsDisplay.config(text = order.displayCartTotals())
    ent_search.delete(0, END)
    txt_itemInfo.configure(state = "normal")
    for i in range(4):
        txt_itemInfo.delete(str(float(i + 1)), END)
    txt_itemInfo.insert("1.0", "Item Info:\n" + order.items[len(order.items) - 1].displayItem())
    img = ImageTk.PhotoImage(Image.open(order.items[len(order.items)-1].displayImage()))
    cnv_itemPic.create_image(0,0,image=img)
    txt_itemInfo.configure(state = "disabled")
    return

def getCustomerFromText(event = None):
    phoneNumber = ent_customerSearch.get()
    order.user.getUserByPhoneNumber(phoneNumber)
    txt_customerInfo.configure(state = "normal")
    for i in range(4):
        txt_customerInfo.delete(str(float(i + 1)), END)
    txt_customerInfo.insert("1.0", order.user.displayUser())
    txt_customerInfo.configure(state = "disabled")
    return

def confirmQuit():
    res = messagebox.askquestion("Quit POS System", "Are you sure you want to quit the Best Buy POS system?")
    if res == "yes":
        window.destroy()
    else:
        return

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
    
def openHistoryWindow(event = None):
    historyWindow = Toplevel(window)
    historyWindow.title("Purchase History")
    historyWindow.rowconfigure(1, weight = 1)
    historyWindow.columnconfigure(0, weight = 1)
    historyWindow.option_add("*Font", 'Verdana 14')
    historyWindow.configure(background = bestbuyblue)
    
    # Customer info panel
    frm_custInfo = Frame(historyWindow, background = bestbuyblue)
    lbl_custInfo = Label(frm_custInfo, width = 40, text = "Customer Info:", 
                             foreground = "white",  background = bestbuyblue, anchor = "w")
    txt_custInfo = Text(frm_custInfo, width = 40, height = 4)
    
    # Purchase history panel
    frm_purchaseHistory = Frame(historyWindow, background = bestbuyblue)
    lbl_purchaseHistory = Label(frm_purchaseHistory, width = 20, text = "Purchase History:", 
                                foreground = "white", background = bestbuyblue, anchor = "w")
    lbl_purchase = Label(frm_purchaseHistory, width = 20, text = "Purchase Info:", 
                         foreground = "white", background = bestbuyblue, anchor = "w")
    txt_purchaseHistory = Text(frm_purchaseHistory, width = 20)
    txt_purchase = Text(frm_purchaseHistory, width = 20)
    
    btn_close = Button(historyWindow, text = "Close", command = lambda :historyWindow.destroy())
    
    # Grid
    lbl_custInfo.grid(row = 0, column = 0, padx = 10, sticky = "ew")
    txt_custInfo.grid(row = 1, column = 0, padx = 10, sticky = "nsew")
    frm_custInfo.grid(row = 0, column = 0, sticky = "nsew")
    frm_custInfo.grid_columnconfigure(0, weight = 1)
    lbl_purchaseHistory.grid(row = 0, column = 0, padx = 10, sticky = "ew")
    lbl_purchase.grid(row = 0, column = 1, padx = 10, sticky = "ew")
    txt_purchaseHistory.grid(row = 1, column = 0, padx = 10, sticky = "nsew")
    txt_purchase.grid(row = 1, column = 1, padx = 10, sticky = "nsew")
    frm_purchaseHistory.grid(row = 1, column = 0, sticky = "nsew")
    frm_purchaseHistory.grid_rowconfigure(1, weight = 1)
    frm_purchaseHistory.grid_columnconfigure(0, weight = 1)
    frm_purchaseHistory.grid_columnconfigure(1, weight = 1)
    btn_close.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "e")

    historyWindow.mainloop()

# Window
window  = Tk()
# window.attributes('-fullscreen', True)
window.title("Best Buy POS System")
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, minsize = 250, weight = 1)
window.columnconfigure(1, minsize = 350)
window.columnconfigure(2, minsize = 300, weight = 1)
window.columnconfigure(3, minsize = 300, weight = 1)

# Font settings
window.option_add("*Font", 'Verdana 14')
style = ttk.Style()
style.configure('.', font = "Verdana 14")

# Logo
root_dir = Path(__file__).resolve().parent.parent
fileName = root_dir / "system" / "bestbuy.png"
# img = Image.open(get_path("bestbuy.png"))
img = Image.open(fileName)
photo = ImageTk.PhotoImage(img)
window.wm_iconphoto(False, photo)

# Admin panel
frm_admin = Frame(window, relief = RAISED, borderwidth = 2, background = bestbuyblue)
cnv_logo = Canvas(frm_admin, background = bestbuyblue, width = photo.width(), height = photo.height(), highlightthickness = 0)
cnv_logo.create_image(0, 0, anchor = "nw", image = photo)
btn_purchaseHist = Button(frm_admin, text = "Purchase History", command = openHistoryWindow)
btn_reprintReceipt = Button(frm_admin, text = "Reprint Receipt")
btn_voidTransaction = Button(frm_admin, text = "Void Transaction")

# Middle panel (cart, totals, search)
frm_middle = Frame(window)
lbl_search = Label(frm_middle, text = "Search:", justify = "left", anchor = "w")
ent_search = Entry(frm_middle)
ent_search.bind('<Return>', getItemFromText)
lbl_categories = Label(frm_middle, text = "ID             Name                Price    ", 
                       font = "Courier 17", anchor = "w")
txt_itemsDisplay = Text(frm_middle, width = 1, background = "#cccccc", font = "Courier 17")
txt_itemsDisplay.insert("1.0", order.displayCartItems())
txt_itemsDisplay.configure(state = "disabled")
lbl_totalsDisplay = Label(frm_middle, text = order.displayCartTotals(), foreground = "red", 
                          justify = "right", anchor = "e", font = "Verdana 20 bold", relief = SUNKEN, borderwidth = 5)
btn_total = Button(frm_middle, text = "Total")

# Item panel
frm_itemInfo = Frame(window, relief = RAISED, borderwidth = 2, background = bestbuyblue)
txt_itemInfo = Text(frm_itemInfo, width = 28, height = 4)
txt_itemInfo.configure(state = "disabled")
cnv_itemPic = Canvas(frm_itemInfo)
nbk_itemOptions = ttk.Notebook(frm_itemInfo)
frm_protection = Frame(nbk_itemOptions)
btn_prot1 = Button(frm_protection, text = "1-Year Protection")
btn_prot2 = Button(frm_protection, text = "2-Year Protection")
btn_prot3 = Button(frm_protection, text = "3-Year Protection")
btn_prot4 = Button(frm_protection, text = "4-Year Protection")
btn_appleCare = Button(frm_protection, text = "Apple Care")
prot_plan_list = [btn_prot1, btn_prot2, btn_prot3, btn_prot4, btn_appleCare]
frm_services = Frame(nbk_itemOptions)
frm_accessories = Frame(nbk_itemOptions)
frm_other = Frame(nbk_itemOptions)
nbk_itemOptions.add(frm_protection, sticky = "nsew", text = "Protection Plans")
nbk_itemOptions.add(frm_services, sticky = "nsew", text = "Services")
nbk_itemOptions.add(frm_accessories, sticky = "nsew", text = "Accessories")
nbk_itemOptions.add(frm_other, sticky = "nsew", text = "Other")

# Customer info panel
frm_customerInfo = Frame(window, relief = RAISED, borderwidth = 2, background = bestbuyblue)
lbl_customerSearch = Label(frm_customerInfo, text = "Customer Search:", foreground = "white",
                           background = bestbuyblue, justify = "left", anchor = "w")
ent_customerSearch = Entry(frm_customerInfo)
ent_customerSearch.bind('<Return>', getCustomerFromText)
txt_customerInfo = Text(frm_customerInfo, width = 28)

txt_customerInfo.configure(state = "disabled")
btn_quit = Button(frm_customerInfo, text = "Quit", command = confirmQuit)

# Grid
cnv_logo.grid(row = 0, column = 0, pady = 10)
btn_purchaseHist.grid(row = 1, column = 0, padx = 10, sticky = "ew")
btn_reprintReceipt.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")
btn_voidTransaction.grid(row = 3, column = 0, padx = 10, sticky = "ew")
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
cnv_itemPic.grid(row = 1, column = 0, padx = 10, sticky = "ew")
nbk_itemOptions.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")
for i in range(5):
    if i % 2 == 0:
        prot_plan_list[i].grid(row = i, column = 0, padx = 10, pady = 10, sticky = "ew")
    else:
        prot_plan_list[i].grid(row = i, column = 0, padx = 10, sticky = "ew")
frm_itemInfo.grid(row = 0, column = 2, sticky = "nsew")
frm_itemInfo.grid_columnconfigure(0, weight = 1)

lbl_customerSearch.grid(row = 0, column = 0, padx = 10, sticky = "ew")
ent_customerSearch.grid(row = 1, column = 0, padx = 10, sticky = "ew")
txt_customerInfo.grid(row = 2, column = 0, padx = 10, sticky = "nsew")
btn_quit.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "ew")
frm_customerInfo.grid(row = 0, column = 3, sticky = "nsew")
frm_customerInfo.grid_rowconfigure(2, weight = 1)
frm_customerInfo.grid_columnconfigure(0, weight = 1)

window.mainloop()


