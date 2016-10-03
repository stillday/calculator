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

# Operation Eingabe Text
operationtext = Tkinter.Label(window, text="Choose math operation (+, -, *, /): ")
operationtext.pack()
#Operation Eingabe
operation = Tkinter.Entry(window)
operation.pack()

# Y Eingabe Text
ytext = Tkinter.Label(window, text="Enter the value for Y: ")
ytext.pack()
# Y Eingabe
y = Tkinter.Entry(window)
y.pack()

def calculation():
    if operation.get() == "I'm a hero":
        kalk = "Yes you are a super hero"

    elif operation.get() == "+":
        kalk = int(x.get()) + int(y.get())
    elif operation.get() == "-":
        kalk = int(x.get()) - int(y.get())
    elif operation.get() == "*":
        kalk = int(x.get()) * int(y.get())
    elif operation.get() == "/":
        kalk = int(x.get()) / int(y.get())

    tkMessageBox.showinfo("Result", kalk)

submit = Tkinter.Button(window, text = "Berechnen", command=calculation)
submit.pack()

window.mainloop()