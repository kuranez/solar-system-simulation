# Changelog

## [1.4] - 2025-06-27 (Final)

### Current Repository State
This version represents the final v.1.4 release with the following core files:
- `constants.py` — Physical constants, colors, and planetary data
- `main.py` — Main loop, event handling, and rendering
- `solarsystem_scale.py` — Scaling and planet size calculations  
- `solarsystem_sim.py` — Sun, Planet, and Body classes for physics and drawing

### Added
- **Mouse wheel zoom:** Both orbits and planet visuals scale dynamically with zoom
- **Modular architecture:** Separated scaling logic into dedicated `solarsystem_scale.py`
- **Enhanced orbit trails:** Improved fade effect for clearer visualization
- **Real-time planet scaling:** Planet sizes update immediately with zoom changes
- **Unified constants:** Centralized all physical and visual constants

### Changed
- Complete refactoring of zoom and scaling system
- Planet sizes now scale proportionally with zoom level
- Improved code organization and modularity
- Optimized drawing and update loops
- Enhanced user interface with better navigation instructions

### Fixed
- Planet size scaling issues during zoom operations
- Orbit trail fade inconsistencies
- Code redundancy in scaling calculations

---

## Version History Overview

### [1.3] - Frame Rate Independence & UI Improvements
- **Added:** Frame rate independent physics
- **Added:** Improved menu texts and navigation instructions
- **Removed:** Buggy orbit and planet visibility toggles
- **Changed:** Enhanced user interface layout
- **Files:** Basic structure with main simulation files

### [1.2] - Enhanced Visuals & Scaling
- **Added:** Improved orbit visuals with trail fade effect
- **Added:** Overhauled scaling and zoom system with additional variables
- **Added:** Overhauled solar system creation process
- **Changed:** Better visual representation of planetary orbits
- **Known Issues:** Toggle orbit/planet functionality became buggy

### [1.1] - Size & Resolution Updates  
- **Added:** Adjusted planet and orbit sizes for better visibility
- **Added:** 720p resolution support (1280x720)
- **Changed:** Improved planet size scaling relative to distances
- **Maintained:** All core simulation features from v1.0

### [1.0] - Initial Release
- **Core Features:** 
  - Simulation of inner and outer planets
  - Keyboard controls for scale and speed adjustment
  - Toggle functionality for orbits and planets
  - Display of planet distances to the Sun
- **Foundation:** Basic solar system simulation with gravitational physics

---

## [1.3] and earlier - Detailed History

See the [README.md](../README.md) for older feature lists and screenshots.

---