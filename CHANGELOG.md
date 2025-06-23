# Changelog

## [1.4a] - 2025-06-23

### Changed
- Refactored zooming logic:
  - Orbits/positions now scale with zoom (using updated scale factor).
  - Planet sizes are recalculated via `calculate_scaled_sizes()` but may not visually update unless reapplied after zoom.
  - Introduced `zoom_factor` to track zoom state.
- Added `solarsystem_scale.py` for scaling logic, allowing planet sizes to scale with zoom.
- Improved modularity: separated scaling logic, centralized constants, and refined drawing code.
- Main loop now updates planet radii based on zoom and recalculates when zoom events occur.

### Known Issue
- **BUG:** As of v.1.4a, only orbits/trails scale with zoom by default; planet sizes may not update visually unless `scaled_sizes` is reapplied after zoom events. This issue is targeted for improvement in v.1.4b.

### Next Goals (for 1.4b)
- Ensure planet sizes always visually scale with zoom, matching orbits/trails.
- Clean up redundant/legacy zoom code and ensure all zoom-related updates are clear and centralized.

---