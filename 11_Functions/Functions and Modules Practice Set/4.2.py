# Write a recursive function sum_of_digits(n) that returns the sum of all digits
# of a given number.

def sum_of_digits(n):
    if(n<=0):
        return sum
    digit = n%10
    global sum
    sum += digit
    n //= 10
    sum_of_digits(n)
sum = 0
print(sum_of_digits(1234))