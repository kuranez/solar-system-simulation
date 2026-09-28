# solarsystem_creation - Factory module: Creates objects in the Solar System like Sun, Planets, Asteroids

import random

import config.simulation
import physics.constants

from objects.body import Body

from physics.orbits import calculate_circular_orbit
from render.scale import calculate_scaled_sizes

from data.sun import SUN_DATA
from data.planets import PLANET_DATA
from data.asteroids import ASTEROID_DATA
from data.tnos import TNO_DATA

from skyfield.api import load
# from skyfield.timelib import Time

def create_solarsystem():
    """Create objects in the solar system using Skyfield for real positions."""
    # Scaling
    default_size = config.simulation.DEFAULT_SCALE
    sun_size = config.simulation.SUN_SIZE
    scaled_sizes = calculate_scaled_sizes(default_size)

    # Load Skyfield data
    # Use most recent DE440s ephemeris for accurate planetary positions
    eph = load('de440s.bsp')
    # Load timescale and get current time
    ts = load.timescale()
    # Set time to now for current positions, or you can set it to a specific date/time
    t = ts.now()
    
    # Create Sun at center with mass from constants
    sun = Body(
        name =  SUN_DATA["Sun"]["name"],    # Name
        x = 0.0, y = 0.0,                   # Position: Center of Screen
        vx = 0.0, vy = 0.0,                 # Intial velocity
        mass = SUN_DATA["Sun"]["mass"],     # Mass
        radius = sun_size,                  # Draw radius -> Display radius not physical radius
        color = SUN_DATA["Sun"]["color"],   # Color
        is_sun = True
    )

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

        # Create Planet objects with scaled size and mass from constants
        planet = Body(
            name = data["name"],
            x = x, y = y, vx = vx, vy = vy,
            mass = data["mass"],
            radius = scaled_sizes[data["name"]],
            color = data["color"],
            track_orbit = True # Enables OrbitTracker
        )

        # Add planet to the list
        planets.append(planet)

   #  sun.draw_line = False
    return [sun] + planets

def create_major_asteroids():
    """Create major asteroids Ceres and Vesta"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    asteroid_radius = config.simulation.MINOR_BASE_SIZE
    major_asteroids = []
    
    for data in ASTEROID_DATA.values():
        x, y, vx, vy = calculate_circular_orbit(sun_mass, data["semi_major_axis"])

    major_asteroids.append(
        Body(
            name = data["name"],
            x = x, y = y, vx = vx, vy = vy,
            mass = data["mass"],
            radius = asteroid_radius,
            color = data["color"],
            is_asteroid = True,
            track_orbit = False
        )
    )

    return major_asteroids

def create_asteroid_belt(num_asteroids: int):
    """Generate asteroids between Mars and Jupiter orbits"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    asteroids = []
    
    # Asteroid belt range (default: 2.2 to 3.2 AU from the Sun)
    inner_radius = config.simulation.INNER_RADIUS
    outer_radius = config.simulation.OUTER_RADIUS

    # Asteroid sizes (default: 0.5 to 2 px)
    min_size = config.simulation.MIN_SIZE
    max_size = config.simulation.MAX_SIZE
    rnd_mass = config.simulation.RND_MASS
    
    for i in range(num_asteroids):
        # Random orbital distance
        dist = random.uniform(inner_radius, outer_radius)
        x, y, vx, vy = calculate_circular_orbit(sun_mass, dist, eccentricity_range = (0.95, 1.05))
        
        asteroids.append(
            Body(
                name="Asteroid",
                x = x, y = y, vx = vx, vy = vy,
                mass = rnd_mass,
                radius = random.uniform(min_size, max_size),
                color = config.colors.ASTEROID_COLORS["Random"],
                is_asteroid = True,
                track_orbit = False
            )
        )
    
    return asteroids

def create_Kuiper_belt(num_objects: int):
    """Generate Kuiper Belt / Trans-Neptunian Objects (TNOs) (30 to 50 AU)"""
    sun_mass = SUN_DATA["Sun"]["mass"]    
    tnos = []
    
    # TNO belt range (default: 30 to 50 AU from the Sun)
    inner_radius = config.simulation.INNER_KUIPER_RADIUS
    outer_radius = config.simulation.OUTER_KUIPER_RADIUS

    # TNO random object size
    min_size = config.simulation.MIN_SIZE
    max_size = config.simulation.MAX_SIZE
    rnd_mass = config.simulation.RND_MASS
    
    for i in range(num_objects):
        # Random orbital distance
        dist = random.uniform(inner_radius, outer_radius)
        x, y, vx, vy = calculate_circular_orbit(sun_mass, dist, eccentricity_range=(0.95, 1.05))

        tnos.append(
            Body(
                name="TNO",
                x = x, y = y, vx = vx, vy = vy,
                mass = rnd_mass,
                radius = random.uniform(min_size, max_size),
                color = config.colors.TNO_COLORS["Random"],
                is_asteroid = True,
                track_orbit = False
            )
        )
    
    return tnos

def create_pluto():
    """Create Pluto as a special case TNO"""
    sun_mass = SUN_DATA["Sun"]["mass"]
    data = TNO_DATA["Pluto"]
    base_size = config.simulation.MINOR_BASE_SIZE
    x, y, vx, vy = calculate_circular_orbit(sun_mass, data["semi_major_axis"])

    pluto = Body(
        name = data["name"],
        x = x, y = y, vx = vx, vy = vy,
        mass = data["mass"],
        radius = base_size,
        color = data["color"],
        track_orbit=True
    )
    
    return pluto