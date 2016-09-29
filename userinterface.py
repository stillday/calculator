def input_number(prompt):
    while True:
        try:
            return int(raw_input(prompt))
        except ValueError:
            print "Bitte gib nur eine Zahl ein"

def math_operat(prompt, operators):
    while True:
        result = raw_input(prompt)
        if result in operators:
            return result
        else:
            print "Please input " + str(operators)