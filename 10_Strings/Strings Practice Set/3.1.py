# Take the string " i love python programming " and:
# 1. Remove extra spaces from both ends
# 2. Convert it to title case
# 3. Count how many times "o" appears


s = " i love python programming "
s1 = s.strip()
print(s1)
# print(s.strip())

s2 = s1.title()
print(s2)
# print(s1.title())

print(s.count('o'))#we can aso use "o"