## Creating the display by importing the pygame module ##

from turtle import width
import pygame

def setImage(screen): 

    image = pygame.image.load("fist.png")

    object_rect = image.get_rect(topleft=(0,0))

    screen.blit(image,object_rect)

    return None

def gameWindow():

    pygame.init()

    width = 1280
    height = 720

    # Creating the screen
    screen = pygame.display.set_mode((width, height))

    # Creating the caption
    pygame.display.set_caption('Rock, Paper, Scissors')

    # Choosing the background colour as white
    Colour_Background = (255,255,255)

    screen.fill(Colour_Background)

    setImage(screen)

    # Updating the display by using flip command
    pygame.display.flip()

    running = True

    while (running):

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                running = False

gameWindow()

    
