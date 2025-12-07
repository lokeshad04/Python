# Write a program that keeps asking the user to enter a password until they
# enter the correct one.
real_password="cyber"

# flag=0
# while(flag==0):
    # entered_password=input("Enter current password: ")
#     if(entered_password==real_password):
#         flag=1
#         print("You entered the correct password")
#         break
#     print("Wrong password try again")
    

entered_password=input("Enter current password: ")
while(real_password != entered_password):
    entered_password=input("Wrong! Enter current password: ")
        
print("success")

    