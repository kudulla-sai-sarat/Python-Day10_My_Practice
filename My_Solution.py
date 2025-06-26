import art
import os


# ToDo Create functions
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def clear_screen():
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("\033", end="")
    print("\n" * 100)

# # Todo: To print thr logo art
# print(art.logo)


# ToDo: Add these functions into Dictionaries as Values , keys = '+', '*', '-', and '/'

calculator_Dict = {"+" : add,
                   "-" : sub,
                   "*" : mul,
                   "/" : div,
}


def calculator():
    print(art.logo)
    check_user_choice = True
    first_num = float(input("What's the First Number: "))
    while check_user_choice:
        for symbol in calculator_Dict:
            print(symbol)
        math_operator = input("Pick an Operation: ")
        next_num = float(input("What's the next number: "))
        math_result = calculator_Dict[math_operator](first_num, next_num)
        print(f"{first_num} {math_operator} {next_num} = {math_result}")
        user_choice = input(f"Type 'y' to continue with {math_result}, or type 'n' to start a new calculation: ")

        if user_choice == 'y':
            first_num = math_result
        else:
            check_user_choice = False
            clear_screen()
            calculator()  # calling function inside function is called recursion


calculator() # Here the actual function is being called when the program runs for first time

# # ToDo: Logic Starts from here
# while True:
#     print(art.logo)
#     check_user_choice = True
#     first_num = float(input("What's the First Number: "))
#     while check_user_choice:
#         for symbol in calculator_Dict:
#             print(symbol)
#         math_operator = input("Pick an Operation: ")
#         next_num = float(input("What's the next number: "))
#         math_result = calculator_Dict[math_operator](first_num, next_num)
#         print(f"{first_num} {math_operator} {next_num} = {math_result}")
#         User_choice = input(f"Type 'y' to continue with {math_result}, or type 'n' to start a new calculation: ")
#
#         if User_choice == 'y':
#             first_num = math_result
#         if User_choice == 'n':
#             check_user_choice = False
#
#     clear_screen()
#

# ToDo: The whole logic can also be made as a function

