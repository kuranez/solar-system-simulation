# solarsystem_creation - Factory module

# import constants
import random
# import math

import config.simulation
import physics.constants

from objects.body import Body

from physics.orbits import calculate_circular_orbit

from data.sun import SUN_DATA
from data.planets import PLANET_DATA
from data.asteroids import ASTEROID_DATA
from data.tnos import TNO_DATA

# from solarsystem_sim import Sun, Planet, Asteroid
from solarsystem_scale import calculate_scaled_sizes

from skyfield.api import load
# from skyfield.timelib import Time

def create_solarsystem():
    """Create objects in the solar system using Skyfield for real positions."""
    # Use the default simulation scale for initial planet rendering sizes.
    scaled_sizes = calculate_scaled_sizes(config.simulation.DEFAULT_SCALE)

    # Load Skyfield data
    # Use most recent DE440s ephemeris for accurate planetary positions
    eph = load('de440s.bsp')
    # Load timescale and get current time
    ts = load.timescale()
    # Set time to now for current positions, or you can set it to a specific date/time
    t = ts.now()
    
    # Create Sun at center with mass from constants
    # New creation method
    sun = Body(
        name = SUN_DATA["Sun"]["name"],     # Name
        x = 0.0, y = 0.0,                   # Position: Center of Screen
        vx = 0.0, vy = 0.0,                 # Intial velocity
        mass = SUN_DATA["Sun"]["mass"],     # Mass
        radius = 2,                         # Draw radius -> Display radius not physical radius
        color = SUN_DATA["Sun"]["color"],   # Color
        is_sun = True
    )

    # Old creation method
    # sun = Sun(0, 0, 2, SUN_DATA["Sun"]["mass"])

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

    # List to hold planet objects
    planets = []
    # Get the Sun object from Skyfield
    sun_obj = eph['SUN']

    # Loop through our planet data and create Planet objects with positions and velocities from Skyfield
    for data in PLANET_DATA.values():
        # Convert name to Uppercase, because Skyfield uses Uppercase
        planet_name_upper = data["name"].upper()
        # Get the correct skyfield object name from our map
        sky_name = skyfield_names.get(planet_name_upper)
        
        if sky_name is None:
            continue # Skip if we don't have a mapping for this planet

        # For Earth, we need to get the planet itself, not the barycenter with the Moon
        if planet_name_upper == "EARTH":
            sky_planet = eph['earth']
        else:
            sky_planet = eph[sky_name]

        # Get position and velocity from Skyfield
        astrometric = (sky_planet - sun_obj).at(t)
        position = astrometric.position
        velocity = astrometric.velocity

        # Convert from AU and AU/day to meters and m/s
        x = position.au[0] * physics.constants.AU
        y = position.au[1] * physics.constants.AU  # Use x and y for 2D projection
        
        vx = velocity.au_per_d[0] * physics.constants.AU / (24 * 3600)
        vy = velocity.au_per_d[1] * physics.constants.AU / (24 * 3600)

        # Create Planet object with scaled size and mass from constants

        planet = Body(
            name = data["name"],
            x = x, y = y,
            vx = vx, vy = vy,
            mass = data["mass"],
            radius = scaled_sizes[data["name"]],
            color = data["color"],
            track_orbit=True # Enables OrbitTracker
        )

        # Old planet creation
        # planet = Planet(
        #     x,
        #     y,
        #     scaled_sizes[data["name"]],
        #     data["mass"],
        #     name=data["name"],
        #     is_inner_planet=data.get("is_inner", False)
        # )
        # # Set velocity from Skyfield data
        # planet.x_vel = vx
        # planet.y_vel = vy
        # # Draw orbit lines for planets (except the Sun)
        # planet.draw_line = True

        # Add planet to the list
        planets.append(planet)

   #  sun.draw_line = False
    return [sun] + planets

