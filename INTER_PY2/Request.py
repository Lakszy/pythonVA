# import sys
from string import *
# # import requests
# # # GET A REQUEST WE USED PARAMS AND URL 
# # payload={'key1:':'value1'}
# # res = requests.get('https://httpbin.org/get',params=payload)

# # print(res.url)


# # # POST A REQUEST WE USED DATA AND TEXT 
# # data={'key1:':'value1'}
# # res1 = requests.post('https://httpbin.org/post',data=payload)

# # print(res1.text\)
# a =[12,3,45,6,78,90]
# string=''.join(str(i)for i in a )
# print(type(string))
# print(string)
# print(sys.version)      

# a=[1,2345,23,4,56,78,9]
# c=list(reversed(a))
# d=list(sorted(a))
# b=a[::-1]
# print(b)
# print(a)
# print(c)
# print(d)


# names={'lakshay':1234,'khattar':189,'lala':90909,'khtam':12345}
# lnames= []
# for i in names:
#     if i[0] == 'k':
#         lnames.append(i)
# print(lnames)

# llnames =[name for name in names if name[0] == 'l']
# print(llnames)

# aa='this is a sample string'
# lm=[]
# cnt=-1
# for i in aa:
#     if i not in lm:
#        lm.append(i)
#        cnt+=1   
# print(lm)
# print(cnt)
# print(set(aa))
 
# arr=[10,20,30,40]
# n=len(arr)
# for i in range(n):
#     for j in range(i,n):
#         for k in range(i,j+1):
#             print(arr[k],end=' ')
#         print()



# str1=input("Enter the string")
# lenw=len(str1)

# for i in range (lenw):
#     for j in range (i+1,lenw+1):    
#         print(str1[i:j])
        

def twoSum(a,target):   
    i,j=0,len(a)-1
    while i<j:  
        sm = a[i] + a[j]
        if target == sm:
            print(a[i],a[j])
            return True
        elif sm < target:
            i=i+1
            
        else:
            j=j-1
    return False

print(twoSum([1,14,10,16,20],26))