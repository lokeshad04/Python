# Write a recursive function fibonacci(n) that prints the first n Fibonacci
# numbers

# def fibonacci(n):
#     '''
#     Print the first n Fibonacci numbers using iteration.
#     '''
#     a, b = 0, 1   # First two Fibonacci numbers

#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b


def fibonacci(n):
    def fib(k):
        if(k<=1):
            return k
        return fib(k-1)+fib(k-2)

    for i in range(n):
        print(fib(i),end=" ")

fibonacci(10)

        
        
        