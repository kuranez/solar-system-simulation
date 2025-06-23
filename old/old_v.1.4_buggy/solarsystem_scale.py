# solarsystem_scale.py

import constants

# Scale calculations
def scale_planet_size(planet_radius, zoom_factor=1.0, is_outer_planet=False):
    """Scale the planet size based on Earth diameter with additional scaling for outer planets."""
    diameter = planet_radius * 2  # Convert radius to diameter
    scale_factor = constants.OUTER_PLANET_SCALE_FACTOR if is_outer_planet else 1  # Apply outer planet scaling if needed
    return (diameter / constants.earth_diameter) * constants.BASE_SIZE * scale_factor * zoom_factor

def calculate_scaled_sizes(zoom_factor=1):
    """Calculate scaled sizes for all planets using radius."""
    scaled_sizes = {
        "Mercury": scale_planet_size(constants.mercury_radius, zoom_factor),
        "Venus": scale_planet_size(constants.venus_radius, zoom_factor),
        "Earth": scale_planet_size(constants.earth_radius, zoom_factor),
        "Mars": scale_planet_size(constants.mars_radius, zoom_factor),
        "Jupiter": scale_planet_size(constants.jupiter_radius, zoom_factor, is_outer_planet=True),
        "Saturn": scale_planet_size(constants.saturn_radius, zoom_factor, is_outer_planet=True),
        "Uranus": scale_planet_size(constants.uranus_radius, zoom_factor, is_outer_planet=True),
        "Neptune": scale_planet_size(constants.neptune_radius, zoom_factor, is_outer_planet=True),
    }
    
    return scaled_sizes

# Get Sizes
scaled_sizes = calculate_scaled_sizes()

def main():
    """Main function to execute calculations and display results."""
    for planet, size in scaled_sizes.items():
        print(f"{planet}: {size:.2f} pixels")

if __name__ == "__main__":
    main()