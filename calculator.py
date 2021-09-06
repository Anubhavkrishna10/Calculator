import tkinter
from tkinter import *
from tkinter import messagebox

val    = ""
A = 0
operator = ""


def btn1_isclicked():
    global val
    val = val+ "1"
    data.set(val)
    
def btn2_isclicked():
    global val
    val = val+ "2"
    data.set(val)

def btn3_isclicked():
    global val
    val = val+ "3"
    data.set(val)

def btn4_isclicked():
    global val
    val = val+ "4"
    data.set(val)

def btn5_isclicked():
    global val
    val = val+ "5"
    data.set(val)

def btn6_isclicked():
    global val
    val = val+ "6"
    data.set(val)

def btn7_isclicked():
    global val
    val = val+ "7"
    data.set(val)

def btn8_isclicked():
    global val
    val = val+ "8"
    data.set(val)

def btn9_isclicked():
    global val
    val = val+ "9"
    data.set(val)

def btn0_isclicked():
    global val
    val = val+ "0"
    data.set(val)

def btn_plusclicked():
    global A
    global operator
    global val
    operator = "+"
    val = val + "+"
    data.set(val)
    data.set(eval(val))

def btn_minusclicked():
    global A
    global operator
    global val
    
    operator = "-"
    val = val + "-"
    data.set(val)
    data.set(eval(val))

def btn_mulclicked():
    global A
    global operator
    global val
   
    operator = "*"
    val = val + "*"
    data.set(val)
    data.set(eval(val))

def btn_divclicked():
    global A
    global operator
    global val
    
    operator = "/"
    val = val + "/"
    data.set(val)
    data.set(val)
    data.set(eval(val))

def c_pressed():
    
    global operator
    global val
    val = ""
    
    operator = ""
    data.set(val)

def result():
    
    global operator
    global val
    val2 = val
    if operator=="+":
        x = eval(val2)
        C =x
        data.set(C)
        val = str(C)

    elif operator=="-":
        x = eval(val2)
        C =x
        data.set(C)
        val = str(C)

    elif operator=="*":
        x = eval(val2)
        C = x
        data.set(C)
        val = str(C)

    elif operator=="/":
        try:
            x = eval(val2)
            data.set(x)
            val = str(x)
        except ZeroDivisionError:
            val = ""
            data.set(val)
            
            
            return None


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("calculator")


data = StringVar()

lbl = Label(
    root,
    text = "Label",
    anchor= SE,
    font = ("bold",20),
    textvariable=data,
    background="#ffffff",
    fg = "#000000"
)
lbl.pack(expand=True,fill = "both")


btnrow1 = Frame(root,bg ="#000000")
btnrow1.pack(expand=True,fill  = "both")


btnrow2 = Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True,fill="both")

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn1_isclicked
)

btn1.pack(side = LEFT,expand=True,fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn2_isclicked
)

btn2.pack(side = LEFT,expand=True,fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn3_isclicked
)

btn3.pack(side = LEFT,expand=True,fill = "both")

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn_plusclicked
    
)

btnplus.pack(side = LEFT,expand=True,fill = "both")


btn4 = Button(
    btnrow2,
    text = "4",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn4_isclicked
)

btn4.pack(side = LEFT,expand=True,fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn5_isclicked
)

btn5.pack(side = LEFT,expand=True,fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn6_isclicked
)

btn6.pack(side = LEFT,expand=True,fill = "both")

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn_minusclicked
)

btnminus.pack(side = LEFT,expand=True,fill = "both")

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn7_isclicked
)

btn7.pack(side = LEFT,expand=True,fill = "both")

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn8_isclicked
)

btn8.pack(side = LEFT,expand=True,fill = "both")

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn9_isclicked
)

btn9.pack(side = LEFT,expand=True,fill = "both")

btnmul = Button(
    btnrow3,
    text = "*",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn_mulclicked
)

btnmul.pack(side = LEFT,expand=True,fill = "both")


btnclear = Button(
    btnrow4,
    text = "C",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=c_pressed
)

btnclear.pack(side = LEFT,expand=True,fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn0_isclicked
)

btn0.pack(side = LEFT,expand=True,fill = "both")

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command = result
)

btnequal.pack(side = LEFT,expand=True,fill = "both")

btndivide = Button(
    btnrow4,
    text = "/",
    font = ("bold",22),
    relief = GROOVE,
    border=0,
    command=btn_divclicked
)

btndivide.pack(side = LEFT,expand=True,fill = "both")

root.mainloop()
