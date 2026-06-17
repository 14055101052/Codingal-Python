import random
num = str(random.randint(0,9))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time")
print("The game ends when you get 1 hero")
count = 0

while True : 
    guess = input("Enter your number : ")

    if num == guess :
        print("You win the game !!")
        print("The number was : ", num, "Number of guesses : ", count)
        break

    else : 
        count = count + 1
        print("Your guess isn't quite right, try again")