# objects.body - Celestial body class

from physics.orbits_tracker import OrbitRecorder

class Body:
    def __init__(self, 
                 name:      str, 
                 x:         float, 
                 y:         float, 
                 vx:        float, 
                 vy:        float, 
                 mass:      float, 
                 radius:    float, 
                 color:     tuple[int, int, int], 
                 is_sun:        bool = False, 
                 is_asteroid:   bool = False, 
                 has_trail:     bool = True, 
                 track_orbit:   bool = False,
                 diameter:      float = None,
                 perihelion:    float = None,
                 aphelion:      float = None):
        # Physical state
        self.name = name
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.diameter = diameter
        self.radius = radius
        self.is_sun = is_sun
        self.is_asteroid = is_asteroid
        
        # HUD & Orbital Telemetry
        self.color = color
        self.has_trail = has_trail
        self.orbit = []

        # Distance Telemetry
        self.distance_to_sun = 0.0
        self.perihelion = perihelion
        self.aphelion = aphelion
        self.min_distance = None # Dynamically tracked perihelion
        self.max_distance = None # Dynamically tracked aphelion


        # Orbit Recorder
        self.orbit_recorder = OrbitRecorder(max_points=360) if track_orbit else None

    # Orbit counter
    @property
    def orbit_count(self) -> int:
        """Convenience property for HUD display."""
        return self.orbit_recorder.orbit_count if self.orbit_recorder else 0