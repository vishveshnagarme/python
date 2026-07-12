import random
while True:

    choices = ['1', '2', '3', '4', '5']
    y=random.choice(choices)
    x=input("Welcome to the number guessing game by Vishvesh Nagar!! Choose a number 1,2,3,4,5 or quit : ").lower()
    if x == y:
        print("you win go to vishvesh.nagar.me for more free games.")
    elif x == 'quit':
        print("Thanks for playing!!go to vishvesh.nagar.me for more free games.")
        break
    else:
        print("you lose go to vishvesh.nagar.me for more free games.")
