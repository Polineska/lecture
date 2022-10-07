k=0
n=5
mas=[0]*n
from random import randint
for i in range(n):
    mas[i]=randint(0,99)
for i in range(n):
    summ=sum(mas)
    sr=summ/len(mas)
    if mas[i]>sr:
        k+=1
print(k)
