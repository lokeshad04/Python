marks = [5,2,21,5,7]
extra_marks = [53,23,32]

print(marks)
marks.append(63) #adds the element in the end of the list
print(marks)
marks.pop() #removes the last element of list
print(marks)

marks.extend(extra_marks) #appends list at the end of another list
print(marks)

marks.reverse() #reverses the list
print(marks)

marks.sort() # sorts the list
print(marks)

marks.remove(21)  #removes the first occurence in the list
print(marks)

marks.insert(1,99)  #(index, value)inserts the value at index value
print(marks)

