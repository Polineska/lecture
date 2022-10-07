n=6
mas=[0]*n
from random import randint
for i in range(0,n,2):
    mas[i]=randint(0,99)
print(mas)
for i in range(0,len(mas)-1,2):
    mas[i],mas[i+1]=mas[i+1],mas[i]
print(mas)
    
