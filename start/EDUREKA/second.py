# for x in range(1,10):   
#     for y in range(x):  
#         print(x,end=" ")#y
#     print()
    
    
# a=[1,2,3,4,5,6]  
# while a:    
#     print(a.pop(-1))   
#     b=["---------------------"]
#     while b:    
#         print(b.pop(-1))   
           
      
    
def fib():  
    f,s=0,1 
    while True: 
        yield f 
        f,s=s,f+s
for x in fib(): 
    if x>50:    
        break
    print(x,end=" ")
    
    
print("Hello","World",sep='?')

a=[1,2,3,4,5,6,7]
print(min(a))
print(sum(a))
print(max(a))



#lambda function
a=lambda x:x*x
print(a(3))

b=lambda x,y: x+y
print(b(12,99))




def sum(x,y):   
    return x+y

print(sum(10,99)) 
    