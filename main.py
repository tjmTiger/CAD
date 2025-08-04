# local
from gui import *
from ecs import *

# standard library
import os
import sys

# external
import pygame

########################
## Pygame Innitiation ##
########################

pygame.init()
screen = pygame.display.set_mode((1280, 720))
fps = 60 # target fps
fpsClock = pygame.time.Clock()
pygame.display.set_caption("OnlyCAD")
path = os.getcwd()
program_icon = pygame.image.load(path + '/img/icon.png')
pygame.display.set_icon(program_icon)

########################

class Window:
    def __init__(self):
        self.objects = []
    
    def process(self, info):
        for object in self.objects:
            object.process(info)

def draw_background(screen):
    screen.fill((250, 218, 221))
    
def input_events():
    global run
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: # close the game
                run = False
            case pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 3: # right mouse button
                        pass

def update_display():
    pygame.display.flip() # pygame.display.update(), but only part of the screen
    fpsClock.tick(fps)

###############
## Prog Loop ##
###############

cad_window = Window()

run = True
window = "cad"
while run:
    draw_background(screen)
    input_events()
    match window:
        case "menu":
            pass
        case "cad":
            cad_window.process([screen])
        case _:
            pass
    update_display()
pygame.quit()
sys.exit()