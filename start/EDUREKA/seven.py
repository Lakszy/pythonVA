# pass by value and refrence 
# mutable
def update(list):   
    print(id(list))
    
    
    
    
    list[1]=25
    print(id(list))
    print("x",list)
    
list=[10,20,30]
print(id(list))
update(list)
print("list",list)   


# def fib(n): 
#     f,s=0,1
#     if n == 1:  
#         print(f)    
         
#     else:   
#         print(f)
#         print(s)
        
#         for i in range(2,n):    
#             c=f+s
#             f,s=s,c
#             print(c,end="  ")
#
# fib(10)



def fact(n):
    while True: 
        if n<=0:
           break   
        else:   
            ans=1
            while n>0:  
                ans*=n           
                n-=1
    print(ans)

fact(5)


def fact(n):    
    if n == 0:      
        return 1
    else:   
        return n*fact(n-1)
    
    
print(fact(10))