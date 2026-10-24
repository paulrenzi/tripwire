# XIAO listener and X500 release harness: first-print revision

The current tail-fin revision adds four flat-print panels and two keyed collars per dart, moves the hanger to the new balance point and re-solves the inert dummy. Pressure and wind figures below are estimates; no fall has been tested.

## Changes from the Heltec version

The incorrect Heltec/OLED package has been replaced throughout the current assemblies, renders and web models by the owned Seeed XIAO ESP32S3 + Wio-SX1262 kit. The original brief and downloaded legacy sources are retained as history. Old model outputs have been removed.

| Model estimate | Old Heltec package | New XIAO package |
| --- | --- | --- |
| Populated processor/radio boards | 0.32 oz | 0.14 oz |
| Printed pod shell/lid/cap | 1.05 oz | 0.90 oz |
| Dart | 5.58 oz | 5.91 oz |
| Harness | 6.47 oz | 6.47 oz |
| Four darts + harness | 1.80 lb | 1.88 lb |
| Hanger from tip | 10.462 in | 10.891 in |

Per the firmware brief, the listener reports alive by radio once per minute. That heartbeat replaces a visual status indication. Native OEM CAD may retain inactive onboard component bodies; no added LED, display or battery-divider circuit is fitted. A smaller cell could reduce nose mass, but its runtime and impact retention need testing; the specified 18650 remains in the real listener models.

The electronics tray is now 1.81 x 1.26 in rather than 3.23 x 1.42 in, with a narrow socket neck that preserves the 19.69 in rod and raises the sound port to 19.69 in above soil (previously 18.50 in). There is no display window, added status LED or voltage-divider part. A removable end cap exposes USB-C and pin access to both BOOT/RESET buttons. Three lid screws replace four; the kit LoRa FPC sits on a light integral top backer. Five mic wires and direct underside BAT connections replace the old board wiring. A stake adapter, separate 18650 stake cradle and an inert ballasted dummy are included.

**Nothing has been printed, drop-tested or flown.** These are nominal geometry and mass estimates, not measured hardware qualification. The actual kit stack spacing, microphone breakout, antenna dimensions, printed fits and filament properties still require measurement. No self-righting, soil penetration, waterproofing, acoustic or radio range result is claimed.

## Display and file units

All dimensions in these notes and render labels use decimal inches; most dimensions use two decimals, and fits, clearances, tolerances and thin walls/film use three. Numerical solver residuals retain extra digits to avoid hiding the nominal match. Mass is in ounces to two decimals, or pounds for totals above one pound; small volumes retain significant digits. Densities are in lb/in³ with the original g/cm³ reference. Source metric figures appear in parentheses only in the source register; nozzle and layer settings retain the explicitly requested metric labels. Sold part names M2, M2x6, M2x8, M3, RX-M2x4, 18650, INR18650-25R, SG90, T18R and DIN934 are unchanged. Source and history files retain their original wording.

**The model and manufacturing units have not changed.** STEP and STL files stay in millimetres; slicers read STL as mm, so rescaling would break printing. GLBs stay in metres, as required by glTF. Machine-readable JSON/CSV field names and unit conventions stay unchanged; numeric values follow the revised geometry, including `mass_g` in `web/manifest.json`. `parameters.py` and the build code still compute in millimetres internally. `display_units.py` converts captions and human reports only. The tail-fin revision changes geometry and recomputes its dependent numeric values.

## Files and reproduction

[REVIEW.html](REVIEW.html) indexes all current renders. `out/` contains fourteen printed STEP/STL pairs, current bought-part CAD, carried/mid-release/stood aircraft assemblies, a stood dart, stake and dummy assemblies, mass/check reports, print manifest and `print-kit.zip`. All STLs are already placed on Z0 in the intended Vyper print orientation; STEP files retain assembly datums. Forty-two functional printed pieces make four real darts and one harness; the coupon, stake and dummy parts are optional alternatives/tools.

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

Inspect every newly generated PNG before running `record_visual_review.py --reviewed`; that command records an explicit inspection attestation and cannot perform visual review itself. All scripts write only in this package. `build.py --render-only`, `--exports-only` and `--verify-only` reuse its generated cache. Rebuild normally after any dimension/mass/source change. `sources/manifest.json` and `sources/xiao-manifest.json` retain source URLs, sizes and hashes.

## Primary source register

