print("Welcome to Food Corner 🍕🍔")
name = input("What is your name?")
print(f"Nice to meet you, {name}!!")
print("This is our menu, what would you like to have -")
print("""
1.  Pizza - Regular/Large
2.  Burger - Regular/Large
3.  Milkshake - Regular/Large
4.  Pasta - Regular/Large 
""")
food = input("Please select your preferred item (1 - 4) : ")
size = input("Please select the size of your preferred item(R or L) :")

if food == "1":
    if size == "R":
        print("Pizza for regular size has been booked for ₹150")
    else:
        print("Pizza of Large size has been booked for ₹250")
elif food == "2":
    if size == "R":
        print("Burger for regular size has been booked for ₹100")
    else:
        print("Burger of Large size has been booked for ₹180")
elif food == "3":
    if size == "R":
        print("Milkshake for regular size has been booked for ₹120")
    else:
        print("Pizza of Large size has been booked for ₹200")
elif food == "4":
    if size == "R":
        print("Pasta for regular size has been booked for ₹130")
    else:
        print("Pizza of Large size has been booked for ₹210")
else:
    print("Invalid choice !!, Please select the given movies only")
print("THANK YOU FOR ORDERING FROM FOOD CORNER ❤❤")



