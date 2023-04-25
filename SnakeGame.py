import pygame
from tkinter import*
import random
import tkinter as tk

#height and the weight of the Screen
width =600
height= 600
speed= 100 # speed 
spaceSize=100
bodyP= 3 #body part 
snake_color= " #0000FF"
apple= "#00FF00"
backround=  "#000000"


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
canvasLable= Canvas(click, bg=backround,heig= height,wit=width )
canvasLable.pack()
click.update()
click_width=click.winfo_width()
click_height= click.winfo_height()
sheight= click.winfo_screenheight()
swidth= click.winfo_screenwidth()

w=(swidth/2)-(click_width/2)
h= (sheight/2)-(click_height/2)






click.mainloop()


