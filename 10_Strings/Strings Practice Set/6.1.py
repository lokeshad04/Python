# Write a program that counts how many vowels are in a given string

s = "Coding in python is fun"
cnt=0
vowels = ['a','e','i','o','u']

for char in s.lower():
    if char in vowels:
        cnt+=1
print(cnt)