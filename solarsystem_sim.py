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
        self.orbit_count = 0  # Sun doesn't orbit but needs the attribute

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        super().draw(DISPLAYSURF, scale, screen_offset_x, screen_offset_y)


# Planets
class Planet(Body):
    cycle_colors = itertools.cycle([
        constants.COLOR_MERCURY,    # Mercury
        constants.COLOR_VENUS,      # Venus
        constants.COLOR_EARTH,      # Earths
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

        # Orbit counting variables
        self.orbit = [] # Initialize orbit trail
        self.orbit_start_index = 0 # Start index for orbit trail
        self.last_complete_orbit = [] # Store the last complete orbit points

        self.orbit_count = 0
        self.prev_x = x
        self.prev_y = y
        self.orbit_detected = False
        self.has_crossed_reference = False  # Flag to track if the reference point has been crossed 

        # Visual indicator variables
        self.flash_timer = 0
        self.flash_duration = 10  # Duration in frames (1 second at 60 FPS)

    def update_position(self, current_solarsystem):
        """Update Positions of objects"""
        # Store previous position for orbit counting
        self.prev_x = self.x
        self.prev_y = self.y

        # Call the update_position method from Body to handle physics
        super().update_position(current_solarsystem)

        # Append current position to the orbit
        self.orbit.append((self.x, self.y))

        # Check if the planet has completed a full orbit
        self._check_orbit_completion()

        # Update the flash timer if it's active
        if self.flash_timer > 0:
            self.flash_timer -= 1

    def _check_orbit_completion(self):
        """Check if the planet has completed a full orbit."""
        # Check if we've crossed the negative x-axis from below to above
        crossed_negative_x = (self.prev_y <= 0 and self.y > 0) and self.x < 0
    
        # Alternative: Check if we've crossed the positive x-axis from above to below
        crossed_positive_x = (self.prev_y >= 0 and self.y < 0) and self.x > 0
        
        # Count the orbit if either crossing is detected
        if crossed_negative_x or crossed_positive_x:
            if not self.orbit_detected:
                self.orbit_count += 1
                self.orbit_detected = True
            
                # Save the current orbit as the last complete orbit
                if len(self.orbit) > self.orbit_start_index:
                    self.last_complete_orbit = self.orbit[self.orbit_start_index:]

                # Mark the beginning of the new orbit
                self.orbit_start_index = len(self.orbit)

                # Set the flash timer to create visual indicator
                self.flash_timer = self.flash_duration

                # Print debug info
                print(f"{self.name} completed orbit #{self.orbit_count}")
        else:    
            # Reset detection flag when we're not in the detection zones
            self.orbit_detected = False

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        """Draw the body with its orbit trail."""
        # Calculate position on screen
        x = self.x * scale + constants.WIDTH / 2 + screen_offset_x
        y = self.y * scale + constants.HEIGHT / 2 + screen_offset_y
        
        # Draw orbit trails
        if self.draw_line:
            # Draw complete orbit if available and we're past the first orbit
            if self.orbit_count > 0 and len(self.last_complete_orbit) >= 2:
                # Draw the last complete orbit with full opacity
                orbit_points = [
                    (
                        px * scale + constants.WIDTH / 2 + screen_offset_x,
                        py * scale + constants.HEIGHT / 2 + screen_offset_y
                    )
                    for px, py in self.last_complete_orbit
                ]
                for i in range(1, len(orbit_points)):
                    pygame.draw.line(DISPLAYSURF, self.color, orbit_points[i - 1], orbit_points[i], 1)
            
            # Draw current orbit path
            if len(self.orbit) >= 2:
                orbit_points = [
                    (
                        px * scale + constants.WIDTH / 2 + screen_offset_x,
                        py * scale + constants.HEIGHT / 2 + screen_offset_y
                    )
                    for px, py in self.orbit
                ]
                for i in range(self.orbit_start_index + 1, len(orbit_points)):
                    pygame.draw.line(DISPLAYSURF, self.color, orbit_points[i - 1], orbit_points[i], 1)
                
                # Draw the connection to the last complete orbit if we have one
                if self.orbit_count > 0 and len(self.last_complete_orbit) > 0 and self.orbit_start_index < len(orbit_points):
                    # Connect the last point of the complete orbit to the first point of current orbit
                    last_point = (
                        self.last_complete_orbit[-1][0] * scale + constants.WIDTH / 2 + screen_offset_x,
                        self.last_complete_orbit[-1][1] * scale + constants.HEIGHT / 2 + screen_offset_y
                    )
                    first_point = orbit_points[self.orbit_start_index]
                    pygame.draw.line(DISPLAYSURF, self.color, last_point, first_point, 1)
        
        # Draw the planet itself
        pygame.draw.circle(DISPLAYSURF, self.color, (int(x), int(y)), int(self.radius))
        
        # If flash timer is active, add a visual indicator (bright ring)
        if self.flash_timer > 0:
            # Calculate flash intensity (fade out effect)
            flash_intensity = self.flash_timer / self.flash_duration
            
            # Draw a larger circle around the planet
            flash_radius = int(self.radius * (1.5 + flash_intensity))
            flash_color = (255, 255, 200)  # Bright yellow/white flash
            
            # Draw as a ring (not filled)
            pygame.draw.circle(DISPLAYSURF, flash_color, (int(x), int(y)), flash_radius, 2)