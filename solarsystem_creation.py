# solarsystem_creation.py

import constants
import random
import math
from solarsystem_sim import Body, Sun, Planet, Asteroid
from solarsystem_scale import calculate_scaled_sizes
from skyfield.api import load, EarthSatellite
from skyfield.timelib import Time

def create_solarsystem():
    """Create objects in the solar system using Skyfield for real positions."""
    # Use the default simulation scale for initial planet rendering sizes.
    scaled_sizes = calculate_scaled_sizes(constants.DEFAULT_SCALE)

    # Load Skyfield data
    # Use most recent DE440s ephemeris for accurate planetary positions
    eph = load('de440s.bsp')
    # Load timescale and get current time
    ts = load.timescale()
    # Set time to now for current positions, or you can set it to a specific date/time
    t = ts.now()

    # Get the Sun object from Skyfield
    sun_obj = eph['SUN']
    # Create Sun at center with mass from constants
    sun = Sun(0, 0, 2, constants.sun_mass)
    # List to hold planet objects
    planets = []

    # Map planet names to the names Skyfield expects for the de440s kernel
    skyfield_names = {
        "MERCURY": "MERCURY",
        "VENUS": "VENUS",
        "EARTH": "EARTH", # Special handling for Earth to get the planet
        "MARS": "MARS BARYCENTER",
        "JUPITER": "JUPITER BARYCENTER",
        "SATURN": "SATURN BARYCENTER",
        "URANUS": "URANUS BARYCENTER",
        "NEPTUNE": "NEPTUNE BARYCENTER",
    }

    # Loop through our planet data and create Planet objects with positions and velocities from Skyfield
    for data in constants.PLANETS_DATA:
        planet_name_upper = data["name"].upper()
        
        # Get the correct skyfield object name from our map
        skyfield_name = skyfield_names.get(planet_name_upper)
        
        if skyfield_name is None:
            continue # Skip if we don't have a mapping for this planet

        # For Earth, we need to get the planet itself, not the barycenter with the Moon
        if planet_name_upper == "EARTH":
            sky_planet = eph['earth']
        else:
            sky_planet = eph[skyfield_name]

        # Get position and velocity from Skyfield
        astrometric = (sky_planet - sun_obj).at(t)
        position = astrometric.position
        velocity = astrometric.velocity

        # Convert from AU and AU/day to meters and m/s
        x = position.au[0] * constants.AU
        y = position.au[1] * constants.AU  # Use x and y for 2D projection
        
        vx = velocity.au_per_d[0] * constants.AU / (24 * 3600)
        vy = velocity.au_per_d[1] * constants.AU / (24 * 3600)

        # Create Planet object with scaled size and mass from constants
        planet = Planet(
            x,
            y,
            scaled_sizes[data["name"]],
            data["mass"],
            name=data["name"],
            is_inner_planet=data.get("is_inner", False)
        )
        # Set velocity from Skyfield data
        planet.x_vel = vx
        planet.y_vel = vy
        # Draw orbit lines for planets (except the Sun)
        planet.draw_line = True
        # Add planet to the list
        planets.append(planet)

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