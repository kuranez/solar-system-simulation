# Solar System Simulation — Documentation (v1.9)

## Overview

This Python/Pygame project simulates a 2D view of the Solar System using Newtonian gravity, real planetary data, and interactive camera controls. 

## Project Features

- Realistic orbits for the eight classical planets and Pluto
- Ephemeris-based startup state for better astronomical realism

- Orbit tracking with per-planet orbit counters
- Flash ring effect when an orbit completes
- Faded orbit trails with automatic trail cleanup

- Procedurally generated asteroid belt and kuiper belt objects.
- Major asteroids Ceres, Vesta, Pallas and Juno

- Screenshot capture with `F12`
- Mouse wheel zoom and left-click drag navigation
- Adjustable simulation speed with keyboard shortcuts

## Project History

**Version 1.8** added ephemeris-based initialization using JPL data through Skyfield, so the planets start from a more accurate real-world configuration instead of a purely synthetic initial layout. The documentation below now includes a module-by-module reference and a step-by-step breakdown of the simulation loop.

**Version 1.9** added more objects, including additional major asteroids, Pluto, and Charon. Pluto was added as a proper trans-Neptunian object (TNO), with its own orbit trail and HUD entry. The update also introduced additional randomly generated TNOs and improved orbit tracking and HUD organization.

**Version 1.9.1 – 1.9.3** refactored the former structure of the project into dedicated modules for specific tasks.

The new structure separates these responsibilities into five main areas:

