#Step 1: We start with an unsorted array.
# Step 2:We look at the two first values[9,34]. Does the lowest value come first? Yes, so we don't need to swap them.
#Step 3: Take one step forward and look at values 34 and 76. Does the lowest value come first? No.
#Step 5: Taking one step forward, looking at 76 and 12.
#Step 6: We must swap so that 12 comes before 76.
#Step 8: Swapping 90 and 2 so that 2 comes first.

mylist = [9,34,76,12,90,2]
n= len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
print(mylist)
