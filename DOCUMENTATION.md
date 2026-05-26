# Solar System Simulation — Documentation (v1.8)

## Overview

This Python/Pygame project simulates a 2D view of the Solar System using Newtonian gravity, real planetary data, and interactive camera controls. Version 1.8 adds ephemeris-based initialization using JPL data through Skyfield, so the planets start from a more accurate real-world configuration instead of a purely synthetic initial layout. The documentation below now includes a module-by-module reference and a step-by-step breakdown of the simulation loop.

The project is split into a small set of focused modules:

- `main.py` — program entry point, object creation, event loop, rendering, and UI
- `constants.py` — physical constants, colors, planetary data, asteroid metadata
- `solarsystem_sim.py` — body classes and physics behaviour
- `solarsystem_scale.py` — helpers that convert real sizes into pixel sizes
- `CHANGELOG.md` — release history

## What Changed in v1.8

- Initial positions and velocities for planets are derived from JPL ephemerides via `skyfield`.
- `de440s.bsp` is used as the planetary data source for the startup state.
- The simulation now begins with more realistic relative placements and orbital directions.
- The existing zoom and UI work from v1.7 remains in place, with v1.8 focused on startup accuracy.

## Features

- Realistic orbits for the eight classical planets
- Ephemeris-based startup state for better astronomical accuracy
- Mouse wheel zoom and left-click drag navigation
- Adjustable simulation speed with keyboard shortcuts
- Orbit tracking with per-planet orbit counters
- Flash ring effect when an orbit completes
- Faded orbit trails with automatic trail cleanup
- Procedurally generated asteroid belt
- Major asteroids Ceres and Vesta
- Screenshot capture with `F12`
- Frame-rate independent physics

## Installation

Install dependencies in your Python environment:

```bash
python -m pip install -r requirements.txt
```

For ephemeris-based initialization, ensure these are available:

```bash
python -m pip install skyfield jplephem
```

Also make sure `de440s.bsp` is present in the project root or in the path expected by `main.py`.

## Running

```bash
python main.py
```

## Controls

- Mouse wheel: zoom in/out
- Left click + drag: pan the view
- `+` / `-`: increase or decrease simulation speed
- `F12`: save a screenshot into `screenshots/`
- `ESC`: quit the simulation

## Core Modules and Functions

### `main.py`

This file ties everything together.

- `create_solarsystem()`
	- Loads the `de440s.bsp` ephemeris with Skyfield.
	- Reads the current time with `ts.now()`.
	- Maps each planet to the corresponding Skyfield body.
	- Converts positions from AU to meters and velocities from AU/day to m/s.
	- Creates `Sun` and `Planet` objects using those values.
- `create_major_asteroids()`
	- Creates Ceres and Vesta as individual major-asteroid bodies.
	- Places them at a random orbital angle around the Sun.
	- Sets velocities for roughly circular orbits.
- `create_asteroid_belt(num_asteroids=500)`
	- Generates lightweight asteroids between 2.2 AU and 3.2 AU.
	- Randomizes angle, size, and slight eccentricity.
	- Uses Sun-only gravity for performance.
- `render_menu_texts()`
	- Draws FPS, title, simulation time, controls, and planet data tables.

### `solarsystem_sim.py`

This module contains the physical object model.

- `Body`
	- `__init__()` stores position, radius, mass, velocity, and orbit data.
	- `attraction(other)` calculates Newtonian force components between two bodies.
	- `update_position(current_solarsystem)` sums gravitational forces and advances position.
	- `draw()` renders the body and its faded trail.
- `Sun(Body)`
	- Marks the central body as the Sun.
	- Reuses the base draw behaviour without orbit-specific logic.
- `Planet(Body)`
	- Adds orbit tracking state, orbit counters, and a flash timer.
	- `update_position()` extends the base physics update with orbit completion checks.
	- `_check_orbit_completion()` detects when a planet has returned close to its start point.
	- `draw()` renders the trail, the planet body, and the orbit-completion ring effect.
- `Asteroid(Body)`
	- Disables orbit trails.
	- `update_position()` only calculates gravity from the Sun for performance.
	- `draw()` culls off-screen asteroids so only visible ones are rendered.

### `solarsystem_scale.py`

- `scale_planet_size(planet_radius, scale, is_outer_planet=False)`
	- Converts a physical diameter into a pixel size.
	- Applies a smaller multiplier for outer planets to keep them visually manageable.
- `calculate_scaled_sizes(scale)`
	- Builds a dictionary of scaled pixel radii for every planet in `PLANETS_DATA`.

### `constants.py`

This module defines the simulation data rather than behavior.

