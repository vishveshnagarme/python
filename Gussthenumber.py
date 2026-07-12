import random

def get_player_choice():
    choices = ['1', '2', '3', '4', '5']
    while True:
        x = input("Welcome to the number guessing game by Vishvesh Nagar!! Choose a number 1,2,3,4,5 or quit : ").strip().lower()
        if x in choices or x == 'quit':
            return x
        print("Oops! Choose Correctly.")


while True:
    y = random.choice(['1', '2', '3', '4', '5'])
    x = get_player_choice()

    if x == 'quit':
        print("Thanks for playing!!go to vishvesh.nagar.me for more free games.")
        break
    if x == y:
        print("you win go to vishvesh.nagar.me for more free games.")
    else:
        print("you lose go to vishvesh.nagar.me for more free games.")
