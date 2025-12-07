age=int(input("Enter your age: "))

if(age>18):
    print("You can drive")
elif(age==18):
    print("Interview")
elif(age==0):
    print("You are just born")
else:
    print("Sorry you cannot drive!")
