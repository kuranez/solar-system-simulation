# 2D Solar System Simulation (v1.7)

2D simulation of our solar system using pygame.  
Based on the [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo) tutorial by [@techwithtim](https://github.com/techwithtim/Python-Planet-Simulation) and inspired by tweaks and additions by [@zerot69](https://github.com/zerot69/Solar-System-Simulation).

## Screenshot

![[screenshot_v-1-7.png]]

## WebApp Demo

> [![Live Demo](https://img.shields.io/badge/🟢%20Live%20App-Solar%20System%20Sim-422C71?style=for-the-badge)](https://apps.kuracodez.space/solar-system-sim/app)
>
> **Modified web version based on this project showcasing different planetary system options**
>
> **For more info see:** [https://github.com/kuranez/solar-system-simulation-web](https://github.com/kuranez/solar-system-simulation-web)
>

---

## Features

- Main planet orbits, inner and outer planets, and asteroid belt including Ceres & Vesta.
- Uses real astronomical data from NASA 
- **Interactive navigation:** Mouse wheel zoom and left-click drag to move view
- **Orbit tracking:** Real-time orbit counter for each planet with completion indicators
- **Enhanced visuals:** Single orbit trail per planet with fade effects
- **Professional UI:** Tabular display of controls and planet information
- **Time tracking:** Real-time simulation time display in years/days/hours/minutes
- **Screenshot support:** Press F12 to capture screenshots directly
- Adjustable simulation speed with keyboard controls
- Frame-rate independent physics
- Color-coded planets with authentic astronomical colors
- Modular code architecture for easy extension

---

## Version Highlights

**New in Version 1.8**
- **Ephemerides Implementation:** Calculation of initial planetary positions using data from NASA's Jet Propulsion Laboratory (JPL) via the Skyfield library.

**Previous in Version 1.7**
- **Zoom Fix:** Adjusted Simulation Scaling.

**Previous in Version 1.6:**
- **Asteroid belt implementation:** Realistic distribution of procedurally generated asteroids between Mars and Jupiter with configurable density, randomized sizes and orbital parameters, and optimized rendering for performance.

**Previous in Version 1.5:**
- **Mouse drag navigation:** Left-click and drag to pan around the solar system
- **Orbit counter system:** Track completed orbits for each planet with visual indicators
- **Enhanced orbit trails:** Only current orbit shown with smooth fade effect
- **Professional UI redesign:** Clean tabular layout for all information
- **Time elapsed display:** Real-time simulation time tracking
- **Built-in screenshots:** F12 key to save simulation images
- **Improved visual feedback:** Flash effects for orbit completions

**Previous in Version 1.4:**
- Mouse wheel zoom: both orbits and planet visuals scale with zoom
- Improved planet scaling logic and modular scaling functions
- Orbit trail fade effect for clearer visualization
- Cleaner, more extensible code structure

---

## Controls

| Control | Action |
|---------|--------|
| **Mouse Wheel** | Zoom In/Out |
| **Left Click + Drag** | Move View |
| **[+] / [-]** | Adjust Speed |
| **F12** | Take Screenshot |
| **[ESC]** | Quit Simulation |

## Screenshots

![screenshot.png](https://raw.githubusercontent.com/kuranez/solar-system-simulation/refs/heads/main/screenshots/Screenshot_v1-6.png)

---

| v.1.0    | v.1.1    | v.1.2    | v.1.3    | v.1.4    | v.1.5    |
|----------|----------|----------|----------|----------|----------|
| ![v.1.0](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-0.png) | ![v.1.1](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-1.jpg) | ![v.1.2](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-2.png) | ![v.1.3](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-3.png) | ![v.1.4](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-4.png) |![v.1.5](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-5.png) |
| **Features & Changes** | **Features & Changes** | **Features & Changes** | **Features & Changes** | **Features & Changes** | **Features & Changes** |
| - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets |
| - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard |
| - Toggle Orbits & Planets | - Toggle Orbits & Planets | - **BUGGY: Toggle Orbits & Planets** | - Pan view with arrow keys or mouse edges | - Pan view with arrow keys or mouse edges | - **NEW:** Adjust view with mouse drag |
| - Display Planet Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun |
|                                | - **NEW: Adjusted Planet & Orbit Sizes** | - **NEW: Overhauled Solar System Creation** | - **NEW: Improved menu texts** | - **NEW: Mouse wheel zoom: both orbits and planet visuals scale with zoom** | - **NEW: Mouse drag navigation** | 
|                                | - **NEW: 720p resolution** | - **NEW: Overhauled Scaling & Zoom (Additional variables)** | - **NEW: Frame rate independent physics** | - **NEW: Improved planet scaling logic and modular scaling functions** | - **NEW: Orbit counter and improved orbit trails** |
|                                |                            | - **NEW: Improved Orbit Visuals (Orbit Trail Fade)** | - **NEW: Removed buggy orbit/planet toggles** | - **NEW: Orbit trail fade effect for clearer visualization** | - **NEW: Time display** |
|                                |                            |                                                        |                                         | - **NEW: Cleaner, more extensible code structure** | - **NEW: Screenshot function** |

---

## Setup

Install Python packages and run `main.py`.

**Dependencies:**
- pygame
- skyfield
- sys
- datetime
- itertools

---

## Roadmap

**Planned Features**

- ✅ **Mouse control navigation** (Added in v.1.5)
- ✅ **Orbit tracking and counters** (Added in v.1.5)
- ✅ **Enhanced orbit drawing** (Added in v.1.5)
- Use of different planet distances from the sun and real value comparison
- Further visual and code optimizations
- **Additional Objects:** Asteroid belt and transneptunian objects

---

## Project Structure

- `main.py` — Main loop, event handling, rendering with enhanced interactive controls
- `constants.py` — Physical constants, colors, planetary data
- `solarsystem_sim.py` — Enhanced Sun, Planet, and Body classes with orbit tracking
- `solarsystem_scale.py` — Scaling and planet size calculations

---
# Changelog

### 🚀 What's New in v1.7

Version 1.7 improves asteroid visibility and simulation polish by introducing individually-instantiated major asteroids and a dedicated `Asteroid` class optimized for performance.

### ✨ Added
- `Asteroid` class (`solarsystem_sim.py`) — lightweight asteroid bodies that only compute Sun gravity and use screen-culling for efficient rendering
- Major asteroids: Ceres and Vesta are instantiated as distinct bodies using `constants.ASTEROID_CERES` and `constants.ASTEROID_VESTA`
- `create_major_asteroids()` (in `main.py`) — creates Ceres and Vesta with appropriate semi-major axes, colors and initial velocities
- Improved asteroid belt generation: `create_asteroid_belt()` now generates a configurable number of asteroids (300 by default) between 2.2–3.2 AU
- Planet orbit completion indicator: visual flash when a planet completes an orbit; planets now track orbit counts

### 🔧 Performance & Rendering
- Asteroids only calculate gravitational attraction to the Sun (no planet interactions) for performance
- Screen culling for asteroids avoids drawing off-screen objects
- Asteroids have no orbit trails to save memory and maintain smooth framerates

### 📝 Notes
- The simulation title and in-game time display have been updated to reflect v1.7
- `constants.py` contains `ASTEROID_CERES` and `ASTEROID_VESTA` entries used by v1.7

---

## Version History Overview

### [1.6] - Asteroid Belt Implementation - Nov 20, 2025

- **Added:** Asteroid belt: complete main belt implementation with 300+ objects. Realistic distribution of procedurally generated asteroids between Mars and Jupiter with configurable density, randomized sizes and orbital parameters, and optimized rendering for performance. 
- **Changed:** Optimized physics: Sun-only gravity calculations for asteroids

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.5...v.1.6

### [1.5] - Improved UI - Jun 29, 2025
- **Added:** Mouse drag navigation, orbit counters, enhanced orbit visualization, orbit completion indicators, improved menu system, time elapsed indicator, screenshot functionality
- **Changed:** UI overhaul with table-based layout, enhanced planet data display, optimized orbit trail rendering
- **Fixed:** Orbit trail memory leaks, UI element positioning, time tracking accuracy

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.4...v.1.5

### [1.4] - Code Organization - Jun 27, 2025
- **Added:** Mouse wheel zoom, modular architecture, enhanced orbit trails, real-time planet scaling, unified constants
- **Changed:** Complete refactoring of zoom and scaling system, improved code organization, optimized drawing and update loops, enhanced user interface
- **Fixed:** Planet size scaling issues, orbit trail fade inconsistencies, code redundancy in scaling calculations

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.3...v.1.4

### [1.3] - Frame Rate Independence & UI Improvements - Oct 20, 2024
- **Added:** Frame rate independent physics
- **Added:** Improved menu texts and navigation instructions
- **Removed:** Buggy orbit and planet visibility toggles
- **Changed:** Enhanced user interface layout
- **Files:** Basic structure with main simulation files

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.2...v1.3

### [1.2] - Enhanced Visuals & Scaling - Oct 20, 2024
- **Added:** Improved orbit visuals with trail fade effect
- **Added:** Overhauled scaling and zoom system with additional variables
- **Added:** Overhauled solar system creation process
- **Changed:** Better visual representation of planetary orbits
- **Known Issues:** Toggle orbit/planet functionality became buggy

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.1...v1.2

### [1.1] - Size & Resolution Updates  - Jul 31, 2024
- **Added:** Adjusted planet and orbit sizes for better visibility
- **Added:** 720p resolution support (1280x720)
- **Changed:** Improved planet size scaling relative to distances
- **Maintained:** All core simulation features from v1.0

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v1.0...v1.1

### [1.0] - Initial Release - Jul 23, 2024
- **Core Features:** 
  - Simulation of inner and outer planets
  - Keyboard controls for scale and speed adjustment
  - Toggle functionality for orbits and planets
  - Display of planet distances to the Sun
- **Foundation:** Basic solar system simulation with gravitational physics

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/commits/v1.0

---
# Sources

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
