print("Welcome to Smart Cash ATM")
pin = input("Please enter your pin : ") #Your pin is 1234
balance = 10000
if pin == "1234":
    print("The balance in your account is : ", balance)
    amount = int(input("Please enter the money withdrawn : "))
    if amount > balance :
     print("Insufficient amount !!!")
    else :
     note_2000 = amount//2000
     amount = amount%2000
     note_500 = amount//500
     amount = amount%500
     note_100= amount//100
     amount = amount%100

     print("number of 2000 notes : ", note_2000)
     print("number of 500 notes : ", note_500)
     print("number of 100 notes : ", note_100)
    
else : 
    print("Please enter your correct pin")


