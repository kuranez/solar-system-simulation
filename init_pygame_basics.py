#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:29:22 2024

@author: kuranez
"""

import pygame, sys
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Set up display
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Solar System Simulation')

# Set up clock
clock = pygame.time.Clock()
FPS = 60
dt  = 0

# Define colors
#WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)

COLOR_TEXT = (255, 255, 255)
COLOR_BACKGROUND = (36, 36, 36)

# Initialize the font module (optional, as it's done by default with pygame.init())
pygame.font.init()

# Create a Font object
# You can pass None to use the default font or provide a path to a specific font file
FONT = pygame.font.SysFont(None, 48)  # None means default font, 48 is the font size

# Render text to a new surface
TEXTSURF = FONT.render('Hello, Pygame!', False, COLOR_TEXT)  # True enables anti-aliasing

# Get the area of the text surface for positioning
TEXTAREA = TEXTSURF.get_rect()
TEXTAREA.center = (200, 150)  # Set text position

# Main game loop
while True:

    # Fill the screen with background color
    DISPLAYSURF.fill(COLOR_BACKGROUND)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # fill the screen with a color to wipe away anything from last frame 
        DISPLAYSURF.fill(COLOR_BACKGROUND)
        
        # Draw the text onto the display surface
        DISPLAYSURF.blit(TEXTSURF, TEXTAREA)
        

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed.")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed.")
            elif event.key == pygame.K_UP:
                print("Up arrow key pressed.")
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed.")
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()  # Allow quitting with the ESC key

        # Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                print(f"Left mouse button clicked at ({mouse_x}, {mouse_y})")
            elif event.button == 3:  # Right mouse button
                mouse_x, mouse_y = event.pos
                print(f"Right mouse button clicked at ({mouse_x}, {mouse_y})")

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            print(f"Mouse moved to ({mouse_x}, {mouse_y})")

        # delta time for framerate-independent physics
        dt = clock.tick(FPS) / 1000
    
    # Update the display
    pygame.display.update()