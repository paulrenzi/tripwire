# Brief: the band cutter, as a real 3D model with an animated exploded view

Work in `cad/bandcutter/` only. Do not edit anything else in the repo, and do not commit or push.

## What this is

A countermeasure against fiber-optic FPV drones. These drones pay out a glass fiber (0.25 mm coated,
0.125 mm glass) from a spool they carry, so the fiber drops onto whatever lies under the drone's path.
The band cutter is a hand-built line, about 32 in high, that carries any fiber lying across it into
fixed blades. **The whole line must cost under $1,000 a mile in parts**, so every part is the
cheapest off-the-shelf part that works, or a small 3D print. The cost and speed model is
`tools/bandmodel/band_model.py`: read its docstring, constants and output first (`py band_model.py`),
then `countermeasures/fiber-cutter.md` and `countermeasures/index.md` for context.

## The concept (fixed; solve problems inside it and write down what you changed and why)

- **The band:** 80 lb nylon monofilament (about 0.04 in), a closed loop out and back, tension about
  10 lb. Each loop covers 660 ft of line: the top run about 32 in above the ground, the return run a
  few inches under it.
- **Guide rods, one every 50 ft:** a 3/8 in × 48 in fiberglass electric-fence rod pushed about 12 in
  into the soil (with a printed drive cap). On top, a **printed guide head** that slides onto the rod
  and locks to it: two eyes, one for each run, each open at the side so the line can be dropped in
  and held by a keeper. The eyes must be smooth (low friction for nylon) and pass the catchers.
- **The blades:** each guide head holds two segments snapped off a standard 18 mm snap-off utility
  blade, one either side of the top run's eye, edges facing the incoming line, replaceable without
  tools. A loop's top run moves one way, so every head on that loop faces the same way.
- **The catchers:** a small printed TPU catcher every 3 ft, held on the line by a fishing crimp sleeve
  (or designed to crimp itself). It has three soft spurs leaning forward round the line, so it
  catches a fiber whichever way the round line has rolled. A fiber lying across the line is caught
  in the crotch between a spur and the line; pulling on it presses the spur toward the line, which
  traps it. The spurs fold back to pass through the guide eyes, the gap between the blades and round
  the pulleys, then spring up again. At the head, the catcher pulls the fiber between the blades and
  its two sides, hanging down over the line, are drawn onto the edges and cut. Design the catcher
  shape and show in detail renders how it catches a fiber and how it passes the blades.
- **Drive posts, one every 1,320 ft:** a 5.5 ft studded steel T-post driven 2 ft, with a printed head
  locked on by a hose clamp. On it, one aftermarket **12 V car power-window motor** (worm gear, sealed;
  pick a common model and use its real dimensions and mounting) turning one shaft with an 8 in
  printed pulley on each side: one drives the loop to the left, one the loop to the right. Plus a
  12 V 20 W panel tilted low on a bracket (matte, to limit glint), a 12 V 7 Ah sealed lead-acid
  battery, a PWM solar controller, an ESP32-C3 SuperMini, an Ai-Thinker Ra-01H LoRa module with a
  wire antenna, a relay or MOSFET driver and fuse, in an off-the-shelf IP65 junction box with glands.
- **Idler posts, at each loop's far end:** a T-post with a printed head carrying a free pulley on 608
  bearings for each loop that ends there (two, where two sections meet) and a simple take-up that
  sets the line tension. The two posts at the ends of the line are guyed to spiral earth anchors.

Look up the real dimensions of every bought part (fiberglass rod, T-post profile and studs, hose
clamp, monofilament, crimp sleeve, snap-off blade, 608 bearing, the window motor, 20 W panel, 7 Ah
battery, junction box, SuperMini, Ra-01H) from datasheets, listings or published CAD, and cite each.
Where something can't be found, mark it MEASURE and make it one parameter.

## What to deliver

1. **Bought parts as real models** at real dimensions, and **printed parts modelled properly**: walls
   for a 0.4 mm nozzle in PETG or ASA (outdoor, UV), TPU for the catcher, fillets, ribs where loads
   go, FDM clearances, bearing seats, the shaft-to-pulley drive, the head-to-post fits, the blade
   holder, the take-up, cable routing into the box, and a print orientation with minimal supports
   for each printed part. STEP and STL of every printed part to `out/`.
2. **Assemblies:** a guide rod with its head, blades and both runs; a drive post; an idler post; and
   a **section**: a drive post, a few guide rods and an idler post with the loop and catchers, shown
   shortened (say so). Check for interference: catchers against eyes, blades and pulleys; line
   against the heads; box and panel against the line.
3. **Mass properties** of each assembly, printed parts at the infill you recommend.
4. **Exploded views and web models,** exactly as was done for the dart in `cad/gpt61/`: read
   `cad/gpt61/BRIEF-exploded.md`, `cad/gpt61/web_export.py`, `cad/gpt61/web/manifest.json` and
   `assets/js/cad-viewer.js`. Deliver in `web/`:
   - `guide_rod.glb`, `drive_post.glb`, `idler_post.glb` and `section.glb`, each one file with an
     8-second glTF animation named `explode` moving every part from assembled (t = 0) to exploded
     along the direction it is actually assembled, in assembly order, with no overlaps when exploded;
   - one node per part, named; metres, Y up; PBR colours that tell printed from bought parts;
     each ≤ 8 MB; read back and run through the Khronos glTF validator (`npx gltf-validator`);
   - `web/manifest.json` in the same schema as `cad/gpt61/web/manifest.json`, so the existing
     viewer reads it unchanged: per part, its node name, display name, printed or bought, mass,
     geometry source and one plain sentence on what it does. Unmeasured things stay flagged.
5. **Renders** to `renders/`: each assembly, each exploded view, a catcher on the line catching a
   fiber (draw the fiber), a catcher folding through the blades, and each printed part in its print
   orientation. **Look at every render yourself** and fix anything crude, wrong or unclear.
6. **`DESIGN.md`:** sources, every change to the concept and why, key dimensions and clearances,
   masses, a parts list with prices that confirms the under-$1,000-a-mile budget, open MEASURE
   items, print settings, and assembly steps. **US customary units** (in, ft, oz, lb, °F) in every
   caption and document; files and internal geometry may stay metric.
7. **One script that regenerates all of it,** runnable from the repo root with the interpreter below.

## Environment

- Windows 11. Python with CadQuery 2.8, OCP, numpy and trimesh: `C:\Users\paulm\.venvs\cad\Scripts\python.exe`.
  You may `pip install` into it (e.g. `pygltflib`). `cad/gpt61/` has working render and export code you
  may copy into `cad/bandcutter/` and adapt; do not modify `cad/gpt61/`.
- Use the web for datasheets and CAD files, and cite them.
- Take as long as you need: run your scripts, read the numbers, look at the renders, iterate.

## Done means

Four valid `.glb` files with named nodes and the `explode` clip, `web/manifest.json`, the renders
you have looked at, STEP/STL of the printed parts, `DESIGN.md`, the regenerating script, and a final
message listing what you made, file sizes, validator output, and anything you could not do.
