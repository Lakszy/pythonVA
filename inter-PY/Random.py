import random
import secrets
from math import *

a=random.random()
print(ceil(a*10))

b=random.randint(1,10)
print(b)

mylist=list("ASDFGHJKL")
c1=random.choice(mylist)
c2=random.choices(mylist,k=3)
random.shuffle(mylist)
print(c1,c2,mylist)



listy=list("ASERTGBN")
d3=secrets.choice(listy)
print(d3)

d1=secrets.randbelow(10)
print(d1)

d2=secrets.randbelow(4)
print(d2)