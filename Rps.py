import random
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
while True:
    player_choice = input("RPS game created by Vishvesh Nagar .Visit vishvesh.nagar.me for more free games!!!Enter rock, paper, or scissors,quit(to QUIT): ").lower()
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock smashes scissors.")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win! Paper covers rock.")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors cut paper.")
    if player_choice == "quit":
        print("Bye Visit vishvesh.nagar.me for more free games!!!")
        break
    else:
        print("You lose! Visit vishvesh.nagar.me for more free games!!!")
