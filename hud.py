import constants


def render_menu_texts(screen, font, clock, total_elapsed_time, planet_data, title="Solar System Simulation v.1.9"):
    """Render HUD overlays (FPS, elapsed time, controls, and planet table)."""
    # Displaying FPS in the upper left corner
    fps_text = "FPS: " + str(int(clock.get_fps()))
    fps_surface = font.render(fps_text, True, constants.COLOR_TEXT)
    screen.blit(fps_surface, (15, 15))

    # Displaying title in the upper right corner
    title_surface = font.render(title, True, constants.COLOR_TEXT)
    title_width, title_height = title_surface.get_size()
    upper_right_x = screen.get_width() - title_width - 15
    upper_right_y = 15
    screen.blit(title_surface, (upper_right_x, upper_right_y))
    
    # Convert seconds to years, days, hours, minutes, seconds
    years = int(total_elapsed_time // (365.25 * 24 * 3600))
    remaining_time = total_elapsed_time % (365.25 * 24 * 3600)
    days = int(remaining_time // (24 * 3600))
    remaining_time = remaining_time % (24 * 3600)
    hours = int(remaining_time // 3600)
    remaining_time = remaining_time % 3600
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    
    # Format time display
    if years > 0:
        time_text = f"Time: {years}y {days}d {hours}h {minutes}m"
    elif days > 0:
        time_text = f"Time: {days}d {hours}h {minutes}m"
    elif hours > 0:
        time_text = f"Time: {hours}h {minutes}m {seconds}s"
    else:
        time_text = f"Time: {minutes}m {seconds}s"
    
    time_surface = font.render(time_text, True, constants.COLOR_TEXT)
    time_width, time_height = time_surface.get_size()
    time_x = screen.get_width() - time_width - 15
    time_y = upper_right_y + title_height + 5  # 5px spacing below title
    screen.blit(time_surface, (time_x, time_y))

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
    nav_col1_width = 160   # Controls column
    nav_col2_width = 120   # Action column

    # Initial position for lower left corner navigation table
    lower_left_x = 15  # Left aligned
    lower_left_y = screen.get_height() - 160  # Fixed starting y position
    
    # Render navigation table headers
    nav_header1 = font.render(nav_headers[0], True, constants.COLOR_TEXT)
    nav_header2 = font.render(nav_headers[1], True, constants.COLOR_TEXT)
    
    screen.blit(nav_header1, (lower_left_x, lower_left_y))
    screen.blit(nav_header2, (lower_left_x + nav_col1_width, lower_left_y))
    
    # Render navigation data rows
    for i, (control, action) in enumerate(navigation_data):
        row_y = lower_left_y + 30 + i * 25  # 30px spacing after header, 25px between rows
        
        # Control column
        control_surface = font.render(control, True, constants.COLOR_TEXT)
        screen.blit(control_surface, (lower_left_x, row_y))
        
        # Action column
        action_surface = font.render(action, True, constants.COLOR_TEXT)
        screen.blit(action_surface, (lower_left_x + nav_col1_width, row_y))

    # Displaying planet information table in the lower right corner
    # Table headers
    table_headers = ["Planets", "Distance from the Sun", "Orbits"]

    # Define column widths for alignment
    col1_width = 80   # Planet names
    col2_width = 180  # Distance
    col3_width = 60   # Orbits

    # Render table headers
    starting_y = screen.get_height() - 240  # Fixed starting y position for the table
    header_y = starting_y
    
    # Column headers
    header1 = font.render(table_headers[0], True, constants.COLOR_TEXT)
    header2 = font.render(table_headers[1], True, constants.COLOR_TEXT)
    header3 = font.render(table_headers[2], True, constants.COLOR_TEXT)
    
    # Position headers from right edge
    right_edge = screen.get_width() - 15
    col3_x = right_edge - col3_width
    col2_x = col3_x - col2_width
    col1_x = col2_x - col1_width
    
    screen.blit(header1, (col1_x, header_y))
    screen.blit(header2, (col2_x, header_y))
    screen.blit(header3, (col3_x, header_y))

    # Render planet data rows
    for i, (name, planet, color) in enumerate(planet_data):
        row_y = header_y + 30 + i * 25  # 30px spacing after header, 25px between rows
        
        # Planet name
        name_surface = font.render(name, True, color)
        screen.blit(name_surface, (col1_x, row_y))
        
        # Distance from sun
        distance_text = f"{round(planet.distance_to_sun / 1000, 1)} km"
        distance_surface = font.render(distance_text, True, color)
        screen.blit(distance_surface, (col2_x, row_y))
        
        # Orbit count
        orbit_text = f"{planet.orbit_count}"
        orbit_surface = font.render(orbit_text, True, color)
        screen.blit(orbit_surface, (col3_x, row_y))
