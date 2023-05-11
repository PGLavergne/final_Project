#!/usr/bin/env python3

import pygame
import random
pygame.init()

# Import Sprites
spr_emptyGrid = pygame.image.load("Sprites/empty_square.png")
flag_square = pygame.image.load("Sprites/flagged_square.png")
spr_grid = pygame.image.load("Sprites/square.png")
sq_1 = pygame.image.load("Sprites/num_1.png")
sq_2 = pygame.image.load("Sprites/num_2.png")
sq_3 = pygame.image.load("Sprites/num_3.png")
sq_4 = pygame.image.load("Sprites/num_4.png")
sq_5 = pygame.image.load("Sprites/num_5.png")
sq_6 = pygame.image.load("Sprites/num_6.png")
sq_7 = pygame.image.load("Sprites/num_7.png")
sq_8 = pygame.image.load("Sprites/num_8.png")
sq_mine = pygame.image.load("Sprites/mine.png")
sq_mineClicked = pygame.image.load("Sprites/mine_explode.png")
sq_mineFalse = pygame.image.load("Sprites/mine_falseAlarm.png")

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)
#code sourced from pyguru123
WIDTH = 10  
HEIGHT = 10  
mine_num = 9 
GRID_SIZE = 32  
BORDER = 16  
top_BORDER = 100  
DISP_WIDTH = GRID_SIZE * WIDTH + BORDER * 2  
DISP_HEIGHT = GRID_SIZE * HEIGHT + BORDER + top_BORDER  
DISP_GAME = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))  

TIMER = pygame.time.Clock()  

pygame.display.set_caption("MINESWEEPER")  

# Create global values
grid = []  # The main grid
mines = []  # Pos of the mines


# Create funtion to draw texts
def writeText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("helvetica", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (WIDTH * GRID_SIZE / 2 + BORDER, HEIGHT * GRID_SIZE / 2 + top_BORDER + yOff)
    DISP_GAME.blit(screen_text, rect)


# Create class grid
class Grid:
    def __init__(self, xGrid, yGrid, type):
        self.xCord = xGrid 
        self.yCord = yGrid  
        self.clicked = False  
        self.mineClicked = False  
        self.mineFalse = False  
        self.flag = False  

        # Create rectObject to handle drawing and collisions
        self.cords = pygame.Rect(BORDER + self.xCord * GRID_SIZE, top_BORDER + self.yCord * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        self.val = type  

    def drawGrid(self):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            DISP_GAME.blit(sq_mineFalse, self.cords)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        DISP_GAME.blit(sq_mineClicked, self.cords)
                    else:
                        DISP_GAME.blit(sq_mine, self.cords)
                else:
                    if self.val == 0:
                        DISP_GAME.blit(spr_emptyGrid, self.cords)
                    elif self.val == 1:
                        DISP_GAME.blit(sq_1, self.cords)
                    elif self.val == 2:
                        DISP_GAME.blit(sq_2, self.cords)
                    elif self.val == 3:
                        DISP_GAME.blit(sq_3, self.cords)
                    elif self.val == 4:
                        DISP_GAME.blit(sq_4, self.cords)
                    elif self.val == 5:
                        DISP_GAME.blit(sq_5, self.cords)
                    elif self.val == 6:
                        DISP_GAME.blit(sq_6, self.cords)
                    elif self.val == 7:
                        DISP_GAME.blit(sq_7, self.cords)
                    elif self.val == 8:
                        DISP_GAME.blit(sq_8, self.cords)

            else:
                if self.flag:
                    DISP_GAME.blit(flag_square, self.cords)
                else:
                    DISP_GAME.blit(spr_grid, self.cords)

    def updateValue(self):
    # Update the value when all grid is generated
        if self.val != -1:
            for x in range(-1, 2):
                if self.xCord + x >= 0 and self.xCord + x < WIDTH:
                    for y in range(-1, 2):
                        if self.yCord + y >= 0 and self.yCord + y < HEIGHT:
                            if grid[self.yCord + y][self.xCord + x].val == -1:
                                self.val += 1
                                
    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xCord + x >= 0 and self.xCord + x < WIDTH:
                    for y in range(-1, 2):
                        if self.yCord + y >= 0 and self.yCord + y < HEIGHT:
                            if not grid[self.yCord + y][self.xCord + x].clicked:
                                grid[self.yCord + y][self.xCord + x].revealGrid()
        elif self.val == -1:
            # Auto reveal all mines if it's a mine
            for m in mines:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()




def gameLoop():
    gameState = "Playing"  # Game state
    mineLeft = mine_num  # Number of mine left
    global grid  # Access global var
    grid = []
    global mines
    t = 1000  # Set time

    # Generating mines
    mines = [[random.randrange(0, WIDTH),
              random.randrange(0, HEIGHT)]]

    for c in range(mine_num - 1):
        pos = [random.randrange(0, WIDTH),
               random.randrange(0, HEIGHT)]
        same = True
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
                    break
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # Generating entire grid
    for j in range(HEIGHT):
        line = []
        for i in range(WIDTH):
            if [i, j] in mines:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)

    # Update of the grid
    for i in grid:
        for j in i:
            j.updateValue()

    # Main Loop
    while gameState != "Exit":
        # Reset screen
        DISP_GAME.fill(bg_color)

        # User inputs
        for event in pygame.event.get():
            # Check for closed window
            if event.type == pygame.QUIT:
                gameState = "Exit"
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameState = "Exit"
                        gameLoop()
            if t <= 1:
                t == 0
                gameState = "Game Over"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameState = "Exit"
                        gameLoop()
                if event.type == pygame.QUIT:
                    gameState = "Exit"
                
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.cords.collidepoint(event.pos):
                                if event.button == 1:
                                    # If player left clicked of the grid
                                    j.revealGrid()
                                    # Toggle flag off
                                    if j.flag:
                                        mineLeft += 1
                                        j.falg = False
                                    # If it's a mine
                                    if j.val == -1:
                                        gameState = "Game Over"
                                        j.mineClicked = True
                                elif event.button == 3:
                                    # If the player right clicked
                                    if not j.clicked:
                                        if j.flag:
                                            j.flag = False
                                            mineLeft += 1
                                        else:
                                            j.flag = True
                                            mineLeft -= 1

        # Check if won
        w = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"

        # Draw Texts
        if gameState != "Game Over" and gameState != "Win":
            t -= 1 
        elif gameState == "Game Over":
            writeText("Game Over!", 50)
            writeText("space to restart", 35, 50)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            writeText("You WON!", 50)
            writeText("space to restart", 35, 50)
        # Draw time
        s = str(t // 10)

        screen_text = pygame.font.SysFont("helvetica", 50).render(s, True, (0, 0, 0))
        DISP_GAME.blit(screen_text, (BORDER, BORDER))
        # Draw mine left
        screen_text = pygame.font.SysFont("helvetica", 50).render(mineLeft.__str__(), True, (0, 0, 0))
        DISP_GAME.blit(screen_text, (DISP_WIDTH - BORDER - 50, BORDER))

        pygame.display.update()  # Update screen

        TIMER.tick(15)  # Tick fps


gameLoop()
pygame.quit()
quit()

