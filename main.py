"""
Solar System Simulation v.1.4a
@author: kuranez
https://github.com/kuranez/Solar-System-Simulation
"""
import constants
import pygame
import sys
from pygame.locals import QUIT
from solarsystem_scale import calculate_scaled_sizes
from solarsystem_sim import Body, Sun, Planet

# Initialize pygame
pygame.init()

# Window Settings
DISPLAYSURF = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
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

# Solar System Creation

def create_solarsystem():
    """Create objects in the solar system using scaled sizes."""
    sun = Sun(0, 0, 2, constants.sun_mass)

    planets_data = [
        
        {"name": "Mercury", 
         "position": -0.387 * Planet.AU, 
         "scaled_size": scaled_sizes["Mercury"], 
         "mass": constants.mercury_mass, 
         "is_inner": True, 
         "velocity": constants.mercury_velocity},
        
        {"name": "Venus", 
         "position": -0.723 * Planet.AU, 
         "scaled_size": scaled_sizes["Venus"], 
         "mass": constants.venus_mass, 
         "is_inner": True, 
         "velocity": constants.venus_velocity},
        
        {"name": "Earth", 
         "position": -1 * Planet.AU, 
         "scaled_size": scaled_sizes["Earth"], 
         "mass": constants.earth_mass, "is_inner": True, 
         "velocity": constants.earth_velocity},
        
        {"name": "Mars", 
         "position": -1.524 * Planet.AU, 
         "scaled_size": scaled_sizes["Mars"], 
         "mass": constants.mars_mass, 
         "is_inner": True, 
         "velocity": constants.mars_velocity},
        
        {"name": "Jupiter", 
         "position": -5.204 * Planet.AU, 
         "scaled_size": scaled_sizes["Jupiter"], 
         "mass": constants.jupiter_mass, 
         "is_inner": False, 
         "velocity": constants.jupiter_velocity},
        
        {"name": "Saturn", 
         "position": -9.573 * Planet.AU, 
         "scaled_size": scaled_sizes["Saturn"], 
         "mass": constants.saturn_mass, 
         "is_inner": False, 
         "velocity": constants.saturn_velocity},
        
        {"name": "Uranus", 
         "position": -19.165 * Planet.AU, 
         "scaled_size": scaled_sizes["Uranus"], 
         "mass": constants.uranus_mass, 
         "is_inner": False, 
         "velocity": constants.uranus_velocity},
        
        {"name": "Neptune", 
         "position": -30.178 * Planet.AU, 
         "scaled_size": scaled_sizes["Neptune"], 
         "mass": constants.neptune_mass, 
         "is_inner": False, 
         "velocity": constants.neptune_velocity},
    ]

    planets = []
    for data in planets_data:
        planet = Planet(data["position"], 
                        0, 
                        data["scaled_size"], 
                        data["mass"], 
                        name=data["name"],
                        is_inner_planet=data["is_inner"])
        planet.y_vel = data["velocity"]
        planet.draw_line = True
        planets.append(planet)

    # Toggle orbit line for the Sun
    sun.draw_line = False  
    
    return [sun] + planets

# Create solar system 
solarsystem = create_solarsystem()

# Assign individual planet variables
sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = solarsystem


# Current Solar System
current_solarsystem = solarsystem