def create_major_asteroids():
    """Create major asteroids Ceres and Vesta"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    major_asteroids = []
    
    for data in ASTEROID_DATA.values():
        x, y, vx, vy = calculate_circular_orbit(sun_mass, data["semi_major_axis"])

    major_asteroids.append(
        Body(
            name=data["name"],
            x = x, y = y, vx = vx, vy = vy,
            mass = data["mass"],
            radius = 2.5,
            color = data["color"],
            is_asteroid=True,
            track_orbit=False
        )
    )

    return major_asteroids

def create_asteroid_belt(num_asteroids: int):
    """Generate asteroids between Mars and Jupiter orbits"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    asteroids = []
    
    # Asteroid belt range (2.2 to 3.2 AU from the Sun)
    inner_radius = 2.2 * physics.constants.AU
    outer_radius = 3.2 * physics.constants.AU
    
    for i in range(num_asteroids):
        # Random orbital distance
        dist = random.uniform(inner_radius, outer_radius)
        x, y, vx, vy = calculate_circular_orbit(sun_mass, dist, eccentricity_range = (0.95, 1.05))

        # Old orbit calc
        # Random angle around the Sun
        # angle = random.uniform(0, 2 * math.pi)
        
        # Calculate x, y position
        # x = dist * math.cos(angle)
        # y = dist * math.sin(angle)
        
        asteroids.append(
            Body(
                name="Asteroid",
                x = x, y = y, vx = vx, vy = vy,
                mass = 1e15,
                radius = random.uniform(0.5, 2),
                color = (128, 128, 128),
                is_asteroid = True,
                track_orbit = False
            )
        )

        # Small random size (1-3 pixels)
        # size = random.uniform(0.5, 2)
        
        # Very small mass (negligible gravitational effect)
        # mass = 1e15  # Much smaller than planets
        
        # Uniform light gray color
        # color = (128, 128, 128)
        
        # asteroid = Asteroid(x, y, size, mass, color)
        
        # Calculate orbital velocity (circular orbit around Sun)
        # orbital_speed = math.sqrt(physics.constants.G * SUN_DATA["Sun"]["mass"] / distance)
        
        # Set velocity perpendicular to position vector
        # asteroid.x_vel = -orbital_speed * math.sin(angle)
        # asteroid.y_vel = orbital_speed * math.cos(angle)
        
        # Add some random eccentricity
        # asteroid.x_vel *= random.uniform(0.95, 1.05)
        # asteroid.y_vel *= random.uniform(0.95, 1.05)
        
        # asteroids.append(asteroid)
    
    return asteroids

def create_Kuiper_belt(num_objects: int):
    """Generate Kuiper Belt / Trans-Neptunian Objects (TNOs) (30 to 50 AU)"""
    sun_mass = SUN_DATA["Sun"]["mass"]    
    tnos = []
    
    # TNO belt range (30 to 50 AU from the Sun)
    inner_radius = 30 * physics.constants.AU
    outer_radius = 50 * physics.constants.AU
    
    for i in range(num_objects):
        # Random orbital distance
        dist = random.uniform(inner_radius, outer_radius)
        x, y, vx, vy = calculate_circular_orbit(sun_mass, dist, eccentricity_range=(0.95, 1.05))

        tnos.append(
            Body(
                name="TNO",
                x = x, y = y, vx = vx, vy = vy,
                mass = 1e15,
                radius = random.uniform(0.5, 2.0),
                color = (160, 160, 160),
                is_asteroid = True,
                track_orbit = False
            )
        )
        
        # Random angle around the Sun
        # angle = random.uniform(0, 2 * math.pi)
        
        # Calculate x, y position
        # x = distance * math.cos(angle)
        # y = distance * math.sin(angle)
        
        # Small random size (1-3 pixels)
        # size = random.uniform(0.5, 2)
        
        # Very small mass (negligible gravitational effect)
        # mass = 1e15  # Much smaller than planets
        
        # Uniform light gray color
        # color = (160, 160, 160)
        
        # tno_object = Asteroid(x, y, size, mass, color)
        
        # Calculate orbital velocity (circular orbit around Sun)
        # orbital_speed = math.sqrt(physics.constants.G * SUN_DATA["Sun"]["mass"] / distance)
        
        # Set velocity perpendicular to position vector
        # tno_object.x_vel = -orbital_speed * math.sin(angle)
        # tno_object.y_vel = orbital_speed * math.cos(angle)
        
        # Add some random eccentricity
        # tno_object.x_vel *= random.uniform(0.95, 1.05)
        # tno_object.y_vel *= random.uniform(0.95, 1.05)
        
        # tno_objects.append(tno_object)
    
    return tnos

def create_pluto():
    """Create Pluto as a special case TNO"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    data = TNO_DATA["Pluto"]
    x, y, vx, vy = calculate_circular_orbit(sun_mass, data["semi_major_axis"])

    pluto = Body(
        name=       data["name"],
        x=x,        y=y,
        vx=vx,      vy=vy,
        mass=       data["mass"],
        radius=     2.5,
        color=      data["color"],
        track_orbit=True
    )
    # pluto_distance = pluto_data["semi_major_axis"]
    # pluto_angle = random.uniform(0, 2 * math.pi)
    
    # pluto = Planet(
    #     pluto_distance * math.cos(pluto_angle),
    #     pluto_distance * math.sin(pluto_angle),
    #     2.5,  # Size in pixels
    #     pluto_data["mass"],
    #     name=pluto_data["name"],
    #     is_inner_planet=False
    # )
    
    # # Calculate orbital velocity
    # orbital_speed = math.sqrt(physics.constants.G * SUN_DATA["Sun"]["mass"] / pluto_distance)
    # pluto.x_vel = -orbital_speed * math.sin(pluto_angle)
    # pluto.y_vel = orbital_speed * math.cos(pluto_angle)
    
    # pluto.color = pluto_data["color"]
    # pluto.draw_line = True  # Show orbit trail for Pluto
    
    return pluto