# local variable have more precdence than gloabl variable which are present throughout the program

c="Hello world"
def func(): 
    c="Edureka"
    print("I am inside the function:",c)

func()
print("I am outside of  the function:",c)


x=19
y=-19+6j
print(type(x),type(y))


my_string="Lakshay"
print(my_string[-3])#starts from -1 from back
print(my_string[3])##starts from 0 from front

a=23
if a>1: 
    for x in range(2,a):    
        if a%x==0:
            print("Not prime")
            break
    else:   
        print("Prime")
else:   
    print("value of a is <=1")
    

#shorthand
a=51
b=7
print("a is less than b ") if a<b else print("b is less than a")


my_list=["Lakshay","khattar","verma","arjun"]

for x in my_list:   
    print(x)

my_str="Hello World"
for x in my_str[0:4]:    
    print(x)
    
    
for x in "Lakshay": 
    if x=='s':  
        pass
    print(x)
print("loop has ended")