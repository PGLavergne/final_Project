import pytest

from Tetris_game import Tetris 
from Tetris_game import Figure

def test_always_fails():
    assert False
def test_initial_x_y():
    figure = Figure(0,3)
    assert figure.x == 0
    #fixed:
    assert figure.y == 3
def test_height_width():
    tetris = Tetris(5,4)
    assert tetris.height == 5
    assert tetris.width == 4
    
def test_new_figure():
    tetris = Tetris(4,5)
    tetris.new_figure()
    assert tetris.x == 3
    assert tetris.y == 0


