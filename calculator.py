from userinterface import input_number
from userinterface import math_operat
import Tkinter
import tkMessageBox

window = Tkinter.Tk()

# X Eingabe Text
xtext = Tkinter.Label(window, text="Enter the value for X: ")
xtext.pack()
# X Eingabe
x = Tkinter.Entry(window)
x.pack()

# Y Eingabe Text
ytext = Tkinter.Label(window, text="Enter the value for Y: ")
ytext.pack()
# Y Eingabe
y = Tkinter.Entry(window)
y.pack()

def plus():
    kalk = int(x.get()) + int(y.get())
    tkMessageBox.showinfo("Result", kalk)

def minus():
    kalk = int(x.get()) - int(y.get())
    tkMessageBox.showinfo("Result", kalk)

def multiplizieren():
    kalk = int(x.get()) * int(y.get())
    tkMessageBox.showinfo("Result", kalk)

def dividieren():
    kalk = int(x.get()) / int(y.get())
    tkMessageBox.showinfo("Result", kalk)

#Button
plus_button = Tkinter.Button(window, text = "+", command=plus)
plus_button.pack()
minus_button = Tkinter.Button(window, text = "-", command=minus)
minus_button.pack()
multi_button = Tkinter.Button(window, text = "*", command=multiplizieren)
multi_button.pack()
divi_button = Tkinter.Button(window, text = "/", command=dividieren)
divi_button.pack()


window.mainloop()