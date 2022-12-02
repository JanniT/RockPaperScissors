## Creating the display by importing the tkinter ##
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 

def gameWindow():
    root = Tk()
    
    root.columnconfigure(0, weight=3)
    root.rowconfigure(1, weight=3)

    # Creating the grid size
    root.geometry("1300x500")
    root.title("Rock Paper Scissors")

    # Quit button
    quit_Button = ttk.Button(root,text="Quit", command=root.destroy)
    quit_Button.grid(column=3, row=3, padx=5, pady=5)

    # Rock button
    photo = PhotoImage(file="Pictures/fist.png")
    rock_button = Button(root, text='Rock', image=photo)
    rock_button.grid(column=0, row = 0)

    # Paper button
    photo = PhotoImage(file="Pictures/paper.png")
    paper_button = Button(root, text='Paper', image=photo)
    paper_button.grid(column=1, row = 0)

    # Scissors button
    photo = PhotoImage(file="Pictures/scissors.png")
    scissors_button = Button(root, text='Scissors', image=photo)
    scissors_button.grid(column=2, row = 0)


    root.mainloop()
    return   

gameWindow()

    
