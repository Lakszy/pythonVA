class pyhton:
    def __init__(self,age,name,desg):   
        self.age=age
        self.name=name
        self.desg=desg

    def Newfunc(self):  
        return "Hello World"
    
    def Newfunc2(self):  
        return "Hello World2"
    
lak=pyhton(19,"Lakahay",'SDI')
print(lak.age)
print(lak.name)
print(lak.desg)
print(lak.Newfunc())
print(lak.Newfunc2())

setattr
getattr