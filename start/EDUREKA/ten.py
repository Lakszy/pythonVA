class Student: 
     
    def __init__(self,name,rollno): 
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    
    class Laptop:   
        def __init__(self): 
             self.name='Hp'   
             self.ram='8gb'
             self.cpu='i5'  
          
        
        
s1= Student('Lakshay','365')
# for accessing the inner class
lapy=s1.lap
print(lapy.name,lapy.ram,lapy.cpu)

#-------------------------------------------------
class A:    
    def feature1(self):  
        print("I am feature 1")
    def feature2(self):  
        print("I am feature 2")
# single level inheritance
class B(A):    
    def feature3(self):  
        print("I am feature 3")
    def feature4(self):  
        print("I am feature 4")
# Multi level inheritance
# class C(B):    
#     def feature5(self):  
#         print("I am feature 5")
#     def feature6(self):  
#         print("I am feature 6")


s1=A()
s2=B()
# inheritance we are getting the feature1 
# which is part of class A in Class B
s2.feature1()
s2.feature4()