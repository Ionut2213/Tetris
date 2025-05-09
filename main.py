import pygame # Don't forget to install this library by using the command pip install pygame
import random # We use this for generating random pieces



pygame.font.init() # Initialize the font module



# GLOBAL VARIABLES

s_widht = 800 # Window width
s_height = 700 # Window height
play_width = 300 # meaning 300 // 2 = 30 width per block
play_height = 600 # meaning 600 // 20 = 20 height per block
block_size = 30 # size of the block

top_left_x = (s_widht - play_width) // 2
top_left_y = s_height - play_height


# FORMAT FOR SHAPES

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]




shapes = [S, Z, I, O, J, L, T] #list of shapes
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)] # colors for the shapes
                        # Index 0 - 6  
                        
                                    




#Functions

class Piece(object): #class for the pieces
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] # Getting the color of the shape
        self.rotation = 0 # Rotation of the shape



def create_grid(locked_positions = {}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)] # Grid of black blocks

    for i in range(len(grid)): # iterate throug the grid
        for j in range(len(grid[i])):
            if (j, i) in locked_positions: # if the position is locked
                color = locked_positions[(j, i)] # get the color of the locked position
                grid[i][j] = color # set the color of the grid to the color of the locked position
    return grid # return the grid with the locked positon
    


def convert_shape_format():
    pass


def valid_space():
    pass



def check_lost():
    pass


def get_shape():
    return Piece(5, 0, random.choice(shapes)) # This function returns a random shape from the list with shapes



def draw_text_middle():
    pass



def draw_grid():
    pass



def clear_rows():
    pass



def draw_next_shape():
    pass



def main():
    pass




def main_menu():
    pass