- **S1: [Holybro X500 V2 official frame CAD and assembly](https://holybro.com/collections/multicopter-kit/products/px4-development-kit-x500-v2).** Unscaled OEM STEP: centre plates, arms, motors, skids, payload rails and clamps; duplicate solids removed, original indices retained. Rail spacing 2.362 in (60 mm), CAD OD 0.370 in (9.4 mm); design clearance uses catalog 0.394 in (10 mm).
- **S2: [Holybro motor and prop drawing](https://cdn.shopify.com/s/files/1/0604/5905/7341/files/X500MotorSpec.png?v=1678791632).** Conservative 10.236 in (260 mm) prop swept diameter; fitted plane and 0.157 in (4 mm) slab thickness remain MEASURE. Translucent swept discs are clearance volumes, not propeller blades.
- **S3: [TowerPro SG90 drawing](https://towerpro.com.tw/product/sg90-7/).** 0.894 x 0.480 x 1.063 in (22.7 x 12.2 x 27 mm) case, 1.272 in (32.3 mm) tab span, 0.32 oz (9 g) catalog mass and 25.00 oz·in (1.8 kg.cm) stall torque. Horn, spline, mounting holes and exact batch remain MEASURE.
- **S4: [Seeed kit wiki: both OEM STEP archives, schematic and XIAO DXF](https://wiki.seeedstudio.com/xiao_esp32s3_&_wio_SX1262_kit_for_meshtastic/).** Native XIAO ESP32S3 STEP and Wio-SX1262-for-XIAO STEP used without scaling. B2B kit connection, USB flashing and underside battery-pad connection are documented here. sources/xiao-manifest.json records exact download URLs and SHA256.
- **S4a: [Seeed XIAO ESP32S3 dimensions and pin map](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).** 0.827 x 0.701 in (21 x 17.8 mm) PCB nominal; D3=GPIO4, D4=GPIO5, D5=GPIO6. Native STEP includes USB-C, BOOT/RESET and WiFi U.FL. Archive top/bottom images identify BAT pads and castellated pins.
- **S4b: [Seeed bare kit SKU 102010611 and included FPC antenna](https://www.seeedstudio.com/Wio-SX1262-with-XIAO-ESP32S3-p-5982.html).** Manufacturer identifies separate WiFi and LoRa antennas and included FPC. No dimensioned antenna drawing was found. Both antenna envelopes, masses and coax lengths are MEASURE. The kit FPC is not the optional 7.677 in (195 mm) SMA antenna.
- **S4c: [Wio-SX1262 radio-module datasheet](https://files.seeedstudio.com/products/SenseCAP/Wio_SX1262/Wio-SX1262_Module_Datasheet.pdf).** Bare radio module 0.457 x 0.433 x 0.116 in (11.6 x 11 x 2.95 mm) is NOT the complete extension board. Extension outline comes from its kit-specific OEM STEP, not this module envelope.
- **S4d: [Rokland XIAO ESP32S3 + Wio-SX1262 kit](https://store.rokland.com/products/seeed-studio-xiao-esp32s3-wio-sx1262-kit-for-meshtastic-lora).** Retailer identifies SKU 102010611 and links the same kit-specific Seeed Wio STEP and schematic. It supplies no additional antenna dimensional drawing; confirm the actual shipped antenna batch.
- **S5: [Samsung INR18650-25R manufacturer specification mirror](https://files.dcpower.eu/datasheets/samsung/INR18650-25R-datasheet.pdf).** 0.722 ± 0.003 in (18.33 ± 0.07 mm) diameter, 2.553 ± 0.006 in (64.85 ± 0.15 mm) length, 1.59 oz (45 g) maximum. Keep flat-top cell and existing cradle. Terminal/insulator details and actual mass MEASURE.
- **S6: [TDK INMP441 outline](https://product.tdk.com/en/search/sw_piezo/mic/mems-mic/info?part_no=INMP441).** Bare IC 0.186 x 0.148 x 0.039 in (4.72 x 3.76 x 1 mm), bottom port 0.010 in (0.25 mm). Generic breakout 0.551 x 0.630 x 0.039 in (14 x 16 x 1 mm) and its hole/pads/mass remain MEASURE.
- **S6a: [TDK AN1124 microphone sealing guidance](https://invensense.tdk.com/wp-content/uploads/2015/02/Recommendations-for-Sealing-InvenSense-Bottom-Port.pdf).** Prototype soft film and 0.031 in (0.8 mm) acoustic cavity are design assumptions; acoustic transfer and water resistance untested.
- **S7: [HellermannTyton T18R UV-stable tie](https://www.hellermanntyton.com.br/produtos/abracadeiras-com-serrilhado-interno/t18r/111-01711).** 3.937 x 0.098 x 0.039 in (100 x 2.5 x 1 mm) strap, 17.98 lbf (80 N) catalog minimum loop strength; installed closed loops reconstructed.
- **S8: [3M5490 PTFE film tape](https://multimedia.3m.com/mws/media/2522949O/3m-ptfe-extruded-film-tape-5490.pdf).** 0.004 in (0.09 mm) total thickness. Friction coefficient 0.12 is an engineering assumption, not a manufacturer specification.
- **S9: [Ruthex RX-M2x4 insert CAD](https://www.ruthex.de/products/ruthex-gewindeeinsatz-m2-70-stuck-rx-m2x4-messing-gewindebuchsen).** Actual knurled manufacturer STEP. 0.142 in (3.6 mm) OD, 0.157 in long; 0.126 in (3.2 mm) pilot and 0.205 in (5.2 mm) pocket are design fit choices.
- **S10: [M2 hex nut dimensions](https://www.accu.co.uk/hexagon-nuts/655596-HPN-M2-PCN).** DIN934 envelope 0.157 in across flats x 0.063 in (1.6 mm) height; metal nuts modelled. Dummy traps have side-loading slots.

Native CAD inspection reports are `sources/xiao-cad-inspection.json` and `sources/wio-cad-inspection.json`. XIAO PCB envelope in its original model is 0.825 x 0.700 in (20.955 x 17.780 mm); USB projection makes the full length 0.885 in (22.482 mm). Wio extension PCB envelope is 0.844 x 0.700 x 0.063 in (21.440 x 17.780 x 1.6 mm), including its outline tab; its supplied model spans 0.287 in (7.3 mm) vertically including the underside connector. Neither CAD has been scaled to make the nominal 0.827 in (21 mm) dimension fit. The source XIAO model lacks a resolved mating B2B connector, so its envelope is reconstructed and flagged MEASURE.

## Pod, wiring and service

The 1.81 x 1.26 in rounded tray has 0.063 in walls and floor, 0.67 in seam height and 0.079 in lid. Its narrow 0.54 in socket neck extends from X 18.90 in to X 21.22 in; the rod enters 0.79 in and stops at X 19.69 in. The hollow riser carries the two power wires from the rod to the shorter electronics tray, which begins at X 21.10 in. This axial neck is needed because a 19.69 in rod buried 2.76 in ends only 16.93 in above soil, while the mic must be at 19.69 in. Reducing tray length without this offset would lower the microphone.

The XIAO rests on four underside edge supports. The Wio extension plugs into the kit B2B connector above it; the model places Wio PCB bottom at Z 0.41 in, with a 0.45 in overall stack envelope. The 0.30 in mating offset is MEASURE; verify it before printing. Lid fingers compress four 0.039 in foam pads against Wio PCB edges, away from the RF can. No soldered tall pin headers are fitted. Locating fences have about 0.012 in clearance outside the XIAO edges.

The mic board stands along the negative Y wall, with its bottom port at X 22.44 in, Z 0.31 in. Its actual port is 19.69 in above the body soil stop. A 0.16 in cavity, 0.031 in annular silicone spacer and 0.002 in soft prototype film connect it to the side opening under an integral 45 degree rain hood. Breakout dimensions and pad/hole placement are MEASURE. Do not assume the waterproof/acoustic performance of this untested membrane.

| INMP441 connection | XIAO pad | GPIO |
| --- | --- | --- |
| SCK / BCLK | D3 | 4 |
| WS / LRCLK | D4 | 5 |
| SD / data | D5 | 6 |
| VDD | 3V3 | Supply |
| GND and L/R select | GND | Ground |

Five short insulated wires are modelled; the microphone L/R select is a local solder bridge to ground, not a sixth long wire. Wire dress and exact solder points remain MEASURE. The long cell pair runs in the original body gutter and along the rod, enters the socket neck through relieved ducts and terminates at the XIAO underside BAT+/BAT- pads. Sourced bottom-view images identify these pads; their small copper envelopes/centres are reconstructed. The XIAO charger does not provide a mechanical battery connector. Use factory-welded insulated cell leads, never solder directly to the can. Verify the actual cell protection arrangement; charger presence alone does not establish pack protection.

The kit LoRa FPC has an explicitly unmeasured 3.94 x 0.39 x 0.012 in nominal envelope; its separate U.FL coax exits a 0.087 in gland above the microphone. A 0.047 in PETG backer extends from the lid, with small tape/tie slots; its outer face is coplanar with the lid so both print flat together. The socket neck floor is also coplanar with the tray base; its teardrop duct has at least 0.067 in roof thickness. Strain-relieve the coax before it reaches U.FL, and seal the gland with removable neutral-cure silicone. The separate WiFi/BLE FPC is on the positive Y wall. Do not replace these with the optional 7.68 in SMA antenna without recomputing mass, balance and clearance. The default overall dart length is 27.01 in; the larger figure than the old 25.35 in package comes from the deliberately provisional FPC envelope.

A 0.75 x 0.55 in end opening gives access to USB-C and a 0.028 in pin path to either button with the printed cap removed. The cap has 0.012 in skirt clearance and a 0.047 in overlapping flange. Seal its perimeter with a removable thin silicone bead or weather tape; it is a prototype service closure, not a tested IP seal. The full pod lid need not be removed to flash. Cable overmould envelope 0.43 x 0.24 in is MEASURE. The lid perimeter has a 0.059 x 0.035 in gland for 0.047 in cord (25% nominal compression); three RX-M2x4 inserts and M2x6 screws clamp it. RTV, solder and service tape are not resolved as exact solids or weighed consumables.

## Tail fins, pressure estimate and flat carriage

Four identical trapezoidal PETG fins sit at 50, 130, 230 and 310 degrees around the rod on two separate slotted collars. The 80/100 degree spacing tilts them closer to vertical so a descending fin clears the next dart's microphone rain hood. Each fin has a 6.46 in root chord, 5.04 in tip chord, 0.59 in exposed radial span and 0.047 in thickness. Its root runs from 14.49 in to 20.94 in from the tip. Maximum radius from the rod axis is 1.02 in; the diagonal orientation limits carried width to about 1.35 in. Four fins add side area in both pitch and yaw.

The two collars begin at 15.28 in and 17.95 in from the tip, each 0.31 in long, with 0.71 in OD and a 0.248 in bore. Two tabs per fin seat in open axial keyways with 0.010 in total thickness clearance and 0.016 in total axial clearance. The fins print on their full broad face; the collars print on an axial end face with vertical bore/keyways. Both need no supports. PETG is solid at the existing profile.

Install the collars and four fins before the pod. Dry-fit all eight tabs; align the open wire reliefs on the cell-wire side and keep them free of adhesive. Bond both collar bores and all fin tabs using a PETG-compatible adhesive verified by a coupon. Roughen/clean the rod locally and hold the panel angles while curing. The mass model includes 0.02 oz total cured adhesive as a MEASURE allowance; the CAD bond films are representative, not exact fillets. Weigh the actual cured build, and use the same joints and fins on the dummy. Joint strength, fin stiffness and long-term creep are untested. Do not rely on a loose sliding collar or on keyway friction. Service requires debonding; the exploded layout identifies the pieces without claiming a reversible dry assembly.

The fin tips stay inside the available dart spacing. This trades away the span of a larger lawn-dart tail: the long chord supplies area while the diagonal panels preserve clearance. No fin, collar or pod scaling is used during release. The tail already sits below and beyond the deck; it does not need to pass through the head slots. Only the head and post cross those gaps. Full-size geometry is included in carried, mid-release, vertical extraction, later prescribed pitch, stood, dummy and web assemblies. The microphone corridor, removable USB cap and complete antenna strip remain unobstructed. This is a span-constrained prototype, not an optimized aerodynamic design.

The limiting sampled fin-to-neighbour-pod gap is **0.056 in**, measured by true B-rep closest distance, at **0.591 in downward extraction** of dart 1 beside dart 2. This is nominal CAD separation, not a tolerance or flex guarantee.

The pressure calculation uses uniform pressure on the union of the actual projected side silhouettes: **CP = sum(projected area x area-centroid distance) / sum(projected area)**. Rod, body including cell, pod, antenna strip/backer, fins and collars are projected onto the longitudinal/transverse plane; occupied pixels remove hidden rod and overlapping fin area. This is a cardboard-cutout estimate. It does not assign validated small-angle force coefficients. `tail_analysis.py` repeats rolls from 0 through 165 degrees in 15 degree steps and halves the raster pitch at each sampled worst case. `out/tail_analysis.json` retains all component areas and centroid distances, both geometries/masses and convergence results.

Aim: at least **2 body widths** behind the CG at the sampled worst roll, to give a visible geometric restoring lever despite uncertainty. One body width means the cradle/gutter breadth **1.469 in**; it excludes the tall hanger. This is a design screen, not a standard or a demonstrated fall-stability requirement. The same denominator is used before and after.

| Model estimate | Before fins | With fins |
| --- | --- | --- |
| Dart mass | 5.22 oz | 5.91 oz |
| CG from tip | 10.017 in | 10.891 in |
| CP from tip, sampled minimum margin | 11.854 in | 13.951 in |
| Static margin, sampled minimum | 1.837 in | 3.059 in |
| Static margin / body width | 1.25 | 2.08 |
| Sampled CP range | 11.854 in to 13.075 in | 13.951 in to 14.636 in |

The old cutout can already place its estimated CP behind its CG because the long pod/antenna has side area. That result does not establish enough restoring force near nose-down, a safe turn from level or adequate damping. The fins add deliberate surfaces in both steering planes; a positive area margin still does not demonstrate self-righting. The model starts at zero fall speed, when this aerodynamic moment is zero. Fin stall, changing pressure distribution, flexibility, pod wakes, angular inertia, propwash and gusts remain unknown. No turn time, minimum release height, upright landing or drop survival is claimed. The dummy drop test must establish the response.

The hanger moves with the new mass solution to **10.891 in from the tip**; its lateral axis follows the new CG. Four darts alone weigh **1.48 lb**; four darts plus the unchanged harness weigh **1.88 lb**. The dummy is re-solved with the same fins, collars and adhesive to match the new mass and all three first moments; matching inertia and aerodynamic response is still approximate.

**Keep flat carriage at the balance point.** A hanger slightly ahead of the CG, toward the point, would make the tail sag and the point rise. To start nose-down under gravity, the support must be slightly aft of the CG, toward the fins. Both signs were recomputed with the moved post mass rather than merely rotating the old drawing.

| Hanger relative to CG | Gravity equilibrium, nose-down positive | Rigid head seating |
| --- | --- | --- |
| Toward point by 0.197 in | -6.88 degrees | Interferes with rotor/plate |
| At CG | -0.00 degrees | Clear |
| Toward tail by 0.197 in | 6.88 degrees | Interferes with rotor/plate |

An aft support could give an initial nose-down bias and shorten the required turn, but it lifts the long tail toward the aircraft, lowers the point toward the ground and puts the round head on an edge. The seating probe finds solid interference with the present horizontal support geometry, so the tilted alternatives are rejected before release qualification. Edge loading/wedging would also change extraction friction. Flat carriage preserves the full-head bearing surface and existing release path; its rotation must begin aerodynamically after release, with timing still unknown. Neither offset option is being advertised as a checked release configuration.

### Wind estimate

A finned dart tends to align with the air it falls through, which can incline its point into the wind rather than vertically. The requested no-drag arithmetic assumes release from rest, no horizontal ground speed, steady wind, vertical impact speed **sqrt(2 x gravity x height)** with **g = 32.174 ft/s²**, and perfect alignment. Tilt from vertical is **atan(wind / vertical impact speed)**.

| Drop | No-drag impact speed | 5 mph wind | 10 mph wind | 15 mph wind |
| --- | --- | --- | --- | --- |
| 16 ft | 32.1 ft/s (21.9 mph) | 12.9 degrees | 24.6 degrees | 34.4 degrees |
| 33 ft | 46.1 ft/s (31.4 mph) | 9.0 degrees | 17.7 degrees | 25.5 degrees |
| 49 ft | 56.2 ft/s (38.3 mph) | 7.4 degrees | 14.6 degrees | 21.4 degrees |

**This is an estimate, not a test or a landing prediction.** Vertical drag lowers the impact speed and increases this tilt for an unchanged relative crosswind. Horizontal drag also accelerates the dart downwind and reduces the relative crosswind, which can reduce tilt; the net result needs coupled flight dynamics or measurements. Fin alignment may lag or oscillate and may not complete in a short drop. These numbers provide neither drift/aim accuracy nor permission to assume an upright impact. `dart_fall_sequence.png` shows illustrative attitudes only; pose spacing is neither time nor distance.

Primary references for the qualitative CG/CP criterion and the simplified calculation are [NASA Glenn: generalized center of pressure](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/generalized-center-of-pressure/), [conditions for stability](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/conditions-for-rocket-stability/) and [falling objects with air resistance](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/falling-object-with-air-resistance/). Applying the cutout method to this irregular, initially horizontal dart is an engineering estimate, not validation by those references.

## Body, balance and harness

The body retains the specified 0.24 x 19.69 in fiberglass spine, 2.76 in nose/soil stop, flat-top 18650 open snap cradle, axial sleeve, integral post and wire gutters. Three short 0.234 in nominal press lands sit in a 0.250 in relieved teardrop bore; the coupon determines the actual fit. Four 0.047 in thick, 0.71 in long cantilevers retain the cell through a 0.66 in throat with lead-in ramps. Axial end walls take impact load rather than the flexible latch tips. The rod tip is a 0.47 in cone with a 0.024 in blunt point for the nominal CAD envelope.

The mass solver moves the post and its sleeve until its X/Y axis agrees with the recomputed dart centre of mass. The nominal CG is **(10.891, 0.243, 0.337) in**; the hanger is **X 10.891 in, Y 0.243 in** from the tip/rod datum. Residual X error is 0.000076 in. This numerical residual is not a real assembly tolerance; weighed stock and printed mass control actual balance.

The existing harness geometry is retained after rechecking the finned darts and their moved hangers: 3.27 in deck radius, 0.13 in deck, 1.89–2.01 in bearing ridge, 2.56 in rotor radius, 0.13 in rotor web and 20 degree release gaps. Slots are 0.80 x 0.61 in for 0.51 in heads and 0.20 in necks. The pilot has 0.010 in radial clearance. Payload rail centres are 2.36 in apart; saddles use 0.42 in seats and four T18R ties. Tall towers are explicitly hollow CAD geometry, not a density multiplier.

The load path remains head -> rotor rim -> PTFE-covered bearing ridge -> plate -> saddles/rails. The SG90 stock horn drives two 0.71 in-spaced M2 studs with axial slip; a keeper washer has 0.016 in running gap and does not clamp the rotor onto the servo shaft. The model checks the case, horn, nuts, pilot and rotor throughout the release sequence. Dart 1 releases at 16 degrees, dart 3 at 32, dart 2 at 48 and dart 4 at 64. Servo travel, torque under friction, creep and shock remain physical qualification items.

## Masses and print settings

**Recommended prototype infill is 100% for every printed part, including the plate.** This is intentional: load-carrying skins/ribs and small fit features should be solid for the first test; large lightening pockets and tower cores are already removed in CAD. The plate estimate is its actual model volume times 0.0459 lb/in³ (1.27 g/cm³) PETG, with no hidden 35% or other infill multiplier. A lighter slicer profile would require a fresh sliced/printed mass and structural assessment. No slicer has been run and no part has been weighed; actual extrusion width, perimeter overlap, holes and filament density will change the result.

| Printed design | Mass at 100% | CAD volume |
| --- | --- | --- |
| body | 1.50 oz | 2.04049 in³ |
| pod_shell | 0.67 oz | 0.912003 in³ |
| pod_lid | 0.20 oz | 0.274225 in³ |
| usb_cap | 0.03 oz | 0.0440002 in³ |
| plate | 4.64 oz | 6.32714 in³ |
| rotor | 1.36 oz | 1.85579 in³ |
| fit_coupon | 0.16 oz | 0.215855 in³ |
| stake_adapter | 0.47 oz | 0.642894 in³ |
| stake_cell_holder | 1.08 oz | 1.46774 in³ |
| dummy_body | 1.83 oz | 2.49432 in³ |
| dummy_lid | 0.14 oz | 0.195827 in³ |
| dummy_head_insert | 0.07 oz | 0.089959 in³ |
| tail_fin | 0.12 oz | 0.167494 in³ |
| tail_collar | 0.07 oz | 0.0886739 in³ |

| Assembly | Nominal mass |
| --- | --- |
| One real dart | 5.91 oz |
| Harness including servo/hardware/ties | 6.47 oz |
| Four real darts + harness | 1.88 lb |
| Inert dummy with ballast | 5.91 oz |

Complete stake installation, including the full 48.00 in nominal 0.39 in stake and 18650: **10.90 oz**. Stake density and all small-stock masses are unmeasured; this total is separate from flight payload.

Full per-component machine-unit masses, volumes, assumptions and XYZ centroids are in [out/mass_properties.csv](out/mass_properties.csv) and [out/mass_properties.json](out/mass_properties.json), including auxiliary printed and dummy parts. Board masses 0.08 oz XIAO/0.06 oz Wio, 0.04 oz mic, 0.03 oz LoRa antenna and 0.01 oz WiFi antenna are unmeasured estimates; the 1.59 oz cell figure is a datasheet maximum. Hardware uses nominal material density and shape centroids. Solder, final adhesive, tape and small protection/connector additions require a weighed allowance before qualification.

Four-dart kit bought hardware:

| Item | Quantity |
| --- | --- |
| 0.24 x 19.69 in fiberglass rods | 4 |
| XIAO ESP32S3 + Wio-SX1262 kits, with both FPC antennas | 4 |
| INMP441 breakouts | 4 |
| Flat-top 18650 cells with factory-welded insulated leads | 4 |
| SG90 positional servo and supplied double horn | 1 |
| RX-M2x4 heat-set inserts | 12 |
| M2x6 pod screws + servo tab screws | 12 +2 |
| M2 drive studs, nominal 0.39 in; nuts for drive and servo | 2 studs; 6 nuts |
| Measured-thread keeper screw, spacer and washer | 1 each |
| T18R ties: body/rod + rails | 12 +4 |
| 0.047 in cord, mic film/cavity seals and foam pads | 4 pod sets |
| PTFE bearing film | 1 annular strip |
| Power pair and 5 short mic wires | 4 wired sets |

Stake option adds one 1.57 in fiberglass offcut and five installation ties; it reuses one complete pod and one cell. Dummy option adds two M2x8 screws, two M2 nuts and the four weighed ballast portions. `out/kits.json` lists printed quantities separately for each option.

Use the Anycubic Vyper 9.65 x 9.65 x 10.24 in, dry PETG, 0.4 mm nozzle (0.016 in), 0.20 mm layers (0.008 in), four perimeters, six top/bottom layers and 100% infill. Start within the filament manufacturer temperature range (typically 455 °F nozzle/176 °F bed), then tune adhesion and fit. Use slow external walls and first layer; do not let supports lock snap reliefs or fill teardrop ducts. All supplied orientations fit the bed.

| Part | Kit/optional qty | Print bounds in | Orientation | Supports |
| --- | --- | --- | --- | --- |
| body | 4 | 8.57 x 1.47 x 2.09 | Flat sole down; post and snaps up | Local only: hanger flange and four snap beams. Clear the flexure reliefs. |
| pod_shell | 4 | 4.02 x 1.47 x 0.70 | Tray floor/neck flat down, opening up | Local only: rain hood, socket lip and mic guide ledges. Block teardrop ducts. |
| pod_lid | 4 | 5.91 x 1.26 x 0.23 | Outside face and FPC backer together on bed | None. Backer top is coplanar with lid outside face. |
| usb_cap | 4 | 0.65 x 0.84 x 0.13 | Outside flange face down, skirt up | None. |
| plate | 1 | 6.97 x 6.48 x 3.00 | Deck underside down, four towers up | None; hollow towers and tie bridges are designed in CAD. |
| rotor | 1 | 5.09 x 5.11 x 0.24 | Head-support face down, hub up | None. |
| fit_coupon | 1 | 2.17 x 0.46 x 0.43 | Four linked block bases down | None; bores 0.232/0.236/0.240/0.244 in increase in X. |
| stake_adapter | 1 | 1.73 x 1.65 x 0.67 | Flat bracket base down; V saddles up | None; small tie-channel bridges; offcut saddle is open. |
| stake_cell_holder | 1 | 3.17 x 2.78 x 0.75 | Flat cradle sole down, snap arms up | Local only under snap beams, as on body. |
| dummy_body | 1 | 8.57 x 1.47 x 2.09 | Flat sole down, pockets up | Local only under hanger flange; nut slots bridge 0.17 in. |
| dummy_lid | 1 | 3.03 x 0.83 x 0.079 | Outside face down | None. |
| dummy_head_insert | 1 | 0.91 x 0.70 x 0.28 | Floor down, ballast pockets up | None. |
| tail_fin | 16 | 6.46 x 0.84 x 0.047 | Entire broad face down, tabs coplanar | None; constant-thickness panel. Print 16 for four darts. |
| tail_collar | 8 | 0.71 x 0.71 x 0.31 | Axial end face down, rod bore vertical | None; open vertical bore and keyways. Print eight for four darts. |

## Hand-placed stake adapter

Use a 48 in fiberglass garden/driveway stake. `Measurements.stake_d` is the single unmeasured OD parameter, default 0.39 in. Two 90 degree V saddles with independent zip ties accept 0.31–0.51 in without reprinting; the circle axis rises as radius*sqrt(2), and all three nominal/end-point sizes are intersected against the clamp. No nominal 0.394 in closed bore is being passed off as an adjustable clamp. A short 0.23–0.24 in fiberglass offcut (1.57 in long) joins the adapter sleeve to the same pod socket; the external bracket stays clear of the pod neck.

Place the pod midway up the stake, not on its 48 in top. Insert the stake by hand, then slide/tie the adapter until the actual mic port is 19.69 in above the actual soil. The depicted burial is 3.94 in only; insertion depth does not determine port height. A separate retaining tie goes around the pod neck and stake through its own adapter tunnel; the offcut is a locator, not a friction-only restraint. Two additional ties hold the separate printed 18650 snap cradle lower down (five stake-installation ties total). This retains the owned cell and direct BAT wiring rather than assuming a USB power bank stays awake at the listener load. The stake battery holder is an optional replacement for the flying body, not extra flight mass. Its cell/cable configuration is shown in stake_assembled.step and stake.glb.

## Inert drop-test dummy

The dummy includes the same four fins, two collars and cured bond allowance, and uses the same 0.24 x 19.69 in rod, hanger location, pod shell/lid/service cap and external FPC backer. A closed twin-pocket ballast cassette replaces the cell cradle inside the dummy body; there is no cell, microphone or electronic stack. A small two-pocket printed head insert replaces the boards. The external backer is retained for approximate shape, while the flexible FPC itself is omitted; matching mass/CG does not match exact aerodynamic flexibility or inertia. Two M2x8 screws and side-loaded M2 captive nuts close the body ballast lid. Foam and adhesive retain the four weighed ballast portions; include their mass within the listed target portions.

Empty dummy assembly estimate: **4.61 oz**. Add **1.30 oz** total steel ballast to target **5.91 oz** and CG **(10.891, 0.243, 0.337) in**. All three model moment residuals are below 0.00004 in.

| Pocket | Weighed steel + fixative | Required centre XYZ in | Equivalent solid-steel block in |
| --- | --- | --- | --- |
| body_front | 0.41 oz | 3.622, 0.660, 0.380 | 0.787 x 0.472 x 0.243 |
| body_rear | 0.71 oz | 5.118, 0.660, 0.380 | 0.787 x 0.472 x 0.423 |
| head_front | 0.09 oz | 21.811, 0.000, 0.276 | 0.256 x 0.512 x 0.147 |
| head_rear | 0.09 oz | 22.283, 0.000, 0.276 | 0.256 x 0.512 x 0.147 |

Steel density 0.2836 lb/in³ (7.85 g/cm³) sets only the equivalent CAD blocks. Steel nuts, washers or shot can be used if their combined weighed mass and packed centre match the table. Locate each portion with foam spacers; immobilise it so impact cannot move the balance. Avoid loose shot. Pocket clearance and positive capacity are checked from the model. Weigh the actual empty print, solve again with measured values, and compare to the actual real dart target; the numerical nominal match alone is insufficient. Use the dummy for controlled bench release and soil drops to determine whether it turns nose-down, when rotation begins, whether it sticks and whether the snaps/post/rod survive. No model result demonstrates these behaviours.

## Checks, limits and assembly

Current run: **164/164 checks pass**. [checks.md](out/checks.md) and [checks.json](out/checks.json) retain every value and scope; STEP/STL round trips and topology are in [export_validation.json](out/export_validation.json).

Local board/mic/lid/cap/wire/ballast fits use actual B-rep intersection volumes with a 1.22047e-06 in³ threshold. Rod press lands, inserts, threads/solder and compressed soft seals have declared intended contact. Frame/prop/leg/ground checks use current exterior parts including the long FPC backer. Vehicle distance numbers are conservative AABB lower bounds; zero does not mean a measured zero gap. Rotor/head contact uses 0.5 degree samples, rotor/body sweep 2 degree, extraction 0.000–3.54 in in 0.20 in steps, and prescribed later pitch 0..90 degrees in 5 degree steps. These are discrete geometric checks, not a continuous or aerodynamic proof.

| State | Scope |
| --- | --- |
| Carried | Four changed darts against frame/rails, 10.24 in prop sweeps, skids, harness, ground and each other. |
| Mid-release | Rotor 16 degrees; dart 1 translated 2.76 in down, three carried. Included in extraction sweep. |
| After extraction | Pitch begins only after 16.93 in downward translation with aircraft 59.06 in above stock ground. No claim that real fall timing follows this path. |
| Stood | 2.76 in rod penetration, body soil stop at Z0, microphone 19.69 in up. Parked aircraft and three carried darts are offset 25.59 in from the stood dart for end-state review. |
| Stake | Adapter at 0.31/0.39/0.51 in stock diameters; mic 19.69 in above soil; separate cell holder. |
| Dummy | Mass and all three moments matched; all four ballast blocks fit their pockets. |

Assembly order:

1. Measure the actual XIAO/Wio stack, kit FPC antennas, mic breakout, servo, cell and rod. Confirm the aircraft rail/clamp arrangement against the OEM model. Print the fit coupon and tune rod_fit_bore before the long body.
2. Print in supplied STL orientations. Remove local supports and deburr; verify every snap flexes independently and the cell wrap cannot touch a sharp edge. Dry-fit with an inert cell-sized gauge.
3. Heat-set three M2 inserts per pod. Seat the mic film and annular seal, install the breakout with port facing the hood and add its soft preload pad. Do not fill the acoustic cavity with rigid adhesive.
4. Solder BAT wires to underside pads before installing the XIAO. Connect INMP441 to D3/D4/D5/3V3/GND and bridge L/R to ground for the selected channel. Keep headers off; inspect solder for shorts. Plug in Wio via B2B and connect the correct LoRa and WiFi U.FLs.
5. Seat the stack on edge supports, dress all five short wires and route cell leads through the neck/gutter strain reliefs. Fit the supplied FPC to the backer without creasing its feed. Seal gland/rod entry with removable neutral-cure silicone.
6. Slide body until its nose is 2.76 in from the sharpened tip. Snap the factory-wired flat-top 18650 into the retained cradle; insulate terminals, fit strain relief/body tie and two rod ties. Fit and bond the tail collars and fin tabs as described above, keeping the wire relief clear; then press the pod onto the final 0.79 in of rod.
7. Fit perimeter cord and foam pads, close the lid with three M2x6 screws and install/seal the USB cap. Remove only the cap for flashing; use a pin for BOOT/RESET if needed. Check actual plug/pin reach before final sealing.
8. Weigh and balance a completed dart. Update the model if the real balance differs materially from the integral hanger; source estimates are not permission to ignore that difference.
9. Mount SG90 below the plate using two M2 nuts/screws. Fit stock horn, two round M2 drive studs and locking nuts, PTFE bearing film, rotor and loose axial keeper. Match replacement screw thread to the actual servo; never clamp payload load into its shaft.
10. Tie four saddles to the rails. Route servo cable through the fixed gutter; use Pixhawk AUX1 signal, regulated servo supply and common ground. Calibrate 0/16/32/48/64 degree positions with inert loads. Load in reverse release order.
11. For stake use, fit a 1.57 in offcut between adapter and pod, tie V saddles to the stake, set the actual mic height to 19.69 in, and fit the lower cell holder and insulated leads.
12. For dummy use, fit/immobilise each weighed ballast portion, side-load the two nuts, screw the body lid down and retain head weights under the pod lid. Confirm actual total mass and balance before release tests.
13. Record bench cycling, proof load, vibration, water/acoustic tests and controlled dummy drops before any field release qualification. The present package has completed none of these physical tests.

## Open MEASURE inputs

The central Measurements dataclass includes sourced stock nominals requiring incoming inspection as well as fully unmeasured estimates. Highest-priority unknowns are B2B spacing, exact kit antenna envelopes/weights, microphone breakout/port, BAT pad location, wire dress, cell/rod/filament mass and printed friction/fit. The garden stake OD is one parameter; clamp geometry spans 0.31–0.51 in.

| Parameter (internal name unchanged) | Nominal input, US display |
| --- | --- |
| rod_d | 0.236 in |
| rod_fit_bore | 0.234 in |
| rod_density | 0.0686 lb/in³ (1.9 g/cm³) |
| cell_d | 0.722 in |
| cell_l | 2.553 in |
| cell_mass | 1.59 oz |
| cell_terminal_d | 0.236 in |
| cell_terminal_h | 0.014 in |
| cell_insulator_d | 0.567 in |
| cell_insulator_t | 0.005 in |
| sg_case_l | 0.894 in |
| sg_case_w | 0.480 in |
| sg_case_h | 1.063 in |
| sg_tabs_span | 1.272 in |
| sg_tab_z | 0.669 in |
| sg_tab_t | 0.079 in |
| sg_hole_pitch | 1.083 in |
| sg_hole_d | 0.079 in |
| sg_axis_from_end | 0.232 in |
| sg_spline_d | 0.189 in |
| sg_spline_teeth | 21 teeth |
| sg_spline_h | 0.130 in |
| sg_screw_d | 0.063 in |
| sg_gear_cap_h | 0.169 in |
| sg_gear_cap_r | 0.224 in |
| sg_rear_cap_r | 0.126 in |
| sg_rear_cap_h | 0.118 in |
| sg_case_corner_r | 0.039 in |
| sg_spline_groove_w | 0.014 in |
| horn_l | 1.063 in |
| horn_w | 0.205 in |
| horn_t | 0.063 in |
| horn_boss_d | 0.276 in |
| horn_boss_h | 0.150 in |
| horn_pin_pitch | 0.709 in |
| mic_board_w | 0.551 in |
| mic_board_l | 0.630 in |
| mic_board_t | 0.039 in |
| mic_port_d | 0.039 in |
| mic_port_x_offset | 0.000 in |
| mic_pad_row_span | 0.433 in |
| mic_pad_pitch | 0.177 in |
| mic_mass | 0.04 oz |
| xiao_mass | 0.08 oz |
| wio_mass | 0.06 oz |
| stack_spacing | 0.295 in |
| fpc_l | 3.937 in |
| fpc_w | 0.394 in |
| fpc_t | 0.012 in |
| fpc_mass | 0.03 oz |
| wifi_l | 0.787 in |
| wifi_w | 0.236 in |
| wifi_mass | 0.01 oz |
| stake_d | 0.394 in |
| stake_burial | 3.937 in |
| ballast_density | 0.2836 lb/in³ (7.85 g/cm³) |
| petg_density | 0.0459 lb/in³ (1.27 g/cm³) |
| petg_modulus | 232060.38 psi |
| printed_allowable_strain | 0.015 (strain) |
| wire_od | 0.041 in |
| prop_plane_from_bottom_plate | 2.244 in |
| prop_sweep_thickness | 0.157 in |
| fin_adhesive_mass | 0.02 oz |

## Exploded web models and visual review

`web_export.py` writes dart, harness, aircraft and stake GLBs in metres with Y up, using named physical-part nodes and an 8-second `explode` clip. Dart/harness/aircraft views expose the populated board stack, mic, cap, lid, seals, wiring and hardware; aircraft first lowers its loaded harness 15.75 in. The stake clip withdraws the retained pod subassembly 3.94 in from the offcut. This is an illustration: disconnect wires, cut disposable ties and unscrew hardware in actual service. Motion does not simulate threads, flexures, cables, falls or continuous collision-free disassembly.

The current mass report supplies per-node mass estimates and source/uncertainty facts in `web/manifest.json`. Servo/horn share the 0.32 oz catalog mass; aircraft solid masses remain null. `validation-readback.json` checks every sampled animation translation and loads each GLB with trimesh; `validation-khronos.json` holds Khronos results. `exploded_checks.json` checks independent endpoint subassemblies for overlap. Full-resolution STEP/STL files remain the manufacturing geometry.

Every final PNG is listed in REVIEW.html. Visual inspection covers all assembled, sectioned, exploded and print orientations; a per-file review receipt is stored in `out/visual_review.json` after inspection. No visual claim replaces a physical fit test.
