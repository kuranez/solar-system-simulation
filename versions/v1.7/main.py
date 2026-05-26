"""
Solar System Simulation v.1.5
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

def create_solarsystem():
    """Create objects in the solar system using scaled sizes."""
    sun = Sun(0, 0, 2, constants.sun_mass)

    # Use planet data from constants
    planets = []
    for data in constants.PLANETS_DATA:
        planet = Planet(
            data["position"] * Planet.AU,
            0,
            scaled_sizes[data["name"]],
            data["mass"],
            name=data["name"],
            is_inner_planet=data["is_inner"]
        )
        planet.y_vel = data["velocity"]
        planet.draw_line = True
        planets.append(planet)

    # Toggle orbit line for the Sun
    sun.draw_line = False  
    
    return [sun] + planets

def create_major_asteroids():
    """Create major asteroids Ceres and Vesta"""
    major_asteroids = []
    
    # Create Ceres
    ceres_data = constants.ASTEROID_CERES
    ceres_distance = ceres_data["semi_major_axis"]
    ceres_angle = random.uniform(0, 2 * math.pi)
    ceres = Planet(
        ceres_distance * math.cos(ceres_angle),
        ceres_distance * math.sin(ceres_angle),
        3,  # Size in pixels
        ceres_data["mass"],
        name=ceres_data["name"],
        is_inner_planet=True
    )
    # Calculate orbital velocity
    orbital_speed = math.sqrt(constants.G * constants.sun_mass / ceres_distance)
    ceres.x_vel = -orbital_speed * math.sin(ceres_angle)
    ceres.y_vel = orbital_speed * math.cos(ceres_angle)
    ceres.color = ceres_data["color"]
    ceres.draw_line = False  # No orbit trail
    major_asteroids.append(ceres)
    
    # Create Vesta
    vesta_data = constants.ASTEROID_VESTA
    vesta_distance = vesta_data["semi_major_axis"]
    vesta_angle = random.uniform(0, 2 * math.pi)
    vesta = Planet(
        vesta_distance * math.cos(vesta_angle),
        vesta_distance * math.sin(vesta_angle),
        2.5,  # Size in pixels
        vesta_data["mass"],
        name=vesta_data["name"],
        is_inner_planet=True
    )
    # Calculate orbital velocity
    orbital_speed = math.sqrt(constants.G * constants.sun_mass / vesta_distance)
    vesta.x_vel = -orbital_speed * math.sin(vesta_angle)
    vesta.y_vel = orbital_speed * math.cos(vesta_angle)
    vesta.color = vesta_data["color"]
    vesta.draw_line = False  # No orbit trail
    major_asteroids.append(vesta)
    
    return major_asteroids

def create_asteroid_belt(num_asteroids=500):
    """Generate asteroids between Mars and Jupiter orbits"""
    asteroids = []
    
    # Asteroid belt range (2.2 to 3.2 AU from the Sun)
    inner_radius = 2.2 * Planet.AU
    outer_radius = 3.2 * Planet.AU
    
    for i in range(num_asteroids):
        # Random orbital distance
        distance = random.uniform(inner_radius, outer_radius)
        
        # Random angle around the Sun
        angle = random.uniform(0, 2 * math.pi)
        
        # Calculate x, y position
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        
        # Small random size (1-3 pixels)
        size = random.uniform(0.5, 2)
        
        # Very small mass (negligible gravitational effect)
        mass = 1e15  # Much smaller than planets
        
        # Uniform light gray color
        color = (128, 128, 128)
        
        asteroid = Asteroid(x, y, size, mass, color)
        
        # Calculate orbital velocity (circular orbit around Sun)
        orbital_speed = math.sqrt(constants.G * constants.sun_mass / distance)
        
        # Set velocity perpendicular to position vector
        asteroid.x_vel = -orbital_speed * math.sin(angle)
        asteroid.y_vel = orbital_speed * math.cos(angle)
        
        # Add some random eccentricity
        asteroid.x_vel *= random.uniform(0.95, 1.05)
        asteroid.y_vel *= random.uniform(0.95, 1.05)
        
        asteroids.append(asteroid)
    
    return asteroids

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



# Render Menu Text
def render_menu_texts():
    # Displaying FPS in the upper left corner
    fps_text = "FPS: " + str(int(clock.get_fps()))
    fps_surface = FONT_1.render(fps_text, True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(fps_surface, (15, 15))

    # Displaying title in the upper right corner
    title = "Solar System Simulation v.1.7"
    title_surface = FONT_1.render(title, True, constants.COLOR_TEXT)
    title_width, title_height = title_surface.get_size()
    upper_right_x = DISPLAYSURF.get_width() - title_width - 15
    upper_right_y = 15
    DISPLAYSURF.blit(title_surface, (upper_right_x, upper_right_y))

    # Displaying time elapsed below the title in the upper right corner
    global total_elapsed_time
    
    # Convert seconds to years, days, hours, minutes, seconds
    years = int(total_elapsed_time // (365.25 * 24 * 3600))
    remaining_time = total_elapsed_time % (365.25 * 24 * 3600)
    days = int(remaining_time // (24 * 3600))
    remaining_time = remaining_time % (24 * 3600)
    hours = int(remaining_time // 3600)
    remaining_time = remaining_time % 3600
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    
    # Format time display
    if years > 0:
        time_text = f"Time: {years}y {days}d {hours}h {minutes}m"
    elif days > 0:
        time_text = f"Time: {days}d {hours}h {minutes}m"
    elif hours > 0:
        time_text = f"Time: {hours}h {minutes}m {seconds}s"
    else:
        time_text = f"Time: {minutes}m {seconds}s"
    
    time_surface = FONT_1.render(time_text, True, constants.COLOR_TEXT)
    time_width, time_height = time_surface.get_size()
    time_x = DISPLAYSURF.get_width() - time_width - 15
    time_y = upper_right_y + title_height + 5  # 5px spacing below title
    DISPLAYSURF.blit(time_surface, (time_x, time_y))

    # Displaying navigation table in the lower left corner
    nav_headers = ["Controls", "Action"]
    navigation_data = [
        ("Mouse Wheel", "Zoom In/Out"),
        ("[Left Click] + Drag", "Move View"),
        ("[+] / [-]", "Adjust Speed"),
        ("[F12]", "Take Screenshot"),
        ("[ESC]", "Quit Simulation"),
    ]

    # Define column widths for navigation table
    nav_col1_width = 160   # Controls column
    nav_col2_width = 120   # Action column

    # Initial position for lower left corner navigation table
    lower_left_x = 15  # Left aligned
    lower_left_y = DISPLAYSURF.get_height() - 160  # Fixed starting y position
    
    # Render navigation table headers
    nav_header1 = FONT_1.render(nav_headers[0], True, constants.COLOR_TEXT)
    nav_header2 = FONT_1.render(nav_headers[1], True, constants.COLOR_TEXT)
    
    DISPLAYSURF.blit(nav_header1, (lower_left_x, lower_left_y))
    DISPLAYSURF.blit(nav_header2, (lower_left_x + nav_col1_width, lower_left_y))
    
    # Render navigation data rows
    for i, (control, action) in enumerate(navigation_data):
        row_y = lower_left_y + 30 + i * 25  # 30px spacing after header, 25px between rows
        
        # Control column
        control_surface = FONT_1.render(control, True, constants.COLOR_TEXT)
        DISPLAYSURF.blit(control_surface, (lower_left_x, row_y))
        
        # Action column
        action_surface = FONT_1.render(action, True, constants.COLOR_TEXT)
        DISPLAYSURF.blit(action_surface, (lower_left_x + nav_col1_width, row_y))

    # Displaying planet information table in the lower right corner
    # Table headers
    table_headers = ["Planets", "Distance from the Sun", "Orbits"]
    planet_data = [
        ("Mercury", mercury, constants.COLOR_MERCURY),
        ("Venus", venus, constants.COLOR_VENUS),
        ("Earth", earth, constants.COLOR_EARTH),
        ("Mars", mars, constants.COLOR_MARS),
        ("Jupiter", jupiter, constants.COLOR_JUPITER),
        ("Saturn", saturn, constants.COLOR_SATURN),
        ("Uranus", uranus, constants.COLOR_URANUS),
        ("Neptune", neptune, constants.COLOR_NEPTUNE)
    ]

    # Define column widths for alignment
    col1_width = 80   # Planet names
    col2_width = 180  # Distance
    col3_width = 60   # Orbits

    # Render table headers
    starting_y = DISPLAYSURF.get_height() - 240  # Fixed starting y position for the table
    header_y = starting_y
    
    # Column headers
    header1 = FONT_1.render(table_headers[0], True, constants.COLOR_TEXT)
    header2 = FONT_1.render(table_headers[1], True, constants.COLOR_TEXT)
    header3 = FONT_1.render(table_headers[2], True, constants.COLOR_TEXT)
    
    # Position headers from right edge
    right_edge = DISPLAYSURF.get_width() - 15
    col3_x = right_edge - col3_width
    col2_x = col3_x - col2_width
    col1_x = col2_x - col1_width
    
    DISPLAYSURF.blit(header1, (col1_x, header_y))
    DISPLAYSURF.blit(header2, (col2_x, header_y))
    DISPLAYSURF.blit(header3, (col3_x, header_y))

    # Render planet data rows
    for i, (name, planet, color) in enumerate(planet_data):
        row_y = header_y + 30 + i * 25  # 30px spacing after header, 25px between rows
        
        # Planet name
        name_surface = FONT_1.render(name, True, color)
        DISPLAYSURF.blit(name_surface, (col1_x, row_y))
        
        # Distance from sun
        distance_text = f"{round(planet.distance_to_sun / 1000, 1)} km"
        distance_surface = FONT_1.render(distance_text, True, color)
        DISPLAYSURF.blit(distance_surface, (col2_x, row_y))
        
        # Orbit count
        orbit_text = f"{planet.orbit_count}"
        orbit_surface = FONT_1.render(orbit_text, True, color)
        DISPLAYSURF.blit(orbit_surface, (col3_x, row_y))

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
    render_menu_texts()

    # delta time for framerate-independent physics
    dt = clock.tick(FPS) / 1000
    

    # Update display
    pygame.display.update()

