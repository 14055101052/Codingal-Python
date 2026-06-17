# try :
#  code that might cause error

# except:
# runs only if error occurs

# else : 
# Runs only if no error occurs in try block

# finally : 
#  Runs always


# try : 
#     print("try block")
# except : 
#     print("something went wrong")
# else : 
#     print("else block")
# finally : 
#     print("finally block")

def check_age(age):
    try : 
        age = int(age)
        if age < 0 :
            raise ValueError("Age is negative")
        if age % 2 == 0:
            print(f"The age {age} is even")
        else : 
            print(f"The age {age} is odd")
    except ValueError as e :
        print(f"Inavlid age : {e}")

input = int(input("Enter age : "))   
check_age(input)
    