a = int(input("Enter a number between 1 and 10: "))


match a:
    case 1:
        print("The value is 1")
    case 3:
        print("The value is 3")
    case 6:
        print("The value is 6")
    case _:
        print("Better luck next time")
        