x=-5
# raise keyword is used when we want to force the error
if x<0: 
    raise Exception("aa")

assert(x>=0),'x should be positive'

a=(int(input("enter a number")))
try:    
    a/0
except Exception as e:
    print(e)
finally:    
    print("Cleainig")

# Creating a our own Error

class ValueToHigh(Exception):
    pass

n=(int(input("entrer")))
if n>100:   
    raise ValueToHigh("lll")