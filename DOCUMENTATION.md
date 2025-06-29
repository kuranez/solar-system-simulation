# Solar System Simulation v1.5 — Full Documentation

## Overview

This Python/Pygame project simulates the solar system using real astronomical data and Newtonian gravity. Version 1.5 introduces interactive mouse navigation, orbit tracking, enhanced UI design, and professional visual feedback. The simulation now features mouse drag navigation, real-time orbit counters, improved trail rendering, and a comprehensive tabular interface. The code maintains its modular structure while adding sophisticated user interaction capabilities.

---

## File Structure

- `main.py` — Main simulation loop; handles events, scaling, rendering, and interactive controls.
- `constants.py` — Physical constants, colors, planetary data.
- `solarsystem_sim.py` — Enhanced classes for Sun, Planet, and Body with orbit tracking and visual effects.
- `solarsystem_scale.py` — Functions for planet size scaling and zoom calculations.
- `README.md` — Project overview and setup.
- `CHANGELOG.md` — Detailed version history and changes.

---

## Key Features (v1.5)

- **Interactive Navigation:** Mouse wheel zoom and left-click drag to pan the view.
- **Orbit Tracking System:** Real-time orbit counters for each planet with completion indicators.
- **Enhanced Visual Feedback:** Flash ring effects when planets complete orbits.
- **Professional UI Design:** Tabular layout for controls and planet information.
- **Time Tracking:** Real-time display of simulated time in years/days/hours/minutes/seconds.
- **Screenshot Functionality:** Built-in F12 screenshot capture with timestamps.
- **Improved Orbit Trails:** Single orbit trail per planet with smooth fade effects and memory management.
- **Real Astronomical Data:** Accurate orbits for all 8 classical planets using NASA data.
- **Responsive Scaling:** Both orbits and planet visual radii scale with zoom level.
- **Adjustable Speed:** Keyboard controls for simulation time step adjustment.
- **Modular Architecture:** Clean separation of concerns for easy extension and maintenance.

---

## How the Simulation Works

### Initialization

- Loads constants (e.g., AU, G, planetary properties).
- Initializes Pygame and the display window.
- Calculates scaled planet sizes for the current zoom.

### Solar System Creation

- Instantiates Sun and planets with:
  - Positions in AU from the Sun.
  - Scaled radii (pixels) from `solarsystem_scale.py`.
  - Realistic masses, velocities, and colors.

### Main Loop

- **Event Handling:**
  - **Mouse Wheel:** Adjusts zoom factor, updating both orbit scale and planet radii.
  - **Mouse Drag:** Left-click and drag to pan the simulation view around the solar system.
  - **Keyboard Controls:** 
    - `[+] / [-]` — Adjusts simulation speed (time step).
    - `[F12]` — Captures screenshot with timestamp.
    - `[ESC]` — Exits the simulation.
- **Simulation Updates:**
  - Updates planetary positions via Newtonian gravity calculations.
  - Tracks orbit completion and increments orbit counters.
  - Manages orbit trail rendering with fade effects and memory optimization.
  - Scales orbits and planet visuals according to current zoom level.
- **Rendering:**
  - Draws orbit trails with distance-based and orbit-count-based fading.
  - Renders planets with flash effects for orbit completions.
  - Displays comprehensive UI with FPS, time elapsed, controls table, and planet data table.
  - Updates real-time information including distances and orbit counts.

---

## Zoom and Scaling Logic

- **Orbits:** Always scale with current zoom factor for consistent relative positioning.
- **Planet Sizes:** Dynamically scaled by both physical size and the current zoom factor.
- **Outer Planets:** Have additional scaling factors to maintain visual clarity at all zoom levels.
- **UI Elements:** Maintain consistent size and positioning regardless of zoom level.
- **Orbit Trails:** Trail rendering adapts to zoom while maintaining visual coherence.

---

## New in v1.5: Interactive Features

### Mouse Navigation
- **Drag to Pan:** Left-click and drag to move the view around the solar system.
- **Zoom:** Mouse wheel to zoom in/out while maintaining planet scaling.
- **Responsive Controls:** Smooth, immediate response to user input.

### Orbit Tracking System
- **Orbit Counters:** Each planet tracks completed orbits with robust detection.
- **Visual Indicators:** Flash ring effect when planets complete orbits.
- **Trail Management:** Only current orbit trail is displayed, clearing on completion.
- **Memory Optimization:** Automatic cleanup of old trail data.

### Enhanced User Interface
- **Tabular Layout:** Professional organization of controls and planet information.
- **Real-time Data:** Live updates of planet distances and orbit counts.
- **Time Display:** Simulation time in user-friendly years/days/hours/minutes format.
- **Screenshot System:** F12 key saves timestamped screenshots to `screenshots/` directory.

