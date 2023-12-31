s1=" Lakshay is my name "
with open("test.txt","a") as f:   
    f.write(s1)
    
s1=" Lakshay is my name "
with open("test.txt","w") as f:   
    f.write(s1)
    
with open("test.txt","r") as f1:   
     s=f1.read()
     print(s)




try:    
    a=int(input("Enter the number"))
    print(a+3)
except Exception as e:
    print("Some error occured",e)