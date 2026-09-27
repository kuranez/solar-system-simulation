# import constants
import config.display
import physics.constants

def render_menu_texts(
        screen, 
        font, 
        clock, 
        total_elapsed_time, 
        planet_data,
        steps_per_frame=1,
        min_steps=1,
        max_steps=64, 
        title="Solar System Simulation v.1.9.2"):
    """Render HUD overlays (FPS, elapsed time, controls, and planet table)."""

    # -------------------------------------------------------------
    # 1. Unified Layout Metrics (Grid & Margins)
    # -------------------------------------------------------------
    PADDING = config.display.PADDING        # Universal distance from screen edges
    ROW_HEIGHT = config.display.ROW_HEIGHT  # Height of each table row
    HEADER_GAP = config.display.HEADER_GAP  # Space between table header and first row
    TEXT_GAP = config.display.TEXT_GAP      # Spacing between multi-line headers
    text_color = config.display.COLOR_TEXT

    # -------------------------------------------------------------
    # 2. Top-Left: FPS Display
    # -------------------------------------------------------------
    fps_text = f"FPS: {int(clock.get_fps())}"
    fps_surf = font.render(fps_text, True, text_color)
    screen.blit(fps_surf, (PADDING, PADDING))

    # -------------------------------------------------------------
    # 3. Top-Right: Title, Simulation Speed & Time
    # -------------------------------------------------------------
    right_edge = screen.get_width() - PADDING
    top_y = PADDING

    # Title
    title_surf = font.render(title, True, text_color)   # Title surface
    title_x = right_edge - title_surf.get_width()       # Title X Position
    title_y = top_y                                     # Title Y Position
    screen.blit(title_surf, (title_x, title_y))         # Render Title
    top_y += title_surf.get_height() + TEXT_GAP         # Spacer

    # Simulation Speed Counter (Current / Min / Max)
    days_per_sec = (steps_per_frame * 86400 / 86400) * int(clock.get_fps() or 60)
    speed_text = f"Speed: {steps_per_frame}x [{min_steps} - {max_steps}] ({steps_per_frame} d/frame)"
    speed_surf = font.render(speed_text, True, text_color)
    speed_x = right_edge - speed_surf.get_width()
    speed_y = top_y
    screen.blit(speed_surf, (speed_x, speed_y))
    top_y += speed_surf.get_height() + TEXT_GAP
    
    # Formatted Elapsed Time
    # Convert seconds to years, days, hours, minutes, seconds
    years = int(total_elapsed_time // (365.25 * 24 * 3600))
    rem = total_elapsed_time % (365.25 * 24 * 3600)
    days = int(rem // (24 * 3600))
    rem = rem % (24 * 3600)
    hours = int(rem // 3600)
    rem = rem % 3600
    minutes = int(rem // 60)
    seconds = int(rem % 60)
    
    # Format time display
    if years > 0:
        time_text = f"Time: {years}y {days}d {hours}h {minutes}m"
    elif days > 0:
        time_text = f"Time: {days}d {hours}h {minutes}m"
    elif hours > 0:
        time_text = f"Time: {hours}h {minutes}m {seconds}s"
    else:
        time_text = f"Time: {minutes}m {seconds}s"
    
    time_surf = font.render(time_text, True, text_color)
    time_x = right_edge - time_surf.get_width()
    time_y = top_y
    screen.blit(time_surf, (time_x, time_y))
    # top_y += time_surf.get_height() + TEXT_GAP

    # -------------------------------------------------------------
    # 4. Bottom-Left: Navigation Table (Bottom-Aligned)
    # -------------------------------------------------------------

    # Displaying navigation table in the lower left corner
    nav_headers = ["Controls", "Action"]
    navigation_data = [
        ("Mouse Wheel", "Zoom In/Out"),
        ("[Left Click] + Drag", "Move View"),
        ("[+] / [-]", "Adjust Speed"),
        ("[F12]", "Take Screenshot"),
        ("[ESC]", "Quit Simulation"),
    ]

    # Define column widths for navigation table
    nav_col1_width = 150   # Controls column
    nav_col2_width = 120   # Action column

    # Caclulate exact table height to align bottom with PADDING
    nav_table_height = HEADER_GAP + len(navigation_data) * ROW_HEIGHT
    nav_start_y = screen.get_height() - PADDING - nav_table_height
    
    # Nav Headers
    nav_header1 = font.render(nav_headers[0], True, text_color)
    nav_header2 = font.render(nav_headers[1], True, text_color)

    nav_x1 = PADDING
    nav_x2 = PADDING + nav_col1_width

    nav_y = nav_start_y
    
    screen.blit(nav_header1, (nav_x1, nav_y))
    screen.blit(nav_header2, (nav_x2, nav_y))
    
    # Nav Rows
    for i, (control, action) in enumerate(navigation_data):
        # row_y = lower_left_y + 30 + i * 25  # 30px spacing after header, 25px between rows
        row_y = nav_start_y + HEADER_GAP + i * ROW_HEIGHT
        
        # Control column
        control_surf = font.render(control, True, text_color)
        screen.blit(control_surf, (PADDING, row_y))
        
        # Action column
        action_surf = font.render(action, True, config.display.COLOR_TEXT)
        screen.blit(action_surf, (PADDING + nav_col1_width, row_y))

    # -------------------------------------------------------------
    # 5. Bottom-Right: Planet Distance Table (Bottom-Aligned)
    # -------------------------------------------------------------
    table_headers = ["Planets", "Distance from the Sun", "Min / Max Distance", "Orbits"]

    # Define column widths for alignment
    col1_width = 80     # Planet names
    col2_width = 195    # Distance (km & AU)
    col3_width = 210    # Min / Max Distance
    col4_width = 55     # Orbits

    total_table_width = col1_width + col2_width + col3_width + col4_width

    # Column X coordinates anchored to screen right edge
    col1_x = screen.get_width() - PADDING - total_table_width
    col2_x = col1_x + col1_width
    col3_x = col2_x + col2_width
    col4_x = col3_x + col3_width

    # Bottom-align the planet table to end exactly at screen.get_height() - PADDING
    planet_table_height = HEADER_GAP + len(planet_data) * ROW_HEIGHT
    planet_start_y = screen.get_height() - PADDING - planet_table_height

    # 1. Render Planet Data Headers
    header1 = font.render(table_headers[0], True, text_color)
    header2 = font.render(table_headers[1], True, text_color)
    header3 = font.render(table_headers[2], True, text_color)
    header4 = font.render(table_headers[3], True, text_color)
    
    screen.blit(header1, (col1_x, planet_start_y))
    screen.blit(header2, (col2_x, planet_start_y))
    screen.blit(header3, (col3_x, planet_start_y))
    screen.blit(header4, (col4_x, planet_start_y))

    # 2. Render Planet Data Rows
    for i, (name, planet, color) in enumerate(planet_data):
        row_y = planet_start_y + HEADER_GAP + i * ROW_HEIGHT 
        
        # Col 1: Planet name
        name_surf = font.render(name, True, color)
        screen.blit(name_surf, (col1_x, row_y))
        
        # Col 2: Current Distance from Sun
        dist_km = int(round(planet.distance_to_sun / 1000))
        dist_au = planet.distance_to_sun / physics.constants.AU
        cur_dist_text = f"{dist_km:,} km ({dist_au:.2f} AU)"
        cur_dist_surf = font.render(cur_dist_text, True, color)
        screen.blit(cur_dist_surf, (col2_x, row_y))

        # Col 3: Dynamic Min / Max Distance
        if planet.min_distance and planet.max_distance:
            min_km = int(round(planet.min_distance / 1000))
            max_km = int(round(planet.max_distance / 1000))
            minmax_text = f"min: {min_km / 1e6:.1f} M | max: {max_km / 1e6:.1f}M km"
        else:
            minmax_text = "-"
        minmax_surf = font.render(minmax_text, True, color)
        screen.blit(minmax_surf, (col3_x, row_y))
        
        # Col 4: Orbit count
        orbit_text = f"{planet.orbit_count}"
        orbit_surface = font.render(orbit_text, True, color)
        screen.blit(orbit_surface, (col4_x, row_y))
