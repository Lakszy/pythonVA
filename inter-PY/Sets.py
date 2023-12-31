myset={1,1,2,3,3,4,3,4,6,7,8,9,10}

# same as set jsut we dont put key value pairs
# ity doesnt allow duplicates

myname=set("Lakshaykhattar")

print(myset)
# I will generate random indexing (everytime)
print(myname)

print(myname.__len__())
myset.add(1211)
myset.add(132)
myset.add(121)
myset.add(11)
print(myset)

for i in myset: 
    print(i)
    
# Iam Union Intersection 
print(myname.union(myset))
print(myname.intersection(myset))
print(myname.difference(myset))#myname - myset


# immutable
# fzx=frozenset([1,2,34,5,6])
# gives error on updation

fzx=set([1,2,34,5,6])
fzx2=set([11,12,34,15,6])
# fzx.update([1,543,21,2,23])

fzx.remove(23)#specified 
fzx.pop()#random 
fzx.discard(23)#when you are not sure of the element existence  
print(fzx)
# pipeline=> means or oper (Union) 
# mpercent=> means and oper  (Intersection) 
print(fzx | fzx2)
