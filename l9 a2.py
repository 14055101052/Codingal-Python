medical = input("Do you have a medical course? (Y/N) : ").strip().upper()
if medical == "Y" :
    print("You are allowed")
else : 
    attend = int(input("Please enter your attendance : "))
    if (attend >= 75) :
        print("You are allowed")
    else : 
        print("You are not allowed")