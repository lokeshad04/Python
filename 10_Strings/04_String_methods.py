'''name = "Loki" #strings are immutable

# name[0] = "D" #You cannot do this

a = len(name)
print(a)
'''
# s = "hello world" #strings are immutable
# a = len(s)
# print(a)
# print(s.upper()) #UPPERCASE ALL LETTERS
# print(s.lower()) #lowercase all letters
# print(s.capitalize()) #uppercase the first letter of the string
# print(s.title()) #First character of eveery word in the string is capitalized

# text = " Hello World "
# print(text.strip()) #Removes spaces and new line character from left and right of the string
# print(text.lstrip()) #removes from left side
# print(text.rstrip()) #removes from right side

text = "Python is fun and fun and fun"
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun","awesome"))  # Replaces all occurences of fun with awesome

text = "Apples,Bananas,Pineapples"
print(text)
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))


text = "Python123"
print(text.isalpha()) #True if all the characters in string are alphabets
print(text.isdigit()) # true if all the characters are digit
print(text.isalnum()) #True if string contains only alphabets and numerical digits
print(text.isspace()) # True if all the characters in the string are whitespace
