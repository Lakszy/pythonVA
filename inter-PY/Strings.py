name="""I'am \
 Lakshay"""
 
# because strings are imutable
# name[9]='p'

print(name[::-1])
print(name[9])
print("Hello "+name)

my_string="      Hello Lakshay       "
print(my_string)

# This will strip of the extra space
my_string=my_string.strip()
print(my_string)

# Checks if the gievn string starts with
print(my_string.startswith("Hello"))

print(my_string.lower())
print(my_string.upper())
# if fisrt letter is capital alraedy it will lowecase it
print(my_string.capitalize())

print(my_string.find("y"))
print(my_string.count("l"))
print(my_string.replace("a","z"))

# How to add each word of string in list
print("-----------------------------")
my_list=my_string.split("  ")
print(my_list)

# how to reverse
new_string=''.join(my_list)
print(new_string)
print("-----------------------------")


print("-----------------------------")
# [a,a,a,a,a,a,] to aaaaaa
lili=['a'] *6
newnewnew=''.join(lili)
print(lili)
print(newnewnew)
print("-----------------------------")

# formatting a string(new method)
# new f string
var =3.321111
var2 =6
stringing="It is variable {:.2f} and {}".format(var,var2)


# f string is fasterprint(myname)
lakshing=f"It is variable {var} and {var2}"

# %d int
# %f float
# %s string
print(stringing)

print(lakshing)


for i in nums:  
    if i%2!=0:
        nums.append(i)
