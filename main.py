import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

values={"+":add,
        "-":sub,
        "*":mul,
        "/":div }

def calc():
    print(art.logo)
    should_accumulate=True
    num1=int(input("Enter the number 1: "))

    while should_accumulate:
        operator=input("+\n-\n*\n/\nenter the operation: ")
        num2=float(input("Enter the number 2: "))
        result = values[operator](num1, num2)
        print(f"{num1}{operator}{num2}={result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ")
        if choice== "y":
            num1=result
        else:
            should_accumulate=False
            print("\n"*20)



calc()

