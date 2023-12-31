import math  as m
# print(list(range(2,50,2)))
print("I am hexadecimal",0x0011101)
print("I am octal",0o0011101)
print("I am binary",0b0011101)


a=10
b=90
print("a:",a,"b:",b)

# a=a+b
# b=a-b
# a=a-b

# or
a,b=b,a
print("a:",a,"b:",b)

# bitwise
a=~5
print(a)
a=15 | 15
a=15 & 15
a=15 ^ 15
print(a)

b=10<<2
#1010 shifts 2 left
#101000 ->40
print(b)


print("THIS IS MATH IMPORT")
x=m.ceil(m.sqrt(90))
print(x)

x=1
while x<10: 
    print("Hello",x,end=" ")
    j=1
    while j<=4: 
        print("rocks",j,end=" ")
        j+=1
    x+=1
    print()
    
    
num=11
for i in range(2,num):   
    if num%i==0:
        print("Not a prime",num)
        break
    else:   
        print("Prime",num)
        break