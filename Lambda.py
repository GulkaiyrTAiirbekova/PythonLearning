#x = lambda a: a+ 60
#print(x(2))

#n=  lambda b,c : b * c
#print(n(212,34))

def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
print(mydoubler(13))

print("----------------------")
mytripler =myfunc(3)
print(mytripler(13))




