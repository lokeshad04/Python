# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
# their squares.
list1 = [1,2,3,4,5]
square = lambda x:x*x
print(list(map(square,list1)))
