'''name = "lokesh"

print(name[0:2]) #goes from index 0 to index [2]-1   i.e   0 to 1

print(name[2:-1])  #same as index 2 to last index i.e -1+6= 5 ->  [2:5]'''

name = "lokii0123456789"

print(name[0:10])
#print(name[0:10:n]) skip n-1 characters
print(name[0:10:1]) #skip 0 characters
print(name[0:10:2]) #skip 2-1 = 1 character
print(name[0:10:3]) #skip 3-1 = 2 characters

print(name[:4]) #Replace the first empty number with 0 # name[0:4]
print(name[1:]) #Replace the second empty number with length of string   # name[1:15]