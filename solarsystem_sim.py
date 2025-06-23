# solarsystem_sim.py

import constants
import pygame
import math
import itertools


# Solar system bodies
class Body:
    
    # Constants
    AU = constants.AU
    G = constants.G
    # DEFAULT_SCALE = constants.DEFAULT_SCALE
    TIMESTEP = constants.TIMESTEP

    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass

        self.color = (0, 0, 0)

        self.sun = False
        self.distance_to_sun = 0

        self.orbit = []

        self.x_vel = 0.0
        self.y_vel = 0.0

        self.draw_line = True


    def attraction(self, other):
        """Calculate the forces in x and y direction"""        
        # Coordinates
        dx, dy = other.x, other.y
        # Distances
        distance_x = dx - self.x
        distance_y = dy - self.y
        # Total Distance
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        if other.sun:
            self.distance_to_sun = distance
        # Force
        force = self.G * self.mass * other.mass / distance**2
        # Angle
        theta = math.atan2(distance_y, distance_x)
        # Forces
        fx = math.cos(theta) * force
        fy = math.sin(theta) * force

        return fx, fy

    def update_position(self, current_solarsystem):
        """Update Positions of objects"""
        # Total forces, conservation of mass
        total_fx = total_fy = 0

        # Calculate gravitational forces from other bodies
        for body in current_solarsystem:
            if self == body:
                continue

            fx, fy = self.attraction(body)
            total_fx += fx
            total_fy += fy

        # Update velocity based on acceleration a = F / m
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # Update position with velocity
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # Append current position to the orbit
        self.orbit.append((self.x, self.y))

        # General limit for orbit length for all bodies
        general_trail_length = 8000  # Maximum points in the orbit for all bodies
        if len(self.orbit) > general_trail_length:
            self.orbit.pop(0)

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        """Draw the body and its faded orbit trail."""
        # Calculate position on screen
        x = self.x * scale + constants.WIDTH / 2 + screen_offset_x
        y = self.y * scale + constants.HEIGHT / 2 + screen_offset_y

        # Draw the faded orbit trail
        if self.draw_line and len(self.orbit) >= 2:
            fade_scale = 1.5  # Adjust this value to control brightness
            orbit_points = [
                (
                    px * scale + constants.WIDTH / 2 + screen_offset_x,
                    py * scale + constants.HEIGHT / 2 + screen_offset_y
                )
                for px, py in self.orbit
            ]
            for i in range(1, len(orbit_points)):
                distance = len(orbit_points) - i
                fade_factor = max(0, min(255, int(255 * (distance / len(orbit_points)) * fade_scale)))
                faded_color = (
                    int(self.color[0] * (1 - fade_factor / 255) + constants.COLOR_BACKGROUND[0] * (fade_factor / 255)),
                    int(self.color[1] * (1 - fade_factor / 255) + constants.COLOR_BACKGROUND[1] * (fade_factor / 255)),
                    int(self.color[2] * (1 - fade_factor / 255) + constants.COLOR_BACKGROUND[2] * (fade_factor / 255))
                )
                pygame.draw.line(DISPLAYSURF, faded_color, orbit_points[i - 1], orbit_points[i], 1)

        # Draw the body (planet or sun)
        pygame.draw.circle(DISPLAYSURF, self.color, (int(x), int(y)), int(self.radius))
    
# Sun
class Sun(Body):

    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, radius, mass)
        self.sun = True
        self.name = "Sun"
        self.color = constants.COLOR_SUN

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        super().draw(DISPLAYSURF, scale, screen_offset_x, screen_offset_y)


# Planets
class Planet(Body):
    cycle_colors = itertools.cycle([
        constants.COLOR_MERCURY,    # Mercury
        constants.COLOR_VENUS,      # Venus
        constants.COLOR_EARTH,      # Earth
        constants.COLOR_MARS,       # Mars
        constants.COLOR_JUPITER,    # Jupiter
        constants.COLOR_SATURN,     # Saturn
        constants.COLOR_URANUS,     # Uranus
        constants.COLOR_NEPTUNE     # Neptune
    ])

    def __init__(self, x, y, radius, mass, name, is_inner_planet=False):
        super().__init__(x, y, radius, mass)
        self.sun = False
        self.name = name
        self.color = next(Planet.cycle_colors)
        self.original_radius = radius  # Store the original size for later zooming

        # Set orbit trail length based on whether it's an inner or outer planet
        self.trail_length = 800 if is_inner_planet else 8000  # Adjust values as needed

    def update_position(self, current_solarsystem):
        """Update Positions of objects"""
        # Call the update_position method from Body to handle physics
        super().update_position(current_solarsystem)

        # Limit the number of points in the orbit based on the specific trail_length
        if len(self.orbit) > self.trail_length:
            self.orbit.pop(0)

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        super().draw(DISPLAYSURF, scale, screen_offset_x, screen_offset_y)     
