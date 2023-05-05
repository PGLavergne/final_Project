import pygame
import random

#Each color is represented as a tuple of 3 integers
#First color is black(no red,green, or blue light)
colors = [
    (0,0,0),
    (120,37,179),
    (100,179,179),
    (80,34,22),
    (80,134,22),
    (180,34,22),
    (180,34,122),
    (180,14,156),
    (100,0,78),
    (120,89,10),
]
#The figure class, arraylist/sequence for our figures
#numbers in each figure represent positions in 4x4 matrix
#Each shape is represented as a list of lists
#The first list in each shape contains the indices of the squares that make up the top half of the shape
#The second list contains the indices of the squares that make up the bottom half of the shape
#For example, the first shape in the list is the L-shaped piece, represented as:
#[[1,5,9,13], [4,5,6,7]]
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
    #Constructor that creates random shapes from the given list of figures
    #Assigns a random color
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0
    
    #Returns current image of the tetris piece based on its type and rotation
    def image(self):
        return self.figures[self.type][self.rotation]

    #Rotates the tetris piece by updating its rotation attribute
    #Increment by 1 and mod to wrap back to 0 if it exceeds the maximum number of rotations for the current type
    #Ex) If the current type is 0, then there are 2 possible rotations
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        

#Now we begin with the tetris class
#The Tetris class has a variety of attributes, score, width,height, and other setting featured for the game itself

class Tetris:
    
    #Constructor, initializes various attributes of the tetris game,creates empty field, and sets game state to 'start'
    def __init__(self,height,width):
        self.level = 2
        self.score = 0
        self.piecesplaced = 0
        self.state = "start"
        #Creates an empty list to store the game field
        self.field = []
        self.height = 0
        self.width = 0
        #Coordinates for the starting tetris piece
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None
        
        self.height = height
        self.width = width
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
    #Checks if current position of falling piece intersects with any existing pieces
    #Method loops over each square of the 4x4 matrix that represents the current position of the falling piece
    #If the position of the sqaure, plus the current position of the falling piece is out of bounds
    #or if the square is already occupied by an existing piece
    #intersection is set to 'True'
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
                    
        #Increment total number of pieces placed by 1 after touching the base
        self.piecesplaced+=1
        #break_lines method called to check if lines have been completed
        self.break_lines()
        #New falling piece generated
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
#initialize the game           
pygame.init()

#Method to increase the speed of the object using the frame rate
def increase_speed():
    global fps
    fps +=5

#Colors, once again
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128, 128, 128)
RED = (255,0,0)

size = (400, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("PaulAllensCard")

done = False
#Controls the speed at which figures fall on their own
clock = pygame.time.Clock()
#Controls the speed at which figures fall after holding down
fps = 25
game = Tetris(20,10)
counter = 0

#Establish usable fonts
font = pygame.font.SysFont('Comic Sans MS', 25, True, False)
font1 = pygame.font.SysFont('Comic Sans MS', 65, True, False)



pressing_down = False
 #Main Game loop
while not done:
    if game.figure is None:
        game.new_figure()
    counter+=1
    if counter > 100000:
        counter = 0
        
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20,10)
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

       
    
    
    screen.fill(BLACK) 
    
    #Loops to draw the figures
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom,game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen,colors[game.field[i][j]],
                                [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])


    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i*4+j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom *(j + game.figure.x) + 1,
                                      game.y + game.zoom *(i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom -2])
                    
    
    text = font.render("Score: " + str(game.score), True, RED)
    text2 = font.render("Pieces Placed " + str(game.piecesplaced), True, WHITE)
    text_game_over = font1.render("YOU SUCK!", True, (255,125,0))
    text_game_over1 = font1.render("Press ESC", True, (255,215, 0))
    
    

    screen.blit(text,[0,0])
    screen.blit(text2,[200,0])
    if game.state =="gameover":
        screen.blit(text_game_over, [20,200])
        screen.blit(text_game_over1, [25,265])
    

    pygame.display.flip()
   
    
    #Increases the speed of the falling objects the longer the game goes on
    #Normal Speed:
    if game.piecesplaced > 5:
        clock.tick(120)
    elif game.piecesplaced > 4:
        clock.tick(60)
    elif game.piecesplaced > 1:
        clock.tick(25)
    else:
        clock.tick(10)
 
    
pygame.quit()
        