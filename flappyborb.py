import pygame
import random

# set up game window
pygame.init()
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Game background
bg_image = pygame.image.load("bg.png").convert()

# The bird!
bird_image = pygame.image.load("borb.png").convert()
background_color = bird_image.get_at((0, 0))
bird_image.set_colorkey(background_color)
bird_image = pygame.transform.scale(bird_image, (80, 70))

# Load and format the pipe image used
pipe_image = pygame.image.load("pipe.jpeg").convert()
pipe_bg = pipe_image.get_at((0,0))
pipe_image.set_colorkey(pipe_bg)
pipe_list = [] 

# Define game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
font = pygame.font.Font(None, 36)

# Define helper functions
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_image.get_rect(midtop = (screen_width+100, random_pipe_pos))
    top_pipe = pipe_image.get_rect(midbottom = (screen_width+100, random_pipe_pos-150))
    return bottom_pipe, top_pipe

# Active pipes 
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

# Pipe random creation during game
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= screen_height:
            screen.blit(pipe_image, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flip_pipe, pipe)

# Collision mechanic with pipes
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            pipe_list.clear()
            game_active = False
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 400:
        return False
    return True

# Displaying the score and updating the score
def score_display(game_state):
    if game_state == "main_game":
        score_surface = font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (screen_width//2, 50))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (screen_width//2, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center = (screen_width//2, 425))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# set up game loop
clock = pygame.time.Clock()
FPS = 60
pipe_height = [200, 300, 400]

bird_rect = bird_image.get_rect(center = (50, screen_height//2)) # define bird rectangle

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, screen_height//2)
                bird_movement = 0
                score = 0
                

    # set up game background
    screen.blit(bg_image, (0, 0))

    # update bird
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # draw bird
    rotated_bird = pygame.transform.rotate(bird_image, -bird_movement * 3)
    bird_rect = rotated_bird.get_rect(center = (50, bird_rect.centery))
    screen.blit(rotated_bird, bird_rect)

    # update and draw pipes
    if game_active:
        pipe_list = move_pipes(pipe_list)
        pipe_list = [pipe for pipe in pipe_list if pipe.right > -50]
        if len(pipe_list) < 2:
            pipe_list.extend(create_pipe())
        draw_pipes(pipe_list)
        game_active = check_collision(pipe_list)

        # update score
        score += 0.01
        high_score = update_score(score, high_score)
        score_display("main_game")
    else:
        score_display("game_over")

    # update game window
    pygame.display.update()
    clock.tick(FPS)