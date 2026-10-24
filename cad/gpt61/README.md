# XIAO listener mechanical prototype

Open [REVIEW.html](REVIEW.html) for the current render gallery and [DESIGN.md](DESIGN.md) for sources, dimensions, masses, print settings and assembly. The listener uses the owned Seeed XIAO ESP32S3 + Wio-SX1262 kit, INMP441 breakout, one 18650 cell and 0.24 x 19.69 in fiberglass rod. The mic port is 19.69 in above soil.

Included: the one-servo four-dart X500 harness, adjustable 0.31–0.51 in stake adapter and cell holder, and an inert dummy with four ballast portions matching the model's mass and XYZ balance. Nothing has been printed, dropped or flown. Antenna envelopes, B2B spacing, actual weights and manufacturing fits remain MEASURE.

The current revision adds four flat PETG fins on two bonded keyed collars per dart, recomputes the balanced hanger and dummy ballast, and includes pressure and wind estimates in DESIGN.md and out/tail_analysis.json. Flat carriage is retained; the tilt candidates interfere at the head seating. Fin response, turn timing and landing attitude require controlled dummy drops. The four-dart print kit adds 16 fins and eight collars.

Run from the repository root using the CAD interpreter:

```powershell
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/fetch_sources.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/fetch_xiao.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/build.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/validate_exports.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/web_export.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/document.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/record_visual_review.py --reviewed
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/validate_package.py
& 'C:\Users\paulm\.venvs\cad\Scripts\python.exe' cad/gpt61/package.py
```

Inspect every newly generated PNG before running `record_visual_review.py --reviewed`; it records your inspection and cannot inspect images itself. All writes stay here. `parameters.py`, `printed.py`, `purchased.py` and `variants.py` are geometry/mass sources. Cache flags are documented in DESIGN.md.

Captions and human documents use US customary units through `display_units.py`. STEP/STL files and the internal model stay in millimetres; GLBs stay in metres. JSON/CSV keys and numeric values, including `mass_g`, keep their original units. The nozzle and layer settings retain their sold metric values with inch equivalents. Source-register metric references and filament/steel density references are intentional exceptions.

For a caption-only repeat of the earlier unit revision, run `render_us_units.py`, then `web_export.py --render-only`; these reuse the geometry cache; build.py --render-only also creates the three tail figures. Re-run `build.py --verify-only`, `validate_exports.py`, and `web_export.py --no-render --no-install` for validators. Inspect all 38 final PNGs, run `record_visual_review.py --reviewed`, then `validate_us_units.py`, `validate_package.py`, `package.py` and `validate_archive.py` to refresh the receipts and print kit. The US-unit validator now checks the current revision, without the obsolete unchanged-geometry baseline.

`out/` contains 14 printed STEP/STL pairs, current assembly STEP files, bought-part references, print manifest, mass tables, checks, independent export validation and print-kit.zip. STLs are on Z0 in their intended Vyper orientations. Recommended infill is intentionally 100%, including the plate; lightening pockets and tower voids are CAD geometry.

`web/` contains dart.glb, harness.glb, aircraft.glb and stake.glb with an 8-second `explode` clip, metres and Y up. Named nodes and source/mass/uncertainty facts are in [web/manifest.json](web/manifest.json). The stake clip lifts the retained pod from its adapter. These are presentation animations, not physical release simulations. Validators check binary/accessor round trips, trimesh loading, endpoint overlaps and Khronos glTF compliance.