- **`config` module:** Contains submodules for display settings (`config.display`), simulation settings (`config.simulation`), and the color palette (`config.color`).
- **`physics` module:** Contains physical constants such as the astronomical unit (AU) and gravitational constant (G) in the `physics.constants` submodule.
- **`objects` module:** Contains a general class for celestial bodies (`objects.body`) and a factory to create a solarsystem containing the sun, planets and minor bodies (`objects.factory).
- **`data` module:** Contains planetary and asteroid data, organized into dedicated submodules using a standardized keyed-dictionary format.
- **`render`module:** Drawing and display logic has been moved here into submodules for bodies (`render.renderer`) and the user interface (`renderer.hud`).

This refactoring makes the project structure more modular and keeps calculations, object creation, configuration, physical constants, and simulation data separated from each other. making the codebase more easy to maintain and scale. 

In previous versions the architecture followed this model:

- **`solarsystem_simulation`** handling bodies and calculations in a strict class hierarchy.
- **`solarsystem_scale`** for dynamic scaling of celestial bodies.
- **`solarsystem_creation`** delegating creation of objects.
- **`constants`** containing data and configuration.

Early version established the basic simulation logic, rendering and user interface.

What began as a simple tutorial project gradually grew into a comprehensive, independent application as new features were continuously added.

## File Layout

- `main.py` — startup, simulation loop, controls, rendering, and object creation
- `config/` — display settings, simulation settings, colors, scale factors
- `objects/` — body classes and factory
- `physics/` — physics calculations (gravity & orbits)
- `render/` — user interface and object rendering
- `data/` — planetary data
- `docs/` — documentation, schemes and changelog

**For more details see:** Folder Structure Diagram

## What Changed in v1.9 and v1.8

**v1.9.1-v1.9.3 — Refactor of legacy modules `solarsystem_sim.py`, `solarsystem_scale.py`, `solarsystem_creation.py` and `constants.py` into new functional modular architecture
- New module domains : Physics, Render, Objects, Data and Configuration.
- Substepping added for improved performance.
- New orbit drawing logic (angle-based instead of point-based).

**v1.9 — Pluto, Asteroid, HUD, and Orbit** Tracking Updates
- Added additional TNO and asteroid objects.
- Improved orbit counting using angular sweep tracking.
- Improved HUD layout and Pluto color consistency.

**v1.8 — Skyfield integration**
- Initial positions and velocities for planets are derived from JPL ephemerides via `skyfield`.
- `de440s.bsp` is used as the planetary data source for the startup state.
- The simulation now begins with more realistic relative placements and orbital directions.
- The existing zoom and UI work from v1.7 remains in place, with v1.8 focused on startup accuracy.


## Installation

Install dependencies in your Python environment:

```bash
python -m pip install -r requirements.txt
```

For ephemeris-based initialization, ensure these are available:

```bash
python -m pip install skyfield jplephem
```

Also make sure `de440s.bsp` is present in the project folder `./data/skyfield/`.

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

# Detailed Documentation
## Folder Structure Diagram

```text
solar-system-simulation/
│
├── config/				# Configuration modules
│   ├── __init__.py
│   ├── colors.py		# Color palette
│   ├── display.py		# Display and window settings
│   └── simulation.py	# Simulation settings (speed and scale)
│
├── data/				# Celestial body data
│   ├── __init__.py
|   ├── bodies/ 
│   |    ├── asteroids.py	# Asteroid data
│   |    ├── planets.py		# Planet data
│   |    ├── sun.py			# Sun data
│   |    └── tnos.py		# TNO data
|   |
|   └── skyfield/ 
|        └── de440s.bsp	    # Skyfield ephimeres data
│
├── objects/			# Celestial body class
│   ├── __init__.py
│   ├── body.py			# Base class for celestial bodies
│   └── factory.py		# Solar system creation factory
│
├── physics/				# Physics module
│   ├── __init__.py
│   ├── engine.py			# Gravity calculations & position updates
│   ├── orbits_tracker.py	# Orbit recording
│   ├── orbits.py			# Orbit calculations
│   └── constants.py		# Physics constants such as AU and G
│
├── render/					# Rendering
│   ├── __init__.py
│   ├── renderer.py			# Object drawing (Celestial bodies, orbits)
│   ├── scale.py			# Object scaling
│   └── hud.py				# Heads-up display (HUD)
│
├── docs/					# Documentation & Changelog
│   ├── architecture/
|   |    ├── (...)
│   |    └── ARCHITECTURE.md
|   |
|   ├── milestones/
|   |    ├── (...)
|   |    └── MILESTONES.md
|   |
|   ├── timeline/
|   |    ├── (...)
|   |    └── HISTORY.md
|   |
│   ├── CHANGELOG.md
│   └── DOCUMENTATION.md
│
└── main.py						# Main entry point

```

## Core Modules and Functions

### 1. `main.py`

- **Initialization**
	→ Pygame
	→ Display
	→ Simulation
- **Simplified Solar System Creation**
- **Main Loop**
	→ Key press event triggers
	→ Physics & Orbit Tracking
	→ Rendering HUD
	→ Display Update

**Fore a more detailed description jump to** How the Simulation works. 
### 2. `config/` - Configuration files

#### 2.1 `config.colors` – Celestial body color scheme

Configuration file for setting up and adjusting the simultation color scheme.

- Configuration file uses a dictionary format.
- **Input format is RGB.**

**Example**
```python
"Mercury":  (173, 168, 165)
```

#### 2.2 `config.scale`

→ upcoming v.1.9.3 Update

##### 2.2.1 Scale Factors

- **Default scale:  Astronomic units → pixel**

- Adjustable sun size
- Planet base display size 
- Outer planet scale factor
- Minor object scale factors

- Asteroid belt range for random generated objects
- Kuiper belt range for random generated objects

##### 2.2.2 Dynamic scaling helpers for zoom

- **`scale_planet_size(...)`**
	**Args**
	- planet_radius : float
	- scale : float
	- is_outer_planet : bool
	**Returns**
	- scale factor
	
- **`calculate_scaled_sizes(...)**
  **Args**
	- scale : float
	**Returns**
	- scaled sizes

#### 2.3 `config.simulation`

- Simulation speed and steps
	→ **Default: 1 day (in seconds)**

#### 2.4 `config.display`

- Display resolution (**Default 1080p**)
- Text color and background color
- Spacing for HUD

### 3. `data/` – Real-world planetary data from NASA

#### 3.1. Solar System Bodies (`./data/bodies/`)

##### 3.1.1 Sun (`data.bodies.sun`)
##### 3.1.2 Planets  (`data.bodies.planet`)
##### 3.1.3 Asteroids  (`data.bodies.asteroid`)
##### 3.1.4 Trans-Neptunian-Objects (TNOs)  (`data.bodies.tno`)

#### 3.2 Skyfield JPL ephimeres data (`./data/skyfield/)
### 4. `physics/` –   Gravity and Orbit Calculations (`physics.engine`)

#### 4.1  `physics.constants`

- **AU:** Astronomical Unit in meters
- **G:** Gravitational Constants in SI-Units
#### 4.2 `physics.engine`

- `calculate_gravity_force(...)
	- **Args**
	- body1
	- body2
	- g=G
	- **Calculation**
	- → **dist** Distance calculation
	- → **force** Gravitational force magnitude
	- → **theta** Angle in radians
	- → **fx, fy** Force components along x and y axes
	- **Returns**
	- fx
	- fy
	- dist
- `update_bodies_physics(...)
	- **Args**
	- major_bodies
	- minor_bodies
	- dt
	- sun: Boolean
	- **Calculation:**
	- add description
- `calculate_orbital_speed(...)`
	- **Args**
	- central_mass
	- distance
	- g=G
- `calculate_circular_orbit(...)` → Update circular to elliptical
	- add description
### 5. `objects`– Solar System Creation
#### 5.1 `objects.body`- Base class for celestial bodies

Body 
- name
- x
- y
- vx
- vy
- etc → ergänzen

Methods:
- orbit_count

→ add and refine description!
#### 5.2 `objects.factoy`- Solar system creation factory

- `create_solarsystem(...)
- `create_major_asteroids(...)`
- `create_asteroid_belt(...)`
- `create_Kuiper_belt(...)`
- `create_Pluto(...)`
### 6. `render/`–  Planet, Orbit and HUD display
#### 6.1 `render.renderer`
#### 6.2 `render.text`

→ upcoming v.1.9.3 Update
#### 6.3 `render.hud`

→ add description


## Roadmap / Planned Features

✅ **Completed Features**

- **Mouse control navigation** (Added in v1.5)
- **Orbit tracking and counters** (Added in v1.5)
- **Enhanced orbit drawing** (Added in v1.5)
- **Asteroid Belt** (Added in v1.6)
- **Asteroids Ceres and Vesta** (Added in v1.7)
- **Asteroids Juno and Pallas** (Added in v1.9)
- **Asteroids Hygea and Eros** (Added in v1.9.2) (Upcoming soon)
- **TNOs Pluto and Charon** (Added in v1.9 and v1.9.2)

⚙️ **In Progress**

- **Additional Objects:** Asteroids (Pallas, Juno) and transneptunian objects (Upcoming v1.9) -> Hygea and Eros to go, Charon to go
- **Web version:** Simplified web version using Panel library (Branched from v1.7)

💡 **Planned Features**

- Toggle to show/hide asteroid belt
- Toggle to show/hide views of inner and outer planets
- Toggle to show/hide asteroids and TNOs
- Kirkwood gaps to show Jupiter's resonance effects
- Use of different planet distances from the sun and real value comparison
- Options to start the simulation at a specific historical or future date.
- Further visual and code optimizations 

## Credits & Sources

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)


---

## Version History 

For detailed version-by-version notes, see `CHANGELOG.md` and the archived versions in [branch version-history](https://github.com/kuranez/solar-system-simulation/tree/version-history)
