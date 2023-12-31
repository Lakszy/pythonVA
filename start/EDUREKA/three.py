list=[]
print(type(list))

my_tuple=()
z=(1,2,3,4,5,6,7)
print(z+(12,3,343,56,2))
for i in z: 
    print(i)
    
    
my_array=()
c=[1,2,3,4,5,6,7]
for t in c: 
    print(t)
    
#this shows tuple is immutable 

#in set hashing is formed to fetch as fast as possible
x={1,2,3,4,5,6,7,8,9}
y={1,2,3,54,75,86,79,8,99}
z=x and y
print(z)



data={"lakshay":99,"Arjun":78,"Verma":89,"khattar":98}
# how to make dictionary of two lists
keys=['lakshay','khattar','arjun','verma']
locks=['pyhton','java','c++','ruby']
news=dict(zip(keys,locks))
# and add after making if needed
news['Tutti']='C#'
# and delete after making if needed
del news['lakshay']
print(news)

# within within within
rpog={'JS':'Atom','CS':'VS','Python':['Pycharm','Submlime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}

print(rpog['CS'])
print(rpog['Python'])
print(rpog['Java']['JSE'])