import pytest
import pygame
from flappy import check_collision

# Unit testing the draw pipes functions 
def test_draw_pipes():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    
    # Create a list of pipe coordinates
    pipes = [
        (150, 150, 50, 300),  
        (300, 0, 50, 200),
        (450, 250, 50, 300)
    ]
    
    # Call the draw_pipes function
    draw_pipes(screen, pipes)
    
    # Check that the pipes are drawn in the correct locations
    assert screen.get_at((175, 125)) == (0, 255, 0, 255) # Top pipe at (150, 150)
    assert screen.get_at((175, 425)) == (0, 255, 0, 255) # Bottom pipe at (150, 150)
    assert screen.get_at((325, 100)) == (0, 255, 0, 255) # Top pipe at (300, 0)
    assert screen.get_at((325, 300)) == (0, 255, 0, 255) # Bottom pipe at (300, 0)
    assert screen.get_at((475, 225)) == (0, 255, 0, 255) # Top pipe at (450, 250)
    assert screen.get_at((475, 525)) == (0, 255, 0, 255) # Bottom pipe at (450, 250)

# Unit testing the collision function 
def test_check_collision(pipes):
    # Create a mock bird rectangle
    bird_rect = pygame.Rect(100, 100, 50, 50)
    
    # Create a list of mock pipe rectangles
    pipes = [
        pygame.Rect(150, 150, 50, 300),  # This should collide with the bird
        pygame.Rect(300, 0, 50, 200),   # This should not collide with the bird
        pygame.Rect(450, 250, 50, 300)  # This should not collide with the bird
    ]
    
    # Test that the function returns False when there is a collision
    assert check_collision(pipes, bird_rect) == False
    
    # Test that the function returns True when there is no collision
    bird_rect = pygame.Rect(100, 400, 50, 50)
    assert check_collision(pipes, bird_rect) == True


