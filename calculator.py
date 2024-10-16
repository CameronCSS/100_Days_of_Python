def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2



operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():


    num1 = float(input("What's the first number?: "))
    print("+ \n - \n * \n / \n")
    opp = input("Pick an operation: ")
    num2 = float(input("What's the next number?: \n"))

    calculation = operations[opp](num1,num2)

    print(f"{num1} {opp} {num2} = {calculation}")

    should_continue = True

    while should_continue:
        ans = input("Type 'y' to continue calculating with 1.0, or type 'n' to start a new calculation:")
        if ans == "y":
            num1 = calculation

        if ans == "n":
            print("\n" * 20)
            calculator()

        print("+ \n - \n * \n / \n")
        opp = input("Pick an operation:  ")
        num2 = float(input("What's the next number?:  "))

        calculation = operations[opp](num1, num2)

        print(f"{num1} {opp} {num2} = {calculation}")

calculator()