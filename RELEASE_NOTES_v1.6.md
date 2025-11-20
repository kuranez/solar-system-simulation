# Release Notes - Version 1.6

**Release Date:** November 20, 2025  

### 🚀 What's New in v1.6

Version 1.6 brings the asteroid belt to life! This release adds the main asteroid belt between Mars and Jupiter.

#### 🌌 **Asteroid Belt Implementation**
- **Realistic placement** - 300+ asteroids positioned between 2.2 and 3.2 AU from the Sun
- **Optimized physics** - Asteroids calculate gravity from the Sun only for maximum performance
- **Accurate orbital mechanics** - Each asteroid follows its own elliptical orbit with slight eccentricity
- **Visual clarity** - Uniform light gray color (192, 192, 192) for easy identification
- **Memory efficient** - No orbit trails for asteroids to maintain smooth performance

### 🎮 **Controls** (Unchanged)

| Control | Action |
|---------|--------|
| **Mouse Wheel** | Zoom In/Out |
| **Left Click + Drag** | Move View |
| **[+] / [-]** | Adjust Speed |
| **[F12]** | Take Screenshot |
| **[ESC]** | Quit Simulation |

### 📊 **Asteroid Belt Specifications**
- **Number of asteroids**: 300 (configurable)
- **Inner boundary**: 2.2 AU from the Sun
- **Outer boundary**: 3.2 AU from the Sun
- **Asteroid color**: Light gray (192, 192, 192)
- **Size range**: 0.5 to 2 pixels
- **Mass**: 1×10¹⁵ kg each (negligible gravitational influence)

### 🔄 **Upgrade Highlights**

**From v1.5 to v1.6:**
- ✅ **Asteroid belt** - Complete main belt implementation with 300+ objects
- ✅ **Optimized physics** - Efficient Sun-only gravity calculations
- ✅ **Visual polish** - Uniform light gray coloring for professional appearance
- ✅ **Performance maintained** - Smooth operation even with hundreds of asteroids

### 📋 **System Requirements**
- Python 3.7+
- pygame library
- 1280x720 minimum screen resolution recommended
- Mouse with scroll wheel for optimal experience
- Fullscreen mode supported

### 💡 **Usage Tips**
- **Zoom to asteroid belt** - Use mouse wheel to zoom in and see the asteroid belt clearly
- **Pan for exploration** - Drag the view to explore different regions of the asteroid belt
- **Compare scales** - Observe the relative sizes of planets and asteroid distribution
- **Capture the belt** - Press F12 to save screenshots showing the asteroid belt

### 🛠️ **Technical Implementation**

#### Asteroid Belt Generation
- **Random distribution** - Asteroids placed at random angles around the Sun
- **Orbital distance variation** - Random distances between 2.2-3.2 AU
- **Velocity calculation** - Circular orbital velocity with random eccentricity (±5%)
- **Color uniformity** - All asteroids use consistent light gray (192, 192, 192)

#### Performance Optimization
- **Simplified physics** - Only Sun gravity calculated, no planet interactions
- **Screen culling** - Asteroids outside viewport are not rendered
- **No orbit trails** - Reduces memory usage and improves performance
- **Efficient rendering** - Simple circle drawing with minimal overhead

### 🔮 **Future Enhancements**
While this version focuses on the general asteroid belt, future updates may include:
- Major asteroids (Ceres, Vesta, Pallas, Juno) with realistic sizes and properties
- Toggle to show/hide asteroid belt

### 🔄 **Upgrade Path**
Version 1.6 maintains full compatibility with v1.5 while adding the asteroid belt feature. All existing functionality remains unchanged. The asteroid belt is automatically generated and rendered alongside planets, requiring no configuration changes.

### 📝 **Notes**
- Major asteroids (Ceres, Vesta, etc.) are not individually represented in this version
- All asteroids have uniform properties for simplicity and performance
- Asteroid-planet gravitational interactions are not simulated
- The belt provides visual representation rather than scientifically accurate individual asteroid tracking

---

**Download:** [Solar System Simulation v1.6](https://github.com/kuranez/Solar-System-Simulation/releases/tag/v1.6)

**Documentation:** [Full Documentation](DOCUMENTATION.md) | [Changelog](CHANGELOG.md)

**Support:** [Issues](https://github.com/kuranez/Solar-System-Simulation/issues) | [Discussions](https://github.com/kuranez/Solar-System-Simulation/discussions)
