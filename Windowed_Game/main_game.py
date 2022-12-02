## Creating the display by importing the tkinter ##
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import onClickRock, onClickPaper, onClickScissors

def gameWindow():
    root = Tk()
    root.columnconfigure(0, weight=3)
    root.rowconfigure(1, weight=2)

    # Creating the grid size
    root.geometry("1300x800")
    root.maxsize(1300, 600)
    root.minsize(1300, 600)
    root.title("Rock Paper Scissors")

    title_label = ttk.Label(root, text="Please choose: \nRock, Paper, Scissors", font=('Helvetica 30 bold'))
    title_label.grid(column=0, row=0)

    # Quit button
    quit_Button = ttk.Button(root,text="Quit",command=root.destroy)
    quit_Button.grid(column=3, row=3, padx=5, pady=5)

    # Rock button
    photo_rock = PhotoImage(file="Pictures/fist.png")
    rock_button = Button(root, text='Rock', image=photo_rock, command=onClickRock.onClickRock)
    rock_button.grid(column=0, row=1)

    # Paper button
    photo_paper = PhotoImage(file="Pictures/paper.png")
    paper_button = Button(root, text='Paper', image=photo_paper, command=onClickPaper.onClickPaper)
    paper_button.grid(column=1, row=1)

    # Scissors button
    photo_scissors = PhotoImage(file="Pictures/scissors.png")
    scissors_button = Button(root, text='Scissors', image=photo_scissors, command=onClickScissors.onClickScissors)
    scissors_button.grid(column=2, row=1)

    root.mainloop()
    return  

gameWindow()

    
