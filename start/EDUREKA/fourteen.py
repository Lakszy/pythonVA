from time import sleep
from threading import *
class Hello(Thread):    
    def run(self):  
        for i in range(5):   
            print("Hello") 
            sleep(1)
    
    
class Hi(Thread):    
    def run(self):  
        for i in range(5):   
            print("Hi")
            sleep(1)
             
     
s1=Hello()
s2=Hi()

# s1.num()
# s2.num()
s1.start()
s2.start()

s1.join()#this will wait s1 to get executed
s2.join()#this will wait s2 to get executed