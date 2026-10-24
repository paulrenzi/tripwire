---
title: Range and cost-per-square-mile model
parent: Research Notes
nav_order: 2
nav_tripwire: 4
---

# Range and cost-per-square-mile model
{: .no_toc }

<p class="vz-lede">Cost per square mile = node cost × nodes per square mile, and <strong>how far a node hears sets how many nodes</strong>. Halve the range and you need four times the nodes.</p>

### Working range estimates, by target

<div class="vz-bars">
  <div class="vz-bar-row"><span class="vz-bar-label">Shahed / Geran, cruise missiles</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:19.4%"></span><span class="vz-bar vz-bar-them-light" style="width:80.6%"></span></span><span class="vz-bar-val">0.6–3.1 mi</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">Large multirotor, Mavic class</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:4.0%"></span><span class="vz-bar vz-bar-them-light" style="width:5.7%"></span></span><span class="vz-bar-val">660–1,600 ft</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>Small or fiber-optic FPV</strong></span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:2.0%"></span><span class="vz-bar vz-bar-us-light" style="width:4.0%"></span></span><span class="vz-bar-val">330–980 ft</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">Measured: cheap array, DJI Phantom</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:1.0%"></span><span class="vz-bar vz-bar-them-light" style="width:0.2%"></span></span><span class="vz-bar-val">160–200 ft</span></div>
  <p class="vz-bar-note">Planning guesses, except the last row (Ghouli, Acta Acustica 2026). Wind, terrain and background noise can halve or double them. No FPV has been range-tested; T11 decides it. VolAnti measured 340 ft on a hovering quad.</p>
</div>

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">1.15 / r²</p><p>nodes per square mile on a triangular grid with spacing r (miles), so 3 nodes hear most points</p></div>
  <div class="vz-card"><p class="vz-card-num">Lines, not areas</p><p>The tripwire covers approaches with a row, not every square mile, which is why it stays cheap</p></div>
  <div class="vz-card"><p class="vz-card-num">Field data</p><p>replaces every row here once it exists</p></div>
</div>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-metric-that-matters" markdown="block">
<summary><span class="layer-title">The metric that matters</span><span class="layer-sub">Cost per square mile, and the triangular-grid rule</span></summary>

**Cost per square mile = node cost × nodes per square mile.**
Node density is set by how far a node can hear the target, and by the need for **at least three nodes** to hear it at once (for a position fix from bearings).

A simple layout rule: on a triangular grid with spacing equal to the detection range *r*, most points are heard by ≥3 nodes. That grid needs about **1.15 / r² nodes per square mile** (r in miles).

</details>

<details class="layer" id="detection-range-by-target-working-estimates" markdown="block">
<summary><span class="layer-title">Detection range by target (working estimates)</span><span class="layer-sub">Each target's sound and range guess, and the few measurements</span></summary>

{: .warning }
> These ranges are planning guesses from public reporting and the general acoustics of each target. They must be replaced with field measurements. Wind, terrain, time of day and background noise can halve or double them.

| Target | Sound source | Working range estimate |
|---|---|---|
| Shahed/Geran-class one-way attack drone | Piston engine, propeller — loud, tonal | 0.6–3.1 mi |
| Cruise missile at low altitude | Jet/turbofan | 0.6–3.1 mi |
| Large multirotor / Mavic-class | Electric motors, props | 660–1,600 ft |
| Small FPV quad | Electric, small props, high-pitched | 330–980 ft |
| Fiber-optic FPV | Same as FPV — no RF, so acoustic is one of few options | 330–980 ft |

Squarehead's commercial array claims small-drone detection out to several hundred yards, consistent with the middle rows.

The first published field number for a cheap node comes from the open-source [VolAnti]({{ site.baseurl }}{% link research/open-source-builds.md %}#volanti) unit: a hovering quad detected at **340 ft** on a street with traffic, with expected range falling from 330–660 ft in still air to 16–82 ft in strong wind. That supports the low end of the small-quad rows and shows how much wind matters.

**Published measurements point lower still** ([full table]({{ site.baseurl }}{% link research/competitors.md %}#what-is-actually-measured)):
- **Cheap MEMS array:** eight cheap MEMS microphones on an ESP32-S3 detected a DJI Phantom to about 160 ft, with an effective range of about 200 ft and 5–8% false positives (Ghouli, *Acta Acustica* 2026).
- **Speaker tone:** studio and shotgun microphones heard a speaker tone set to a hovering drone's level at 230–310 ft in low wind and 120–150 ft in high wind (*Sensors* 2025).
- **None of these used an FPV.** Treat 330–980 ft for FPVs as unproven until T11.

</details>

<details class="layer" id="worked-examples" markdown="block">
<summary><span class="layer-title">Worked examples</span><span class="layer-sub">What area coverage costs at each range</span></summary>

| Range *r* | Nodes / sq mi | At $100 / node | At $450 / node (phone benchmark) |
|---|---|---|---|
| 1.9 mi | 0.33 | **$33 / sq mi** | $150 / sq mi |
| 0.6 mi | 3 | **$300 / sq mi** | $1,340 / sq mi |
| 980 ft | 33 | **$3,310 / sq mi** | $14,900 / sq mi |
| 490 ft | 132 | **$13,200 / sq mi** | $59,600 / sq mi |

Takeaways:

- Against Shahed-class targets, area coverage is **cheap** at any node price — national-scale coverage is realistic (Ukraine shows this).
- Against small electric drones, density explodes. Wide-area coverage is unrealistic; protect **points** (bases, positions, critical infrastructure) instead.
- Halving node cost and **doubling range** are worth the same: doubling range cuts density by 4×. Range improvements (height, windscreens, better arrays and classifiers) may be the bigger lever.

</details>

<details class="layer" id="what-drives-range" markdown="block">
<summary><span class="layer-title">What drives range</span><span class="layer-sub">Wind, terrain, height, background noise and the mic</span></summary>

- **Source loudness and frequency:** low-frequency engine tones travel further; high-pitched small props fade faster.
- **Spreading loss:** ~6 dB lost per doubling of distance, plus air absorption that grows with frequency.
- **Background noise:** a quiet rural night vs. a city day can be 30 dB apart.
- **Wind:** turbulence at the mic adds low-frequency noise; wind direction also bends sound.
- **Terrain and height:** obstacles block; ground absorbs; height helps (see [M4]({{ site.baseurl }}{% link models/m04-elevated-nodes.md %})).
- **Array gain:** combining N mics adds up to ~10·log₁₀(N) dB against diffuse noise — about 6 dB for 4 mics, 9 dB for 8.

</details>
