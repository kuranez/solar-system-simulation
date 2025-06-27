# Solar System Simulation v1.4 — Full Documentation

## Overview

This Python/Pygame project simulates the solar system using real astronomical data and Newtonian gravity. Version 1.4 introduces mouse wheel zoom, improved scaling, and a modular approach to planet sizes. Orbits and planet visuals can both scale with zoom. The code is structured for extensibility and clarity.

---

## File Structure

- `main.py` — Main simulation loop; handles events, scaling, rendering.
- `constants.py` — Physical constants, colors, planetary data.
- `solarsystem_sim.py` — Classes for Sun, Planet, and Body (physics, drawing).
- `solarsystem_scale.py` — Functions for planet size scaling and zoom calculations.
- `README.md` — Project overview and setup.

---

## Key Features (v1.4)

- Real orbits for all 8 classical planets using NASA data.
- Mouse wheel zoom that scales both orbits and planet visual radii.
- Adjustable simulation speed and screen navigation.
- Modular code: planet scaling and simulation logic are separated.
- Orbit trails with fade effect.
- Color-coded planets and display of distance to the sun.

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
  - **Mouse Wheel:** Adjusts zoom factor, which updates both orbit scale and planet radii.
  - **Arrow Keys/Mouse at Edge:** Pans the simulation view.
  - **Keyboard:** Adjusts simulation speed or exits.
- **Simulation:**
  - Updates positions via Newtonian gravity.
  - Scales orbits and planet visuals according to current zoom.
  - Draws orbit trails and planets.
  - Displays FPS, title, navigation help, and planet distances.

---

## Zoom and Scaling Logic

- **Orbits:** Always scale with current zoom.
- **Planet Sizes:** Scaled by both physical size and the current zoom factor.
- **Outer Planets:** Have an additional scaling factor to keep them visually manageable.

---

## Core Modules and Functions

### `constants.py`
- Physics constants, planet/sun data, and display colors.

### `solarsystem_sim.py`
- **Body:** Base class with physics and orbit trail logic.
- **Sun:** Inherits from Body, with special color and no trail.
- **Planet:** Inherits from Body, with unique color cycling and trail length.

### `solarsystem_scale.py`
- **scale_planet_size:** Returns pixel radius for a planet given its physical radius and the current zoom.
- **calculate_scaled_sizes:** Returns a mapping of planet names to their current display radii.

### `main.py`
- Handles all user input and events.
- Recalculates planet sizes and orbit scales on zoom.
- Draws all objects and renders UI elements.

---

## Extending or Modifying

- **Add new planets:** Update `constants.py`, `planets_data` in `main.py`, and optionally `solarsystem_scale.py` for custom scaling.
- **Customize scaling:** Edit scale formulas in `solarsystem_scale.py`.

---

## Roadmap

**Planned Features**

- Mouse control navigation
- Orbit drawing improvements
- Use of different planet distances from the sun and real value comparison
- Further visual and code optimizations
- **Web version:** Refactor rendering logic to support a JavaScript/Pyodide frontend.
- **Additional Objects:** Asteroid belt and transneptunian objects

---

## Known Limitations in v1.4

- Zooming is multiplicative and can become awkward at extreme levels.
- Some code redundancy in how planet radii are recalculated and applied.
- Multiple approaches for updating planet radii coexist; pick the one that works best for your setup.

---

## Example: Adding a New Planet

1. Add its data to `constants.py`.
2. Add it to `planets_data` in `main.py`.
3. Optionally, update scaling function if needed.

---

## Credits

**Based on Tech With Tim, zerot69, rastr-0 and NASA planetary data.**

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

---