import tkinter as tk
import random
options = ["rock", "paper", "scissors"]


def check_win(player_choice, computer_pick):
    if player_choice == "rock" and computer_pick == "scissors":

        return ("You won!")
    elif player_choice == "paper" and computer_pick == "rock":

        return ("You won!")
    elif player_choice == "scissors" and computer_pick == "paper":

        return ("You won!")
    elif player_choice == computer_pick:
        return ("Game Tie!")
    else:
        return("You lost!")


def computer_pick():
    random_number = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2
    computer = options[random_number]
    return (computer)


def play(player_choice):
    computer_choice = computer_pick()
    result = check_win(player_choice, computer_choice)
    result_label.config(text=f"You chose {player_choice}, the computer chose {computer_choice}. {result}")




# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the game label
game_label = tk.Label(root, text="Choose your move:")
game_label.pack()

# Create the button widgets
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack()

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
