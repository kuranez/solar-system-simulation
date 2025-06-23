# Changelog

## [1.4b] - Unreleased

### Changed
- Planet sizes now always visually scale with zoom, matching orbits/trails.
- Refined scaling logic in `solarsystem_scale.py` for better consistency.
- Updated `main.py` to ensure planet radii are updated after every zoom/pan event.

---

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
- **BUG:** As of v.1.4a, only orbits/trails scale with zoom by default; planet sizes may not update visually unless `scaled_sizes` is reapplied after zoom events. This issue is targeted for improvement in 1.4b.

---

## [1.4] - 2025-06-20

### Added
- Mouse wheel zoom that scales both orbits and planet visuals.
- Planet size scaling logic using `solarsystem_scale.py`.
- Improved orbit fade effect.

### Changed
- Modularized code: separated physics, scaling, and UI.
- Unified constants in `constants.py`.

### Known Issues
- Some redundant logic in how planet sizes are updated on zoom.
- Outer planets may appear too large at extreme zoom.

---

## [1.3] and earlier

See the [README.md](../README.md) for older feature lists and screenshots.

---