- Display size and colors
- Physical constants such as `AU`, `G`, and `TIMESTEP`
- Sun properties
- Planet properties in `PLANETS_DATA`
- Major asteroid metadata for Ceres and Vesta

## How the Simulation Works

### 1. Startup and configuration

When `main.py` starts, it initializes Pygame, opens a fullscreen display, creates a font, and sets up a simulation clock. It also loads the current scale factor, the zoom speed, and the initial screen offsets used for panning.

### 2. Build the body list

`create_solarsystem()` creates the Sun and the eight planets. For each planet:

- The matching Skyfield body is looked up from `de440s.bsp`.
- The current ephemeris time is sampled.
- The 3D position is projected into the 2D simulation plane.
- The position is converted from AU into meters.
- The orbital velocity is converted from AU/day into meters/second.
- A `Planet` instance is created with the matching mass and scaled radius.

After that, `create_major_asteroids()` adds Ceres and Vesta, and `create_asteroid_belt()` adds a field of small asteroids.

### 3. Main loop timing

Each frame, the loop calls `clock.tick(FPS)` and clears the screen. The simulation time is advanced by `Body.TIMESTEP`, and the on-screen time display is converted into years, days, hours, minutes, and seconds.

### 4. Input handling

The event loop listens for:

- Mouse wheel input to zoom the view in and out
- Left mouse drag to pan the simulation window
- `+` and `-` to increase or decrease the timestep
- `F12` to save a screenshot
- `ESC` to exit cleanly

Zooming updates the scale factor, recalculates scaled planet sizes, and applies the new radii to the active bodies.

### 5. Physics update

Every body updates its position each frame:

- `Body.update_position()` calculates the gravitational force from every other body and updates velocity and position.
- `Planet.update_position()` uses the same base physics and then checks whether the planet has completed an orbit.
- `Asteroid.update_position()` only uses the Sun as the gravitational source to keep the belt inexpensive to simulate.

The orbit logic stores trail points, limits trail length, and detects a completed orbit when the planet returns close enough to its starting position after traveling far enough.

### 6. Rendering

After updating positions, each body draws itself.

- Bodies with trails render faded orbit lines.
- Planets render their body and, when an orbit is completed, a brief highlight ring.
- Asteroids render only when they are inside the visible screen area.

The HUD is then drawn on top, including the FPS counter, title, navigation help, and the planet table on the lower right.

### 7. Asteroid behaviour

The asteroid belt is intentionally simplified:

- Asteroids are lightweight and numerous.
- They orbit only under the Sun’s gravity.
- They do not keep trail history.
- Off-screen asteroids are skipped during rendering.

That keeps the simulation responsive even with hundreds of extra objects.

## Orbit Tracking Details

Planet orbit completion uses a distance-based check against the start of the current trail.

- A minimum trail length is required before orbit completion can be detected.
- A threshold near the starting point prevents false positives.
- An internal flag prevents the same orbit from being counted multiple times.
- When an orbit is completed, the trail is reset and the flash timer is activated.

## Scaling and Zoom

Planet size scaling is tied to zoom so the display remains readable as the user changes the view.

- Inner and outer planets use the same base sizing formula.
- Outer planets receive an extra scale reduction to keep them from dominating the screen.
- Zoom changes affect both orbital placement and visible planet size.

## File Layout

- `main.py` — startup, simulation loop, controls, rendering, and object creation
- `constants.py` — physical values, colors, and body data
- `solarsystem_sim.py` — body classes and physics
- `solarsystem_scale.py` — size scaling helpers
- `versions/` — historical snapshots for earlier releases
- `de440s.bsp` — ephemeris file used for startup state

## Extending the Project

- Add new bodies by extending `constants.py` and `main.py`.
- Add new behaviors in `solarsystem_sim.py` if they affect physics or rendering.
- Adjust visual sizing in `solarsystem_scale.py`.
- Mirror the architecture if you want to port the simulation to a web frontend.

## Troubleshooting & Notes

- If screenshots fail, check that `screenshots/` exists and is writable.
- If `de440s.bsp` is missing, ephemeris-based startup will not work as intended.
- If `skyfield` is unavailable, install the required dependencies before running the simulation.
- Very large zoom values can make the visual scale awkward; the defaults are tuned for normal use.

## Roadmap / Planned Features

- Additional named asteroids such as Pallas and Juno
- Kirkwood gap visualization
- Toggle controls for the asteroid belt
- Web-friendly rendering and alternate frontend targets

## Credits & Sources

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

## Contributing

Pull requests, bug reports, and feature requests are welcome!

---

For detailed version-by-version notes, see `CHANGELOG.md` and the archived versions in 
