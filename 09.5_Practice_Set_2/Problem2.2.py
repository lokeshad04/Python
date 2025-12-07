# Write a program using match case that simulates a simple calculator.
#  1 Ask the user for two numbers and an operation (+, -, *, /).
#  2 Perform the operation using match case .
n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
operator=input("enter operator: ")
match operator:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case "*":
        print(n1*n2)
    case "/":
        print(n1/n2)
    case _:
        print("invalid")