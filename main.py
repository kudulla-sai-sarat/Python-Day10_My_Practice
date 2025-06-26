def add(n1, n2):
    return n1 + n2

# ToDo: create functions for Subtract, Multiply and Divide

def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# ToDo: Add these functions into Dictionaries as Values , keys = '+', '*', '-', and '/'

calculator_Dict = {"+" : add,
                   "-" : sub,
                   "*" : mul,
                   "/" : div,
}


# ToDo: Access the * key from the Dictionary and perform Multiply for 4 * 8

print(calculator_Dict["*"](4, 8))