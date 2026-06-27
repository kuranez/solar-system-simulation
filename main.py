"""
Solar System Simulation v.1.9
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""
import constants
import math
import pygame
import random
import sys
from pygame.locals import QUIT
from solarsystem_scale import calculate_scaled_sizes
from solarsystem_sim import Body, Sun, Planet, Asteroid
from solarsystem_creation import create_solarsystem, create_major_asteroids, create_asteroid_belt
from hud import render_menu_texts
import datetime  # For screenshot timestamps


# Initialize pygame
pygame.init()

# Window Settings
DISPLAYSURF = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Solar System Simulation')

FONT_1 = pygame.font.SysFont(None, 21)

# Clock
clock = pygame.time.Clock()
FPS = 60
dt = 0

# Scale and Movement Settings

# Initial scale factor for the solar system
scale = constants.DEFAULT_SCALE  # This is the zoom factor for positions
# How fast zoom in/out should change scale
zoom_speed = scale * 0.1  # 10 % per scroll step
screen_offset_x = 0  # Offset for horizontal movement
screen_offset_y = 0  # Offset for vertical movement
scaled_sizes = calculate_scaled_sizes(scale)

# Control Variables
dragging = False
drag_start_x, drag_start_y = 0, 0

# Time tracking
simulation_start_time = 0  # Will be set when simulation starts
total_elapsed_time = 0  # Total simulated time in seconds

# Solar System Creation

# Create solar system 
solarsystem = create_solarsystem()

# Assign individual planet variables
sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = solarsystem

# Create major asteroids (Ceres and Vesta)
major_asteroids = create_major_asteroids()

# Create asteroid belt
asteroids = create_asteroid_belt(num_asteroids=300)

# Current Solar System (combine all bodies)
current_solarsystem = solarsystem + major_asteroids + asteroids

planet_hud_data = [
    ("Mercury", mercury, constants.COLOR_MERCURY),
    ("Venus", venus, constants.COLOR_VENUS),
    ("Earth", earth, constants.COLOR_EARTH),
    ("Mars", mars, constants.COLOR_MARS),
    ("Jupiter", jupiter, constants.COLOR_JUPITER),
    ("Saturn", saturn, constants.COLOR_SATURN),
    ("Uranus", uranus, constants.COLOR_URANUS),
    ("Neptune", neptune, constants.COLOR_NEPTUNE),
]

# Main Loop
while True:
    clock.tick(FPS)
    DISPLAYSURF.fill(constants.COLOR_BACKGROUND)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Mouse events for zooming
        if event.type == pygame.MOUSEWHEEL:
            # Use event.y to determine the scroll direction
            # Positive value means scroll up (zoom in), negative means scroll down (zoom out)
            if event.y > 0:
                scale *= 1.1  # Zoom in (increase scale)
            elif event.y < 0:
                scale /= 1.1  # Zoom out (decrease scale)
            # Ensure scale is within a reasonable range (not too small or too large)
            scale = max(constants.DEFAULT_SCALE * 0.05, min(scale, constants.DEFAULT_SCALE * 10))
            # Recalculate planet sizes for new scale
            scaled_sizes = calculate_scaled_sizes(scale)
            # Update each planet's radius
            for body in current_solarsystem:
                if hasattr(body, "name") and body.name in scaled_sizes:
                    body.radius = scaled_sizes[body.name]
        
        # Mouse dragging events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                dragging = True
                drag_start_x, drag_start_y = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Get the current mouse position
                current_x, current_y = pygame.mouse.get_pos()
                # Calculate the difference from the start position
                dx = current_x - drag_start_x
                dy = current_y - drag_start_y
                # Update the screen offsets based on the mouse movement
                screen_offset_x += dx
                screen_offset_y += dy
                # Update the drag start position for the next motion event
                drag_start_x, drag_start_y = current_x, current_y

        # Keyboard events for speed control
        if event.type == pygame.KEYDOWN:
            # Adjust simulation speed using [+] or [-] from both regular keys and numpad
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                Body.TIMESTEP += 3600 * 24  # Increase time step (faster)
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                Body.TIMESTEP -= 3600 * 24  # Decrease time step (slower)

            # # Check mouse position for screen movement (for future use)
            # mouse_x, mouse_y = pygame.mouse.get_pos()  # Get current mouse position
            # if mouse_x <= 10:  # If mouse is at the left edge
            #     screen_offset_x += 5
            # elif mouse_x >= constants.WIDTH - 10:  # If mouse is at the right edge
            #     screen_offset_x -= 5
            # if mouse_y <= 10:  # If mouse is at the top edge
            #     screen_offset_y += 5
            # elif mouse_y >= constants.HEIGHT - 10:  # If mouse is at the bottom edge
            #     screen_offset_y -= 5

            # Exit the program with ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            # Take screenshot with F12 key
            if event.key == pygame.K_F12:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = f"screenshots/solar_system_{timestamp}.png"
                pygame.image.save(DISPLAYSURF, screenshot_path)
                print(f"Screenshot saved to: {screenshot_path}")

    # Draw and update Solar System, new sizes
    for body in current_solarsystem:
        body.update_position(current_solarsystem)
        body.draw(DISPLAYSURF, scale, screen_offset_x, screen_offset_y)
    
    # Update total elapsed simulation time
    total_elapsed_time += Body.TIMESTEP

    # Render menu texts and planet distances
    render_menu_texts(DISPLAYSURF, FONT_1, clock, total_elapsed_time, planet_hud_data)

    # delta time for framerate-independent physics
    dt = clock.tick(FPS) / 1000
    

    # Update display
    pygame.display.update()

