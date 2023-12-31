list=[]
n=int(input("Enter the length of array:"))
for i in range(n):  
    x=int(input("Enter the value of array:"))
    list.append(x)

print(list)

f=int(input("Enter the element you want to search:"))
found= False
index=-1
for j in range(n):  
    if f == list[j]:    
        found=True 
        index=j
        break   

if found:
    print("Element found at:",j)
else:
    print("Element not found")