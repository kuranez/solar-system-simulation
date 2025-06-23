# Solar System Simulation

2D simulation of our solar system using pygame.  
Based on the [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo) tutorial by [@techwithtim](https://github.com/techwithtim/Python-Planet-Simulation) and inspired by tweaks and additions by [@zerot69](https://github.com/zerot69/Solar-System-Simulation).

---

## Features

- Orbits of inner and outer planets of our solar system
- Uses real astronomical data from NASA
- Scalable zoom: mouse wheel adjusts both orbits and planet sizes (from v1.4)
- Adjustable simulation speed
- Frame-rate independent physics
- Pan view with arrow keys or by moving the mouse to the screen edges
- Color-coded planets and faded orbit trails
- Modular code: separated logic for simulation, scaling, and drawing

---

## Version Highlights

**New in Version 1.4:**
- Mouse wheel zoom: both orbits and planet visuals scale with zoom
- Improved planet scaling logic and modular scaling functions
- Orbit trail fade effect for clearer visualization
- Cleaner, more extensible code structure

**New in Version 1.3:**
- Improved menu texts
- Frame rate independent physics
- Removed orbit and planet visibility options

---

## Screenshots

![screenshot.png](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-3.png)

---

| v.1.0    | v.1.1    | v.1.2    |
|----------|----------|----------|
| ![v.1.0](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-0.png) | ![v.1.1](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-1.jpg) | ![v.1.2](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-2.png) |
| **Features & Changes** | **Features & Changes** | **Features & Changes** |
| - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets |
| - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard |
| - Toggle Orbits & Planets | - Toggle Orbits & Planets | - **BUGGY: Toggle Orbits & Planets** |
| - Display planet distances to Sun | - Display Distances to the Sun | - Display Distances to the Sun |
|                                | - **NEW: Adjusted Planet & Orbit Sizes** | - **NEW: Overhauled Solar System Creation** |
|                                | - **NEW: 720p resolution** | - **NEW: Overhauled Scaling & Zoom (Additional variables)** |
|                                |                            | - **NEW: Improved Orbit Visuals (Orbit Trail Fade)** |

---

## Setup

Install Python packages and run `main.py`, or fork and run a copy on [replit.com](https://replit.com/@kuranez/Solar-System-Simulation#main.py).

**Dependencies:**
- pygame
- itertools

---

## Roadmap

**Planned Features:**
- Asteroid belt and transneptunian objects
- Mouse controls for zoom and navigation
- Improved scaling and performance for web version (Pyodide/PyScript)
- Use of different planet distances from the sun and real value comparison
- Further visual and code optimizations

---

## Project Structure

- `main.py` — Main loop, event handling, rendering
- `constants.py` — Physical constants, colors, planetary data
- `solarsystem_sim.py` — Sun, Planet, and Body classes for physics and drawing
- `solarsystem_scale.py` — Scaling and planet size calculations
- `CHANGELOG.md` — Detailed version changes
- `DOCUMENTATION_v1.4.md` — Full documentation for v1.4 and later

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
