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

        # Metadata for HUD calculations
        self.perihelion = None
        self.aphelion = None

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
        general_trail_length = 20000  # Maximum points in the orbit for all bodies
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

        # Orbit counting variables (angle-based to remain stable with large timesteps)
        self.orbit_count = 0
        self.prev_x = x
        self.prev_y = y
        self.previous_angle = math.atan2(y, x)
        self.accumulated_angle = 0.0

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

        # Check if the planet has completed a full orbit
        sun = next((body for body in current_solarsystem if getattr(body, "sun", False)), None)
        if sun is not None:
            self._check_orbit_completion(sun)

        # Update the flash timer if it's active
        if self.flash_timer > 0:
            self.flash_timer -= 1

    def _check_orbit_completion(self, sun):
        """Count completed orbits by tracking angular sweep around the Sun."""
        current_angle = math.atan2(self.y - sun.y, self.x - sun.x)

        # Normalize delta to [-pi, pi] to handle angle wraparound at +/-pi.
        delta = current_angle - self.previous_angle
        if delta > math.pi:
            delta -= 2 * math.pi
        elif delta < -math.pi:
            delta += 2 * math.pi

        self.accumulated_angle += delta
        completed_orbits = int(abs(self.accumulated_angle) / (2 * math.pi))

        if completed_orbits > 0:
            self.orbit_count += completed_orbits
            # Keep remainder to preserve progress toward the next orbit.
            self.accumulated_angle = math.fmod(self.accumulated_angle, 2 * math.pi)
            self.flash_timer = self.flash_duration
            print(f"{self.name} completed orbit #{self.orbit_count}")

        self.previous_angle = current_angle

    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        """Draw the body with its orbit trail."""
        # Calculate position on screen
        x = self.x * scale + constants.WIDTH / 2 + screen_offset_x
        y = self.y * scale + constants.HEIGHT / 2 + screen_offset_y
        
        # Draw orbit trail with fade effect
        if self.draw_line and len(self.orbit) >= 2:
            # Calculate the fade factor based on orbit count
            # Each completed orbit makes the trail 10% darker
            orbit_fade_multiplier = max(0.1, 1.0 - (self.orbit_count * 0.1))
            
            fade_scale = 1.0  # Adjust this value to control brightness
            orbit_points = [
                (
                    px * scale + constants.WIDTH / 2 + screen_offset_x,
                    py * scale + constants.HEIGHT / 2 + screen_offset_y
                )
                for px, py in self.orbit
            ]
            
            # Draw the trail with both distance fade and orbit count fade
            for i in range(1, len(orbit_points)):
                # Distance-based fade (older parts of trail are more faded)
                distance = len(orbit_points) - i
                distance_fade_factor = max(0, min(255, int(255 * (distance / len(orbit_points)) * fade_scale)))
                
                # Combine orbit count fade with distance fade
                combined_fade = orbit_fade_multiplier * (1 - distance_fade_factor / 255)
                
                faded_color = (
                    int(self.color[0] * combined_fade + constants.COLOR_BACKGROUND[0] * (1 - combined_fade)),
                    int(self.color[1] * combined_fade + constants.COLOR_BACKGROUND[1] * (1 - combined_fade)),
                    int(self.color[2] * combined_fade + constants.COLOR_BACKGROUND[2] * (1 - combined_fade))
                )
                
                pygame.draw.line(DISPLAYSURF, faded_color, orbit_points[i - 1], orbit_points[i], 1)
        
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

class Asteroid(Body):
    def __init__(self, x, y, radius, mass, color=(192, 192, 192)):
        super().__init__(x, y, radius, mass)
        self.sun = False
        self.name = "Asteroid"
        self.color = color  # Set asteroid color
        self.draw_line = False # Asteroids don't need orbit trails
    
    def draw(self, DISPLAYSURF, scale, screen_offset_x=0, screen_offset_y=0):
        """Optimized draw for asteroids"""
        x = self.x * scale + constants.WIDTH / 2 + screen_offset_x
        y = self.y * scale + constants.HEIGHT / 2 + screen_offset_y
        
        # Only draw if on screen (culling)
        if 0 <= x <= constants.WIDTH and 0 <= y <= constants.HEIGHT:
            # Draw as simple circle (no fade trails)
            pygame.draw.circle(DISPLAYSURF, self.color, (int(x), int(y)), max(1, int(self.radius)))

    def update_position(self, current_solarsystem):
        """Only calculate attraction to the Sun for performance"""
        # The Sun is the first object in the solar system list
        sun = current_solarsystem[0]
        fx, fy = self.attraction(sun)
        self.x_vel += fx / self.mass * self.TIMESTEP
        self.y_vel += fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        # No orbit trail needed