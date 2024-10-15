#Imports all needed functions and data from modules
from random import *
from math import *
import pygame
#Initializes the pygame module
pygame.init()
#Creates a window to draw on, (1000,500) are the x and y sizes of the window
win=pygame.display.set_mode((1000,500))
#Creates a variable, which how long the window is open
run=True
#While the window is open
while run:
    #checks every event since the last frame
    for event in pygame.event.get():
        #if the red X at the top is clicked
        if event.type==pygame.QUIT:
            #window is no longer open. 
            run=False
    #fills thje window with a pure black color
    win.fill((0,0,0))
    #Updates the window, creating a new frame
    pygame.display.update()
#The window is closed
pygame.quit()