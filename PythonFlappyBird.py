'''
Recreating Flappy Bird in Python
using pygame
'''

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((576, 1024)) # x, y
clock = pygame.time.Clock()

# 1. Import surface and assignt to a variable
bg_surface = pygame.image.load('assets/background-day.png').convert()
# .convert() converts the image into a form that's easier for pygame to work with
# helps pygame run the game at a more consistent speed

# 2. Assign the scaled version to the surface
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert() # Importing floor asset
floor_surface = pygame.transform.scale2x(floor_surface).convert()

# Main Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # For preventing error message when exiting the game

    screen.blit(bg_surface,(0,0)) # 0, 0 is the top left corner.
    '''
    Increase Y = going down
    Decreate Y = going up
    Increase X = going right
    '''
    screen.blit(floor_surface,(0,704)) # Placing floor asset on screen

    pygame.display.update() # Displays any updates that occur during the main game loop
    clock.tick(120) # Max frame rate is 120 fps