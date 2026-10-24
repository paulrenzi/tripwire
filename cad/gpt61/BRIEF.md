# Brief: turn the tripwire listener and its drone release into a real 3D model

Work in `cad/gpt61/` only. Do not edit anything else in the repo, and do not commit or push.

## The problem you are fixing

The concept below is settled, and it is not your job to rethink it. The problem is that the existing models (`cad/v2.py`, `cad/v3.py`) do not turn it into a credible 3D model. They are boxes, cylinders and extrusions that no mechanical engineer would produce. There are no real wall sections, fillets, ribs, draft, snap geometry, wire channels or fastener features. The bought parts are blocks, the drone is missing from the assembly, and many dimensions are guesses. The project owner's verdict: "nobody would build models like that."

Your job is to produce the model a competent mechanical designer would produce for a first prototype print. That means real parts, at real dimensions, that fit together, and that you could hand to someone to print and assemble.

## The concept (fixed)

Read `build-hardware.md` §1–2 for the full text and `models/tripwire.md` for context.

- **The listener ("dart")** is one 6 mm × 500 mm solid fiberglass rod, which serves as the spike, the spine and the mast. On it are two printed parts:
  - **A body near the tip.** Its nose sits 70 mm back from the sharpened rod tip, so at most 70 mm of rod goes into soil. It holds one 18650 Li-ion cell beside the rod, snapped into an open cradle. A sleeve runs back along the rod to a hanger post at the dart's balance point. The post's neck and round head hang the dart from the harness.
  - **A head pod on the rod's top end.** It holds a Heltec WiFi LoRa 32 V3 board upright, an INMP441 I²S mic breakout looking out of a side port under a rain hood, and the LoRa whip antenna out of the top. Cell power runs up the rod to the pod in two wires.
  - The dart stands in soil with the mic about 0.5 m up.
- **The harness** hangs four darts flat, side by side, under the Holybro X500 V2's two 10 mm payload rails. It is one printed plate zip-tied to the rails, carrying one SG90 servo and a printed rotor on the servo.
  - Each dart's hanger post comes up through a slot in the plate, and its round head rests on the rotor's rim.
  - The rim has one gap per dart, at a different angle for each. Each 16° servo step brings one gap under one head, and that dart drops.
  - The darts' weight goes rotor → a bearing ridge on the plate → plate, not into the servo.
  - The servo is driven from Pixhawk AUX 1.
- **The current numbers** (estimates from the old model): a dart weighs ~127 g, the hanger sits ~246 mm from the tip, and a dart is ~564 mm long with the pod plus an 82 mm whip.

If, while modelling, you find a real physical conflict (a part cannot fit, a load path fails, something collides), keep the concept and solve it within the concept. Write down what you changed and why. Do not swap in a different concept.

## What to deliver

1. **Bought parts as real models,** built from datasheets, manufacturer drawings or published STEP/CAD files (find and use them where they exist). Cite the source of each dimension in a comment. Model:
   - **Holybro X500 V2:** centre plates, arms, motors, props as swept discs, landing gear, the payload rails and their clamps.
   - **SG90:** case, mounting tabs, output spline and a horn.
   - **Heltec V3:** PCB with the OLED, USB-C, U.FL connector, buttons and header rows.
   - **INMP441 breakout,** with its port.
   - **18650 cell.**
   - **The rod.**
   - **The whip, and the zip ties** where they go.

   Where a dimension truly cannot be found, mark it MEASURE and make it one parameter.
2. **Printed parts modelled properly:**
   - wall thicknesses suited to 0.4 mm-nozzle PETG;
   - fillets and chamfers where they belong;
   - ribs where loads need them;
   - real snap-fit geometry for the cell (lead-in, retention, a deflection check);
   - FDM clearances (press fit on the rod, sliding fit for the rotor, slot clearances);
   - wire channels with strain relief;
   - a sealed but serviceable pod (how it opens, how the board is held, how the cable gets in);
   - the rotor's horn interface;
   - heat-set inserts or captive nuts if any fastener is used;
   - a print orientation for each part that needs no supports, or minimal supports.
3. **A full assembly with the drone,** in carried, mid-release and stood-in-soil states, with interference checks against the frame, props, legs and the ground plane. Report what you checked and the results.
4. **Mass properties from the model,** with infill stated: each part, each dart, the balance point (which sets the hanger position), and the harness.
5. **Exports and renders:**
   - STEP and STL for every printed part to `cad/gpt61/out/`, and a STEP of the full assembly.
   - Renders to `cad/gpt61/renders/`: the assembly on the drone, one dart standing, a section through the body and through the pod, and each printed part in its print orientation.
   - CadQuery is installed at `C:\Users\paulm\.venvs\cad\Scripts\python.exe`. Use it. You may use `cad/render.py` (VTK) or write a better renderer.
   - **Look at every render yourself.** If something looks crude, wrong or unclear, fix the model or the view and re-render before you finish.
6. **`cad/gpt61/DESIGN.md`:**
   - what you modelled and from which sources;
   - every change you made to the concept and why;
   - the key dimensions and clearances;
   - the masses;
   - the open MEASURE items;
   - print settings per part;
   - assembly steps.

## Environment

- Windows 11, PowerShell or Git Bash. Python CAD scripts run with `C:\Users\paulm\.venvs\cad\Scripts\python.exe`.
- Use the web for datasheets and CAD files, and cite them.
- `cad/params.py` has some sourced dimensions and several guesses. Treat it as a lead, not a source.
- Take as long as you need. Run your scripts, read the numbers, look at the renders, iterate.