# Render Menu Text
def render_menu_texts():
    # Displaying FPS in the upper left corner
    fps_text = "FPS: " + str(int(clock.get_fps()))
    fps_surface = FONT_1.render(fps_text, True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(fps_surface, (15, 15))

    # Displaying title in the upper right corner
    title = "Solar System Simulation v.1.5a"
    title_surface = FONT_1.render(title, True, constants.COLOR_TEXT)
    title_width, title_height = title_surface.get_size()
    upper_right_x = DISPLAYSURF.get_width() - title_width - 15
    upper_right_y = 15
    DISPLAYSURF.blit(title_surface, (upper_right_x, upper_right_y))

    # Displaying navigation texts in the lower left corner
    navigation_texts = [
        "Navigation :",
        "[Mouse Wheel] : Zoom In/Out",
        "[Left Click] +  Drag : Move View",
        "[+] / [-] : Adjust Speed",
        "[ESC] : Quit",
    ]

    # Prepare surfaces for navigation texts
    navigation_surfaces = [FONT_1.render(text, True, constants.COLOR_TEXT) for text in navigation_texts]
    
    # Initial position for lower left corner navigation
    lower_left_x = 15  # Left aligned
    lower_left_y = DISPLAYSURF.get_height() - 160  # Fixed starting y position

    # Render each navigation item with 15px spacing
    for i, surface in enumerate(navigation_surfaces):
        surface_width, surface_height = surface.get_size()
        DISPLAYSURF.blit(surface, (lower_left_x, lower_left_y + i * (surface_height + 15)))  # 15 pixels spacing

    # Displaying planet distance texts in the lower right corner
    distance_title = "Distance from the Sun:"
    planet_distances = [
        ("Mercury", mercury, constants.COLOR_MERCURY),
        ("Venus", venus, constants.COLOR_VENUS),
        ("Earth", earth, constants.COLOR_EARTH),
        ("Mars", mars, constants.COLOR_MARS),
        ("Jupiter", jupiter, constants.COLOR_JUPITER),
        ("Saturn", saturn, constants.COLOR_SATURN),
        ("Uranus", uranus, constants.COLOR_URANUS),
        ("Neptune", neptune, constants.COLOR_NEPTUNE)
    ]

    distance_title_surface = FONT_1.render(distance_title, True, constants.COLOR_TEXT)
    distance_title_width, distance_title_height = distance_title_surface.get_size()
    lower_right_x = DISPLAYSURF.get_width() - distance_title_width - 15
    DISPLAYSURF.blit(distance_title_surface, (lower_right_x, 475))

    # Adjusting spacing for planet distances (5 pixels narrower)
    for i, (name, planet, color) in enumerate(planet_distances):
        distance_text = f"{name}: {round(planet.distance_to_sun / 1000, 1)} km"
        surface = FONT_1.render(distance_text, True, color)
        distance_text_width, distance_text_height = surface.get_size()
        lower_right_x = DISPLAYSURF.get_width() - distance_text_width - 15
        DISPLAYSURF.blit(surface, (lower_right_x, 505 + i * 25))  # 25 pixels between each item


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

            # Exit the program with ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            # Recalculate planet sizes based on the updated zoom factor
            # scaled_sizes = calculate_scaled_sizes(zoom_factor)

    # Move the screen with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen_offset_x += 5
    if keys[pygame.K_RIGHT]:
        screen_offset_x -= 5
    if keys[pygame.K_UP]:
        screen_offset_y += 5
    if keys[pygame.K_DOWN]:
        screen_offset_y -= 5

    # Move screen if the mouse is near the borders
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position

    # If mouse is near the screen's left or right edge, move the screen horizontally
    if mouse_x <= 10:  # Left border
        screen_offset_x += 5
    elif mouse_x >= constants.WIDTH - 10:  # Right border
        screen_offset_x -= 5

    # If mouse is near the screen's top or bottom edge, move the screen vertically
    if mouse_y <= 10:  # Top border
        screen_offset_y += 5
    elif mouse_y >= constants.HEIGHT - 10:  # Bottom border
        screen_offset_y -= 5

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

    # Draw and update Solar System, new sizes
    for body in current_solarsystem:
        body.update_position(current_solarsystem)
        body.draw(DISPLAYSURF, scale, screen_offset_x, screen_offset_y)
    # else:
    #    body.draw(DISPLAYSURF, screen_offset_x, screen_offset_y)  # Just draw the Sun as is, with no scaling or orbit lines

    # Render menu texts and planet distances
    render_menu_texts()

    # delta time for framerate-independent physics
    dt = clock.tick(FPS) / 1000
    

    # Update display
    pygame.display.update()
    
