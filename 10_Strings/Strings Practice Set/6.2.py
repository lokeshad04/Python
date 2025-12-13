# Take a user input string and check if it is a palindrome (same forwards and
# backwards).

s1 = input("Palindrome checker. Enter your string: ")
# s2 = s1[::-1]
# if(s1==s2):
#     print("Palindrome")
if(s1==s1[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")
