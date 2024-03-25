# Theodore
# calculator

print("Calculator")

sum = 0

while True:
    # input
    x1 = input("Enter first number     : ")
    x2 = input("Enter second number    : ")
    op = input("Enter operator         : ")

    # process
    if op == "+":
        sum = int(x1) + int(x2)
    elif op == "-":
        sum = int(x1) - int(x2)
    elif op == "*":
        sum = int(x1) * int(x2)
    elif op == "/":
        sum = int(x1) / int(x2)

    # output
    print (f"Sum                    : {sum} ")
    res = input("Continue? (Yes/No)     : ")
    if res == "No":
        print("Exit")
        break;
