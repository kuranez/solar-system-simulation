from physics.constants import AU
from config.colors import TNO_COLORS

# TNOs
TNO_DATA = {
    "Pluto": {
        "name":                 "Pluto",
        "radius":               1188.3e3 / 2,           # meters
        "mass":                 1.303e22,               # kg
        "semi_major_axis":      39.48 * AU,             # AU
        "orbital_velocity":     4740,                   # m/s
        "color":                TNO_COLORS["Pluto"],    # rgb
    }
}