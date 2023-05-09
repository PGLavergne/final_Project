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

#NOTE create an instance of tetris and then create an instance of a figure and you can call that specific created object
#Create an instance inside of an instance, that way we can use methods defined in the tetris class  
def test_new_figure():
    tetris = Tetris(100,60)
    tetris.figure = Figure(4,5)
    tetris.new_figure()
    assert tetris.figure.x == 3
    assert tetris.figure.y == 0
def test_intersects():
    tetris = Tetris(100,60)
    #Create a new figure that intentionally intersects the x coordinate of our tetris board
    tetris.figure = Figure(100,5)
    assert tetris.intersects()
def test_freeze():
    tetris = Tetris(100,60)
    #Create a new figure and place it at the bottom
    tetris.figure = Figure(10,60)
    a = tetris.piecesplaced
    tetris.freeze()
    b = tetris.piecesplaced
    #If the total number of pieces placed has incremented by one, then success
    assert a < b
#def test_break_lines():
 #   tetris = Tetris(5,4)
  #  tetris.figure = Figure(1,4)
   # tetris.break_lines

def test_go_space():
    tetris = Tetris(50,50)
    tetris.figure = Figure(25,25)
    a = tetris.figure.y
    tetris.go_space()
    b = tetris.figure.y
    assert a > b

def test_go_down():
    tetris = Tetris(100,60)
    tetris.figure = Figure(10,20)
    a = tetris.figure.y
    tetris.go_down()
    b = tetris.figure.y
    assert a < b





    



    


