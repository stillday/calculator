x = int(raw_input("Enter the value for X: "))
print x

operation = raw_input("Choose math operation (+, -, *, /):")
print operation

y = int(raw_input("Enter the value for Y: "))
print y

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
