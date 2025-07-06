"""
Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.
"""
mylist =[99,65,213,46,3,9,34]
n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)

print(mylist)


