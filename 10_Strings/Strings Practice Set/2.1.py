# Given text = "Python Programming" , do the following:
# 1. Print the first 6 characters
# 2. Print the last 6 characters
# 3. Print every second character from the string

text = "Python Programming"
print(text[0:6])  #index 0 to 5 first 6 characters

print(len(text))
#for last 6 characters
print(text[-6:])
# print(text[12:])


print(text[::2])