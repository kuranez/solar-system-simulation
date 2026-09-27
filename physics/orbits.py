# physics.orbits - Orbit calculations

import math
import random
from physics.constants import G

def calculate_orbital_speed(central_mass, distance, g=G):
    """Calculate circular orbital velocity: v = sqrt(G * M / r)"""
    return math.sqrt(g * central_mass / distance)

def calculate_circular_orbit(central_mass, distance, angle=None, eccentricity_range=(1.0, 1.0)):
    """
    Returns initial position (x, y) and velocity (vx, vy) for a circular/near-circular orbit.
    """
    if angle is None:
        angle = random.uniform(0, 2 * math.pi)

    x = distance * math.cos(angle)
    y = distance * math.sin(angle)

    speed = calculate_orbital_speed(central_mass, distance)
    
    # Optional eccentricity variation
    if eccentricity_range != (1.0, 1.0):
        speed *= random.uniform(*eccentricity_range)

    vx = -speed * math.sin(angle)
    vy = speed * math.cos(angle)

    return x, y, vx, vy