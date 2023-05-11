import pygame
import random
import unittest
from unittest.mock import patch

class TestPianoTilesGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        self.clock = pygame.time.Clock()
        self.note_speed = 20
        self.note_size = 100
        self.note_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
        self.note_paths = ['a', 's', 'd', 'f']
        self.pressed_paths = set()
        self.falling_notes = []
        self.score = 0
        self.title_font = pygame.font.Font(None, 72)
        self.subtitle_font = pygame.font.Font(None, 36)
        self.score_font = pygame.font.Font(None, 36)

    def tearDown(self):
        pygame.quit()

    def test_create_note(self):
        with patch('random.choice') as mock_choice:
            mock_choice.side_effect = [('a', (255, 0, 0)), (2, (0, 0, 255)), (1, (0, 255, 0))]
            note = create_note()
            self.assertEqual(note['path'], 'a')
            self.assertEqual(note['color'], (255, 0, 0))
            self.assertEqual(note['rect'].x, 0)
            self.assertEqual(note['rect'].y, -self.note_size / 4)
            self.assertEqual(note['rect'].width, self.note_size)
            self.assertEqual(note['rect'].height, self.note_size)

            note = create_note()
            self.assertEqual(note['path'], 'd')
            self.assertEqual(note['color'], (0, 0, 255))
            self.assertEqual(note['rect'].x, 2 * (self.screen.get_width() // len(self.note_paths)))
            self.assertEqual(note['rect'].y, -self.note_size / 4)
            self.assertEqual(note['rect'].width, self.note_size)
            self.assertEqual(note['rect'].height, self.note_size)

            note = create_note()
            self.assertEqual(note['path'], 's')
            self.assertEqual(note['color'], (0, 255, 0))
            self.assertEqual(note['rect'].x, 1 * (self.screen.get_width() // len(self.note_paths)))
            self.assertEqual(note['rect'].y, -self.note_size / 4)
            self.assertEqual(note['rect'].width, self.note_size)
            self.assertEqual(note['rect'].height, self.note_size)

    def test_move_notes(self):
        note = {'path': 'a', 'color': (255, 0, 0), 'rect': pygame.Rect(0, 0, self.note_size, self.note_size)}
        self.falling_notes = [note]
        move_notes()
        self.assertEqual(note['rect'].y, self.note_speed)

        note = {'path': 'd', 'color': (0, 0, 255),
                'rect': pygame.Rect(3 * (self.screen.get_width() // len(self.note_paths)), 0, self.note_size,
                                    self.note_size)}
        self.falling_notes = [note]
        move_notes()
        self.assertEqual(note['rect'].y, self.note_speed)
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define fonts
title_font = pygame.font.Font(None, 72)
subtitle_font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 36)

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
    score_text = score_font.render('Score: {}'.format(score), True, white)
    screen.blit(score_text, (10, 10))

def draw_zones():
    zone_width = screen_width // len(note_paths)
    zone_height = screen_height // 10
    for i, path in enumerate(note_paths):
        zone_x = i * zone_width
        zone_y = screen_height - zone_height
        zone_rect = pygame.Rect(zone_x, zone_y, zone_width, zone_height)
        pygame.draw.rect(screen, white, zone_rect, 2)
        zone_text = score_font.render(path.upper(), True, white)
        screen.blit(zone_text, (zone_x + zone_width // 2 - zone_text.get_width() // 2, zone_y + zone_height // 2 - zone_text.get_height() // 2))

def show_title_screen():
    title_text = title_font.render('Piano Tiles', True, white)
    subtitle_text = subtitle_font.render('Press A/S/D/F key to start', True, white)

    title_x = screen_width // 2 - title_text.get_width() // 2
    title_y = screen_height // 3
    subtitle_x = screen_width // 2 - subtitle_text.get_width() // 2
    subtitle_y = title_y + title_text.get_height() + 50
    screen.fill(black)
    screen.blit(title_text, (title_x, title_y))
    screen.blit(subtitle_text, (subtitle_x, subtitle_y))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
# Game loop
clock = pygame.time.Clock()
TestPianoTilesGame()
show_title_screen()

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
    if len(falling_notes) < 2:
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
    clock.tick(45)

# Clean up
pygame.quit()


