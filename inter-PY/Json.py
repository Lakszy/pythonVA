# person={"name":"John","age":18,"city":"Delhi","hasChildren":False,"title":["engineer","programmer"]}

# # dictionary to json
# perJSON= json.dumps(person,  indent=4)
# print(perJSON)

# # converting back to dictionary
# person = json.loads(perJSON)
# print(person)
# # ------------------- load(s) dump(s)---------------------   
   
# # writting into the file
# with open('person.json','w') as file:
#     json.dump(person,file,indent=4)
   
# # Now Reading from the file
# with open('person.json','r') as file:   
#     json.load(file)
#     print(person)

# # ------------------- load() dump()---------------------   
import json

# Creating your own Class and object
class User: 
    def __init__(self,age,name):    
        self.age=age
        self.name=name
        
user=User(29,'Max')

def encode_user(o):    
    if isinstance(o,User): 
        return{'age':o.age, 'name':o.name, o.__class__.__name__:True}
    else:   
        return("Type Error")

userJSON=json.dumps(user,default=encode_user)
print(userJSON)