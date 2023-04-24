import pygame
from tkinter import*
import random
import tkinter as tk

#height and the weight of the Screen
WIdth =600
height= 600
speed= 100 # speed 
spaceSize=100
bodyP= 3 #body part 
snake_color= " #0000FF"
apple= "#00FF00"
Backround= " #000000"


class Snake: 
    pass

class Apple: 
    pass

def turn():
    pass
def direction( ): 
    pass
def collisions():
    pass
def gameOver(): 
    pass





click= tk.Tk() #window define it as click 
click.title(" Snake Game ")# title 

score= 0  # label to show the score 
direction= 'down '
Label=Label(click,text=" Score: " .format(score))
Label.pack()

click.mainloop()


