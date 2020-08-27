'''
Write a Python program to create GUI for below said operations with Tkinter
Arithmetic operations
'''

from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry('350x200')
lbl0 = Label(window)
lbl0.grid(column=4,row=0)
lbl = Label(window, text="Enter first Value")
lbl.grid(column=0, row=2)
txt = Entry(window,width=10)
txt.grid(column=1, row=2)
lbl1 = Label(window, text="Enter second value")
lbl1.grid(column=0, row=3)
txt1 = Entry(window, width=10)
txt1.grid(column=1, row=3)

def addi():
    a = int(txt.get()) + int(txt1.get())
    a = str(a)
    b = "The answer is " +a
    lbl0.configure(text = b)

btn1 = Button(window, text="+", command = addi)
btn1.grid(column=0,row=5)

def subt():
    a = int(txt.get()) - int(txt1.get())
    a = str(a)
    b = "The answer is " +a
    lbl0.configure(text = b)

btn2 = Button(window, text="-", command = subt)
btn2.grid(column=1,row=5)

def multi():
    a = int(txt.get()) * int(txt1.get())
    a = str(a)
    b = "The answer is " +a
    lbl0.configure(text = b)

btn3 = Button(window, text="*", command = multi)
btn3.grid(column=2,row=5)

def divi():
    a = int(txt.get()) / int(txt1.get())
    a = str(a)
    b = "The answer is " +a
    lbl0.configure(text = b)

btn3 = Button(window, text="/", command = divi)
btn3.grid(column=3,row=5)

window.mainloop()
