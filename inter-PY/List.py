my_num=[8,76,5,4,3,45,67,43,45,6]
new_list=sorted(my_num)
print(new_list)
print(my_num)

# i am concat
lak= my_num + new_list
print(lak)

# Slicing
# This will start from 1 index and go all the way to 6 
w=lak[1:6]
print("I am index",w) 

# This will reverse
p=lak[::-1]
print("I am Reverse",p)

# this will jump 2 index
a= lak[::2]
print("I am a jumper",a)

# I am copy without disturbing the original
my_cpy=my_num[:]
my_cpy.append(89)
print(my_cpy)
print(my_num)


#Tuple to List
mymy=(1,11,2,34,5,6,78,1) 
yuyu=list(mymy)
print(type(yuyu))#list
print(type(mymy))#tuple

# unpacking 
age1,*age2=mymy
print(age1)
print(age2)
