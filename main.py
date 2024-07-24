import constants
import pygame
import sys
from pygame.locals import QUIT
from solarsystem import Body, Sun, Planet

# Initialize pygame
pygame.init()

# Window Settings
DISPLAYSURF = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption('Solar System Simulation')

FONT_1 = pygame.font.SysFont("Trebuchet MS", 21)
FONT_2 = pygame.font.SysFont("Trebuchet MS", 16)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Solar System Bodies
# Parameters: x, y, radius, mass

sun = Sun(0, 0, constants.sun_radius * Body.SCALE, constants.sun_mass)
sun.draw_line = False

mercury = Planet(
    -constants.mercury_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.mercury_radius / constants.earth_radius * 1e9 * 3 * Body.SCALE,
    constants.mercury_mass)
mercury.y_vel = constants.mercury_velocity
mercury.draw_line = True

venus = Planet(
    -constants.venus_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.venus_radius / constants.earth_radius * 1e9 * 3 * Body.SCALE,
    constants.venus_mass)
venus.y_vel = constants.venus_velocity
venus.draw_line = True

earth = Planet(
    -constants.earth_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.earth_radius / constants.earth_radius * 1e9 * 3 * Body.SCALE,
    constants.earth_mass)
earth.y_vel = constants.earth_velocity
earth.draw_line = True

mars = Planet(
    -constants.mars_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.mars_radius / constants.earth_radius * 1e9 * 3 * Body.SCALE,
    constants.mars_mass)
mars.y_vel = constants.mars_velocity
mars.draw_line = True

jupiter = Planet(
    -constants.jupiter_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.jupiter_radius / constants.earth_radius * 1e9 * Body.SCALE,
    constants.jupiter_mass)
jupiter.y_vel = constants.jupiter_velocity
earth.draw_line = True

saturn = Planet(
    -constants.saturn_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.saturn_radius / constants.earth_radius * 1e9 * Body.SCALE,
    constants.saturn_mass)
saturn.y_vel = constants.saturn_velocity
saturn.draw_line = True

uranus = Planet(
    -constants.uranus_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.uranus_radius / constants.earth_radius * 1e9 * Body.SCALE,
    constants.uranus_mass)
uranus.y_vel = constants.uranus_velocity
uranus.draw_line = True

neptune = Planet(
    -constants.neptune_perihelion / constants.earth_perihelion * Body.AU, 0,
    constants.neptune_radius / constants.earth_radius * 1e9 * Body.SCALE,
    constants.neptune_mass)
neptune.draw_line = True

# Solar System
solarsystem = [
    sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
]

inner_planets = [sun, mercury, venus, earth, mars]

outer_planets = [sun, jupiter, saturn, uranus, neptune]

current_solarsystem = solarsystem

