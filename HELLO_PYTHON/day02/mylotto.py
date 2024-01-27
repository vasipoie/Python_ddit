from random import random
arr = list(range(1,45+1))

for i in range(1,1000):
    rnd = int(random()*45)
    a = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a
    
#print(arr)

six = list(range(0,6))

for x in range(0,6):
    #print(arr[x])
    six[x] = arr[x]

six.sort()
print(six)