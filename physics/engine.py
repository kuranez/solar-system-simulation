# physics/engine.py
import math
from physics.constants import G

def compute_gravity_force(body1, body2, g=G):
    """Compute gravitational force vector exerted on body1 by body2."""
    dx = body2.x - body1.x
    dy = body2.y - body1.y
    dist_sq = dx * dx + dy * dy
    dist= math.sqrt(dist_sq)
    
    if dist == 0:
        return 0.0, 0.0, 0.0
    
    force = g * body1.mass * body2.mass / dist_sq
    theta = math.atan2(dy, dx)

    return math.cos(theta) * force, math.sin(theta) * force, dist

def update_bodies_physics(bodies, dt, sun=None):
    """
    Unified physics update:
    - Major bodies (planets): full N-body or Sun-centered gravity
    - Minor bodies (asteroids): fast Sun-only attraction
    """
    # for old bodies
    # for body in bodies:
    #    if getattr(body, "is_sun", False):
    #        continue

    for body in bodies:
        if body.is_sun:
            continue

        total_fx, total_fy = 0.0, 0.0

        # 1. Compute gravitational forces

        # for old bodies
        # if getattr(body, "is_asteroid", False) and sun:

        if body.is_asteroid and sun:
            # Fast 1-body gravitation for asteroids
            fx, fy, dist = compute_gravity_force(body, sun)
            total_fx += fx
            total_fy += fy
            body.distance_to_sun = dist
        else:
            # Full N-body gravity for planets
            for other in bodies:
                if body is other:
                    continue
                fx, fy, dist = compute_gravity_force(body, other)
                total_fx += fx
                total_fy += fy
                if other.is_sun:
                    body.distance_to_sun = dist

        # 2. Integrate velocity & position (Euler step)
        body.vx += (total_fx / body.mass) * dt
        body.vy += (total_fy / body.mass) * dt
        body.x += body.vx * dt
        body.y += body.vy * dt

        # for old bodies
        # if getattr(body, "has_trail", False):
        #     body.orbit.append((body.x, body.y))
        #     if len(body.orbit) > 20000:
        #         body.orbit.pop(0)

        # 3. Dynamically track min & max distances
        if body.distance_to_sun > 0:
            if body.min_distance is None or body.distance_to_sun < body.min_distance:
                body.min_distance = body.distance_to_sun
            if body.max_distance is None or body.distance_to_sun > body.max_distance:
                body.max_distance = body.distance_to_sun

        # Update orbit data if enabled
        # if body.orbit_tracker:
        #     body.orbit_tracker.record_position(body.x, body.y)
        #     if sun:
        #         body.orbit_tracker.update_orbit_count(body.x, body.y, sun.x, sun.y)
        if body.orbit_recorder and sun:
            body.orbit_recorder.update(body.x, body.y, sun.x, sun.y)