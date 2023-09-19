import tkinter as tk
from tkinter import simpledialog

# tkinter window
root = tk.Tk()
root.withdraw()

p1 = False
p2 = False
# No of tries each player took to guess the number
pl1_tries = 0
pl2_tries = 0

# player 1 enter the number to guess
try:
    pl1 = simpledialog.askstring("MMG", "Player 1 Enter a Number:")
    if pl1 is not None:
        pl1 = list(pl1)
        print("mastermind game")
        print("player2:")
        # player 2's turn to guess the number
        while True:
            pl2 = simpledialog.askstring("MMG", "Player 2 Enter a Number:")
            if pl2 is not None:
                pl2 = list(pl2)
                pl2_tries += 1
                p2 = True

            if pl1 == pl2:
                print("Mastermind! The Numbers Are The Same")
                break
            elif common := [digit for digit in pl1 if digit in pl2]:
                common_str = ", ".join(map(str, common))
                print("Common Digits:", common_str)
                p2 = True
    else:
        print("player1 enter a valid number")
except Exception as e:
    print(f"An error occurred: {e}")

# player 2 enter the number to guess

try:
    pl2 = simpledialog.askstring("MMG", "Player 2 Enter a Number:")
    if pl2 is not None:
        pl2 = list(pl2)
        print("player1 :")
        # player 2's turn to guess the number
        while True:
            pl1 = simpledialog.askstring("MMG", "Player 1 Enter a  Number:")
            if pl1 is not None:
                pl1 = list(pl1)
                pl1_tries += 1
                p1 = True
            if pl1 == pl2:
                print("Mastermind! The Numbers Are the Same")
                break
            elif common := [digit for digit in pl1 if digit in pl2]:
                common_str = ", ".join(map(str, common))
                print("Common Digits:", common_str)
                p1 = True
    else:
        print("player2 enter a valid number")
except Exception as e:
    print(f"An error occurred: {e}")

# display of No of tries by each player
if p1 is not False and p2 is not False:
    print(f"No of tries by player 1: {pl1_tries}")
    print(f"No of tries by player 2: {pl2_tries}")
    print("results:")
    if pl1_tries == pl2_tries:
        print("It Was a Draw")
    elif pl1_tries > pl2_tries:
        print("Player 2 is the Mastermind")
    elif pl2_tries > pl1_tries:
        print("Player 1 is the Mastermind")
    else:
        print("No Masterminds here")
else:
    print("no one played,run the game again")
root.mainloop()
