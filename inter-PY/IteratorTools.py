# iteratools: products,permutaion,combinations,accumulate, groupBy and infinite iterators 
from itertools import product

a=[1,2]
b=[11]
prod=product(a,b,repeat=2)
# a cross b
print(list(prod))

from itertools import combinations
from itertools import permutations
from itertools import accumulate
import operator

a=[1,2,3,4]

accmul=accumulate(a,func=operator.mul)
pro=permutations(a,2)
com=combinations(a,2)
acc=accumulate(a)

print("I am accumulate with multiply",list(accmul))
print("I am permutations",list(pro))
print("I am combinations",list(com))
print("I am accumulate",list(acc))

from itertools import groupby

persons=[{'name':'Tim','age':28},{'name':'Jim','age':25},
         {'name':'Tom','age':21},{'name':'Jom','age':25}]


obj= groupby(persons,key= lambda x: x['age'])
for key ,value in obj: 
    print(key,list(value))
