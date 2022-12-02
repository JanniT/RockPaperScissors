from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

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