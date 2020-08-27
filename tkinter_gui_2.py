'''
Write a Python program to create GUI for below said operations with Tkinter
Age calculator
'''

from tkinter import *
from tkinter.ttk import *
from datetime import date
window=Tk()
window.title("Age Calculation")
window.geometry('350x200')
lbl0 = Label(window)
lbl0.grid(column=2, row=0)
lbl = Label(window, text="Enter your name ")
lbl.grid(column=0,row=1)
txt = Entry(window, width=10)
txt.grid(column=1, row=1)
lbl1 = Label(window, text="Enter your age")
lbl1.grid(column=0, row=3)
combo1 = Combobox(window, width=10)
day = []
day.append("Day")
for i in range (1,32):
    day.append(i)

combo1['values'] = day
combo1.current(0)
combo1.grid(column=0, row=4)

month = []
month.append("Month")
for i in range(1,13):
    month.append(i)
combo2 = Combobox(window, width=10)
combo2['values'] = month
combo2.current(0)
combo2.grid(column=1,row=4)

combo3 = Combobox(window,width=10)
year = []
year.append("Year")
for i in range(1950,2020):
    year.append(i)
combo3['values'] = year
combo3.current(0)
combo3.grid(column=2, row=4)

def clicked():
    n = txt.get()
    d=int(combo1.get())
    m=int(combo2.get())
    y=int(combo3.get())
    m = calculateAge(date(y,m,d))
    m = str(m)
    f = n +", your age is " +m
    lbl0.configure(text=f)
    
def calculateAge(bday):
    today = date.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    return age
btn = Button(window, text="Click me", command=clicked)
btn.grid(column=1,row=7)
window.mainloop()
