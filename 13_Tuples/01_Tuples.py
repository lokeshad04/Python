#Tuples are ORDERED , IMMUTABLE
# FASTER than LISTS (because tuples are immutable)
# used as DICTIONARY KEYS(since they are hashable)
# safe from unintended modifications 

a = (3, 2, 22, 13)

print(a)
print(a[2])

# a[3] = 32    shows error because 'tuple' object does not support item assignment

b = [1, ] # this is the way to create a TUPLE with one element(comma ',' is required)

print(b[0])