# render/renderer.py
import pygame
import config.display

def draw_orbit_trail(surface, body, scale, offset_x, offset_y):
    """Draw smooth, faded orbit trail"""
    # 
    if not body.orbit_recorder or len(body.orbit_recorder.points) < 2:
        return

    pts = body.orbit_recorder.points
    n_pts = len(pts)
    
    # Screen projection
    screen_pts = [
        (int(px * scale + offset_x), int(py * scale + offset_y))
        for px, py in pts
    ]

    bg_color = config.display.COLOR_BACKGROUND

    # Draw segments in larger chunks or fast lines
    for i in range(1, n_pts):
        fade = i / n_pts
        faded_color = (
            int(body.color[0] * fade + bg_color[0] * (1 - fade)),
            int(body.color[1] * fade + bg_color[1] * (1 - fade)),
            int(body.color[2] * fade + bg_color[2] * (1 - fade)),
        )
        pygame.draw.line(surface, faded_color, screen_pts[i - 1], screen_pts[i], 1)

def draw_body(surface, body, scale, offset_x, offset_y):
    """Project and draw celestial body and its orbit."""
    center_x = body.x * scale + offset_x
    center_y = body.y * scale + offset_y

    # Off-screen culling for minor asteroids
    if body.is_asteroid:
        if not (0 <= center_x <= config.display.WIDTH and 0 <= center_y <= config.display.HEIGHT):
            return
        
    # Draw trail first (behind planet)
    if body.orbit_recorder:
        draw_orbit_trail(surface, body, scale, offset_x, offset_y)

    # Draw body circle
    pygame.draw.circle(surface, body.color, (int(center_x), int(center_y)), max(1, int(body.radius)))
    
    # Draw revolution flash ring
    if body.orbit_recorder and body.orbit_recorder.flash_timer > 0:
        flash_intensity = body.orbit_recorder.flash_timer / body.orbit_recorder.flash_duration
        flash_radius = int(body.radius * (1.5 + flash_intensity))
        pygame.draw.circle(surface, (255, 255, 200), (int(center_x), int(center_y)), flash_radius, 2)