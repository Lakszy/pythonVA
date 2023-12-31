from functools import reduce

add10 = lambda x: x+10
print(add10(5))


mul = lambda x,y: x*y
print(mul(10,20))

points2D=[(6,7),(4,3),(2,3),(11,21)]
print(points2D)
# Now this will sorted acc to the sum of each
sorty=sorted(points2D,key=lambda x: x[0]+x[1])
print(sorty)


a=[1,2,3,4,5,6,7,8]
b=map(lambda x:x+2,a)
c=filter(lambda x:x % 2 == 0,a)
d=reduce(lambda x,y: x*y, a)
print(list(b))
print(list(c))
print(d)