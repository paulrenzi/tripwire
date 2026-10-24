"""Band model: long polyester strap loops on cheap rods that carry a fibre FPV's line into a guarded blade.

The line is hand-laid. The band is 1/2 in polyester packing strap, a closed loop out and back,
joined with a strapping seal. A flat strap cannot roll, so everything on it can point one way, and
it stretches far less than nylon. Every 1,320 ft of line has one drive post in its middle: a 12 V
car power-window motor turning a printed pulley for the loop on each side. Each loop runs 660 ft
to an idler post, a T-post with a printed pulley and a hanging weight that holds the tension. The
top run rides about 32 in up, outer face up; the return run hangs a few inches under it, outer face
down. Between the posts the strap rides on printed rollers on 3/8 in fibreglass fence rods, one
every 50 ft; the return run's roller is split so the fins pass down its middle.

A stiff printed fin stands on the outer face every 4 ft. Each has a forward-facing V slot, about
1/2 in wide at the mouth and narrowing to a throat thinner than the fibre. When the strap moves, a
fibre lying across it is held back by the drag of its own legs, so it runs down the V and jams in
the throat. The wedge multiplies that drag into a pinch, so the harder the fibre pulls back the
tighter it holds. At each rod a blade segment sits in a guarded channel beside the fin's path, at
the throat's height, above the strap. Each fin has a groove the blade passes through, so the blade
crosses the throat and shears what is held there. The strap powers the cut, the fibre's tension
plays no part, and the strap never comes near the edge.

It runs only when the tripwire's radio trigger says a drone is near, plus one clearing stroke an
hour (one rod spacing) for a drone that lands and waits. A box that stops hearing the trigger's
heartbeat runs clearing strokes more often, so jamming the link slows the line but never stops it.
A drop in motor current means a broken loop, and the box reports it over the same radio.

Not costed here: the line needs a mown strip about 3 ft either side, or to run above what grows
there. A wedge that grabs a fibre also grabs a grass blade.

Prints: sag and stretch, the fin's grip, line speed, the longest wait from a fibre landing to its
cut and how far out the line must sit, drag, torque and power at a drive post, the daily energy
budget, and parts per mile.

    py band_model.py [--rod 50] [--loop 660] [--rpm 90] [--pulley 8] [--catch 4] [--cut-lb 1] [--mu 0.05]

Stdlib only. Every number marked ASSUME is a planning number, not a measurement. Whether the fin
catches a fibre from leg drag alone, the force to shear it, and the roller drag set whether this
works at all, and all three are guesses until tested.
"""
import argparse, math

MILE = 5280.0
LBF = 4.448
DRONE_MPH = 43.0           # a fibre FPV's top speed (threat-profile)

# ---- the band ---------------------------------------------------------------------------------
LINE = "1/2 in polyester strap, 0.028 in, 800 lb"
LINE_LB_FT = 0.0083        # 9.0 mm2 of PET at 1.38 g/cm3
LINE_BREAK_LB = 800
LINE_E_PSI = 1.2e6         # oriented PET strap, about 8 GPa ASSUME
LINE_AREA_IN2 = 0.5 * 0.028
LINE_PER_FT = 0.019        # $119 for a 6,500 ft coil, by the skid (Zoro, 2026-10)
THERMAL_PER_F = 9.4e-6     # PET, per deg F
TEMP_SWING_F = 100         # summer day to winter night ASSUME
TENSION_LB = 20.0          # a hanging weight at each idler ASSUME
MISALIGN_DEG = 1.0         # rods off a straight line, so the strap presses on each roller ASSUME
MU = 0.05                  # printed roller on a steel pin, as a drag fraction ASSUME
CATCH_LB = 0.01            # a fin pushing through a roller or past the blade ASSUME
CUT_LB = 1.0               # extra pull while a fin carries a fibre across the blade ASSUME (R4)

# ---- the fin's grip ---------------------------------------------------------------------------
FIBRE_LB_FT = 0.00004      # 0.06 g a metre
FIBRE_MU = 0.5             # fibre dragged over grass ASSUME
LEG_FT = 300               # fibre on the ground either side that the fin drags ASSUME
WEDGE_DEG = 5              # half-angle of the V at the throat
WEDGE_MU = 0.3             # printed plastic on fibre coating ASSUME

# ---- the drive --------------------------------------------------------------------------------
MOTOR = "12 V car power-window motor (worm, sealed)"
MOTOR_KGCM = 30            # rated, typical aftermarket listing
MOTOR_EFF = 0.4            # ASSUME
EVENT_MIN = 3              # minutes of running per trigger: the drone crosses in seconds

