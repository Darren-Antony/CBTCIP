import tkinter as tk
import random as rn


# function to validate game rules
def game(plyr):
    computer_choice = rn.choice(["rock", "paper", "scissors"])
    cmp.config(text=f"Computer chose: {computer_choice}")
    ply.config(text=f"your choice:{plyr}")
    if plyr == computer_choice:
        result.config(text=f"Its a draw")
    elif (
            (plyr == "rock" and computer_choice == "scissors")
            or (plyr == "scissors" and computer_choice == "paper")
            or (plyr == "paper" and computer_choice == "rock")
    ):
        result.config(text="You win!")
    else:
        result.config(text="Computer wins!")


# main window
root = tk.Tk()

lbl = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 40), bg="gold")
lbl.pack()
lbl2 = tk.Label(root, text="Player vs Computer ", font=30)
lbl2.pack()

# frame for buttons
frame = tk.Frame(root)
frame.pack()

# button representing rock, paper and scissors
rock = tk.Button(frame, text="stone✊", font=30, command=lambda: game("rock"), bg="navajo white")
paper = tk.Button(frame, text="paper🖐️", font=30, command=lambda: game("paper"))
scissors = tk.Button(frame, text="scissors✌️", font=30, command=lambda: game("scissors"), bg="sky blue")

rock.grid(row=0, column=0, padx=10)
paper.grid(row=0, column=1, padx=10)
scissors.grid(row=0, column=2, padx=10)
cmp = tk.Label(root, text="", font=20)
cmp.pack()
ply = tk.Label(root, text="", font=20)
ply.pack()
result = tk.Label(root, text="", font=20)
result.pack()
root.mainloop()
