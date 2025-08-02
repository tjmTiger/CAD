# local

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

################
## Basic Func ##
################

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
run = True
window = "cad"
while run:
    draw_background(screen)
    input_events()
    match window:
        case "menu":
            pass
        case "cad":
            pass
            # cad_window.run([screen])
        case _:
            pass
    update_display()
pygame.quit()
sys.exit()