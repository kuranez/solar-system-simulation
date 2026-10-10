# Solar System Simulation — Documentation (v1.9.3)

## Overview

This Python/Pygame project simulates a 2D view of the Solar System using Newtonian gravity, real planetary data from NASA and JPL ephemerides, and interactive camera controls.

---

## Project Features

- **Realistic Celestial Physics:** Realistic orbits for the eight classical planets and Pluto calculated via Newtonian gravitational mechanics.
- **Ephemeris-Based Startup:** Initial planetary positions and velocities derived directly from JPL DE440s ephemerides via `skyfield`.
- **Dynamic Orbit Tracking:** Angle-based revolution tracking with per-planet completed orbit counters and telemetry.
- **Visual Feedback:** Orbit trails with smooth distance-based fading and expanding flash-ring indicators on orbital completion.
- **Minor Celestial Bodies:** Procedurally generated Asteroid Belt and Kuiper Belt (Trans-Neptunian Objects / TNOs) alongside major asteroids (Ceres, Vesta, Pallas, Juno).
- **Interactive Controls:** Smooth mouse wheel zooming, left-click drag panning, and real-time simulation speed adjustments.
- **Heads-Up Display (HUD):** Comprehensive telemetry tables showing real-time distances (km and AU), dynamic min/max distances (perihelion/aphelion), orbit counters, simulation speed, and framerate.
- **Media Capture:** High-resolution screenshot capture with `F12`.

---

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

---
## File Layout

- `main.py` — startup, simulation loop, controls, rendering, and object creation
- `config/` — display settings, simulation settings, colors, scale factors
- `objects/` — body classes and factory
- `physics/` — physics calculations (gravity & orbits)
- `render/` — user interface and object rendering
- `data/` — planetary data
- `docs/` — documentation, schemes and changelog

