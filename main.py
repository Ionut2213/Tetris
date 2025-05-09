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




#Functions

class Piece(): #class for the pieces
    pass



def create_grid():
    pass


def convert_shape_format():
    pass


def valid_space():
    pass



def check_lost():
    pass


def get_shape():
    pass



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