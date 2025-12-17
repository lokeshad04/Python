def sum(a,b):
    c = a+b
    global z #Please modify global variable z
    z = 1  # This will refer to global vaiable z and not create a local variable
    return c

z = 9
print(z)
print(sum(2,3))
print(z)