**For more details see:** [[#Folder Structure Diagram|Folder Structure Diagram]]

---
## What Changed in v1.9 and v1.8

**v1.9.1-v1.9.3 — Refactor of legacy modules `solarsystem_sim.py`, `solarsystem_scale.py`, `solarsystem_creation.py` and `constants.py` into new functional modular architecture**
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

---

## Installation

1. Clone the repository and install required dependencies:

```bash
python -m pip install -r requirements.txt
```

2. For ephemeris-based initialization, verify that `skyfield` and `jplephem` are installed:

```bash
python -m pip install skyfield jplephem
```

3. Ensure the JPL ephemeris file `de440s.bsp` is present in the project root directory.

---

## Running

Launch the simulation from the terminal:

```bash
python main.py
```

---

## Controls

| Control | Action |
| :--- | :--- |
| **Mouse Wheel** | Zoom in / Zoom out (adjusts position scale and visual radii) |
| **Left Click + Drag** | Pan camera view across the orbital plane |
| **`+` / `=` / `NumPad +`** | Increase simulation speed (increases physics substeps per frame, up to 64x) |
| **`-` / `NumPad -`** | Decrease simulation speed (decreases physics substeps per frame, down to 1x) |
| **`F12`** | Capture and save a screenshot to `screenshots/` |
| **`ESC`** | Cleanly exit the simulation |

---
## Extending the Project

- ~~Add new bodies by extending `constants.py` and `main.py`.~~
- ~~Add new behaviors in `solarsystem_sim.py` if they affect physics or rendering.~~
- ~~Adjust visual sizing in `solarsystem_scale.py`.~~
- Mirror the architecture if you want to port the simulation to a web frontend.

## Troubleshooting & Notes

- **Screenshot Directory:** Ensure a `screenshots/` folder exists and is writable if capturing screenshots with `F12`.
- **Ephemeris Data:** If `de440s.bsp` is missing from the working directory, Skyfield will attempt to download it automatically upon first run.
- **Zoom Boundaries:** Scale factor is clamped between $0.05 \times$ and $10 \times$ of `DEFAULT_SCALE` to ensure visual stability.

---

## How the Simulation Works

### 1. Startup and Configuration

When `main.py` starts, it initializes Pygame and imports settings from the dedicated configuration modules:
- Display configuration (`config.display`) for window dimensions, fullscreen mode, colors, and HUD spacing.
- Simulation parameters (`config.simulation`) for default timestep, substepping, and speed settings.
- Scale factors (`config.scale`) and color schemes (`config.colors`).

### 2. Build the Body List

Celestial object creation is delegated to `objects.factory`:
- **Sun & Classical Planets:** `create_solarsystem()` initializes the Sun at the coordinate origin and loads JPL DE440s ephemerides via `skyfield` for the current timestamp (`ts.now()`). Positions (AU) and velocities (AU/day) are projected onto the 2D orbital plane and converted to SI units ($\text{m}$ and $\text{m/s}$).
- **Major Asteroids:** `create_major_asteroids()` generates Ceres, Vesta, Pallas, and Juno based on `data.asteroids.ASTEROID_DATA`.
- **Procedural Belts:** `create_asteroid_belt(500)` and `create_Kuiper_belt(100)` generate randomized minor bodies within specific AU boundaries.
- **Pluto:** `create_pluto()` generates Pluto as a tracked Trans-Neptunian Object using `data.tnos.TNO_DATA`.
- **Optimization Partitioning:** Bodies are partitioned into `major_bodies` (Sun, planets, major asteroids, Pluto) and `minor_bodies` (procedural asteroids and TNOs).

### 3. Main Loop Timing

The main loop in `main.py` is regulated at 60 FPS using Pygame's clock:
- `clock.tick(FPS)` enforces the frame rate and returns delta time.
- `DISPLAYSURF.fill(config.display.COLOR_BACKGROUND)` clears the framebuffer each frame.
- **Substepping Architecture:** To maintain numerical orbital stability at high speeds without orbital derailing, simulation speed is controlled by `steps_per_frame` (ranging from $1\times$ to $64\times$).
- In each frame, the physics engine runs `steps_per_frame` integration sub-cycles, each advancing the simulation clock by `BASE_TIMESTEP` ($86,400\text{ s} = 1\text{ day}$).
- `total_elapsed_time` increments by `BASE_TIMESTEP` on every substep and is converted by the HUD into formatted years, days, hours, minutes, and seconds.

### 4. Input Handling

Pygame's event queue handles user interaction:
- **Mouse Wheel (`pygame.MOUSEWHEEL`):** Adjusts `scale` by $\pm 10\%$, clamps within valid bounds ($0.05\times - 10\times$), and recalculates scaled visual radii for all planets using `calculate_scaled_sizes(scale)`.
- **Mouse Drag (`pygame.MOUSEBUTTONDOWN`, `MOUSEBUTTONUP`, `MOUSEMOTION`):** Tracks left-click dragging and updates `screen_offset_x` and `screen_offset_y` to pan the viewport.
- **Speed Keys (`+` / `-`):** Increments or decrements `steps_per_frame` between $1$ and $64$.
- **Hotkeys:** `F12` saves timestamped PNG screenshots to `screenshots/`; `ESC` exits the application.

### 5. Physics Update (Main Loop Integration)

Inside the main loop, physics integration executes across `steps_per_frame` substeps:

```python
for _ in range(steps_per_frame):
    update_bodies_physics(major_bodies, minor_bodies, BASE_TIMESTEP, sun=sun)
    total_elapsed_time += BASE_TIMESTEP
```

Key mechanics in `physics.engine`:
- **Gravitational Force Calculation:** Pairwise gravitational force is calculated via Newton's Universal Law of Gravitation:
  $$F = G \frac{m_1 m_2}{r^2}$$
  Force components $F_x = F \cos(\theta)$ and $F_y = F \sin(\theta)$ are resolved using $\theta = \text{atan2}(\Delta y, \Delta x)$.
- **$N$-Body Major Body Interaction:** Full mutual gravitational attraction is calculated between all major celestial bodies. Velocities and positions are updated using semi-implicit Euler integration:
  $$v \leftarrow v + \frac{\sum F}{m} \Delta t, \quad x \leftarrow x + v \Delta t$$
- **$1$-Body Central Force for Minor Bodies:** Procedural asteroids and TNOs compute gravitational attraction solely toward the Sun, reducing algorithmic complexity from $O(N^2)$ to $O(N)$.
- **Dynamic Telemetry:** Planetary distances to the Sun are tracked in real-time, updating dynamic minimum (`min_distance`) and maximum (`max_distance`) recorded distances.
- **Orbit Recording:** Immediately following the physics substepping loop, `OrbitRecorder.update(body.x, body.y, sun.x, sun.y)` is invoked for all major bodies to record trail points and track orbital revolutions.

####  Physics Changes from previous versions

Physics calculations are decoupled from the body instances and handled centrally by `physics.engine`:

- **`update_bodies_physics()`** computes gravitational forces using Newton's law of universal gravitation ($G \cdot \frac{m_1 m_2}{r^2}$).
- **N-body interaction:** Full mutual gravitational interactions are computed between all major celestial bodies.
- **Sun-only gravity optimization:** Minor bodies (asteroids and TNOs) only compute gravitational attraction towards the Sun, drastically reducing computational overhead ($O(N)$ instead of $O(N^2)$).
- **Substepping:** The frame timestep ($\Delta t$) is split into smaller substeps to prevent planetary orbits from destabilizing or derailing at high simulation speeds.
- **Orbit tracking:** Position updates feed into `physics.orbits_tracker`, which tracks orbital sweeps and detects completed revolutions.

### 6. Rendering (Main Loop Integration)

Rendering executes once per frame following the physics updates:
1. **Screen Center Projection:** Viewport center coordinates are calculated incorporating panning offsets:
   $$\text{screen\_cx} = \frac{\text{WIDTH}}{2} + \text{screen\_offset\_x}, \quad \text{screen\_cy} = \frac{\text{HEIGHT}}{2} + \text{screen\_offset\_y}$$
2. **Body and Trail Rendering (`render.renderer.draw_body`):**
   - **Viewport Culling:** Off-screen minor bodies are skipped before drawing to maintain high rendering performance.
   - **Faded Orbit Trails (`draw_orbit_trail`):** Orbit history points stored in the body's `OrbitRecorder` deque are transformed to screen space and rendered as fading dots with distance-weighted alpha blending.
   - **Body Sphere:** Drawn with `pygame.draw.circle` using the body's color and dynamically scaled radius.
   - **Revolution Flash Effect:** When an orbit completes, an expanding glowing ring (`(255, 255, 200)`) is drawn around the planet for the duration of `flash_timer`.
3. **HUD Rendering (`render.hud.render_menu_texts`):**
   - Renders top-left FPS counter, top-right simulation speed and elapsed time, bottom-left navigation controls, and bottom-right planetary telemetry table.
4. **Buffer Display:** `pygame.display.update()` flips the display buffer.

#### Render changes from previous versions

- **`render.renderer`- module**:
	  - Renders orbit paths and faded trail histories based on recorded positions.
	  - Draws celestial bodies using dynamically scaled radii.
	  - Triggers visual completion effects (such as the flash ring indicator when an orbit is completed).
	  - Skips off-screen minor bodies (viewport culling) to sustain performance.
- **`render.hud`- module`**:
	-  Overlays the heads-up display, rendering the framerate counter, elapsed simulation time, navigation controls, and the planet statistics table.
	- `main.py` concludes each cycle by flipping the display buffer (`pygame.display.flip()`).

### 7. Asteroid Behaviour

The asteroid belt is intentionally simplified:

- Asteroids are lightweight and numerous.
- They orbit only under the Sun’s gravity. 
- They do not keep trail history.
- Off-screen asteroids are skipped during rendering.

#### Asteroid simulation in detail
The asteroid belt is simulated with high-performance approximations:

- **Distribution:** Asteroids are generated between $2.2\text{ AU}$ and $3.2\text{ AU}$ from the Sun with randomized radii ($0.5 - 2.0\text{ px}$) and low mass ($10^{15}\text{ kg}$).
- **Orbital Dynamics:** Generated with near-circular orbital speeds ($v = \sqrt{\frac{G M_{\odot}}{r}}$) with minor randomized eccentricity factors ($0.95 - 1.05$).
- **$1$-Body Central Force:** Asteroid trajectories are influenced exclusively by the Sun's gravitational field, maintaining smooth 60 FPS performance with hundreds of active objects.
- **No Trail Overhead:** Minor bodies have `track_orbit = False` and `has_trail = False`, avoiding memory and recording overhead.
- **Viewport Culling:** Asteroids outside the visible screen boundaries are discarded during the render pass.

*(Note: Adding Jupiter's gravitational perturbations to model Kirkwood gaps is tracked in the [Future Updates / To-Do List](#future-updates--to-do-list).)*

### 8. Orbit Tracking Details

Orbit tracking utilizes an **angle-based angular sweep** system implemented in `physics.orbits_tracker.OrbitRecorder`:

- **Angle Sampling:** At each step, the planet's polar angle relative to the Sun is calculated via $\theta = \text{atan2}(y - y_{\odot}, x - x_{\odot})$.
- **Wraparound Handling:** Angle differences $\Delta\theta$ crossing the $[-\pi, \pi]$ boundary are normalized to the shortest angular path.
- **Uniform Point Buffering:** A point $(x, y)$ is appended to a `deque(maxlen=360)` each time the accumulated angle sweep exceeds `angle_step` ($1.0^\circ$). This guarantees a uniform 360-point trail representing exactly one complete revolution, independent of orbital speed or frame rate.
- **Revolution Detection:** Total cumulative angular sweep `orbit_sweep_total` is tracked. When $\text{orbit\_sweep\_total} \ge 2\pi$, `orbit_count` increments, the remainder is retained, and `flash_timer` is set to 10 frames to trigger the visual flash ring.

### 9. Scaling and Zoom

Scaling mechanics manage the translation between astronomical physical coordinates (meters) and screen space (pixels), as well as visual planet sizing:

- **Position Scaling:** Converts physical coordinates to screen offsets using `DEFAULT_SCALE` ($350\text{ px}/\text{AU}$):
  $$x_{\text{screen}} = x_{\text{phys}} \cdot \text{scale} + \text{screen\_cx}$$
- **Dynamic Planet Sizing:** Real planet diameters vary across several orders of magnitude. The scaling system calculates visible draw radii proportional to Earth's base size ($50\text{ px}$), adjusted for zoom level and scaled down for outer gas giants by `OUTER_PLANET_SCALE_FACTOR` ($0.6$, a 40% reduction) to prevent visual overlap.
- **Zoom Responsiveness:** When the user zooms, both orbital positions and visual planet radii scale proportionally.

*(Note: Consolidating all scaling constants and helper routines into a standalone `config.scale` module is tracked in the [Future Updates / To-Do List](#future-updates--to-do-list).)*

---
# Detailed Documentation

## Folder Structure & Contents

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

The primary executable script orchestrating startup, event polling, physics substepping, and rendering.

- **Initialization:**
  - Configures Pygame fullscreen display and window caption.
  - Initializes clock, framerate (`FPS = 60`), and substepping parameters (`steps_per_frame = 1`, `BASE_TIMESTEP = 86400`).
  - Sets up camera state (`scale`, `screen_offset_x`, `screen_offset_y`, `dragging`).
- **Solar System Instantiation:**
  - Instantiates `solarsystem`, `major_asteroids`, `asteroids`, `tno_belt`, and `pluto` via `objects.factory`.
  - Partitions objects into `major_bodies` (evaluated for mutual $N$-body gravity) and `minor_bodies` (Sun-only gravity).
  - Prepares `planet_hud_data` tuple list for HUD rendering.
- **Main Execution Loop:**
  - Event dispatcher handling zooming, dragging, speed adjustment, screenshot capture, and clean exit.
  - Physics substepping loop executing `update_bodies_physics` and updating `total_elapsed_time`.
  - Orbit recorder update for all `major_bodies`.
  - Screen rendering loop calling `draw_body` for all active bodies.
  - HUD overlay invocation via `render_menu_texts`.
  - Display refresh via `pygame.display.update()`.

**For a more detailed description jump to** [[#How the Simulation Works|How the Simulation works]]. 

---

### 2. `config/` — Configuration Files

#### 2.1 `config.colors` — Celestial Body Color Scheme

Contains standardized RGB color definitions for celestial bodies and HUD elements.

- **`SUN_COLOR`:** Solar surface color `{"Sun": (252, 150, 1)}`.
- **`PLANET_COLORS`:** Dictionary mapping planet names to RGB tuples (e.g., `"Earth": (107, 147, 214)`, `"Mars": (193, 68, 14)`).
- **`ASTEROID_COLORS`:** Colors for major asteroids (Ceres, Vesta, Pallas, Juno) and random belt objects.
- **`TNO_COLORS`:** Colors for Pluto `(200, 200, 255)` and random Kuiper Belt objects.

#### 2.2 `config.scale` — Scale Factors and Dynamic Scaling *(Module Specification)*


> [!NOTE]
> This section defines the specification for the dedicated `config.scale` module, consolidating scale constants from `config.simulation` and dynamic sizing routines from `render.scale`.

##### 2.2.1 Scale Constants

- **`DEFAULT_SCALE`:** Base conversion factor from astronomical units to screen pixels ($350\text{ px} / \text{AU}$).
- **`SUN_SIZE`:** Draw radius for the Sun ($2\text{ px}$).
- **`BASE_SIZE`:** Reference display size for Earth ($50\text{ px}$).
- **`OUTER_PLANET_SCALE_FACTOR`:** Outer planet scaling multiplier ($0.6$).
- **`MINOR_BASE_SIZE`:** Draw radius for major asteroids and Pluto ($2.5\text{ px}$).
- **`MIN_SIZE` / `MAX_SIZE`:** Radius range for procedurally generated asteroids ($0.5\text{ px} - 2.0\text{ px}$).
- **`INNER_RADIUS` / `OUTER_RADIUS`:** Main asteroid belt boundaries ($2.2\text{ AU} - 3.2\text{ AU}$).
- **`INNER_KUIPER_RADIUS` / `OUTER_KUIPER_RADIUS`:** Kuiper belt boundaries ($30.0\text{ AU} - 50.0\text{ AU}$).

##### 2.2.2 Dynamic Scaling Helpers

```python
def scale_planet_size(planet_radius: float, scale: float, is_outer_planet: bool = False) -> float:
    """
    Scale planet visual draw radius relative to Earth's diameter, current zoom scale,
    and outer planet reduction factors.
    
    Args:
        planet_radius (float): Physical radius of the planet in meters.
        scale (float): Current screen scale factor (px/m).
        is_outer_planet (bool): Whether to apply the outer planet reduction factor.
        
    Returns:
        float: Computed draw radius in pixels.
    """
```

```python
def calculate_scaled_sizes(scale: float) -> dict[str, float]:
    """
    Compute a dictionary mapping each planet's name to its scaled display radius.
    
    Args:
        scale (float): Current screen scale factor (px/m).
        
    Returns:
        dict[str, float]: Dictionary of {planet_name: display_radius_px}.
    """
```

#### 2.3 `config.simulation` — Simulation Configuration

- **`TIMESTEP`:** Base physical time delta per sub-step ($86,400\text{ s} = 1\text{ day}$).
- **`SUBSTEP`:** Default number of physics substeps per frame ($1$).

#### 2.4 `config.display` — Display and Layout Settings

- **`WIDTH`, `HEIGHT`:** Native window resolution ($1920 \times 1080$).
- **`COLOR_BACKGROUND`:** Background canvas color `(36, 36, 36)`.
- **`COLOR_TEXT`:** Primary UI font color `(255, 255, 255)`.
- **`PADDING`, `ROW_HEIGHT`, `HEADER_GAP`, `TEXT_GAP`:** Layout grid constants for HUD alignment.

---

### 3. `data/` — Real-World Planetary and Ephemeris Data

All physical values are stored in SI units (meters, kilograms, seconds, meters/second).

#### 3.1 `data.sun` — Sun Data

Contains `SUN_DATA` dictionary:
- `name`: `"Sun"`
- `radius`: Physical solar radius ($696,350,000\text{ m}$)
- `mass`: Solar mass ($1.98892 \times 10^{30}\text{ kg}$)
- `color`: RGB tuple from `config.colors.SUN_COLOR`

#### 3.2 `data.planets` — Planetary Constants (`PLANET_DATA`)

Keyed dictionary containing physical and orbital properties for Mercury through Neptune:

| Planet | Position (AU) | Perihelion (m) | Diameter (m) | Mass (kg) | Orbital Velocity (m/s) | `is_inner` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mercury** | -0.387 | $46.0 \times 10^9$ | $4,879 \times 10^3$ | $0.330 \times 10^{24}$ | 47,400 | `True` |
| **Venus** | -0.723 | $107.5 \times 10^9$ | $12,104 \times 10^3$ | $4.870 \times 10^{24}$ | 35,020 | `True` |
| **Earth** | -1.000 | $147.1 \times 10^9$ | $12,756 \times 10^3$ | $5.970 \times 10^{24}$ | 29,780 | `True` |
| **Mars** | -1.524 | $206.7 \times 10^9$ | $6,792 \times 10^3$ | $0.642 \times 10^{24}$ | 24,060 | `True` |
| **Jupiter** | -5.204 | $740.6 \times 10^9$ | $142,984 \times 10^3$ | $1898 \times 10^{24}$ | 13,060 | `False` |
| **Saturn** | -9.573 | $1357.6 \times 10^9$ | $120,536 \times 10^3$ | $568 \times 10^{24}$ | 9,680 | `False` |
| **Uranus** | -19.165 | $2732.7 \times 10^9$ | $51,118 \times 10^3$ | $86.8 \times 10^{24}$ | 6,800 | `False` |
| **Neptune** | -30.178 | $4471.1 \times 10^9$ | $49,528 \times 10^3$ | $102 \times 10^{24}$ | 5,430 | `False` |

#### 3.3 `data.asteroids` — Major Asteroid Data (`ASTEROID_DATA`)

Keyed dictionary containing physical properties and orbital characteristics:
- **Ceres:** Radius $473\text{ km}$, Mass $9.393 \times 10^{20}\text{ kg}$, Semi-major axis $2.77\text{ AU}$, Velocity $17.9\text{ km/s}$.
- **Vesta:** Radius $262.7\text{ km}$, Mass $2.59 \times 10^{20}\text{ kg}$, Semi-major axis $2.36\text{ AU}$, Velocity $19.3\text{ km/s}$.
- **Pallas:** Radius $256\text{ km}$, Mass $2.11 \times 10^{20}\text{ kg}$, Semi-major axis $2.77\text{ AU}$, Velocity $17.0\text{ km/s}$.
- **Juno:** Radius $118\text{ km}$, Mass $2.67 \times 10^{19}\text{ kg}$, Semi-major axis $2.67\text{ AU}$, Velocity $18.0\text{ km/s}$.

#### 3.4 `data.tnos` — Trans-Neptunian Object Data (`TNO_DATA`)

- **Pluto:** Radius $594.15\text{ km}$, Mass $1.303 \times 10^{22}\text{ kg}$, Semi-major axis $39.48\text{ AU}$, Velocity $4.74\text{ km/s}$.

#### 3.5 Ephemeris Data (`de440s.bsp`)

The binary JPL ephemeris kernel provides high-precision positions and velocities for celestial bodies relative to the solar system barycenter.

---

### 4. `physics/` — Gravity and Orbit Calculations

#### 4.1 `physics.constants`

- **`AU`:** $149,597,870,700\text{ m}$ (Astronomical Unit).
- **`G`:** $6.67428 \times 10^{-11}\text{ m}^3\text{kg}^{-1}\text{s}^{-2}$ (Gravitational constant).

#### 4.2 `physics.engine`

Handles gravitational vector arithmetic and numerical integration.

- **`compute_gravity_force(body1, body2, g=G)`:**

  Calculates the 2D gravitational force vector exerted on `body1` by `body2`:
  1. Distance vector: $\Delta x = x_2 - x_1$, $\Delta y = y_2 - y_1$.
  2. Euclidean distance: $r = \sqrt{\Delta x^2 + \Delta y^2}$. If $r = 0$, returns `(0.0, 0.0, 0.0)`.
  3. Force magnitude: $F = G \frac{m_1 m_2}{r^2}$.
  4. Polar angle: $\theta = \text{atan2}(\Delta y, \Delta x)$.
  5. Directional force components: $F_x = F \cos(\theta)$, $F_y = F \sin(\theta)$.
  6. Returns `(fx, fy, dist)`.

- **`update_bodies_physics(major_bodies, minor_bodies, dt, sun=None)`:**

  Executes physical state integration for all simulation entities:
  
  - **Major Bodies:** Evaluates pairwise forces with all other major bodies. Updates velocity and position via semi-implicit Euler steps:
    $$v_x \leftarrow v_x + \frac{F_x}{m} \Delta t, \quad v_y \leftarrow v_y + \frac{F_y}{m} \Delta t$$
    $$x \leftarrow x + v_x \Delta t, \quad y \leftarrow y + v_y \Delta t$$
    Updates distance to Sun, dynamically tracking `min_distance` and `max_distance`.
	
  - **Minor Bodies:** Computes central force exclusively against `sun`, applying Euler updates and updating `distance_to_sun`.

#### 4.3 `physics.orbits`

Keplerian orbital mathematics and initialization helpers.

- **`calculate_orbital_speed(central_mass, distance, g=G)`:**
  Computes circular orbital velocity:
  $$v = \sqrt{\frac{G \cdot M}{r}}$$
- **`calculate_circular_orbit(central_mass, distance, angle=None, eccentricity_range=(1.0, 1.0))`:**
  Generates 2D initial state vectors `(x, y, vx, vy)` for a body at radius $r$:
  $$x = r \cos(\theta), \quad y = r \sin(\theta)$$
  $$v_x = -v \sin(\theta), \quad v_y = v \cos(\theta)$$
  Applies an optional randomized scalar multiplier from `eccentricity_range` to simulate eccentric orbits.

#### 4.4 `physics.orbits_tracker`

Implements the `OrbitRecorder` class for angle-based revolution tracking.

- **`OrbitRecorder(max_points=360, angle_step_deg=1.0)`:**
	
	- `points`: `deque(maxlen=360)` storing $(x, y)$ coordinates.
	- `angle_step`: Radian threshold per point ($1.0^\circ = \frac{\pi}{180}\text{ rad}$).
	- `angle_accumulator`: Accumulates swept angle toward the next point.
	- `orbit_sweep_total`: Accumulates swept angle toward a full $360^\circ$ ($2\pi\text{ rad}$) revolution.
	- `orbit_count`: Completed revolution counter.
	- `flash_timer`: Remaining frames for visual flash ring effect.
	
- **`update(x, y, sun_x=0.0, sun_y=0.0)`:**

	Computes polar angle relative to Sun, calculates shortest angular displacement across boundary wrapping, samples trail points into `points` deque, increments `orbit_count` upon completing $2\pi$ radians, and triggers `flash_timer`.
  
- **`clear()`:** Clears recorded points and resets accumulators.

---

### 5. `objects/` — Object Models and Creation Factory

#### 5.1 `objects.body` — Celestial Body Class

Defines the unified `Body` class representing any entity in the simulation:

```python
class Body:
    def __init__(self, name: str, x: float, y: float, vx: float, vy: float,
                 mass: float, radius: float, color: tuple[int, int, int],
                 is_sun: bool = False, is_asteroid: bool = False,
                 has_trail: bool = True, track_orbit: bool = False,
                 diameter: float = None, perihelion: float = None, aphelion: float = None):
```

- **Physical Attributes:** `name`, `x`, `y`, `vx`, `vy`, `mass`, `radius`, `diameter`, `is_sun`, `is_asteroid`.
- **Telemetry & Rendering:** `color`, `has_trail`, `distance_to_sun`, `perihelion`, `aphelion`, `min_distance`, `max_distance`.
- **Orbit Tracking:** `orbit_recorder` (holds `OrbitRecorder` instance when `track_orbit=True`).
- **Properties:** `@property orbit_count` returns current completed revolution count.

#### 5.2 `objects.factory` — Solar System Creation Factory

Encapsulates factory routines to build celestial systems:

- **`create_solarsystem()`:**
	
	1. Instantiates the Sun at $(0, 0)$ with solar mass and display radius.
	2. Loads JPL DE440s ephemeris via `skyfield` and samples planetary positions and velocities for the current timestamp `ts.now()`.
	3. Maps planetary coordinates to meters and m/s, calculates scaled visual radii, and constructs `Body` instances for Mercury through Neptune with `track_orbit=True`.
	4. Returns `[sun] + planets`.
	
- **`create_major_asteroids()`:**

  Instantiates Ceres, Vesta, Pallas, and Juno from `data.asteroids.ASTEROID_DATA` using circular orbital mechanics.
  
- **`create_asteroid_belt(num_asteroids: int)`:**

  Generates `num_asteroids` procedural asteroids distributed between `INNER_RADIUS` ($2.2\text{ AU}$) and `OUTER_RADIUS` ($3.2\text{ AU}$) with randomized radii ($0.5 - 2.0\text{ px}$) and masses ($10^{15}\text{ kg}$).
  
- **`create_Kuiper_belt(num_objects: int)`:**

  Generates `num_objects` procedural TNOs distributed between `INNER_KUIPER_RADIUS` ($30\text{ AU}$) and `OUTER_KUIPER_RADIUS` ($50\text{ AU}$).

- **`create_pluto()`:**

  Instantiates Pluto as an orbit-tracked TNO from `data.tnos.TNO_DATA`.

---

### 6. `render/` — Viewport and Graphics Rendering

#### 6.1 `render.renderer`
Implements drawing routines for celestial bodies, trails, and visual effects:

- **`draw_orbit_trail(surface, body, scale, offset_x, offset_y, point_radius=1)`:**

  Iterates through points in `body.orbit_recorder.points`. Projects each physical point $(p_x, p_y)$ to screen space. Skips points outside screen bounds. Computes distance-faded RGB values blended with `COLOR_BACKGROUND` and renders smooth anti-aliased dots.

- **`draw_body(surface, body, scale, offset_x, offset_y)`:**

  Projects body coordinates to screen space. Applies viewport culling to skip off-screen minor bodies. Draws orbit trail, renders the filled body circle with clamped radius `max(1, int(body.radius))`, and renders an expanding glowing flash ring if `flash_timer > 0`.

#### 6.2 `render.text` *(Upcoming Specification)*

> [!NOTE]
> Planned module to encapsulate font management, text measurement, alignment helpers, and rendered surface caching.

#### 6.3 `render.hud`

Implements `render_menu_texts(...)` to render the heads-up display overlay:

- **Top-Left:** Real-time FPS counter (`clock.get_fps()`).
- **Top-Right:** Simulation title, current speed multiplier ($N\text{x}$ and days/frame), and formatted elapsed time ($y, d, h, m, s$).
- **Bottom-Left:** Keyboard and mouse controls reference table.
- **Bottom-Right:** Comprehensive planetary statistics table displaying:
  - Planet Name (color-coded).
  - Current Distance to Sun (formatted in $\text{km}$ and $\text{AU}$).
  - Dynamic Perihelion / Aphelion ($\text{min} / \text{max}$ recorded distances in millions of $\text{km}$).
  - Orbit Count (completed revolutions).

---

## Future Updates / To-Do List

The following tasks and refactorings are planned for upcoming releases:

- [ ] **Physics: Jupiter Perturbation on Asteroids**
  - Extend `physics.engine.update_bodies_physics` so minor bodies in the asteroid belt optionally calculate gravitational perturbations from Jupiter in addition to the Sun.
  - Model Kirkwood resonance gaps dynamically within the asteroid belt.
- [ ] **Architecture: `config.scale` Module Refactoring**
  - Extract all scale and boundary constants (`DEFAULT_SCALE`, `SUN_SIZE`, `BASE_SIZE`, `OUTER_PLANET_SCALE_FACTOR`, `MINOR_BASE_SIZE`, `MIN_SIZE`, `MAX_SIZE`, `INNER_RADIUS`, `OUTER_RADIUS`, `INNER_KUIPER_RADIUS`, `OUTER_KUIPER_RADIUS`) from `config.simulation` into a dedicated `config.scale` module.
  - Move dynamic sizing helpers (`scale_planet_size`, `calculate_scaled_sizes`) from `render.scale` into `config.scale`.
  - Update imports across `main.py`, `objects.factory`, and `render.renderer`.
- [ ] **Render: Dedicated `render.text` Module**
  - Implement a centralized typography and text rendering module for font caching, text wrapping, and UI surface optimization.
- [ ] **Orbits: Elliptical Orbit Generator**
  - Transition asteroid and TNO generation from circular approximations (`calculate_circular_orbit`) to true Keplerian elliptical initializations (semi-major axis, eccentricity, argument of periapsis).
- [ ] **Objects: Additional Asteroids and TNOs**
  - Add physical data and factory integration for asteroids **Hygiea** and **Eros**.
  - Add the **Pluto-Charon** binary barycenter system.
- [ ] **UI: Visibility Toggles**
  - Implement keyboard/UI toggles to show or hide the Asteroid Belt, Kuiper Belt, orbit trails, and inner/outer planet groups.

---

## Roadmap / Planned Features

✅ **Completed Features**

- **Mouse Navigation & Viewport Controls** (Panning and zooming, added in v.1.5)
- **Angle-Based Orbit Tracking & Counters** (Accurate $360^\circ$ angular sweep tracking, points v.1.5 → angles v.1.9)
- **Fading Orbit Trails & Flash Ring Effects** (added in v.1.5)
- **Procedural Asteroid Belt & Kuiper Belt** (added in v.1.6 – v.1.9)
- **Major Asteroids** (Ceres, Vesta, Pallas, Juno, added in v.1.7 – v.1.9)
- **Trans-Neptunian Objects** (Pluto and Charon, added in v.1.9 – v.1.9.3)
- **JPL DE440s Ephemeris Integration** (Accurate real-world startup states via Skyfield, added in v.1.8)
- **Domain-Driven Modular Architecture** (`config`, `data`, `objects`, `physics`, `render`, added in v.1.9.1-1.9.3)

⚙️ **In Progress**
- **Additional Objects:** Asteroids (Pallas, Juno) and transneptunian objects (Upcoming v1.9.3) -> Hygea and Eros to go, Charon to go
- **Web version:** Simplified web version using Panel library (Branched from v1.7)
- Additional minor bodies (Hygiea, Eros, Charon)
- Web version (interactive exploration using Panel library)

💡 **Planned Features**
- Interactive visual toggles (toggling belts, trails, telemetry)
- Real-time comparison between simulated and theoretical orbital parameters
- Arbitrary date selection for ephemeris initialization

---

## Credits & Sources

- **Tech With Tim** — Pygame physics simulation tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- **rastr-0** — Solar system orbital mechanics guide: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- **Zerot69** — Solar System Simulation reference implementation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- **NASA NSSDC** — Planetary Fact Sheet & physical constants: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
- **NASA JPL** — DE440s Planetary Ephemerides via [Skyfield](https://rhodesmill.org/skyfield/)

---

## Version History

For detailed version-by-version release notes, refer to `CHANGELOG.md` and the archived branches in the [repository history](https://github.com/kuranez/solar-system-simulation/tree/version-history).
