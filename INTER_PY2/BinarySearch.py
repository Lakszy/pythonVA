def bin(mylist,key):    
    l=0
    r=len(mylist)-1
    fnd=False
    while(l<=r and not fnd):
        middle=(l+r)//2
        if mylist[middle] == key:      
             fnd = True
             
        else:
            if key > mylist[middle]:    
                r= middle - 1
            else:   
                l= middle + 1    
                
    return fnd
    
    
print(bin([2,3,56,13,1],56))           
print(bin([2,3,56,13,1],26))           