# Solar System Simulation

2D simulation of our solar system using pygame.  
Based on the [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo) tutorial by [@techwithtim](https://github.com/techwithtim/Python-Planet-Simulation) and inspired by tweaks and additions by [@zerot69](https://github.com/zerot69/Solar-System-Simulation).

---

## Features

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

---

## Version Highlights

**New in Version 1.5:**
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

![screenshot.png](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-5.png)

---

| v.1.0    | v.1.1    | v.1.2    | v.1.3    | v.1.4    |
|----------|----------|----------|----------|----------|
| ![v.1.0](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-0.png) | ![v.1.1](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-1.jpg) | ![v.1.2](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-2.png) | ![v.1.3](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-3.png) | ![v.1.4](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-4.png) |
| **Features & Changes** | **Features & Changes** | **Features & Changes** | **Features & Changes** | **Features & Changes** |
| - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets | - Simulation of Inner & Outer Planets |
| - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard | - Adjust Scale & Speed with Keyboard |
| - Toggle Orbits & Planets | - Toggle Orbits & Planets | - **BUGGY: Toggle Orbits & Planets** | - Pan view with arrow keys or mouse edges | - Pan view with arrow keys or mouse edges |
| - Display planet distances to Sun | - Display Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun | - Display Distances to the Sun |
|                                | - **NEW: Adjusted Planet & Orbit Sizes** | - **NEW: Overhauled Solar System Creation** | - **NEW: Improved menu texts** | - **NEW: Mouse wheel zoom: both orbits and planet visuals scale with zoom** |
|                                | - **NEW: 720p resolution** | - **NEW: Overhauled Scaling & Zoom (Additional variables)** | - **NEW: Frame rate independent physics** | - **NEW: Improved planet scaling logic and modular scaling functions** |
|                                |                            | - **NEW: Improved Orbit Visuals (Orbit Trail Fade)** | - **NEW: Removed buggy orbit/planet toggles** | - **NEW: Orbit trail fade effect for clearer visualization** |
|                                |                            |                                                        |                                         | - **NEW: Cleaner, more extensible code structure** |

---

## Setup

Install Python packages and run `main.py`, or fork and run a copy on [replit.com](https://replit.com/@kuranez/Solar-System-Simulation#main.py).

**Dependencies:**
- pygame
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
- **Web version:** Refactor rendering logic to support a JavaScript/Pyodide frontend.
- **Additional Objects:** Asteroid belt and transneptunian objects

---

## Project Structure

- `main.py` — Main loop, event handling, rendering with enhanced interactive controls
- `constants.py` — Physical constants, colors, planetary data
- `solarsystem_sim.py` — Enhanced Sun, Planet, and Body classes with orbit tracking
- `solarsystem_scale.py` — Scaling and planet size calculations
- `CHANGELOG.md` — Detailed version changes
- `DOCUMENTATION.md` — Full documentation for current version

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
