class Employee: 
    def __init__(self,name,salary): 
        self.name=name
        self.salary=salary
    def getSalary(self):
        print(self.salary)
        
        
lakshay=Employee('Lakshay',"10000000")        
print(lakshay.salary)
lakshay.getSalary()

       
arjun=Employee('Arjun',"20000000") 
print(arjun.name)