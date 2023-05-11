import pytest
import pygame
from flappy import check_collision

# Tests that the function returns True when there are no pipes in the list. 
def test_collision_no_pipes():
    assert check_collision([], pygame.Rect(50, 256, 34, 24)) == True

# Tests that the function returns True when the bird does not collide with any pipes and stays within the screen boundaries. 
def test_no_collision():
    pipes = [pygame.Rect(300, 0, 52, 320), pygame.Rect(300, 400, 52, 320)]
    assert check_collision(pipes, pygame.Rect(50, 256, 34, 24)) == True

# Tests that the function returns False when the bird collides with a pipe. 
def test_collision_with_pipe():
    pipes = [pygame.Rect(50, 0, 52, 320), pygame.Rect(50, 400, 52, 320)]
    assert check_collision(pipes, pygame.Rect(50, 256, 34, 24)) == False

# Tests that the function returns False when the bird goes above the screen. 
def test_collision_above_screen():
    pipes = [pygame.Rect(50, 0, 52, 320), pygame.Rect(50, 400, 52, 320)]
    assert check_collision(pipes, pygame.Rect(50, -100, 34, 24)) == False


