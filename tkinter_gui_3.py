'''
Create a window with tkinter widgets
'''

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import messagebox
window = Tk()
window.title("Copy Selling app")
window.geometry('550x300')

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='My orders')
new_item.add_separator()
new_item.add_command(label='Update account')
new_item.add_separator()
new_item.add_command(label='Log out')

menu.add_cascade(label='My Account', menu=new_item)
window.config(menu=menu)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Personal Details')
tab_control.add(tab2, text='Order')

lbl0 = Label(tab1, text="Fill in the Details")
lbl0.grid(column=2, row=0)

lbl1 = Label(tab1, text="Name")
lbl1.grid(column=0, row=2)

txt1 = Entry(tab1, width=15)
txt1.grid(column=1, row=2)

lbl2 = Label(tab1, text = "Gender")
lbl2.grid(column=0, row=3)

selected = IntVar()
rad1 = Radiobutton(tab1, text="Male", value=1, variable=selected)
rad2 = Radiobutton(tab1, text="Female", value=2, variable=selected)
rad1.grid(column=1, row=3)
rad2.grid(column=2, row=3)

lbl3 = Label(tab1, text = "Address")
lbl3.grid(column=0, row=4)

add = scrolledtext.ScrolledText(tab1, width=30, height=10)
add.grid(column=1, row=4)

lbl4 = Label(tab2, text="Order Details")
lbl4.grid(column=2, row=0)

lbl6 = Label(tab2, text="Copies")
lbl6.grid(column=0, row=1)

li = ["Select", "Classmate", "Mikado", "Bina", "Blue Book"]
combo = Combobox(tab2, width=10)
combo['values'] = li
combo.current(0)
combo.grid(column=1, row=1)

lbl5 = Label(tab2, text="No of copies")
lbl5.grid(column=0, row=3)

spin = Spinbox(tab2, from_=0, to=100, width=5)
spin.grid(column=1, row=3)

lbl6 = Label(tab2, text="Rate the page:")
lbl6.grid(column=0, row=4)

txt2 = Entry(tab2, width=5)
txt2.grid(column=1, row=4)

style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar', background='black')

bar = Progressbar(tab2, length=50, max=10, style='black.Horizontal.TProgressbar')
bar.grid(column=3, row=4)
def rate():
    n=int(txt2.get())
    if (n > 10):
        messagebox.showerror("Error", "Rate the page out of 10")
    else:
        bar['value'] = n
        n = str(n)
        messagebox.showinfo("Rating", "You have rated the page "+n +" out of 10")
    
btn0 = Button(tab2, text="Put Rating", command=rate)
btn0.grid(column=2, row=4)

def clicked():
    if(combo.get()=="Select"):
        messagebox.showerror("Error", "Select the type of copy")
    elif(spin.get=="" or txt1.get()=="" or selected.get()==0):
        messagebox.showerror("Error", "Please fill your details properly or no. of copies")
    else:
        response = messagebox.askyesno("Order Confirmation", "Do you really want to place the order?")
        if response == True:
            messagebox.showinfo("Successful attempt", "No. of Copies: "+spin.get() +"\nCopy Type: "+combo.get( ) +"\nOrdered By: "+txt1.get())
        else:
             messagebox.showerror("Unsuccessful attempt", "Order was not placed")
        
        
btn1 = Button(tab2, text="Place Order", command=clicked)
btn1.grid(column=3, row=7)
tab_control.pack(expand=1, fill= 'both')
window.mainloop()
