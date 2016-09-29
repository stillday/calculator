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
    if operation == "I'm a hero":
        print "Yes you are a super hero"

    if operation == "+":
        tkMessageBox.showinfo(x + y)
    elif operation == "-":
        tkMessageBox.showinfo(x - y)
    elif operation == "*":
        tkMessageBox.showinfo(x * y)
    elif operation == "/":
        tkMessageBox.showinfo(x / y)

submit = Tkinter.Button(window, text = "Submit", command=calculation)
submit.pack()

window.mainloop()