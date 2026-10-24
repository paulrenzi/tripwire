---
title: "M10 — Hybrid: acoustic + passive RF + camera"
parent: Sensor Models
nav_order: 10
---

# M10 — Hybrid: acoustic + passive RF + camera cueing
{: .no_toc }

<p class="vz-lede">Acoustic as the cheap wide-area tripwire, other sensors only where they add the most. This is how a credible military system will be judged.</p>

<div class="vz-meters">
  <div class="vz-meter vz-meter-key"><span class="vz-meter-name">Feasibility</span><span class="vz-dots" aria-label="4 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i></span><span class="vz-meter-v">4/5</span></div>
  <div class="vz-meter vz-meter-key"><span class="vz-meter-name">Payoff</span><span class="vz-dots" aria-label="4 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i></span><span class="vz-meter-v">4/5</span></div>
  <div class="vz-meter"><span class="vz-meter-name">Technical readiness</span><span class="vz-dots" aria-label="4 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i></span><span class="vz-meter-v">4/5</span></div>
  <div class="vz-meter"><span class="vz-meter-name">Cost per sq mi</span><span class="vz-dots" aria-label="3 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i><i class=""></i></span><span class="vz-meter-v">3/5</span></div>
  <div class="vz-meter"><span class="vz-meter-name">Persistence</span><span class="vz-dots" aria-label="4 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i></span><span class="vz-meter-v">4/5</span></div>
  <div class="vz-meter"><span class="vz-meter-name">Deployability</span><span class="vz-dots" aria-label="3 of 5"><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i><i class=""></i></span><span class="vz-meter-v">3/5</span></div>
</div>

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Unit cost</p><p>acoustic nodes everywhere ($60–120 each) + RF sensor ($50–500) and PTZ/thermal camera ($300–2,000+) at selected sites (est.)</p></div>
  <div class="vz-card"><p class="vz-card-num">Best against</p><p>all targets, including confirming what the acoustic layer flags</p></div>
  <div class="vz-card"><p class="vz-card-num">Payoff</p><p>Turns detections into something buyers' systems (Lattice, TAK) act on.</p></div>
</div>

## How it works

| Layer | What it adds | Cheap version |
|---|---|---|
| **Acoustic mesh (M1)** | Wide coverage, works without line of sight, works against **fiber-optic FPVs and pre-programmed drones that emit no radio** | ESP32 + MEMS array |
| **Passive RF** | Detects control/video links (2.4/5.8 GHz, 900 MHz, etc.); can give direction to the drone *and* the pilot | Software-defined radio (RTL-SDR/HackRF-class) + directional antennas |
| **Camera (visible/thermal)** | Confirms the target and gives a precise bearing/elevation | PTZ camera slewed to the acoustic track |
| **Radar data (only if a site already has it)** | Precise range and speed | Not part of our kit: radar emits and can be targeted. Fuse an existing feed; never add one |

The acoustic track **cues** the camera or RF sensor where to look; agreement between layers cuts false alarms sharply.

## Strengths

- Each layer covers another's blind spot. Acoustic catches what RF misses (fiber-optic and autonomous drones); RF and cameras catch quiet electric drones that acoustic hears only at short range.
- Sky Fortress already fuses acoustic data with radar feeds.
- Every layer we add is passive: acoustic, receive-only RF and cameras emit nothing for an adversary to locate.

## Limits and risks

- Integration work: shared timestamps, shared coordinate frames, track fusion.
- Cameras and RF sensors need power and bandwidth; place them sparingly.
- Passive RF raises legal issues in peacetime (intercepting communications).

## Open questions

- What's the false-alarm reduction when acoustic + camera must agree?
- Cheapest camera that can confirm a small quad at 980–1,600 ft.

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="rating-history" markdown="block">
<summary><span class="layer-title">Rating history</span><span class="layer-sub">Each change to the rating, and why</span></summary>

| Date | Rating | Why |
|---|---|---|
| 2026-10-15 | 4 | All components exist; integration is engineering, not research. |

</details>

<details class="layer" id="sources" markdown="block">
<summary><span class="layer-title">Sources</span><span class="layer-sub">Every source on this page</span></summary>

- [Militarnyi — SkyFortress fuses acoustic and radar data](https://militarnyi.com/en/news/lit-ukr-skyfortress-acoustic-uav-detection/)
- [arXiv 2007.07396 — Real-time drone detection with visible, thermal and acoustic sensors](https://arxiv.org/pdf/2007.07396)

</details>
