class A:    
    def  __init__(self):    
        print("Hello i am A")
class B:    
    def  __init__(self):    
        print("Hello i am B")
        
class C(A,B):  
      
    def  __init__(self):    
        super().__init__()    
        print("Hello i am C")
        # it has accssed the leftmost node which is A
        
s1=C()


# Polymorphism
# operators overloading  
class Student:  
    def __init__(self,m1,m2):   
        self.m1=m1  
        self.m2=m2
#add operators overloading   
    def __add__(self,other):   
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3=Student(m1,m2)
        
        return s3
#method overloading/overidding
    def sum(self,a=None,b=None,c=None):
        
        sum=0    
        
        if a!=None and b!=None and c!=None: 
            sum = a+b+c
            return sum
        elif a!=None and b!=None:   
            sum =a+b
            return sum
        else:
            sum=a
            return sum



s1=Student(21,11)   
s2=Student(31,61)

s3=s1+s2
print(s3.m1)

print(s1.sum(1,9))


