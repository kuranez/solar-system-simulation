# solarsystem_scale.py

# import constants
from data.planets import PLANET_DATA
import config.simulation

# Scale calculations

def scale_planet_size(
        planet_radius: float, 
        scale: float, 
        is_outer_planet: bool=False) -> float:
    """Scale the planet size based on Earth diameter and current scale (zoom)."""
    
    diameter = planet_radius * 2

    # Short variables
    earth_diameter = PLANET_DATA["Earth"]["diameter"] 
    base = config.simulation.BASE_SIZE
    default = config.simulation.DEFAULT_SCALE
    outer = config.simulation.OUTER_PLANET_SCALE_FACTOR

    # Scale outer planets
    scale_factor = outer if is_outer_planet else 1

    # Multiply by scale so planet size grows/shrinks with zoom
    return (diameter / earth_diameter) * base* scale_factor * scale / default

def calculate_scaled_sizes(scale: float) -> dict[str, float]:
    """Calculate scaled sizes for all planets using radius and current scale."""
    scaled_sizes = {}
    
    # Add planets from PLANETS_DATA
    for planet_data in PLANET_DATA.values():
        # Short variables
        planet_name = planet_data["name"]
        planet_radius = planet_data["radius"]
        is_outer = not planet_data["is_inner"]
        # Scale sizes
        scaled_sizes[planet_name] = scale_planet_size(planet_radius, scale, is_outer_planet=is_outer)
    
    return scaled_sizes
