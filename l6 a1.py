# citizenship = input("Are you indian ? Yes/No : ")
# age = int(input("Enter your age : "))

# if citizenship.lower() == "yes" and age >= 18 :
#     print("You can vote")
# else :
#      print("You cannot vote")

ch = input("Enter a character : ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else :
    print("Special Character")