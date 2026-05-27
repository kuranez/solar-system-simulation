# 2D Solar System Simulation

This Python/Pygame project simulates the solar system using real astronomical data and Newtonian gravity.  Version 1.8 introduces ephemeris-based initialization using data from JPL (via the Skyfield library) so planetary starting positions and velocities are more physically accurate.

Based on the [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo) tutorial by [@techwithtim](https://github.com/techwithtim/Python-Planet-Simulation) and inspired by tweaks and additions by [@zerot69](https://github.com/zerot69/Solar-System-Simulation).

[![Live Demo](https://img.shields.io/badge/🟢%20Live%20App-Solar%20System%20Sim-422C71?style=for-the-badge)](https://apps.kuracodez.space/solar-system-sim/app)

---

## Screenshot

![Screenshot](screenshots/screenshot-v-1-8.png)

## Core Features

- Orbits of inner and outer planets of our solar system
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

## Setup

Install Python packages and run `main.py`. 

**Dependencies:**
- pygame
- skyfield
- jplephem
- itertools

## Controls

| Control | Action |
|---------|--------|
| **Mouse Wheel** | Zoom In/Out |
| **Left Click + Drag** | Move View |
| **[+] / [-]** | Adjust Speed |
| **F12** | Take Screenshot |
| **[ESC]** | Quit Simulation |

## Project Structure

- `main.py` — Main loop, event handling, rendering with enhanced interactive controls
- `constants.py` — Physical constants, colors, planetary data
- `solarsystem_sim.py` — Enhanced Sun, Planet, and Body classes with orbit tracking
- `solarsystem_scale.py` — Scaling and planet size calculations
- `de440a.bsp`  — 
- `CHANGELOG.md` — Detailed version changes
- `DOCUMENTATION.md` — Full documentation for current version

## WebApp Demo
 
 Simplified web version based on this project showcasing different planetary system options .
 
 **WebApp:** [https://apps.kuracodez.space/solar-system-sim](https://apps.kuracodez.space/solar-system-sim/app) 
 
 **For more info see:** [https://github.com/kuranez/solar-system-simulation-web](https://github.com/kuranez/solar-system-simulation-web)


---

## Version Highlights

**New in Version 1.8**
- **Ephemerides Implementation:** Calculation of initial planetary positions using data from NASA's Jet Propulsion Laboratory (JPL) via the Skyfield library

**Previous in Version 1.7**
- **Zoom Fix:** Adjusted Simulation Scaling
- **Added:** Visual orbit completion indicator.
- **Added:** Asteroids Ceres & Vesta

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
- **Mouse wheel zoom:** both orbits and planet visuals scale with zoom
- Improved planet scaling logic and modular scaling functions
- Orbit trail fade effect for clearer visualization
- Cleaner, more extensible code structure

**Previous in Version 1.3:**
- Improved menu texts
- **Frame rate independent physics**
- Removed orbit and planet visibility options

**Previous in Version 1.2:**
- Enhanced visuals & scaling

**Previous in Version 1.1:**
- Size & resolution updates

### Initial Release

**Core Features:** 

  - Simulation of inner and outer planets
  - Keyboard controls for scale and speed adjustment
  - Toggle functionality for orbits and planets
  - Display of planet distances to the Sun
  
 **Foundation:** Basic solar system simulation with gravitational physics

---

## Milestones & Roadmap

✅ **Completed Features**

- **Mouse control navigation** (Added in v1.5)
- **Orbit tracking and counters** (Added in v1.5)
- **Enhanced orbit drawing** (Added in v1.5)
-  **Asteroid Belt** (Added in v1.6)
- **Asteroids Ceres and Vesta** (Added in v1.7)

⚙️ **In Progress**

- **Additional Objects:** Asteroids (Pallas, Juno) and transneptunian objects (Upcoming v1.8)
- **Web version:** Simplified web version using Panel library (Branched from v1.7)

💡 **Planned Features**
- Toggle to show/hide asteroid belt
- Toggle to show/hide views of inner and outer planets
- Toggle to show/hide asteroids and TNOs
- Kirkwood gaps to show Jupiter's resonance effects
- Use of different planet distances from the sun and real value comparison
- Options to start the simulation at a specific historical or future date.
- Further visual and code optimizations 

---
## Sources

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

---

## Contributing

Pull requests, bug reports, and feature requests are welcome!

---
