## Creating the display by importing the tkinter ##
from tkinter import *
from tkinter import ttk

# def setImage(screen): 

#     image_Size = Tk()
#     picture = PhotoImage(file='fist.png')
#     Button(image_Size, text='Rock', image=picture)
#     # Photo size: 388x348

#     return None

def gameWindow():
    root = Tk()
    
    root.columnconfigure(0, weight=5)
    root.rowconfigure(1, weight=5)

    # Creating the grid size
    root.geometry("800x500")
    root.resizable(0, 0)
    root.title("Rock Paper Scissors")


    # Quit button
    quit_Button = ttk.Button(root,text="Quit", command=root.destroy)
    quit_Button.grid(column=1, row=3, padx=5, pady=5)


    image_Size = Tk()
    picture = PhotoImage(file='fist.png')
    Button(image_Size, text='Rock', image=picture)



    root.mainloop()
    return   

gameWindow()

    
