import random
import tkinter as tk

def play(player_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    if player_choice == computer_choice:
        outcome = "It's a tie! Visit vishvesh.nagar.me for more free games!!!"
    elif player_choice == "rock" and computer_choice == "scissors":
        outcome = "You win! Rock smashes scissors.Visit vishvesh.nagar.me for more free games!!!"
    elif player_choice == "paper" and computer_choice == "rock":
        outcome = "You win! Paper covers rock.Visit vishvesh.nagar.me for more free games!!!"
    elif player_choice == "scissors" and computer_choice == "paper":
        outcome = "You win! Scissors cut paper.Visit vishvesh.nagar.me for more free games!!!"
    else:
        outcome = "You lose! The computer beat you.Visit vishvesh.nagar.me for more free games!!!"
        
    result_label.config(text="Computer chose: " + computer_choice + "\n\n" + outcome)

def play_rock():
    play("rock")

def play_paper():
    play("paper")

def play_scissors():
    play("scissors")

window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("300x350")

title_label = tk.Label(window, text="Choose your weapon!", font=("Arial", 14))
title_label.pack(pady=10)

btn_rock = tk.Button(window, text="Rock", width=15, command=play_rock)
btn_rock.pack(pady=5)

btn_paper = tk.Button(window, text="Paper", width=15, command=play_paper)
btn_paper.pack(pady=5)

btn_scissors = tk.Button(window, text="Scissors", width=15, command=play_scissors)
btn_scissors.pack(pady=5)

result_label = tk.Label(window, text="Make a move to start!", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()
