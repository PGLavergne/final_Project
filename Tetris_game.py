import pygame
import random


colors = [
    (0,0,0),
    (120,37,179),
    (100,179,179),
    (80,34,22),
    (80,134,22),
    (180,34,22),
    (180,34,122),
]
#The figure class, arraylist/sequence for our figures
#main list contains figure types
#numbers in each figure represent positions in 4x4 matrix
#Try and add some missing figures
class Figure:
    
    x = 0
    y = 0
    
    figures = [
        [[1,5,9,13], [4,5,6,7]],
        [[1,2,5,9], [0,4,5,6], [1,5,9,8], [4,5,6,10]],
        [[1,2,6,10], [5,6,7,9], [2,6,10,11], [3,5,6,7]],
        [[1,4,5,6], [1,4,5,9], [4,5,6,9], [1,5,6,9]],
        [[1,2,5,6]],
    ]

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0
    
    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        

#Now we begin with the tetris class
#state tells us if were still playing or not
#field is the field of the game that contains 0's where it is empty and colors where there are figures

class Tetris:
    
    def __init__(self,height,width):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None
        
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j  in range(width):
                new_line.append(0)
            self.field.append(new_line)
    
    #Creates a new figure and positions it at coordinates: (3,0)
    def new_figure(self):
        self.figure = Figure(3,0)
    
    
    #Go in and check each cell in the 4x4 matrix of the current figure
    #check if self.field[][] > 0
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i*4+j in self.figure.image():
                    if i + self.figure.y> self.height -1 or \
                        j + self.figure.x > self.width -1 or \
                        j +self.figure.x < 0 or \
                        self.field[i + self.figure.y][j + self.figure.x]> 0:
                            intersection = True
        return intersection
    
    #This method will determine if the figure has reached the bottom and checks for intersections
    #If true, the figure should stop and remain fixed at the bottom
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i *4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state="gameover"
    
    #Now, let's check and see if any horizontal lines need to be destroyed
    #Create a new figure if thats the case, if it already intersects then gg
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] ==0:
                    zeros+=1
            if zeros == 0:
                    lines+=1
                    for i1 in range(i,1,-1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
    
    #Now we must implement the move methods:
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
        
    def go_down(self):
        self.figure.y +=1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
            
    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x
    
    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation
            
pygame.init()


            
            

        
    
    
    
    
    