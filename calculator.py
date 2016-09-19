from userinterface import input_number
from userinterface import math_operat

x = input_number("Enter the value for X: ")

operation = math_operat("Choose math operation (+, -, *, /): ")

y = input_number("Enter the value for Y: ")

if operation == "I'm a hero":
    print "Yes you are a super hero"

if operation == "+":
    print x + y
elif operation == "-":
    print x - Y
elif operation == "*":
    print x * y
elif operation == "/":
    print x / y
else:
    print "You did not provide the correct math operation."
