# wins
comp_wins = 0
player_wins = 0

import random

#players choice
def Choose_Option():
    user_choice = input("Choose Rock, Paper, or Scissors:")
    if user_choice in ("Rock", "rock", "R", "r"):
        user_choice = "r"
    elif user_choice in ("Paper", "paper", "P", "p"):
        user_choice = "p"
    elif user_choice in ("Scissors", "scissors", "S", "s"):
        user_choice = "s"
    elif user_choice in ("Gun", "gun", "G", "g"):
        user_choice = "g"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

#rng computer *randint*
def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice

#while loop, comes back to when playing again
while True:
    print ("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print ("")
    
    #long boring shit
    if user_choice == "r":
        if comp_choice == "r":
            print ("You chose rock. The computer chose rock. You tied.")
        elif comp_choice == "p":
            print ("You chose rock. The computer chose paper. You lost.")
            comp_wins += 1
        elif comp_choice == "s":
            print ("You chose rock. The computer chose scissors. You won")
            player_wins += 1
    elif user_choice == "p":
        if comp_choice == "r":
            print ("You chose paper. The computer chose rock. You won.")
            player_wins += 1
        elif comp_choice == "p":
            print ("You chose paper. The computer chose paper. You tied.")
        elif comp_choice == "s":
            print ("You chose paper. The computer chose scissors. You lost")
            comp_wins += 1
    elif user_choice == "s":
        if comp_choice == "r":
            print ("You chose scissors. The computer chose rock. You lost.")
            comp_wins += 1
        elif comp_choice == "p":
            print ("You chose scissors. The computer chose paper. You won.")
            player_wins += 1
        elif comp_choice == "s":
            print ("You chose scissors. The computer chose scissors. You tied")
    elif user_choice == "g":
        print ("You're fucking that kid that chose gun... You win")
        player_wins += 1
    
    print ("")
    print ("Player wins: " + str(player_wins))
    print ("Computer wins: " + str(comp_wins))
    print ("")
    
    #play again pussyy
    user_choice = input ("Do you want to play again? (y/n)")
    if user_choice in ("Y", "y", "Yes", "yes"):
        pass
    elif user_choice in ("N", "n", "No", "no"):
        break
    else:
        break