# Aleksander Gomez 
# SW Methods Final 
# Due: 05/11/2023
# Initial Imports
import pygame 
import sys 
import random 

# Game Functions
#----------------
def game_floor():
      screen.blit(floor_base, (floor_x_pos, 450))
      screen.blit(floor_base, (floor_x_pos + 288, 450))

def check_collision(pipes):
    # Pipe collision
    for pipe in pipes: 
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
         return False
    return True

def create_pipe():
    random_pipe_pos = random.randint(200, 450)
    bottom_pipe = pipe_surface.get_rect(midtop = (350, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (350, random_pipe_pos - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
# Trying to make this better
# def score_display(game_state):
#     if game_state == "main_game":
#         score_surface = font.render(str(int(score)), True, (255, 255, 255))
#         score_rect = score_surface.get_rect(center = (288//2, 50))
#         screen.blit(score_surface, score_rect)
#     if game_state == "game_over":
#         score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
#         score_rect = score_surface.get_rect(center = (288//2, 50))
#         screen.blit(score_surface, score_rect)

#         high_score_surface = font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
#         high_score_rect = high_score_surface.get_rect(center = (288//2, 425))
#         screen.blit(high_score_surface, high_score_rect)

# def update_score(score, high_score):
#     if score > high_score:
#         high_score = score
#     return high_score


#----------------


# Game Variables
#----------------- 
gravity = .5
bird_movement = 0 
#-----------------

# Game Window
#-----------------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((288, 512))
font = pygame.font.Font(None, 36)
score = 0
high_score = 0
#-----------------

# Game assets 
#-----------------
# background
background = pygame.image.load('assets/background-day.png').convert()

# Bird
bird = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_rect = bird.get_rect(center = (50, 256))

# Floor 
floor_base = pygame.image.load('assets/base.png').convert_alpha()
floor_x_pos = 0 

# Message 
message = pygame.image.load('assets/message.png').convert_alpha()
game_over_rect = message.get_rect(center = (144, 256))

# Pipe 
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_list = []
pipe_height = [200, 300, 400]

SPAWNPIPE = pygame.USEREVENT 
pygame.time.set_timer(SPAWNPIPE, 1200)

#-----------------

# Game logic 
#-----------------
game_active = True 
while True: 

    # Loop to run the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and game_active == False:
                bird_rect.center = (50, 256)
                bird_movement = 0 
                pipe_list.clear()
                score = 0 
                game_active = True 
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
    # Game background
    screen.blit(background, (0,0)) 

    # Bird movement
    if game_active: 
        bird_movement += gravity 
        bird_rect.centery += bird_movement 
        screen.blit(bird, bird_rect)

        # Draw pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        game_active = check_collision(pipe_list) 
        # Check collision

         # update score
    #     score += 0.01
    #     high_score = update_score(score, high_score)
    #     score_display("main_game")
    # else: 
    #     screen.blit(message, game_over_rect) 
    #     score_display("game_over")
    # Animate floor 
    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0 

    # Run the game
    pygame.display.update()
    clock.tick(60) 


#-----------------