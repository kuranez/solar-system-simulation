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

![screenshot.png](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-4.png)

---
## Version Comparison

| Version | Screenshot | Key Features & Changes |
|---------|------------|-----------------------|
| **v1.0** | ![v1.0](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-0.png) | - Simulation of inner & outer planets<br>- Adjust scale & speed with keyboard<br>- Toggle orbits & planets<br>- Display planet distances to Sun |
| **v1.1** | ![v1.1](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-1.jpg) | - All v1.0 features<br>- **NEW:** Adjusted planet & orbit sizes<br>- **NEW:** 720p resolution<br>- Display distances to the Sun |
| **v1.2** | ![v1.2](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-2.png) | - All v1.1 features<br>- **NEW:** Overhauled solar system creation<br>- **NEW:** Overhauled scaling & zoom<br>- **NEW:** Improved orbit visuals (trail fade)<br>- **BUGGY:** Toggle orbits & planets |
| **v1.3** | ![v1.3](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-3.png) | - All v1.2 features<br>- Pan view with arrow keys or mouse edges<br>- **NEW:** Improved menu texts<br>- **NEW:** Frame rate independent physics<br>- **NEW:** Removed buggy orbit/planet toggles |
| **v1.4** | ![v1.4](https://raw.githubusercontent.com/kuranez/Solar-System-Simulation/refs/heads/main/screenshots/Screenshot_v1-4.png) | - All v1.3 features<br>- **NEW:** Mouse wheel zoom (scales orbits & planets)<br>- **NEW:** Enhanced orbit trail fade effect<br>- **NEW:** Modular code structure |


---

## Setup

Install Python packages and run `main.py`, or fork and run a copy on [replit.com](https://replit.com/@kuranez/Solar-System-Simulation#main.py).

**Dependencies:**
- pygame
- itertools

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
