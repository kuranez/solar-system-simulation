# config.simulation - Simulation Configuration

from physics.constants import AU

# Scale Factors
DEFAULT_SCALE = 350 / AU  # 1 AU = 350 px
OUTER_PLANET_SCALE_FACTOR = 0.6  # Outer Planets are 40% smaller
BASE_SIZE = 50  # Base size for planets in px

# Simulation Speed
TIMESTEP = 3600 * 24.0 # Seconds in 1 day 