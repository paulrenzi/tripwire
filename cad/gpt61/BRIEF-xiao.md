# Brief: rebuild the listener around the board we actually own

Work in `cad/gpt61/` only. Do not edit anything else in the repo, and do not commit or push. This is a revision of your own package from 2026-10-15/16 (`BRIEF.md`, `BRIEF-exploded.md`, `DESIGN.md`), so read those first.

## What is wrong now

Every listener model is built around the **Heltec WiFi LoRa 32 V3** (about 50 × 25 mm, OLED, on-board LoRa). We never used that board. The boards that were bought, flashed and will be fielded are the **Seeed Studio XIAO ESP32S3 + Wio-SX1262 kit** (Meshtastic kit, Rokland/Seeed). So the pod, its board hold, its antenna exit, its cable entry, its mass and the dart's balance point are all wrong, and so is everything downstream: the hanger position, the harness load, the four-dart payload mass and the web models.

## The board (research it properly)

- Seeed XIAO ESP32S3 (about 21 × 17.8 mm, USB-C on one short edge, castellated pins, battery pads BAT+/BAT− on the underside with an on-board Li-ion charger, BOOT and RESET buttons, U.FL connector for the Wi-Fi/BLE antenna) stacked on the **Wio-SX1262** LoRa board through the kit's board-to-board connector, with the kit's LoRa antenna on its U.FL/IPEX connector. Find Seeed's drawings, KiCad/STEP files or wiki dimensions for both boards and the kit's antenna, cite them, and model them. Mark anything you cannot source as MEASURE.
- There is **no OLED, no LED and no battery-voltage divider** on this board in our firmware. The board reports alive by radio once a minute, so the pod does not need a window. It does need the USB-C port reachable for flashing without taking the dart apart (a plug or a cap is fine), and the BOOT button reachable or reachable with a pin.
- The mic is an **INMP441 breakout**, wired to XIAO D3 (SCK/BCLK), D4 (WS) and D5 (SD), plus 3V3 and GND, by about 5 short wires. Its port must still look out of the pod side under a rain hood, and it must sit at **about 0.5 m above the soil** when the dart stands, as before.
- Power is still one **18650 cell** in the body near the tip, with two wires up the rod, now to the XIAO's BAT+/BAT− pads. Keep the cell and its snap cradle unless you find a better reason; if the much smaller board lets a smaller cell make sense, say so in DESIGN.md but keep the 18650 in the model.

## What stays fixed

The concept in `BRIEF.md` stays: one 6 × 500 mm fiberglass rod as spike, spine and mast; a body near the tip with the cell and hanger post; a head pod on the top end; four darts hung flat under the Holybro X500 V2 on the one-servo rotor harness. Keep the printer constraint: **Anycubic Vyper, 245 × 245 × 260 mm bed, PETG, 0.4 mm nozzle**, no or minimal supports.

## What to deliver

1. **The pod redesigned for the XIAO + Wio-SX1262 stack:** board hold, antenna exit (the kit's antenna on top, as the whip was), mic port and rain hood, cable entry with strain relief, how it opens and seals, USB-C access. It should be as small and light as the board allows. Remove the Heltec model from the dart and the assemblies (keep its source files if you like, but nothing on the dart should be Heltec).
2. **Everything downstream recomputed from the model:** each part's mass, the dart's mass and balance point, the hanger position (it sits at the balance point), the harness (resize or re-check the plate, slots and rotor if the dart changed enough to matter; re-check that the plate's mass is stated at the infill you actually recommend, not 100% unless you mean it), and four darts plus harness.
3. **Re-run every check** (interference with frame, props, legs and the ground, carried / mid-release / stood) and update `checks.md` / `checks.json`.
4. **A stake adapter:** a small printed clamp that holds the same pod (with its board, mic and antenna) on a hand-placed fiberglass stake, so the pod can be used before any drone drop. The stake is a 48 in (1.22 m) fiberglass garden/driveway stake; its diameter is **MEASURE**, make it one parameter, default 10 mm, and design the clamp to take a range (say 8–13 mm) with a screw or zip tie. The mic must sit at 0.5 m on the stake too. Power on the stake is a USB power bank or the 18650 in a small printed holder; your call, explained.
5. **A drop-test dummy:** the dart body, printable, with a ballast pocket so that a dart with the dummy matches the real dart's mass and balance point (state the ballast mass, e.g. steel nuts or lead shot). This is for testing whether a released dart turns nose-down and sticks, before anyone builds real darts.
6. **Regenerate the whole package** so nothing still shows the Heltec: `out/` (STEP + STL for every printed part including the stake adapter and dummy, the print kit zip, manifests, mass tables), `renders/` (every render, plus the stake adapter and dummy in print orientation and assembled), `REVIEW.html`, `web/` (`web_export.py`: dart, harness and aircraft GLBs with the explode animation, plus a GLB of the pod on the stake if you can, and `manifest.json`), and the validators. **Look at every render yourself** and fix anything crude or unclear before you finish. Delete renders and outputs that no longer correspond to anything.
7. **`DESIGN.md` updated:** the new board and its sources, every change and why, key dimensions and clearances, all masses, the open MEASURE items, print settings per part for the Vyper, and assembly steps. Keep it honest that nothing has been printed, dropped or flown. Add a short section at the top listing what changed from the Heltec version, with old and new masses side by side.

## Environment

- Windows 11. CadQuery is at `C:\Users\paulm\.venvs\cad\Scripts\python.exe`; use it for every script.
- Use the web for datasheets and CAD files, and cite them.
- Take as long as you need: run, read the numbers, look at the renders, iterate. Finish with a short summary of what changed and the new key numbers.
