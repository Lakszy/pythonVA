# # deco->adds extra (extends behaviour of a function 
# with decorators) functionality to the functions

def nn(func):  
     
    def wrap(*args, **kwargs): 
        print("start") 
        result=func(*args, **kwargs)
        print("end")
        return(result)
    return(wrap)

@nn
def add10(x):
    return x+5

res=add10(15)
print(res)

# import functools

# def repeat(num_times):
    
#     def deco_rep(func): 
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):   
#             for _ in range(num_times):  
#                 result = func(*args, **kwargs)
#             return result   
#         return wrapper
#     return deco_rep

# @repeat(num_times=4)
# def greet(name):    
#     print(f"hello{name}")
    
# greet('Lakshay')