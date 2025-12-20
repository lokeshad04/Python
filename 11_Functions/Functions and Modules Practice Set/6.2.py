# Write a function multiply(a, b) that has a proper docstring explaining what
# it does. Then use help(multiply) to display the docstring.

def multiply(a,b):
    '''
    Docstring for multiply
    Parameters:
        :param a: First number
        :param b: second number

    Returns:
        int or float: The product of a and b
    '''
    return a*b

print(multiply(5,14))
print(help(multiply))