# ---- power, one drive post ---------------------------------------------------------------------
PANEL_W = 20               # 12 V 20 W panel
BATT_WH = 84               # 12 V 7 Ah sealed lead-acid: charges in frost, unlike lithium
BATT_USABLE = 0.5          # lead-acid lasts if held above half charge
STANDBY_W = 0.072          # 6 mA at 12 V: controller, MCU asleep, LoRa listening in bursts ASSUME
WINTER_SUN_H = 1.5         # full-sun hours a day in a Ukrainian December ASSUME
SOLAR_EFF = 0.7            # panel to battery, PWM controller, dirt ASSUME

# ---- parts, $ each, small batch (retail listings 2026-10 unless est.) --------------------------
P_ROD = 2.0                # 3/8 x 48 in fibreglass fence rod, $1.99-2.49
P_GUIDE = 0.6              # printed head, two rollers (one split) on steel pins (est.)
P_BLADE = 0.05             # one segment snapped off an 18 mm utility blade (est.)
P_CATCH = 0.04             # printed PETG fin, snapped through a hole punched in the strap (est.)
P_TPOST = 7.0              # 5.5 ft studded steel T-post
P_IDLER = 3.0              # printed pulley head, two 608 bearings, weight bag filled on site (est.)
P_SEAL = 0.1               # strapping seal, one a loop
P_END = 16                 # each end of the line: spiral earth anchor and guy (est.)
DRIVE = [                  # one drive post
    ("T-post", P_TPOST),
    (MOTOR + ", aftermarket", 15),
    ("12 V 20 W panel", 20),
    ("12 V 7 Ah sealed lead-acid", 18),
    ("PWM solar controller, low-voltage cutoff", 5),
    ("ESP32-C3 SuperMini and Ra-01H LoRa (868 MHz)", 9),
    ("relay or MOSFET driver, current sense, fuse, wire, glands", 5),
    ("IP65 junction box", 3),
    ("printed head, two 8 in pulleys, bearings (est.)", 4),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rod", type=float, default=50.0, help="ft between guide rods (each has a blade)")
    ap.add_argument("--loop", type=float, default=660.0, help="ft of line one loop covers, drive to idler")
    ap.add_argument("--rpm", type=float, default=90.0, help="drive pulley rpm under load ASSUME")
    ap.add_argument("--pulley", type=float, default=8.0, help="in, drive pulley diameter")
    ap.add_argument("--catch", type=float, default=4.0, help="ft between fins on the strap")
    ap.add_argument("--cut-lb", type=float, default=CUT_LB, help="lbf to carry a fibre across the blade ASSUME")
    ap.add_argument("--mu", type=float, default=MU, help="drag fraction at each roller ASSUME")
    a = ap.parse_args()

    sag_in = LINE_LB_FT * a.rod ** 2 / (8 * TENSION_LB) * 12
    loop_len = 2 * a.loop
    stretch_ft = TENSION_LB / (LINE_E_PSI * LINE_AREA_IN2) * loop_len
    thermal_ft = THERMAL_PER_F * TEMP_SWING_F * loop_len
    print(f"{LINE} on rods every {a.rod:.0f} ft: sag {sag_in:.1f} in at {TENSION_LB:.0f} lb "
          f"({TENSION_LB / LINE_BREAK_LB:.1%} of break).")
    print(f"  A {loop_len:,.0f} ft loop stretches {stretch_ft:.1f} ft under tension and moves "
          f"{thermal_ft:.1f} ft over a {TEMP_SWING_F} F swing,")
    print(f"  so the hanging weight needs about {stretch_ft + thermal_ft + 1:.0f} ft of travel "
          f"(nylon mono stretched about 37 ft).")

    leg_oz = FIBRE_LB_FT * LEG_FT * FIBRE_MU * 16
    pinch_oz = leg_oz / (2 * math.sin(math.radians(WEDGE_DEG)))
    lock = math.tan(math.radians(WEDGE_DEG)) < WEDGE_MU
    print(f"\nThe fin's grip: {LEG_FT} ft of fibre dragged over grass pulls back about {leg_oz:.1f} oz a leg; "
          f"a {WEDGE_DEG} deg wedge")
    print(f"  turns that into about {pinch_oz:.1f} oz of pinch each side, and it "
          f"{'locks' if lock else 'does NOT lock'} (tan {WEDGE_DEG} deg = "
          f"{math.tan(math.radians(WEDGE_DEG)):.2f} vs friction {WEDGE_MU}).")
    print(f"  The cut force runs through the fin, not the fibre, so the grip only has to stop it slipping out.")

    fps = a.rpm * math.pi * a.pulley / 12 / 60
    wait_s = (a.catch + a.rod) / fps
    drone_fps = DRONE_MPH * 5280 / 3600
    print(f"\nLine speed {fps:.1f} ft/s ({a.rpm:.0f} rpm on an {a.pulley:.0f} in pulley).")
    print(f"  Longest wait from a fibre landing to its cut: a fin {a.catch:.0f} ft away, then one rod "
          f"spacing: {wait_s:.0f} s.")
    print(f"  A drone at {DRONE_MPH:.0f} mph flies {wait_s * drone_fps:,.0f} ft meanwhile; add the fibre's fall "
          f"time and trigger lag to get how far out the line must sit.")

    # drag of one loop: both runs press on every roller, and every fin pushes through rollers and past blades
    n = math.hypot(LINE_LB_FT * a.rod, 2 * TENSION_LB * math.sin(math.radians(MISALIGN_DEG)))
    guides = a.loop / a.rod
    drag = 2 * guides * a.mu * n + 2 * a.loop / a.catch * CATCH_LB * a.catch / a.rod
    loop_lb = drag + a.cut_lb
    post_lb = 2 * drag + a.cut_lb
    kgcm = post_lb * a.pulley / 2 * LBF * 2.54 / 9.81
    w_run = 2 * drag * LBF * fps * 0.3048 / MOTOR_EFF
    w_cut = post_lb * LBF * fps * 0.3048 / MOTOR_EFF
    print(f"\nOne {a.loop:.0f} ft loop drags {drag:.1f} lbf empty, {loop_lb:.1f} lbf cutting "
          f"(tension {TENSION_LB:.0f} lb holds it).")
    print(f"  Drive post, two loops: {post_lb:.1f} lbf, {kgcm:.0f} kg cm at the shaft; {w_run:.0f} W running, "
          f"{w_cut:.0f} W cutting. A window motor is rated about {MOTOR_KGCM} kg cm.")

    event_wh = w_cut * EVENT_MIN / 60
    clear_wh = w_run * (a.rod + a.catch) / fps / 3600 * 24
    standby_wh = STANDBY_W * 24
    panel_wh = PANEL_W * WINTER_SUN_H * SOLAR_EFF
    spare = panel_wh - standby_wh - clear_wh
    print(f"\nEnergy a day, one drive post: standby {standby_wh:.1f} Wh, hourly clearing strokes {clear_wh:.1f} Wh.")
    print(f"  A {PANEL_W} W panel makes about {panel_wh:.0f} Wh on a December day, leaving {spare:.0f} Wh: "
          f"{spare / event_wh:.0f} triggers a day at {event_wh:.1f} Wh ({EVENT_MIN} min each).")
    print(f"  The battery holds {BATT_WH * BATT_USABLE:.0f} Wh above half charge: "
          f"{BATT_WH * BATT_USABLE / (standby_wh + clear_wh):.0f} sunless days, or "
          f"{BATT_WH * BATT_USABLE / event_wh:.0f} triggers.")

    drives = math.ceil(MILE / (2 * a.loop))
    loops = 2 * drives
    idlers = drives + 1
    rods = math.ceil(MILE / a.rod) - drives - idlers + 1
    line_ft = loops * (2 * a.loop + 10)
    catches = math.ceil(line_ft / a.catch)
    drive_each = sum(c for _, c in DRIVE)
    parts = [
        (f"{LINE}, {line_ft:,.0f} ft, {loops} seals", line_ft * LINE_PER_FT + loops * P_SEAL),
        (f"Fins, {catches:,}", catches * P_CATCH),
        (f"Fibreglass rods with roller heads and a blade, {rods}", rods * (P_ROD + P_GUIDE + P_BLADE)),
        (f"Idler posts, {idlers}: T-post, pulley head, weight", idlers * (P_TPOST + P_IDLER)),
        (f"Drive posts, {drives} at ${drive_each:.0f}", drives * drive_each),
        ("End anchors and guys, 2", 2 * P_END),
    ]
    total = sum(c for _, c in parts)
    print(f"\nA mile: {loops} loops, {drives} drive posts, small-batch parts (est.):")
    for name, c in parts:
        print(f"  {name:58s} ${c:5,.0f}")
    print(f"  {'Total':58s} ${total:5,.0f}")
    print("\nOne drive post:")
    for name, c in DRIVE:
        print(f"  {name:58s} ${c:3.0f}")


if __name__ == "__main__":
    main()
