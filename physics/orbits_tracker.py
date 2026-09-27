# physics.orbit_tracker - Module for keeping track of orbit points

from collections import deque
import math

# class OrbitTracker:
#     def __init__(self, max_points=1000, min_distance_step=1e9): # Performance mode: Try 600 max points, 2e9 step
#         """
#         :param max_points: Max points in trail (1000 is plenty for a smooth trail).
#         :param min_distance_step: Minimum distance (meters) body must move before recording a new point.
#         """
#         # deque(maxlen=...) automatically drops the oldest item in O(1) time
#         self.points = deque(maxlen = max_points)
#         self.min_distance_sq = min_distance_step ** 2
        
#         # Orbit revolution tracking
#         self.orbit_count = 0
#         self.previous_angle = None
#         self.accumulated_angle = 0.0
#         self.flash_timer = 0
#         self.flash_duration = 10

#     def record_position(self, x, y):
#         """Only stores points if the body has moved a minimum distance (subsampling)."""
#         if not self.points:
#             self.points.append((x, y))
#             return

#         last_x, last_y = self.points[-1]
#         dist_sq = (x - last_x) ** 2 + (y - last_y) ** 2
        
#         # Subsampling: only add if moved sufficiently
#         if dist_sq >= self.min_distance_sq:
#             self.points.append((x, y))

#     def update_orbit_count(self, x, y, sun_x=0.0, sun_y=0.0):
#         """Track completed revolutions around the central body."""
#         current_angle = math.atan2(y - sun_y, x - sun_x)
        
#         if self.previous_angle is None:
#             self.previous_angle = current_angle
#             return

#         delta = current_angle - self.previous_angle
#         if delta > math.pi:
#             delta -= 2 * math.pi
#         elif delta < -math.pi:
#             delta += 2 * math.pi

#         self.accumulated_angle += delta
#         completed = int(abs(self.accumulated_angle) / (2 * math.pi))

#         if completed > 0:
#             self.orbit_count += completed
#             self.accumulated_angle = math.fmod(self.accumulated_angle, 2 * math.pi)
#             self.flash_timer = self.flash_duration
            
#         self.previous_angle = current_angle

#         if self.flash_timer > 0:
#             self.flash_timer -= 1


class OrbitRecorder:
    def __init__(self, 
                 max_points = 360, 
                 angle_step = math.radians(1.0)):
        """
        Records orbit points based on angular sweep (e.g. 1 point every ~1 degree).
        :param max_points: Maximum points to hold for the trail (360 is exactly one full revolution).
        :param angle_step: Angular threshold in radians before recording the next point.
        """
        self.points = deque(maxlen=max_points)
        self.angle_step = angle_step
        self.last_angle = None
        self.accumulated_angle = 0.0
        
        # Telemetry
        self.orbit_count = 0
        self.flash_timer = 0
        self.flash_duration = 10
        
    def update(self, x, y, sun_x=0.0, sun_y=0.0):
        """Called after physics integration to record points and count revolutions."""
        current_angle = math.atan2(y - sun_y, x - sun_x)
        if self.last_angle is None:
            self.last_angle = current_angle
            self.points.append((x, y))
            return
        # Calculate shortest angular delta [-pi, pi]
        delta = current_angle - self.last_angle
        if delta > math.pi:
            delta -= 2 * math.pi
        elif delta < -math.pi:
            delta += 2 * math.pi
        # Record a point whenever swept angle exceeds step
        if abs(delta) >= self.angle_step:
            self.points.append((x, y))
            self.last_angle = current_angle
        # Orbit revolution tracking
        self.accumulated_angle += delta
        completed = int(abs(self.accumulated_angle) / (2 * math.pi))
        if completed > 0:
            self.orbit_count += completed
            self.accumulated_angle = math.fmod(self.accumulated_angle, 2 * math.pi)
            self.flash_timer = self.flash_duration
        if self.flash_timer > 0:
            self.flash_timer -= 1