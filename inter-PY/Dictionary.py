mydict={"name":"lakshay","age":21,"city":"NewYork"}
# accesing
print(mydict["name"])

# adding
mydict["postal"]=110024
print("new",mydict)

# deleting
del mydict["city"]
print("Deleted ",mydict)

if "name" in mydict:    
    print(mydict["age"])
  
print(mydict.keys())
print(mydict.values())
print(mydict.items())

mydict_cpy=mydict.copy()
print(mydict_cpy)

#  I am update
mydict_2={"add":2901,"Gender":"Male"}
mydict.update(mydict_2)
print(mydict)

clear()
copy()
fromkeys()
get()
popitem()
setdefault(key, value=None)