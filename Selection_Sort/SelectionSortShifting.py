mylist = [23,2,67,45,24,9,1]
n= len(mylist)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if mylist[j] <mylist[min_index]:
            min_index=j
        mylist[i],mylist[min_index]= mylist[min_index],mylist[i]

print(mylist)