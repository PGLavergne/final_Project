from tkinter import*
import random
import tkinter as tk

#Screens or the window's higth and weidth 
Gwidth =600
Gheight= 600
speed= 50# speed 
spaceSize=20
bodyParts= 5 #body part 
backround=  "#FFFFFF"
snake_color= "#0000FF"
food_color= "#00FF00"

click= tk.Tk() #window define it as click 
click.title("Snake Game")# title 
#click.resizable(0,0)
score= 0  # label to show the score
direction= 'down'

#title for the score 
Score_label=Label(click, text="Score:{}".format(score), font=('score font',20))
Score_label.pack()
canvas=Canvas(click,bg=backround, height= Gheight,width=Gwidth)
canvas.pack()

#Class snake with using Canvas class from tkinter
class Snake(tk.Canvas): 
    def __init__(self):
         super().__init__(click, bg=backround, height=Gheight, width=Gwidth)
         self.body_size=bodyParts
         self.coordinates= []
         self.squares=[]

         for i in range(0, bodyParts):
            self.coordinates.append([0,0])# for snake to appear in top left 

         for x,y in self.coordinates:
            square= canvas.create_rectangle(x,y, x+spaceSize, y+spaceSize, fill=snake_color, tag= "snake")  #making square shapes for snake
            self.squares.append(square)

 #the object class which is being refered to food       
class Food: 
    def __init__(self):
        x=random.randint(0,(Gwidth/spaceSize)-1) * spaceSize    # to generated integer by using randint 
        y= random.randint(0,(Gheight/spaceSize)-1) * spaceSize
        self.coordinates= [x,y]
        self.canvas=canvas
        self.identity= canvas.create_oval(x, y, x+ spaceSize, y + spaceSize,fill= food_color, tag= "Food")


# function for moves 
def next_move(snake, food):
    global score
    x,y= snake.coordinates[0]
    if direction== "up": 
         y -=spaceSize # to move 1 space up
        
    elif direction== "down":
        y +=spaceSize # to move 1 space down
        
    elif  direction=="right":
        x +=spaceSize

    elif  direction=="left":
        x -=spaceSize
    snake.coordinates.insert(0,(x,y))
    square= canvas.create_rectangle(x,y, x + spaceSize, y+spaceSize, fill= snake_color)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        score += 1

        Score_label.config(text=" Score:{}".format(score) )
        canvas.delete(food.identity)
        food=Food()
    else: 

        del snake.coordinates[-1]
        canvas.delete("snake")
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if collisions(snake):
        gameOver()
    else: 
        click.after(speed, next_move, snake, food)

#Function for snake to change directions 
def changeDirection(new_direction):
    
    global direction

    if new_direction== 'right':
        if direction != 'left':
            direction=new_direction

    elif new_direction== 'left':
        if direction != 'right':
            direction=new_direction

    elif new_direction== 'up':
        if direction != 'down':
            direction=new_direction
    elif  new_direction== 'down':
        if direction != 'up':
            direction=new_direction       

# function for if snake touch the walls or itself 
def collisions(snake):
    x ,y= snake.coordinates[0]
    if x<0 or x>=Gwidth: #game width 
        print("GameOver") 
        return True
    elif y<0 or y>= Gheight: #game height 
        print("GameOver") 

        return True
    
    for body_part in  snake.coordinates[1:]: 
        if x==body_part[0] and y== body_part[1]:
            print("GameOver") 
            return True 
    
    return False 

#Game over function 
def gameOver():
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

click.bind('<Left>', lambda event: changeDirection('left'))
click.bind('<Right>', lambda event: changeDirection('right'))
click.bind('<Up>', lambda event: changeDirection('up'))
click.bind('<Down>', lambda event: changeDirection('down'))


snake= Snake()
food= Food()
next_move(snake, food)

click.mainloop()