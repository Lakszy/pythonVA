age=int(input("Enter your age: "))

# if (age>18):
#     print("Good to go")
# else:
#     print("Too Good So You Can Go Home!")
    
match age: 
        case 1:
            print("Matched 1")
        case 51:
            print("Matched 51")
        case 41:
            print("Matched 41")
        case 31:
            print("Matched 31")
        case 21:
            print("Matched 21")
        case 11:
            print("Matched 11")
        case _:
            print("Default")