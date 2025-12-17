def sum(a,b):
    # a and b are LOCAL VARIABLES i.e. can only be accessed inside the function
    c= a+b
    z = 2 # local variable which is destroyed after this function returns
    return c

z = 8 # z is a GLOBAL VARIABLE i.e declared outside any function , can be used throughout program
print(z)
print(sum(4,6))
print(z)
# print(a)
# print(b)
# print(c) # error saying c not defined because function only keeps variable until it returns