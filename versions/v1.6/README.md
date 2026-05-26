# 2D Solar System Simulation (v1.6)

2D simulation of our solar system using pygame.  
Based on the [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo) tutorial by [@techwithtim](https://github.com/techwithtim/Python-Planet-Simulation) and inspired by tweaks and additions by [@zerot69](https://github.com/zerot69/Solar-System-Simulation).

## Screenshot

![[Solar-System-Sim/2D-Solar-System-Sim-Link/versions/v1.6/screenshot/Screenshot_v1-6.png]]

## Features

- Main planet orbits and asteroid belt.
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
- math
- itertools

## Project Structure

- `main.py` — Main loop, event handling, rendering with enhanced interactive controls
- `constants.py` — Physical constants, colors, planetary data
- `solarsystem_sim.py` — Enhanced Sun, Planet, and Body classes with orbit tracking
- `solarsystem_scale.py` — Scaling and planet size calculations

# Changelog

## [1.6] - 2025-11-20 (Current Release)

### 🚀 What's New in v1.6

Version 1.6 brings the asteroid belt to life — a procedurally generated main belt rendered between Mars and Jupiter.

#### 🌌 Asteroid Belt Implementation
- Realistic placement: 300+ asteroids positioned between 2.2 and 3.2 AU from the Sun
- Optimized physics: asteroids calculate gravity from the Sun only for maximum performance
- Accurate orbital mechanics: each asteroid follows its own elliptical orbit with slight eccentricity
- Visual clarity: uniform light gray color (192, 192, 192) for easy identification
- Memory efficient: no orbit trails for asteroids to maintain smooth performance

### 📊 Asteroid Belt Specifications
- Number of asteroids: 300 (configurable)
- Inner boundary: 2.2 AU from the Sun
- Outer boundary: 3.2 AU from the Sun
- Asteroid color: Light gray (192, 192, 192)
- Size range: 0.5 to 2 pixels
- Mass: 1×10^15 kg each (negligible gravitational influence)

### 🔄 Upgrade Highlights (from v1.5)
- Asteroid belt: complete main belt implementation with 300+ objects
- Optimized physics: Sun-only gravity calculations for asteroids
- Visual polish: uniform light gray coloring for professional appearance
- Performance retained: smooth operation with hundreds of asteroids

### 📝 Notes
- Major asteroids (Ceres, Vesta, Pallas, Juno) are not individually represented in v1.6; they may appear in later releases as individually-instantiated bodies
- All asteroids share uniform properties for simplicity and performance
- Asteroid-planet gravitational interactions are not simulated


---

## Version History Overview

### [1.5] - Improved UI
- **Added:** Mouse drag navigation, orbit counters, enhanced orbit visualization, orbit completion indicators, improved menu system, time elapsed indicator, screenshot functionality
- **Changed:** UI overhaul with table-based layout, enhanced planet data display, optimized orbit trail rendering
- **Fixed:** Orbit trail memory leaks, UI element positioning, time tracking accuracy

### [1.4] - Code Organization
- **Added:** Mouse wheel zoom, modular architecture, enhanced orbit trails, real-time planet scaling, unified constants
- **Changed:** Refactoring of zoom and scaling system, improved code organization, optimized drawing and update loops
- **Fixed:** Planet size scaling issues, orbit trail fade inconsistencies

### [1.3] - Frame Rate Independence & UI Improvements
- **Added:** Frame rate independent physics and improved menu texts
- **Removed:** Buggy orbit and planet visibility toggles

### [1.2] - Enhanced Visuals & Scaling
- **Added:** Improved orbit visuals with trail fade effect and overhauled scaling

### [1.1] - Size & Resolution Updates
- **Added:** 720p resolution support (1280x720) and adjusted planet sizes

### [1.0] - Initial Release
- **Core Features:** Basic solar system simulation with gravitational physics, keyboard controls, toggle functionality, and planet distance display

---
# Sources

- Tech With Tim's tutorial: [YouTube](https://www.youtube.com/watch?v=WTLPmUHTPqo)
- Article by rastr-0: [teletype.in](https://teletype.in/@rastr_0/solar_system)
- Zerot69's Solar System Simulation: [GitHub](https://github.com/zerot69/Solar-System-Simulation)
- Planetary Data from NASA: [nssdc.gsfc.nasa.gov](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
