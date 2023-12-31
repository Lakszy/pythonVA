# COUNTER
# from collections import Counter

# lak="asasasasdsdfdfdsasdfaslasllslslsl"
# # mylist=lak.split(" ")
# my_count=Counter(lak)
# # my_count=Counter(mylist)

# print(my_count)#keys() , values() , items()

# print(my_count.most_common(1))
# # But if I want to get the tuple which is most common
# print(my_count.most_common(1)[0][0])




# /NAMEDTUPLE
# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt=Point(1,-4)
# print(pt.x,pt.y)
# print(pt)



# # ORDERDEDICT
# od_dict={}
# od_dict['a']=1
# od_dict['b']=2
# od_dict['s']=3
# od_dict['c']=4
# od_dict['d']=5
# print(od_dict)

# defaultDict it wiil have a  default value if no value is being paased to it

# deque
from collections import deque
d= deque()

d.append(1)
d.append(4)
d.appendleft(3)
d.append(2)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extend([4,32,1,11])
print(d)
d.extendleft([4,32,1,11])
print(d)
# ek ek elem ki pos bdha dega
d.rotate(2)

print(d)
