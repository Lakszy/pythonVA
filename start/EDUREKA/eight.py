from functools import reduce

f= lambda a: a*a
res=f(21)
print(res)


# filter map reduce
nums=[5,7,8,5,4,3,3,2,2,7,45,6,6]
evens=list(filter(lambda n: n%2==0 ,nums))
doubles =list(map(lambda n: n*2,evens))
sum = reduce(lambda a, b: a + b, doubles)
print(evens)
print(doubles)
print(sum)


# Decorators:- just to change or add functionality in the existing code

def div(a,b):   
    return(a/b)

def new_div(func):  
    
    def inner(a,b): 
# we cant chnage the functionality it has to be a/b
        if a<b: 
            a,b=b,a 
            return func(a,b)
    return(inner)                         
            
div=new_div(div)
print(div(2,4))