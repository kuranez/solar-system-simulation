# Solar System Simulation v1.4a — Full Documentation

## Overview

This project simulates the solar system in 2D using Python and Pygame. It models planetary motion using Newton's laws of gravity and real astronomical data. Version 1.4a introduces a refactored zoom system and a modular codebase for easier scaling, maintenance, and future enhancements.

---

## File Structure

- `main.py` — Main simulation loop, event handling, rendering.
- `constants.py` — Physical constants, colors, planetary data.
- `solarsystem_sim.py` — Classes for celestial bodies (Sun, Planet, Body base class).
- `solarsystem_scale.py` — Functions for planet size scaling and zoom calculations.
- `README.md` — Project overview and setup instructions.

---

## Key Features

- Realistic orbits for all 8 planets using NASA data.
- Scalable zoom: orbits scale on zoom, planet sizes recalculated (see below).
- Adjustable simulation speed and view navigation.
- Modular, extensible code structure.

---

## How the Simulation Works

### Initialization

- Loads constants (AU, G, planetary masses, initial positions, display parameters).
- Initializes Pygame and creates the main display surface.
- Calculates scaled planet sizes based on real diameters and a base pixel size.

### Solar System Creation

- Sun and planets are instantiated as objects:
  - Positions are set in astronomical units (AU) from the sun.
  - Each planet uses a size from `scaled_sizes` (calculated per zoom factor).
  - Initial velocities correspond to their real orbital velocities.

### Main Loop

- **Event Handling:**
  - **Mouse Wheel:** Zoom in/out by adjusting `zoom_factor` (affects orbit scaling and planet size calculation).
  - **Arrow Keys/Mouse:** Pan the view.
  - **Keyboard:** Adjust simulation speed or exit.
- **Simulation:**
  - Updates planetary positions using Newtonian gravity.
  - Orbits and positions are scaled by the current zoom factor.
  - Planet radii are recalculated and updated on zoom events.
  - Draws faded orbit trails and planets onto the surface.

---

## Zooming and Scaling Logic

- **Orbits:** Always scale with the current zoom (affects positions and orbit trails).
- **Planet Sizes:** Calculated by `calculate_scaled_sizes(zoom_factor)`. Must be reapplied to each planet after zoom changes.
- **Outer Planets:** Have a configurable size reduction factor.

---

## Core Modules and Functions

### `constants.py`
- Defines all display, physics, and planetary constants.
- Contains color definitions for each planet.

### `solarsystem_sim.py`
- **Body:** Base class for all celestial objects. Handles physics, orbit trails, and drawing.
- **Sun:** Inherits from `Body`. Custom color and no orbit trail by default.
- **Planet:** Inherits from `Body`. Handles unique color cycling, orbit trail length, and zoomable radius.

### `solarsystem_scale.py`
- **scale_planet_size:** Given a planet radius and current zoom, returns the display radius in pixels.
- **calculate_scaled_sizes:** Returns a dict mapping planet names to their display radii for a given zoom.

### `main.py`
- Handles all user input, event processing, and the main simulation/render loop.
- Creates the solar system and updates planet sizes on zoom.
- Renders FPS, title, navigation instructions, and planet distances.

---

## How to Extend or Modify

- To add new planets or objects: Extend `planets_data` in `main.py` and update `constants.py`.
- To improve scaling/zooming: Adjust functions in `solarsystem_scale.py` and ensure recalculation hooks are present in the main loop.
- For web or further optimization: Refactor draw/update logic for compatibility with other renderers (e.g., Pyodide/PyScript).

---

## Known Limitations in v1.4a

- **Planet sizes do not update visually on zoom unless `scaled_sizes` is recalculated and reapplied.**
- Orbits always scale with zoom correctly.
- See [GitHub Issue #14](https://github.com/kuranez/solar-system-simulation/issues/14) for tracking this bug.

---

## Example: Adding a New Planet

1. Add mass, radius, perihelion, and color to `constants.py`.
2. Add an entry to `planets_data` in `main.py`.
3. Add a scaling rule in `solarsystem_scale.py` if different from existing.

---

## Credits

- Inspired by Tech With Tim, zerot69, and NASA planetary data.

---