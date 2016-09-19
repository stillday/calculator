def input_number(prompt):
    while True:
        try:
            return int(raw_input(prompt))
        except ValueError:
            print "Bitte gib nur eine Zahl ein"

def math_operat(prompt, operators):
    result = raw_input(prompt)
    if result in operators
    print result
    return result
