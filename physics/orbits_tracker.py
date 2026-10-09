# physics.orbit_recorder- Module for keeping track of orbit points

from collections import deque
import math

class OrbitRecorder:
    def __init__(
            self, 
            max_points = 360, 
            angle_step_deg = 1.0):
        """
        Angle-based orbit recorder.
        :param max_points: Buffer size (360 points = 1 complete revolution).
        :param angle_step_deg: Store 1 point every N degrees (default: 1.0°).
        """
        self.points = deque(maxlen=max_points)
        self.angle_step = math.radians(angle_step_deg)  # 1° in rad

        self.last_angle = None

        self.angle_accumulator = 0.0     # Tracks progress toward the next 1° point
        self.orbit_sweep_total = 0.0      # Tracks progress toward full 360° revolution
        
        # Telemetry
        self.orbit_count = 0
        self.flash_timer = 0
        self.flash_duration = 10
        
    def update(self, x, y, sun_x = 0.0, sun_y = 0.0):
        """
        Calculates angle to the Sun, records a point every 1° of sweep,
        and counts full 360° revolutions.
        """
        current_angle = math.atan2(y - sun_y, x - sun_x)

        # First point initialization
        if self.last_angle is None:
            self.last_angle = current_angle
            self.points.append((x, y))
            return
        
       # 1. Calculate shortest angle delta [-pi, pi] across the wraparound
        delta = current_angle - self.last_angle
        if delta > math.pi:
            delta -= 2 * math.pi
        elif delta < -math.pi:
            delta += 2 * math.pi

        self.last_angle = current_angle
        abs_delta = abs(delta)
        
        # # Record a point whenever swept angle exceeds step
        # if abs(delta) >= self.angle_step:
        #     self.points.append((x, y))
        #     self.last_angle = current_angle

        # 2. Angle-based point sampling (every 1.0°)
        self.angle_accumulator += abs_delta
        if self.angle_accumulator >= self.angle_step:
            self.points.append((x, y))
            # Subtract step to keep fractional remainder for the next point
            self.angle_accumulator %= self.angle_step

        # 3. Full Orbit Revolution Tracking (360°)
        self.orbit_sweep_total += abs_delta
        if self.orbit_sweep_total >= (2 * math.pi):
            completed = int(self.orbit_sweep_total / (2 * math.pi))
            self.orbit_count += completed
            self.orbit_sweep_total %= (2 * math.pi)
            self.flash_timer = self.flash_duration

        if self.flash_timer > 0:
            self.flash_timer -= 1


    def clear(self):
        """Reset trail points."""
        self.points.clear()
        self.last_angle = None
        self.angle_accumulator = 0.0