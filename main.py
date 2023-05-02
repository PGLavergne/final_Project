import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 255, 255)

# Define fonts
font = pygame.font.Font(None, 36)

# Define game variables
falling_notes = []
score = 0
note_speed = 20
note_size = 100
note_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
note_paths = ['a', 's', 'd', 'f']
pressed_paths = set()

# Define functions
def create_note():
    note_path = random.choice(note_paths)
    note_color = random.choice(note_colors)
    note_x = note_paths.index(note_path) * (screen_width // len(note_paths))
    note_y = -note_size / 4
    note_rect = pygame.Rect(note_x, note_y, note_size, note_size)
    return {'path': note_path, 'color': note_color, 'rect': note_rect}

def move_notes():
    for note in falling_notes:
        note['rect'].move_ip(0, note_speed)

def draw_notes():
    for note in falling_notes:
        pygame.draw.rect(screen, note['color'], note['rect'])

def check_collision():
    for note in falling_notes:
        if note['rect'].bottom >= screen_height:
            falling_notes.remove(note)
            if note['path'] in pressed_paths:
                global score
                score += 1

def update_score():
    score_text = font.render('Score: {}'.format(score), True, white)
    screen.blit(score_text, (10, 10))

def draw_zones():
    zone_width = screen_width // len(note_paths)
    zone_height = screen_height // 10
    for i, path in enumerate(note_paths):
        zone_x = i * zone_width
        zone_y = screen_height - zone_height
        zone_rect = pygame.Rect(zone_x, zone_y, zone_width, zone_height)
        pygame.draw.rect(screen, white, zone_rect, 2)
        zone_text = font.render(path.upper(), True, white)
        screen.blit(zone_text, (zone_x + zone_width // 2 - zone_text.get_width() // 2, zone_y + zone_height // 2 - zone_text.get_height() // 2))

# Game loop
clock = pygame.time.Clock()
game_running = True

while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in note_paths:
                pressed_paths.add(event.unicode)

    # Generate new notes
    if len(falling_notes) < 4:
        falling_notes.append(create_note())

    # Move and draw notes
    screen.fill(black)
    draw_zones()
    move_notes()
    draw_notes()

    # Check for collisions
    check_collision()

    # Update score
    update_score()

    # Update display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Clean up
pygame.quit()


