income = int(input("Enter your income : "))
if (income >= 40000) :
    if (income > 60000) :
        print("First check is done, you are elgible for premium stock")
    if (income > 80000) :
        print("Second check is done, you are elgible for ultra premium stock")
    else : 
        print("Validation complete (Normal category)")
else : 
    print("income amount is less than the required amount")


age = int(input("Enter your age : "))
if (age >= 18) :
    if (age <= 19) :
        print("You are in teens")
    elif (age <= 29) :
        print("You are in you 20s")
    else : 
        print("User is a senior citizen")