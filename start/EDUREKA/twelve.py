from abc import ABC, abstractmethod
 
#method overriding
class A:
    def show(self): 
        print("I am show in A")

class B(A):
    def show(self): 
        print("I am show in B")
#   pass
 
a=B()
a.show()   

#method overriding we can understand in that way if my
#father has a phone i can call that phone mine,But if I
#have a phone I will priotrize it over my father's phone




# ABSTARCT CLASSES
# abstarct class should have atleast one abstract method 
# An abstract method is a method that has
# a declaration but does not have an implementation.
# While designing large functional units we use 
# abstract class. When we want to provide a common 
# interface for different implementations of a component,
#->You cannot create object of a abstract classes
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
 
class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
 
class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
  
# Driver code
R = Triangle()
R.noofsides()
 
R = Pentagon()
R.noofsides()
