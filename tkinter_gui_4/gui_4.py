'''
Design UI as shown in unamed.png
'''

from tkinter import *
from tkinter.ttk import *

def doNothing():
    filewin = Toplevel(root)
    lbl = Label(filewin, text = "Hello!")
    lbl1 = Label(filewin, text = "You are under test phase")
    lbl.pack()
    lbl1.pack()

def co():
    filewin = Toplevel(root)
    lbl = Label(filewin, text = "Hello!")
    lbl.pack()

root = Tk()
root.geometry('450x620')
root.title("Main window")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New file...", command = doNothing)
filemenu.add_separator()
filemenu.add_command(label="Open...", command = doNothing)
filemenu.add_command(label="Open last closed", command = doNothing)
filemenu.add_command(label="Open recent", command = doNothing)
filemenu.add_separator()
filemenu.add_command(label="Save", command = doNothing)
filemenu.add_command(label="Save all", command = doNothing)
filemenu.add_command(label="Save as", command = doNothing)
filemenu.add_command(label="Save copy as", command = doNothing)
filemenu.add_command(label="Revert", command = doNothing)
filemenu.add_separator()
filemenu.add_command(label="Close", command = doNothing)
filemenu.add_command(label="Close all", command = doNothing)
filemenu.add_separator()
filemenu.add_command(label="Restart", command = doNothing)
filemenu.add_command(label="Exit", command = root.destroy)
menubar.add_cascade(label = "File", menu=filemenu)

optionmenu = Menu(menubar, tearoff=0)
optionmenu.add_command(label = "Run", command = doNothing)
optionmenu.add_command(label = "Run cell", command = doNothing)
optionmenu.add_separator()
optionmenu.add_command(label = "New Project", command = doNothing)
optionmenu.add_command(label = "open project", command = doNothing)
optionmenu.add_command(label = "Close project", command = doNothing)
optionmenu.add_separator()
optionmenu.add_command(label = "Profile", command = doNothing)
menubar.add_cascade(label = "Option", menu=optionmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Report issue", command = doNothing)
helpmenu.add_command(label = "Dependencies", command = doNothing)
helpmenu.add_separator()
helpmenu.add_command(label = "File documentation", command = doNothing)
helpmenu.add_command(label = "Online documentation", command = doNothing)
helpmenu.add_separator()
helpmenu.add_command(label = "Help index", command = doNothing)
menubar.add_cascade(label = "Help", menu=helpmenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About Software", command=doNothing)
aboutmenu.add_command(label = "Version", command=doNothing)
menubar.add_cascade(label = "About", menu=aboutmenu)

root.config(menu=menubar)
left = Frame(root, relief="solid")
right = Frame(root, relief="solid")
left.pack(side="left", expand=True, fill = "both")
right.pack(side="left", expand=True, fill = "both")

top = LabelFrame(left, text="Widgets")
top.pack(side="top",expand=True, fill = "both", padx=3, pady=3)

lb1 = Listbox(top, bg="white", fg="black")
lb1.insert(1, "None")
lb1.insert(2, "Button")
lb1.insert(3, "Canvas")
lb1.insert(4, "Checkbutton")
lb1.insert(5, "Entry")
lb1.insert(6, "Label")
lb1.insert(7, "Labelframe")
lb1.insert(8, "Listbox")
lb1.insert(9, "Message")
lb1.insert(10, "Radiobutton")
lb1.insert(11, "Text")
lb1.grid(row=0, column=0, sticky= W, pady=2)
v1 = IntVar()
c1 = Checkbutton(top, text="multi-placement", variable=v1)
c1.grid(row=3, column=3, sticky=W, pady=2)

b=Frame(left, relief="solid")
b.pack(side="bottom",expand=True, fill="both")
bu = Button(b, text="Put Color on Clipboard", command=co)
bu.pack(expand=False, fill="x")

a = LabelFrame(right, text="GUI Type")
a.pack(side="top", expand=True, fill="both", padx=3, pady=3)

v2 = IntVar()
m = Radiobutton(a, text="Main Window", variable=v2, value=1)
m.grid(row=0, column=0, sticky=W, pady=2)

d = Radiobutton(a, text="Dialog", variable=v2, value=2)
d.grid(row=1, column=0, sticky=W, pady=2)

v5 = IntVar()
c9 = Checkbutton(a, text="Hide OK Button", variable=v5)
c9.grid(row=3, column=3,sticky=W, pady=2)

be = LabelFrame(right, text="Window Options")
be.pack(expand=True, fill="both", padx=3, pady=3)
v3 = IntVar()
c2 = Checkbutton(be, text="Main Menu", variable=v3)
c2.grid(row=0, column=0, sticky=W, pady=2)
c3 = Checkbutton(be, text="Status Bar", variable=v3)
c3.grid(row=1, column=0, sticky=W, pady=2)
c4 = Checkbutton(be, text="Resizable", variable=v3)
c4.grid(row=2, column=0, sticky=W, pady=2)

lb = Label(be, text="Snap Size")
lb.grid(row=3, column=3)
sp = Spinbox(be, from_=0, to=20, width=5)
sp.grid(row=3, column=4)

c = LabelFrame(right, text="Standard Dialog")
c.pack(side="bottom", expand=True, fill="both", padx=3, pady=3)
v4 = IntVar()
c5 = Checkbutton(c, text="Messages", variable=v3)
c5.grid(row=0, column=0, sticky=W, pady=2)
c6 = Checkbutton(c, text="Color choose", variable=v3)
c6.grid(row=1, column=0, sticky=W, pady=2)
c7 = Checkbutton(c, text="File Open/Save", variable=v3)
c7.grid(row=2, column=0, sticky=W, pady=2)
c8 = Checkbutton(c, text="Alarm Handler", variable=v3)
c8.grid(row=3, column=0, sticky=W, pady=2)
root.mainloop()
