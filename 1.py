array=[1,2,3,4,5]
delta=4
k=0
for i in range(len(array)):
    if (array[i])-min(array)==delta:
        k+=1
print(k)
