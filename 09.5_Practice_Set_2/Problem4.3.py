# Use a while loop to reverse a given number (e.g., 123 → 321).
original_num = int(input("Enter the number: "))

tmp = original_num
rev_num=0
while(tmp>0):
    rev_num= tmp%10 + rev_num * 10
    tmp//=10
print(rev_num)