# def mygenerators(num):
#     print('starting')
#     while num>0:    
#         yield num
#         num=-1
        
# cd = mygenerators(4)

# value = next(cd)
# print(value)
# genartors are memory effiecent so auto fast

def first(n):
    num=0
    while num<n:
        yield n 
        num+=1
        
#------------------------------------------------# 
def fib(limit):
    f,s=0,1
    while f<limit:
        yield f
        f,s=s,f+s

fibo=fib(30)
for i in fibo:
    print(i)