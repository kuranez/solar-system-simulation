# config.simulation - Simulation Configuration

from physics.constants import AU

# -------------------------------------------------------------
# Simulation Settings
# -------------------------------------------------------------

# Simulation Speed
TIMESTEP = 3600 * 24.0 # Seconds in 1 day 

# Substep
SUBSTEP = 1

# FPS & Clock in main.py

# -------------------------------------------------------------
# Scale Factors
# -------------------------------------------------------------

# Astronomic Unit in px
DEFAULT_SCALE = 350 / AU    # 1 AU = 350 px

# Sun Size
SUN_SIZE = 2    # Sun draw radius in px 

# Major Planet Scaling
OUTER_PLANET_SCALE_FACTOR = 0.6 # Outer Planets are 40% smaller
BASE_SIZE = 50                  # Base size for planets in px

# Minor object scaling
MINOR_BASE_SIZE = 2.5   # Base size for major asteroids and TNOs
MIN_SIZE = 0.5          # Min size for random objects
MAX_SIZE = 2.0          # Max size for random objects
RND_MASS = 1e15         # Mass for random objects

# Asteroid Belt Range for random objects
INNER_RADIUS = 2.2 * AU     # (2.2 to 3.2 AU from the sun)
OUTER_RADIUS = 3.2 * AU

# Kuiper Belt Range for random objects
INNER_KUIPER_RADIUS = 30 * AU    # (30 to 50 AU from the sun)
OUTER_KUIPER_RADIUS = 50 * AU

