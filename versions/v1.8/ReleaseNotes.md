# Release Notes - Version 1.8

**Release Date:** May 23, 2026

### 🚀 What's New in v1.8

Version 1.8 marks a major leap in scientific accuracy for the simulation. The initial positions of all planets are now calculated in real-time using high-precision data from NASA's Jet Propulsion Laboratory (JPL), providing an authentic snapshot of the solar system at the moment the simulation begins.

#### 🛰️ **Real-Time Planetary Positions with JPL Ephemerides**
- **High-Precision Data:** Initial planet positions and velocities are now derived from the JPL DE440s ephemeris, the same data used by NASA for space mission navigation.
- **Dynamic Starting Configuration:** Every time you run the simulation, it starts with the planets in their actual current locations in the solar system.
- **Skyfield Integration:** The powerful `skyfield` library has been integrated to handle the complex astronomical calculations, ensuring accuracy and reliability.
- **2D Projection:** The 3D coordinates from the ephemeris are accurately projected onto a 2D plane for visualization.

### 🔄 **Upgrade Highlights**

**From v1.7 to v1.8:**
- ✅ **Dynamic Initial Positions:** Replaced static, manually-defined starting positions with real-time data from JPL.
- ✅ **Enhanced Realism:** The simulation now offers a scientifically accurate representation of the solar system's state.
- ✅ **New Dependency:** Added `skyfield` library for astronomical calculations.

### 🛠️ **Technical Implementation**

- **JPL Ephemeris:** The simulation loads the `de440s.bsp` planetary ephemeris file.
- **Position Calculation:** For each planet, the simulation calculates its 3D vector position and velocity relative to the Sun at the current time.
- **Unit Conversion:** Coordinates and velocities are converted from astronomical units (AU) to the simulation's internal metric system (meters, m/s).
- **2D Projection:** The `x` and `y` components of the 3D vectors are used to place the planets on the 2D screen, creating a top-down view of the ecliptic plane.

### 📋 **New Dependencies**
- **skyfield:** This library is now required to run the simulation. It can be installed via `pip install skyfield`.


### 🔮 **Future Enhancements**
- Integration of major asteroids (Ceres, Vesta) using their real JPL ephemeris data.
- Options to start the simulation at a specific historical or future date.

---

**Download:** [Solar System Simulation v1.8](https://github.com/kuranez/Solar-System-Simulation/releases/tag/v1.8)

**Documentation:** [Full Documentation](4%20GitHub/2D%20Solar%20System%20Simulation/Documentation.md) | [Changelog](Solar-System-Sim/2D-Solar-System-Sim-Link/CHANGELOG.md)

**Support:** [Issues](https://github.com/kuranez/Solar-System-Simulation/issues) | [Discussions](https://github.com/kuranez/Solar-System-Simulation/discussions)

---

**Full Changelog**: https://github.com/kuranez/solar-system-simulation/compare/v.1.7...v.1.8