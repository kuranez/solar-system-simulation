# data.planets - Planet Constants

from config.colors import PLANET_COLORS

PLANET_DATA = {
    # Inner Planets
    "Mercury": {
        "name":         "Mercury",
        "position":     -0.387,                     # AU from Sun
        "perihelion":   46.0e9,                     # meters
        "diameter":     44879e3,                    # meters
        "radius":       4879e3 / 2,                 # meters
        "mass":         0.33e24,                    # kg
        "velocity":     47.40e3,                    # m/s
        "color":        PLANET_COLORS["Mercury"],   # rgb
        "is_inner":     True
    },
    "Venus": {
        "name":         "Venus",
        "position":     -0.723,
        "perihelion":   107.5e9,
        "diameter":     12104e3,
        "radius":       12104e3 / 2,
        "mass":         4.87e24,
        "velocity":     35.02e3,
        "color":        PLANET_COLORS["Venus"],
        "is_inner":     True
    },
    "Earth": {
        "name":         "Earth",
        "position":     -1.0,
        "perihelion":   147.1e9,
        "diameter":     12756e3,   
        "radius":       12756e3 / 2,
        "mass":         5.97e24,
        "velocity":     29.78e3,
        "color":        PLANET_COLORS["Earth"],
        "is_inner":     True
    },
    "Mars": {
        "name":         "Mars",
        "position":     -1.524,
        "perihelion":   206.7e9,
        "diameter":     6792e3,
        "radius":       6792e3 / 2,
        "mass":         0.642e24,
        "velocity":     24.06e3,
        "color":        PLANET_COLORS["Mars"],
        "is_inner":     True
    },
    # Outer Planets
    "Jupiter": {
        "name":         "Jupiter",
        "position":     -5.204,
        "perihelion":   740.6e9,
        "diameter":     142984e3,
        "radius":       142984e3 / 2,
        "mass":         1898e24,
        "velocity":     13.06e3,
        "color":        PLANET_COLORS["Jupiter"],
        "is_inner":     False
    },
    "Saturn": {
        "name":         "Saturn",
        "position":     -9.573,
        "perihelion":   1357.6e9,
        "diameter":     120536e3,
        "radius":       120536e3 / 2,
        "mass":         568e24,
        "velocity":     9.68e3,
        "color":        PLANET_COLORS["Saturn"],
        "is_inner":     False
    },
    "Uranus": {
        "name":         "Uranus",
        "position":     -19.165,
        "perihelion":   2732.7e9,
        "diameter":     51118e3,
        "radius":       51118e3 / 2,
        "mass":         86.8e24,
        "velocity":     6.80e3,
        "color":        PLANET_COLORS["Uranus"],
        "is_inner":     False
    },
    "Neptune": {
        "name":         "Neptune",
        "position":     -30.178,
        "perihelion":   4471.1e9,
        "diameter":     49528e3,
        "radius":       49528e3 / 2,
        "mass":         102e24,
        "velocity":     5.43e3,
        "color":        PLANET_COLORS["Neptune"],
        "is_inner":     False
    }
}