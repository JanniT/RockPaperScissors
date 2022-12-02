## Creating the display by importing the tkinter ##
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

def gameWindow():
    root = Tk()
    
    root.columnconfigure(0, weight=3)
    root.rowconfigure(1, weight=2)

    # Creating the grid size
    root.geometry("1300x800")
    root.title("Rock Paper Scissors")

    title_label = ttk.Label(root, text="Please choose: \nRock, Paper, Scissors", font=('Helvetica 30 bold'))
    title_label.grid(column=0, row=0)

    # Quit button
    quit_Button = ttk.Button(root,text="Quit", command=root.destroy)
    quit_Button.grid(column=3, row=3, padx=5, pady=5)

    # Rock button
    photo_rock = PhotoImage(file="Pictures/fist.png")
    rock_button = Button(root, text='Rock', image=photo_rock, command=onClickRock)
    rock_button.grid(column=0, row=1)

    # Paper button
    photo_paper = PhotoImage(file="Pictures/paper.png")
    paper_button = Button(root, text='Paper', image=photo_paper) #, command=onClickPaper)
    paper_button.grid(column=1, row=1)

    # Scissors button
    photo_scissors = PhotoImage(file="Pictures/scissors.png")
    scissors_button = Button(root, text='Scissors', image=photo_scissors) #, command=onClickScissors)
    scissors_button.grid(column=2, row=1)


    root.mainloop()
    return   

def onClickRock(): 
    root = Tk()
    root.columnconfigure(0, weight=10)
    root.rowconfigure(1, weight=10)

    # Creating the grid size
    root.geometry("400x250")
    root.title("Rock")

    # Back button
    quit_Button = ttk.Button(root,text="Back", command=root.destroy)
    quit_Button.grid(column=1, row=3, padx=5, pady=5)

    choise_text = ttk.Label(root, text="You chose ROCK!", font=('Helvetica 20 bold'))
    choise_text.grid(column=0, row=0)

    userChoise = "Rock"
    computer_choise = computer_Choise() 

    computer_text = ttk.Label(root, text=(f"Computer chose {computer_choise}!"), font=('Helvetica 15 bold'))
    computer_text.grid(column=0, row=1)
 
    if (userChoise == computer_choise): 
        tie_text = ttk.Label(root, text="It's a tie", font=('Helvetica 15 bold'))
        tie_text.grid(column=0, row=2)
    
    elif (computer_choise == "Rock" and userChoise == "Scissors"): 
        computer_text1 = ttk.Label(root, text="Scissors beats rock,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text1.grid(column=0, row=2)

    elif (computer_choise == "Paper" and userChoise == "Rock"):
        computer_text2 = ttk.Label(root, text="Scissors beats rock,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text2.grid(column=0, row=2)
        
    elif (computer_choise == "Scissors" and userChoise == "Paper"):
        computer_text3 = ttk.Label(root, text="Scissors beats rock,\ncomputer wins!", font=('Helvetica 15 bold'))
        computer_text3.grid(column=0, row=2)

    else: 
        win_text = ttk.Label(root, text="You win!", font=('Helvetica 15 bold'))
        win_text.grid(column=0, row=2)

    root.after(5000, lambda:root.destroy())
    return 

def computer_Choise(): 
    choiseList = ['R', 'P', 'S']
    computerChoise = random.choices(choiseList)
    computerChoise=','.join(computerChoise)

    if computerChoise == "R":
        return "Rock"
    elif computerChoise == "P":
        return "Paper"
    else:
        return "Scissors"

    
# def onClickPaper(): 
#     root = Tk()
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(1, weight=2)

#     # Creating the grid size
#     root.geometry("500x500")
#     root.title("Paper")

#     # Back button
#     quit_Button = ttk.Button(root,text="Back", command=root.destroy)
#     quit_Button.grid(column=3, row=3, padx=5, pady=5)
    
#     photo_paper = PhotoImage(file="Pictures/paper.png")
#     paper_button = Button(root, text='Paper', image=photo_paper)
#     paper_button.grid(column=1, row=1)
#     return

# def onClickScissors(): 
#     root = Tk()
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(1, weight=2)

#     # Creating the grid size
#     root.geometry("500x500")
#     root.title("Scissors")

#     # Back button
#     quit_Button = ttk.Button(root,text="Back", command=root.destroy)
#     quit_Button.grid(column=3, row=3, padx=5, pady=5)
    
#     photo_scissors = PhotoImage(file="Pictures/scissors.png")
#     scissors_button = Button(root, text='Scissors', image=photo_scissors)
#     scissors_button.grid(column=2, row=1)
#     return


gameWindow()

    
