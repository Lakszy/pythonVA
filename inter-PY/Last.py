def foo(a,b,*args,**kwargs):    
    print(a,b)
    for i in args:
        print(i)
        print("args end")    
    for keys in kwargs:
        print("iam k",keys,kwargs[keys])
  
sev=9#keyword arguments  
foo(2,3,sev=9,s=5)

# unpacking list into arguments
def funk(a,b,c):    
    print(a,b,c)

mylist=[1,4,5]
funk(*mylist)

mydict={'a':1,'b':4,'c':5}
funk(**mydict)

# we just have to write( global varname)
# to access outside the func


# how can we chnage immutable objects
#immmutable objects contain within mutable can be changed 