# Main Loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Adjust Simulation Scale
            if event.key == pygame.K_UP:
                Body.SCALE += 10 / Body.AU
            elif event.key == pygame.K_DOWN:
                Body.SCALE -= 10 / Body.AU

            # Adjust Simulation Spped
            if event.key == pygame.K_RIGHT:
                Body.TIMESTEP += 3600 * 24
            elif event.key == pygame.K_LEFT:
                Body.TIMESTEP -= 3600 * 24

            # Toggle Orbit Lines on/off
            if event.key == pygame.K_q:
                mercury.draw_line = not mercury.draw_line
                venus.draw_line = not venus.draw_line
                earth.draw_line = not earth.draw_line
                mars.draw_line = not mars.draw_line
                jupiter.draw_line = not jupiter.draw_line
                saturn.draw_line = not saturn.draw_line
                uranus.draw_line = not uranus.draw_line
                neptune.draw_line = not neptune.draw_line
            elif event.key == pygame.K_1:
                mercury.draw_line = not mercury.draw_line
            elif event.key == pygame.K_2:
                venus.draw_line = not venus.draw_line
            elif event.key == pygame.K_3:
                earth.draw_line = not earth.draw_line
            elif event.key == pygame.K_4:
                mars.draw_line = not mars.draw_line
            elif event.key == pygame.K_5:
                jupiter.draw_line = not jupiter.draw_line
            elif event.key == pygame.K_6:
                saturn.draw_line = not saturn.draw_line
            elif event.key == pygame.K_7:
                uranus.draw_line = not uranus.draw_line
            elif event.key == pygame.K_8:
                neptune.draw_line = not neptune.draw_line

            # Toggle Planets on/off
            if event.key == pygame.K_a:
                current_solarsystem = solarsystem
            elif event.key == pygame.K_s:
                current_solarsystem = inner_planets
            elif event.key == pygame.K_d:
                current_solarsystem = outer_planets

    # ---> Draw and update Solar System <---
    DISPLAYSURF.fill(constants.COLOR_BACKGROUND)

    for body in current_solarsystem:
        body.update_position(current_solarsystem)
        body.draw(DISPLAYSURF)

    # Display Menu Text
    fps_text = FONT_2.render("FPS: " + str(int(clock.get_fps())), True,
                             constants.COLOR_TEXT)
    DISPLAYSURF.blit(fps_text, (15, 15))

    # Settings
    scale_text = FONT_2.render("Press UP / DOWN to adjust Simulation Scale",
                               True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(scale_text, (15, 45))

    speed_text = FONT_2.render("Press RIGHT / LEFT to adjust Simulation Speed",
                               True, constants.COLOR_TEXT)
    DISPLAYSURF.blit(speed_text, (15, 75))

    # Orbit Lines
    orbit_text = FONT_2.render(
        "Press Q or Number Keys 1-8 to toggle Orbit Lines", True,
        constants.COLOR_TEXT)
    DISPLAYSURF.blit(orbit_text, (15, 105))

    # Planets
    all_text = FONT_2.render("Press A to show all Planets", True,
                             constants.COLOR_TEXT)
    DISPLAYSURF.blit(all_text, (15, 135))

    inner_text = FONT_2.render("Press S to show Inner Planets", True,
                               constants.COLOR_TEXT)
    DISPLAYSURF.blit(inner_text, (15, 165))

    outer_text = FONT_2.render("Press D to show Outer Planets", True,
                               constants.COLOR_TEXT)
    DISPLAYSURF.blit(outer_text, (15, 195))

    # Display Planet Names and Distances
    sun_surface = FONT_1.render("Distance from the Sun", True,
                                constants.COLOR_TEXT)
    DISPLAYSURF.blit(sun_surface, (15, 445))

    mercury_surface = FONT_1.render(
        "Mercury: " + f"{round(mercury.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_MERCURY)
    DISPLAYSURF.blit(mercury_surface, (15, 475))

    venus_surface = FONT_1.render(
        "Venus: " + f"{round(venus.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_VENUS)
    DISPLAYSURF.blit(venus_surface, (15, 505))

    earth_surface = FONT_1.render(
        "Earth: " + f"{round(earth.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_EARTH)
    DISPLAYSURF.blit(earth_surface, (15, 535))

    mars_surface = FONT_1.render(
        "Mars: " + f"{round(mars.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_MARS)
    DISPLAYSURF.blit(mars_surface, (15, 565))

    jupiter_surface = FONT_1.render(
        "Jupiter: " + f"{round(jupiter.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_JUPITER)
    DISPLAYSURF.blit(jupiter_surface, (15, 595))

    saturn_surface = FONT_1.render(
        "Saturn: " + f"{round(saturn.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_SATURN)
    DISPLAYSURF.blit(saturn_surface, (15, 625))

    uranus_surface = FONT_1.render(
        "Uranus: " + f"{round(uranus.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_URANUS)
    DISPLAYSURF.blit(uranus_surface, (15, 655))

    neptune_surface = FONT_1.render(
        "Neptune: " + f"{round(neptune.distance_to_sun / 1000, 1)} km", True,
        constants.COLOR_NEPTUNE)
    DISPLAYSURF.blit(neptune_surface, (15, 685))

    pygame.display.update()
    clock.tick(FPS)
