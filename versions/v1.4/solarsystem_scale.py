# solarsystem_scale.py

import constants

# Scale calculations

def scale_planet_size(planet_radius, scale, is_outer_planet=False):
    """Scale the planet size based on Earth diameter and current scale (zoom)."""
    diameter = planet_radius * 2
    scale_factor = constants.OUTER_PLANET_SCALE_FACTOR if is_outer_planet else 1
    # Multiply by scale so planet size grows/shrinks with zoom
    return (diameter / constants.earth_diameter) * constants.BASE_SIZE * scale_factor * scale / constants.DEFAULT_SCALE

def calculate_scaled_sizes(scale):
    """Calculate scaled sizes for all planets using radius and current scale."""
    return {
        "Mercury": scale_planet_size(constants.mercury_radius, scale),
        "Venus": scale_planet_size(constants.venus_radius, scale),
        "Earth": scale_planet_size(constants.earth_radius, scale),
        "Mars": scale_planet_size(constants.mars_radius, scale),
        "Jupiter": scale_planet_size(constants.jupiter_radius, scale, is_outer_planet=True),
        "Saturn": scale_planet_size(constants.saturn_radius, scale, is_outer_planet=True),
        "Uranus": scale_planet_size(constants.uranus_radius, scale, is_outer_planet=True),
        "Neptune": scale_planet_size(constants.neptune_radius, scale, is_outer_planet=True),
    }
    
#     return scaled_sizes

# # Get Sizes
# scaled_sizes = calculate_scaled_sizes()

# def main():
#     """Main function to execute calculations and display results."""
#     for planet, size in scaled_sizes.items():
#         print(f"{planet}: {size:.2f} pixels")

# if __name__ == "__main__":
#     main()