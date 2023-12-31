nums=[7,6,5,4,3,2,1]

it =iter(nums)

print(it.__next__())

class TopTen:   
    def __init__(self): 
        self.num = 1
 
# we have created our own iterator
    def __iter__(self): 
        return self
        
    def __next__(self): 
        
        if self.num <= 10:  
            val=self.num
            self.num+=1
            return val
        
        else:   
            raise StopIteration
           
values =TopTen()
for i in values:
     print(i)
   
   
def Add(x,y):   
    while(y!=0):    
        carr=x&y
        x=x^y
        y= carr << 1
    return x

    
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

print('The sum of a and b without using + is:',Add(a,b))


def topten():   
    n=1
    
    while n<=10:    
        sq=n*n
        yield sq
        n+=1
        
values=topten()

for i in values:    
    print(i)