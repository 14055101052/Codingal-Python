import random
while True : 
    user_action = input("Enter a choice(rock, paper, scissor) : ")
    possibile_action = ["rock", "paper", "scissor"]
    com_action = random.choice(possibile_action)
    print(f"\nYour choice is {user_action} and computer choice is {com_action}")

    if user_action == com_action:
        print("It is a tie")
    elif user_action == "rock" :
        if com_action == "scissor" : 
            print("Rock smashes scissor, You win")
        else : 
            print("Paper smashes rock, Computer wins")
    elif user_action == "paper" :
        if com_action == "rock" : 
            print("Paper smashes rock, You win")
        else : 
            print("Scissor smashes paper, Computer wins")
    elif user_action == "scissor" :
        if com_action == "paper" : 
            print("Scissor smashes paper, You win")
        else : 
            print("Rock smashes scissor, Computer wins")

    play_again = input("Play again ? (Y/N) : ")
    if play_again.upper() == "N":
        break

