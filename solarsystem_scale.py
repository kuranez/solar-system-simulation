# solarsystem_scale.py

# import constants
from data.planets import PLANET_DATA
import config.simulation

# Scale calculations

def scale_planet_size(planet_radius, scale, is_outer_planet=False):
    """Scale the planet size based on Earth diameter and current scale (zoom)."""
    diameter = planet_radius * 2
    scale_factor = config.simulation.OUTER_PLANET_SCALE_FACTOR if is_outer_planet else 1
    # Multiply by scale so planet size grows/shrinks with zoom
    return (diameter / PLANET_DATA["Earth"]["diameter"]) * config.simulation.BASE_SIZE * scale_factor * scale / config.simulation.DEFAULT_SCALE

def calculate_scaled_sizes(scale):
    """Calculate scaled sizes for all planets using radius and current scale."""
    scaled_sizes = {}
    
    # Add planets from PLANETS_DATA
    for planet_data in PLANET_DATA.values():
        planet_name = planet_data["name"]
        planet_radius = planet_data["radius"]
        is_outer = not planet_data["is_inner"]
        scaled_sizes[planet_name] = scale_planet_size(planet_radius, scale, is_outer_planet=is_outer)
    
    return scaled_sizes
    
#     return scaled_sizes

# # Get Sizes
# scaled_sizes = calculate_scaled_sizes()

# def main():
#     """Main function to execute calculations and display results."""
#     for planet, size in scaled_sizes.items():
#         print(f"{planet}: {size:.2f} pixels")

# if __name__ == "__main__":
#     main()