from tkinter import*
import pygame
import random
import tkinter as tk

click= tk.Tk() #window define it as click 
click.title(" Snake Game ")# title 
click.resizable(0,0)
score= 0  # label to show the score
direction= 'down'

Game_width =700
Game_height= 700
speed= 50 # speed 
space_Size=50
body_Parts= 5 #body part 
backround=  "#000000"
snake_color= " #0000FF"
food_color= "#00FF00"

label=Label(click, text="Score:{}".format(score))
label.pack()
canvas=Canvas(click,bg=backround, height= Game_height,width=Game_width)
canvas.pack()


class Snake: 
    def __init__(self):
        self.body_size=body_Parts
        self.coordinates= []
        self.squares=[]

        for i in range(0, body_Parts):
            self.coordinates.append([0,0])# for snake to appear in top left 

        for x,y in self.coordinates:
            square= Canvas. create_rectangle(x,y, x+space_Size, y+space_Size, fill=snake_color, tag= "snake")
            self.square.append(square)
        
class Food: 
    def __init__(self):
        x=random.randint(0,(screen_width/space_Size)-1) * space_Size
        y= random.randint(0,(screen_height/space_Size)-1) * space_Size
        self.coordinates= [x,y]
        Canvas.create_oval(x,y, x+space_Size, y+ space_Size,fill= food_color, tag= " Food ")

def next_turn(snake, food):
    x,y= snake.coordinates[0]
    if direction== "up": 
         y-=space_Size # to move 1 space up
        
    elif direction== "down":
        y+=space_Size # to move 1 space down
        
    elif  direction=="right":
        x+=space_Size

    elif  direction=="left":
        x-=space_Size
    snake.coordinates.insert(0,(x,y))

    square= canvas.create_rectangle(x,y, x + space_Size, y+space_Size, fill= snake_color)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score 
        score += 1

        label.config(text=" Score{}".format(score) )
        canvas.delete("food")
        food=Food()
    else: 

        del snake.coordinates[-1]
        canvas.delete(snake, square[-1])
        del snake.squares[-1]

    if change_direction(snake):
        game_over()
    else: 
        click.after(speed, next_turn, snake, food)
def change_direction(new_direction):
    global direction

    if new_direction== 'left':
        if direction != 'right':
            direction=new_direction

    elif new_direction== 'right':
        if direction != 'left':
            direction=new_direction

    elif new_direction== 'up':
        if direction != 'down':
            direction=new_direction
    elif  new_direction== 'down':
        if direction != 'up':
            direction=new_direction       

def check_collisions(snake):
    x ,y= snake.coordinates[0]
    if x<0 or x>=Game_width: 
        return True
    elif y<0 or y>= Game_height: 
        return True
    
    for body_part in  snake.coordinates[1:]: 
        if x==body_part[0] and y== body_part[1]:
                  return True 
    
    return False 

def game_over():
    canvas.delete(ALL)
    canvas.create_text( canvas.winfo_width()/2 ,
                       canvas.winfo_height()/2, 
                       font=('consolas', 70), 
                       text="Game Over", 
                       fill= "Blue",tag= "gameover")
 


click.update()
#change the front

click_width= click.winfo_width()
click_height= click.winfo_height()
screen_width= click.winfo_screenwidth()
screen_height= click.winfo_screenheight()
x=int((screen_width/2) - (click_width/2))
y=int((screen_height/2) - (click_height/2))
click.geometry(f"{click_width}x{click_height}+{x}+{y}")

click.bind('<left>', lambda even: change_direction('left'))
click.bind('<right>', lambda even: change_direction('right'))
click.bind('<up>', lambda even: change_direction('up'))
click.bind('<down>', lambda even: change_direction('down'))


snake= Snake()
food= Food()
next_turn(snake, food)

click.mainloop()