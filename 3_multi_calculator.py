# Calculator

sum = 0

#input
x1 = input ("enter x1: ")
x2 = input ("enter x2: ")
op = input ("enter operator: ")

#process
if op == "+":
    sum = int(x1) + int(x2)
elif op == "-":
    sum = int(x1) - int(x2)
elif op == "*":
    sum = int(x1) * int(x2)
elif op == "/":
    sum = int(x1) / int(x2)
#output
print(f"sum: {sum}")