---

## Core Modules and Functions

### `constants.py`
- Physics constants, planet/sun data, and display colors.

### `solarsystem_sim.py`
- **Body:** Base class with enhanced physics, orbit trail logic, and interaction handling.
- **Sun:** Inherits from Body, with special rendering and no trail generation.
- **Planet:** Enhanced with orbit tracking, flash effects, trail management, and completion detection.
  - `orbit_count` — Tracks completed orbits with robust angle-based detection.
  - `flash_timer` — Manages visual feedback for orbit completions.
  - `trail_points` — Optimized trail rendering with automatic cleanup.
  - Advanced fade effects combining distance-based and orbit-count-based algorithms.

### `solarsystem_scale.py`
- **scale_planet_size:** Returns pixel radius for a planet given its physical radius and the current zoom.
- **calculate_scaled_sizes:** Returns a mapping of planet names to their current display radii.

### `main.py`
- **Enhanced Event Handling:** Mouse drag navigation and comprehensive keyboard controls.
- **UI Rendering:** Professional tabular layouts with `render_menu_texts()` function.
- **Time Tracking:** Real-time simulation time calculation and display.
- **Screenshot System:** Integrated F12 screenshot functionality with timestamp naming.
- **Drag State Management:** Smooth mouse drag implementation with proper state tracking.
- **Dynamic Updates:** Real-time recalculation of planet sizes and orbit scales on zoom.

---

## Controls Reference

| Control | Action |
|---------|--------|
| **Mouse Wheel** | Zoom In/Out |
| **Left Click + Drag** | Move View |
| **[+] / [-]** | Adjust Speed |
| **[F12]** | Take Screenshot |
| **[ESC]** | Quit Simulation |

---

## Extending or Modifying

- **Add new planets:** Update `constants.py`, `planets_data` in `main.py`, and optionally `solarsystem_scale.py` for custom scaling.
- **Customize scaling:** Edit scale formulas in `solarsystem_scale.py`.
- **Enhance UI:** Modify `render_menu_texts()` in `main.py` for additional information displays.
- **Add new controls:** Extend the event handling section in the main loop.
- **Customize orbit tracking:** Modify orbit detection logic in the Planet class `update_position()` method.

---

## Roadmap

**Completed in v1.5**
- ✅ **Mouse control navigation** — Left-click drag and mouse wheel zoom
- ✅ **Orbit tracking and counters** — Real-time orbit completion detection
- ✅ **Enhanced orbit drawing** — Single trail with fade effects and memory management
- ✅ **Professional UI design** — Tabular layouts and comprehensive information display

**Planned Features**
- Use of different planet distances from the sun and real value comparison
- Further visual and code optimizations
- **Web version:** Refactor rendering logic to support a JavaScript/Pyodide frontend.
- **Additional Objects:** Asteroid belt and transneptunian objects
- **Advanced Controls:** Pause/play functionality and time step presets
- **Enhanced Visuals:** Particle effects and improved planet textures

---

## Known Limitations in v1.5

- Zooming is multiplicative and can become awkward at extreme levels.
- Screenshot functionality requires the `screenshots/` directory to exist.
- Orbit completion detection may occasionally miss very fast orbits at high simulation speeds.
- Performance may degrade slightly with very long simulation runs due to time tracking overhead.

---

## Technical Implementation Details

### Orbit Tracking Algorithm
- Uses angle-based detection with proper handling of the first orbit
- Robust detection prevents false positives from orbital perturbations
- Memory efficient with automatic cleanup of completed orbit data

### UI Rendering System
- Tabular layouts with precise column alignment
- Real-time updates without performance impact
- Responsive design that adapts to different screen sizes

### Mouse Drag Implementation
- Smooth panning with proper state management
- Immediate visual feedback and responsive controls
- Coordinate system handling for accurate view positioning

---

## Example: Adding a New Planet

1. **Add planetary data** to `constants.py`:
   ```python
   new_planet_mass = 1.234e24  # kg
   new_planet_velocity = 15000  # m/s
   COLOR_NEW_PLANET = (255, 100, 50)  # RGB
   ```

2. **Add to planets_data** in `main.py`:
   ```python
   {"name": "NewPlanet", 
    "position": -2.5 * Planet.AU, 
    "scaled_size": scaled_sizes["NewPlanet"], 
    "mass": constants.new_planet_mass, 
    "is_inner": True, 
    "velocity": constants.new_planet_velocity}
   ```

3. **Update scaling function** in `solarsystem_scale.py` if custom scaling is needed.

4. **Add color mapping** for UI display in `main.py` planet_data list.

---

## Credits

**Based on Tech With Tim, zerot69, rastr-0 and NASA planetary data.**

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

---