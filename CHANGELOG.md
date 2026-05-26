# Changelog

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