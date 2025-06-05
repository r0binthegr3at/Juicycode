from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askstring
from tkinter import ttk
import tkinter
root = Tk()
root.title("Tkinter DEMO")
root.geometry("750x500")

def dropdown():
    frame = Frame(root)
    frame.pack()
    langs = ["C", "C++", "Java", "Python", "PHP", "Rust", "Bash"]
    Combo = ttk.Combobox(frame, values=langs)
    Combo.set("Pick fav lang")
    Combo.pack(padx=5, pady=5)

#Entry box example
def login():
    U1 = Label(root, text="Username")
    U1.pack(side=LEFT)
    E1 = Entry(root, bd=5)
    E1.pack(side=LEFT)

#message box alert demo
def msgbox():
    messagebox.showinfo("Message Box", "System alert")

#spinbox example
def spin():
    w = Spinbox(root, from_=0, to=10)
    w.pack(side=RIGHT)

#scroll bar example with for loop
def scrollDEMO():
    SB = Scrollbar(root) #SB means scrollbar
    SB.pack(side=RIGHT, fill=Y)
    SL = Listbox(root, yscrollcommand=SB.set)
    for line in range(51):
        SL.insert(END, "Line number>: " + str(line))
    SL.pack(side=LEFT, fill=BOTH)
    SB.config(command=SL.yview)

#Printing text
def textDEMO(): #function for txt demo on menubar
    txt = Text(root)
    txt.insert(INSERT, "Hello World!!!")
    txt.insert(END, "Peace....")
    txt.pack()
    txt.tag_add("here", "1.0", "1.4")
    txt.tag_config("here", background="yellow", foreground="blue")

#doing shit with files 
#def fshit():

#def sel():
#    selection = "Value>: " + str(var1.get()) #var defined lower down
#    label.config(text = selection)

#Input demos in Input demos menu
def int_demo():
    ND = askinteger("Input", "Input an Int")
    print(ND)

def float_demo():
    FD1 = askfloat("Input", "Enter floating point number")
    print(FD1)

def str_demo():
    SD1 = askstring("Input", "Enter name")
    print(SD1)

#buttons example
def buttonDEMO():
    C1_VAR = IntVar()
    C2_VAR = IntVar()
    CB1 = Checkbutton(root, text="Music", variable=C1_VAR, onvalue=1, \
                      offvalue=0, height=10, width=20)
    CB2 = Checkbutton(root, text="Video", variable=C2_VAR, onvalue=1, \
                      offvalue=0, height=10, width=20)
    CB1.pack(side=LEFT)
    CB2.pack(side=RIGHT)
    

menubar = Menu(root)
#cm means condiment menu
cm = Menubutton(root, text="Pizza Sauces", relief=RAISED) #opts: flat, groove, raised, solid or sunken
cm.grid()
cm.menu = Menu(cm, tearoff=0)
cm["menu"] = cm.menu #yes this is right, go away

#button that does popup
mb = Button(root, text="System Alert!", command=msgbox)
mb.place(x=100,y=150)

#vars deffed as Int for condiments ting
rvar = IntVar()
svar = IntVar()
kvar = IntVar()

#deffin stuff for scale ting
#var1 = DoubleVar()
#scale1 = Scale(root, variable=var1)
#scale1.pack(anchor=E)
#SC_B = Button(root, text="Scale Value", command=sel)
#SC_B.pack(anchor=E)
#slideL1 = Label(root)
#slideL1.pack()

#deffed condiments 
cm.menu.add_checkbutton(label="Ranch", variable=rvar)
cm.menu.add_checkbutton(label="Siracha", variable=svar)
cm.menu.add_checkbutton(label="Ketchup", variable=kvar)
cm.pack()

in_menu = Menu(menubar, tearoff=0)
drop_menu = Menu(menubar, tearoff=0)
demomenu = Menu(menubar,tearoff=0)
exitmenu = Menu(menubar, tearoff=0)

exitmenu.add_command(label="Exit", command=root.quit) #Program exit

demomenu.add_command(label="TextDemo", command=textDEMO)
demomenu.add_command(label="Scrollbar", command=scrollDEMO)
demomenu.add_command(label="Spinbox", command=spin)
demomenu.add_command(label="Buttons", command=buttonDEMO)
demomenu.add_separator()
demomenu.add_command(label="Login", command=login)

drop_menu.add_command(label="Basic drop", command=dropdown)

in_menu.add_command(label="Integer input", command=int_demo)
in_menu.add_command(label="Floating Point input", command=float_demo)
in_menu.add_command(label="String input", command=str_demo)

menubar.add_cascade(label="Demos", menu=demomenu)
menubar.add_cascade(label="Input demos", menu=in_menu)
menubar.add_cascade(label="Dip out", menu=exitmenu)
menubar.add_cascade(label="Drop downs", menu=drop_menu)

root.config(menu=menubar)
root.mainloop()

