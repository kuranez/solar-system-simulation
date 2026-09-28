"""
Solar System Simulation v.1.9.3
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""

import sys
import datetime  # For screenshot timestamps

import pygame
from pygame.locals import QUIT

import config.colors
import config.display
import config.simulation

from physics.engine import update_bodies_physics

from render.renderer import draw_body
from render.scale import calculate_scaled_sizes
from render.hud import render_menu_texts

from objects.factory import create_solarsystem, create_major_asteroids, create_pluto, create_asteroid_belt, create_Kuiper_belt

# Initialize pygame
pygame.init()

# Window Settings
DISPLAYSURF = pygame.display.set_mode((config.display.WIDTH, config.display.HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Solar System Simulation')

FONT_1 = pygame.font.SysFont(None, 21)

# Clock
clock = pygame.time.Clock()
FPS = 60
dt = 0

# Simulation speed : Substepping to fix planet orbits with increased speed
steps_per_frame = config.simulation.SUBSTEP     # Default: 1
BASE_TIMESTEP = config.simulation.TIMESTEP      # Default: 1 day per physics step

# -------------------------------------------------------------
# Scale and Movement Settings
# -------------------------------------------------------------

# Initial scale factor for the solar system
scale = config.simulation.DEFAULT_SCALE  # This is the zoom factor for positions
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

# -------------------------------------------------------------
# Solar System Creation
# -------------------------------------------------------------
# Create solar system 
solarsystem = create_solarsystem()

# Assign individual planet variables
sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = solarsystem

# Create major asteroids (Ceres and Vesta)
major_asteroids = create_major_asteroids()

# Create asteroid belt
asteroids = create_asteroid_belt(num_asteroids=500)

# Create TNOs
tno_belt = create_Kuiper_belt(num_objects=100)
pluto = create_pluto()

# Performance Tweak : Seperate into major and minor bodies
major_bodies = solarsystem + major_asteroids + [pluto]
minor_bodies = asteroids + tno_belt

# Current Solar System (combine all bodies)
# current_solarsystem = solarsystem + major_asteroids + asteroids + tno_belt + [pluto]
current_solarsystem = major_bodies + minor_bodies

planet_hud_data = [
    ("Mercury", mercury,    config.colors.PLANET_COLORS["Mercury"]),
    ("Venus",   venus,      config.colors.PLANET_COLORS["Venus"]),
    ("Earth",   earth,      config.colors.PLANET_COLORS["Earth"]),
    ("Mars",    mars,       config.colors.PLANET_COLORS["Mars"]),
    ("Jupiter", jupiter,    config.colors.PLANET_COLORS["Jupiter"]),
    ("Saturn",  saturn,     config.colors.PLANET_COLORS["Saturn"]),
    ("Uranus",  uranus,     config.colors.PLANET_COLORS["Uranus"]),
    ("Neptune", neptune,    config.colors.PLANET_COLORS["Neptune"]),
    ("Pluto",   pluto,      config.colors.TNO_COLORS["Pluto"])
]

# !!!!!!!!!
# Main Loop
# !!!!!!!!!
while True:
    clock.tick(FPS)
    DISPLAYSURF.fill(config.display.COLOR_BACKGROUND)

    # -------------------------------------------------------------
    # Keybinds
    # -------------------------------------------------------------
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
            scale = max(config.simulation.DEFAULT_SCALE * 0.05, min(scale, config.simulation.DEFAULT_SCALE * 10))
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
            if event.key in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS):
                steps_per_frame = min(64, steps_per_frame + 1)
            elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                steps_per_frame = max(1, steps_per_frame -1)

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

    # -------------------------------------------------------------
    # Update and draw celestial bodies
    # -------------------------------------------------------------
    for _ in range(steps_per_frame):
        # Physics update - Seperate major and minor body loops
        update_bodies_physics(
            major_bodies,
            minor_bodies,
            BASE_TIMESTEP,
            sun=sun
        )

        total_elapsed_time += BASE_TIMESTEP

    # Tweak: Update OrbitRecorder once per frame (after all substeps)    
    for body in major_bodies:
        if body.orbit_recorder:
            body.orbit_recorder.update(body.x, body.y, sun.x, sun.y)

    # Render all bodies
    screen_cx = config.display.WIDTH    / 2 + screen_offset_x
    screen_cy = config.display.HEIGHT   / 2 + screen_offset_y

    for body in current_solarsystem:
        draw_body(DISPLAYSURF, body, scale, screen_cx, screen_cy)


    # -------------------------------------------------------------
    # Render HUD
    # -------------------------------------------------------------
    # Render menu texts and planet distances
    render_menu_texts(
        DISPLAYSURF, 
        FONT_1, 
        clock, 
        total_elapsed_time,
        planet_hud_data,
        steps_per_frame = steps_per_frame)

    # -------------------------------------------------------------
    # Misc
    # -------------------------------------------------------------
    # delta time for framerate-independent physics
    dt = clock.tick(FPS) / 1000
    
    # Update display
    pygame.display.update()

