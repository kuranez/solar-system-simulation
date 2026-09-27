# data.asteroids - Asteroid Constants

from physics.constants import AU
from config.colors import ASTEROID_COLORS

# Major Asteroids
ASTEROID_DATA = {
    "Ceres": {
        "name":             "Ceres",
        "radius":           473e3,                      # meters
        "mass":             9.393e20,                   # kg
        "semi_major_axis":  2.77 * AU,                  # AU
        "orbital_velocity": 17900,                      # m/s
        "color":            ASTEROID_COLORS["Ceres"]    # rgb
    },
    "Vesta": {
        "name":             "Vesta",
        "radius":           262.7e3,
        "mass":             2.59e20,
        "semi_major_axis":  2.36 * AU,
        "orbital_velocity": 19300,
        "color":            ASTEROID_COLORS["Vesta"]
    },
    "Pallas": {
        "name":             "Pallas",
        "radius":           256e3,
        "mass":             2.11e20,
        "semi_major_axis":  2.77 * AU,
        "orbital_velocity": 17000,
        "color":            ASTEROID_COLORS["Pallas"]
    },
    "Juno": {
        "name":             "Juno",
        "radius":           118e3,
        "mass":             2.67e19,
        "semi_major_axis":  2.67 * AU,
        "orbital_velocity": 18000,
        "color":            ASTEROID_COLORS["Juno"]
    }
}