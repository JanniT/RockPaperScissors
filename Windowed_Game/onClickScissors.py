from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import computer_Choise

def onClickScissors(): 
    root = Tk()
    root.columnconfigure(0, weight=10)
    root.rowconfigure(1, weight=10)

    # Creating the grid size
    root.geometry("350x250")
    root.title("Scissors")

    # Back button
    back_Button = ttk.Button(root,text="Back", command=root.destroy)
    back_Button.grid(column=1, row=3, padx=10, pady=10)

    choise_text = ttk.Label(root, text="You chose Scissors!", font=('Helvetica 20 bold'))
    choise_text.grid(column=0, row=0)

    userChoise = "Scissors"
    computer_choise = computer_Choise.computer_Choise() 

    computer_text = ttk.Label(root, text=(f"Computer chose {computer_choise}!"), font=('Helvetica 15 bold'))
    computer_text.grid(column=0, row=1)
 
    if (userChoise == computer_choise): 
        tie_text = ttk.Label(root, text="It's a tie", font=('Helvetica 15 bold'))
        tie_text.grid(column=0, row=2)
    
    elif (computer_choise == "Rock" and userChoise == "Scissors"): 
        computer_text1 = ttk.Label(root, text="Rock beats Scissors,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text1.grid(column=0, row=2)

    elif (computer_choise == "Paper" and userChoise == "Rock"):
        computer_text2 = ttk.Label(root, text="Paper beats Rock,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text2.grid(column=0, row=2)
        
    elif (computer_choise == "Scissors" and userChoise == "Paper"):
        computer_text3 = ttk.Label(root, text="Scissors beats Paper,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text3.grid(column=0, row=2)

    else: 
        win_text = ttk.Label(root, text="You win!", font=('Helvetica 15 bold'))
        win_text.grid(column=0, row=2)

    root.after(3000, lambda:root.destroy())
    return