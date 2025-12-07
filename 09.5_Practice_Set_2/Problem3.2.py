# Print the multiplication table of a number (entered by user).
number = int(input("Enter number: "))
for i in range(1,11):
    print(number,"X",i,"=",number*i)