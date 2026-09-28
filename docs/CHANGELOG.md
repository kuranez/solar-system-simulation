# Changelog

## v1.9.2 - Refactor of `solarsystem_sim.py` into `physics/` and `objects/` modules - Sep 28, 2026

**Commit:** [eb6b0a1](https://github.com/kuranez/solar-system-simulation/commit/eb6b0a11aa5ebd1966272a881c36f49c27615f13)

**Why this change?**

The initial Skyfield implementation in v1.8 introduced repeated physics calculations in `solarsystem_creation.py` to verify whether the methods in `solarsystem_sim.py` were causing issues with orbital behavior.

To improve scalability and maintainability, `solarsystem_sim.py` was refactored and its methods were reorganized into dedicated modules.

**How does it work now?**

* **`physics/` module:** Contains physical calculations, including gravity (`physics.engine`) and orbital calculations (`physics.orbits`).
* **`objects/` module:** Uses a single base class for celestial bodies (`objects.body`) to simplify object creation and reduce duplication.

**Other changes**

* **`render/` module:** Contains the HUD (`render.hud`) and rendering methods (`render.renderer`).
* **Orbit tracking:** Replaced orbit-trail-point sampling with angle-based sampling (`physics.orbits_tracker`).
* **Bugfix:** Planets derailing with increased simulation speed by adding sub-steps.

**The physics engine, orbit tracking, object creation, and rendering are now clearly separated into dedicated modules.**


## v1.9.1 - Refactor of `constants.py` into `config`-, `data/` and `physics/`-modules - Sep 27, 2026

**Commit:**[37a259f](https://github.com/kuranez/solar-system-simulation/commit/37a259fb0b0edc32e8628ccb6d973b437b40de52)

**Why this change?**

The `constants.py` file contained physical constants, display settings, simulation settings, and planetary data in different formats as a leftover from previous versions.

**How does it work now?**

- **`config`-Module:** Contains submodules for display settings (`config.display`), simulation settings (`config.simulation`) and the color palette (`config.color`).
- **`physics`-Module:** Physical constants such as the Astronomical unit (AU) and gravitational constant (G) can now be found here in the `physics.constants`submodule.
- **`data`-Module:** Planetary and asteroid data can now be found here, neatly organized in sub-modules using a standardized keyed-dictionary format. 


## v1.9.0 - Pluto, HUD, and Orbit Tracking Updates - Jun 27, 2026

**Features**

- **Pluto support:** Pluto is now created as a proper TNO object and included in the on-screen HUD.
- **Minor-body expansion:** Added Pallas and Juno to the generated major-asteroid set.
- **Orbit trail for Pluto:** Pluto now renders with an orbit trail like the major planets.
- **HUD layout adjustment:** Increased spacing around the lower-right planet table so Pluto is not flush against the screen border.
- **Additional** randomly generated TNO objects to keep Pluto company.


**Bugfixes & Improvements**

- **Orbit counting stability:** Orbit counting now uses angular sweep tracking, which remains stable when simulation speed is increased.
- **HUD refactor:** Menu rendering now receives the screen surface explicitly instead of depending on globals from `main.py`.
- **Module rework:** Split HUD rendering into [hud.py](solar-system-simulation/hud.py) and Pluto/TNO creation into [solarsystem_creation.py](solar-system-simulation/solarsystem_creation.py) for cleaner organization.
- **Pluto color consistency:** Added a shared Pluto color constant and aligned Pluto rendering with it.

## v1.8 - Ephemerides & Skyfield Integration - May 26, 2026 (Current Release)

**Features**

- **Ephemerides Implementation:** Initial planetary positions and velocities are now calculated from JPL ephemerides via the Skyfield library, improving the physical accuracy of the simulation start state.
- **Ephemeris data included:** `de440s.bsp` (or local equivalent) can be used to produce precise initial conditions for all major planets.
- **Improved initialization:** More accurate planetary initialization logic and improved conversion from astronomical units to display coordinates.
- **Dependency notes:** `skyfield` (and its optional backend `jplephem`) are recommended to reproduce exact ephemeris-based initialization.

**Bugfixes & Improvements**

- Minor UI text and menu updates to reflect ephemeris options and dependencies.
- Small fixes to scaling/zoom logic carried over from v1.7 to ensure consistent behavior when using ephemeris-based positions.

##### File History (v1.7 - v1.8)
- Changed file: versions/v1.8/main.py
- Changed file: versions/v1.8/constants.py
- Changed file: versions/v1.8/solarsystem_sim.py
- Changed file: versions/v1.8/solarsystem_scale.py
- Added file: de440s.bsp (ephemeris binary) or configured to load from environment

---

## v1.7 - Major Asteroids Ceres & Vesta - Nov 21, 2025

**Features**

- **Zoom Fix:** Adjusted Simulation Scaling.
- **Added:** Orbit completion indicator. Visual flash, when a planet completes an orbit.
- **Major asteroids:** Added Ceres and Vesta as individual major-asteroid objects.

##### File History (v1.6 - v1.7)
- Changed file: versions/v1.7/constants.py
- Changed file: versions/v1.7/main.py
- Changed file: versions/v1.7/solarsystem_scale.py
- Changed file: versions/v1.7/solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.6...v.1.7

---
## v1.6 - Asteroid Belt Implementation - Nov 20, 2025

**Features**

- **Realistic placement** - 300+ asteroids positioned between 2.2 and 3.2 AU from the Sun
- **Optimized physics** - Asteroids calculate gravity from the Sun only for maximum performance
- **Accurate orbital mechanics** - Each asteroid follows its own elliptical orbit with slight eccentricity
- **Visual clarity** - Uniform light gray color (192, 192, 192) for easy identification
- **Memory efficient** - No orbit trails for asteroids to maintain smooth performance

##### File History (v1.5 - v1.6)
- Changed file: versions/v1.6/constants.py
- Changed file: versions/v1.6/main.py
- Changed file: versions/v1.6/solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.5...v.1.6

---

## v1.5 - Improved UI - Jun 29, 2025

**Features**

- **Mouse drag navigation:** Left-click and drag to move the view around the solar system
- **Orbit counter system:** Each planet now tracks and displays completed orbits
- **Enhanced orbit visualization:** Only the most recent orbit trail is displayed with visual fade effect
- **Orbit completion indicators:** Flash ring effect when planets complete an orbit
- **Improved menu system:** Tabular layout for controls and planet information
- **Time elapsed indicator:** Real-time display of simulated time in years/days/hours/minutes
- **Screenshot functionality:** Press F12 to save screenshots directly from the simulation
- **Professional UI layout:** Organized display with proper table formatting

##### File History (v1.4 - v1.5)
- Changed file: versions/v1.5/constants.py
- Changed file: versions/v1.5/main.py
- Changed file: versions/v1.5/solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.4...v.1.5


---
## v1.4 - Code Organization -  Jun 27, 2025

**Features**

- **Added:** Mouse wheel zoom, modular architecture, enhanced orbit trails, real-time planet scaling, unified constants
- **Changed:** Complete refactoring of zoom and scaling system, improved code organization, optimized drawing and update loops, enhanced user interface
- **Fixed:** Planet size scaling issues, orbit trail fade inconsistencies, code redundancy in scaling calculations
##### File History (v1.3 - v1.4)
- Changed file: versions/v1.4/constants.py
- Changed file: versions/v1.4/main.py
- Changed file: versions/v1.4/README.md
- Changed file: versions/v1.4/solarsystem_scale.py
- Changed file: versions/v1.4/solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.3...v.1.4

---

## v1.3 - Frame Rate Independence & UI Improvements  - Oct 20, 2024

**Features**

- **Added:** Frame rate independent physics
- **Added:** Improved menu texts and navigation instructions
- **Removed:** Buggy orbit and planet visibility toggles
- **Changed:** Enhanced user interface layout
- **Files:** Basic structure with main simulation files

##### File History (v1.2 - v1.3)
- Changed file: versions/v1.3/main.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.2...v1.3

---
## v1.2 Enhanced Visuals & Scaling - Oct 20, 2024

**Features**

- **Added:** Improved orbit visuals with trail fade effect
- **Added:** Overhauled scaling and zoom system with additional variables
- **Added:** Overhauled solar system creation process
- **Changed:** Better visual representation of planetary orbits
- **Known Issues:** Toggle orbit/planet functionality became buggy
##### File History (v1.1 - v1.2)
- Changed file: versions/v1.2/constants.py
- Changed file: versions/v1.2/main.py
- Changed file: versions/v1.2/solarsystem_scale.py
- Changed file: versions/v1.2/solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.1...v1.2

---
## v1.1 - Size & Resolution Updates - Jul 31, 2024

**Features**

- **Added:** Adjusted planet and orbit sizes for better visibility
- **Added:** 720p resolution support (1280x720)
- **Changed:** Improved planet size scaling relative to distances
- **Maintained:** All core simulation features from v1.0

##### File History (v1.0 - v1.1)
- Changed file: versions/v1.1/constants.py
- Changed file: versions/v1.1/main.py
- Changed file: versions/v1.1/README.md
- Created file: solarsystem_scale.py
- Renamed: solarsystem.py -> solarsystem_sim.py

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.0...v1.1

---

## v1.0 - Initial Release - Jul 23, 2024

**Core Features:** 

  - Simulation of inner and outer planets
  - Keyboard controls for scale and speed adjustment
  - Toggle functionality for orbits and planets
  - Display of planet distances to the Sun
  
 **Foundation:** Basic solar system simulation with gravitational physics

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/commits/v1.0








