# physics.engine - Gravity and Position calculations

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

    # Gravitational force magnitude: F = G * (m1 * m2) / r^2
    force = g * body1.mass * body2.mass / dist_sq

    # Angle between bodies in radians
    theta = math.atan2(dy, dx)

    # Force components along X and Y axes
    fx = math.cos(theta) * force
    fy = math.sin(theta) * force

    return fx, fy, dist

def update_bodies_physics(major_bodies, minor_bodies, dt, sun=None):
    """
    Optimized physics update using familiar trigonometry:
    - Major bodies (planets): N-body gravity ONLY with other major bodies.
    - Minor bodies (asteroids/TNOs): Fast 1-body gravity to the Sun.
    """
    # -------------------------------------------------------------
    # 1. Major Bodies (Planets & Pluto)
    # -------------------------------------------------------------
    for body in major_bodies:
        if body.is_sun:
            continue
        total_fx = 0.0
        total_fy = 0.0
        # Planets only pull/get pulled by other major bodies (Sun + planets)
        for other in major_bodies:
            if body is other:
                continue
            fx, fy, dist = compute_gravity_force(body, other)
            total_fx += fx
            total_fy += fy
            if other.is_sun:
                body.distance_to_sun = dist
        # Velocity and position integration (Euler step)
        body.vx += (total_fx / body.mass) * dt
        body.vy += (total_fy / body.mass) * dt
        body.x += body.vx * dt
        body.y += body.vy * dt
        # Distance telemetry (min/max tracking)
        if body.distance_to_sun > 0:
            if body.min_distance is None or body.distance_to_sun < body.min_distance:
                body.min_distance = body.distance_to_sun
            if body.max_distance is None or body.distance_to_sun > body.max_distance:
                body.max_distance = body.distance_to_sun
    # -------------------------------------------------------------
    # 2. Minor Bodies (Asteroids & TNOs)
    # -------------------------------------------------------------
    if sun:
        for asteroid in minor_bodies:
            # Asteroids only get pulled by the Sun (1-body central force)
            fx, fy, dist = compute_gravity_force(asteroid, sun)
            asteroid.vx += (fx / asteroid.mass) * dt
            asteroid.vy += (fy / asteroid.mass) * dt
            asteroid.x += asteroid.vx * dt
            asteroid.y += asteroid.vy * dt
            asteroid.distance_to_sun = dist