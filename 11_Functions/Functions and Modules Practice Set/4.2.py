# Write a recursive function sum_of_digits(n) that returns the sum of all digits
# of a given number.

sum = 0
def sum_of_digits(n):
    global sum
    if(n<=0):
        return sum
    digit = n%10
    
    sum += digit
    n //= 10
    return sum_of_digits(n)
print(sum_of_digits(1234))