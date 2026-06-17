import random
import math

number = random.randint(1, 100)
user_guess = float(input("Guess the square root of the number: "))
actual_sqrt = math.sqrt(number)

print("The random number was:", number)

if round(user_guess, 2) == round(actual_sqrt, 2):
    print("Correct! Well done!")
else:
    print("Incorrect guess.")
    print("The correct square root is:", round(actual_sqrt, 2))