# class Computer: 
#     # special variable       and special method
#          #__name__                   __init
    
# # constructor(object)     
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
        
#     def config(self):   
#         print("Config is",self.cpu,self.ram) 
             
# comp1=Computer("i5",16)
# comp2=Computer("i7",8)
# comp1.config()
# comp2.config()


class Lakshay:  
    def __init__(self): 
        self.age=28
        self.name="Lakshay"
    # self here means jo bhi call krre uske sath lag jao 
    def update(self): 
        self.age=80
        
    def compare(self,other):    
        if self.age == other.age:   
            return True

c1=Lakshay()
c2=Lakshay()

# c1 will be treated as self cauz it is calling an d other as c2
if c1.compare(c2): 
    print("BOth are same")
else:   
    print("both are not same")

print(c1.age)
c2.update()
print(c2.age)

if c1.compare(c2): 
    print("BOth are same")
else:   
    print("both are not same")