---
title: What the line gains in lives
parent: Research Notes
nav_order: 0.3
---

# What the forward line gains in lives
{: .no_toc }

<p class="vz-lede">What a minute of warning from a forward line does for troops' lives, against the ~10 seconds a sensor at the position gives. <strong>A Fermi estimate: a range, not a number.</strong> No source measures what warning does to drone casualties.</p>

<div class="stats">
  <div class="stat"><p class="stat-num">1–4</p><p class="stat-label">of every 100 drone casualties averted, our central guess</p></div>
  <div class="stat"><p class="stat-num">0.3–14</p><p class="stat-label">the plausible range</p></div>
  <div class="stat"><p class="stat-num">5–8</p><p class="stat-label">with a guard on the supply road too, on guarded roads</p></div>
  <div class="stat"><p class="stat-num">~50%</p><p class="stat-label">of casualties come in the rear, moving: who the minute is for</p></div>
</div>

### From 100 casualties to about 4

<div class="vz-funnel">
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:100%"></span><span class="vz-funnel-num">100</span><span class="vz-funnel-txt"><strong>drone casualties</strong> · in a unit with no radio detector</span></div>
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:50%"></span><span class="vz-funnel-num">50</span><span class="vz-funnel-txt"><strong>were moving in the rear</strong> · rotation, resupply, recovery, evacuation <em>claimed</em></span></div>
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:25%"></span><span class="vz-funnel-num">25</span><span class="vz-funnel-txt"><strong>from FPVs that fly in across the line</strong> · not ones already waiting in ambush <em>guess</em></span></div>
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:15%"></span><span class="vz-funnel-num">15</span><span class="vz-funnel-txt"><strong>that the line hears</strong> <em>guess · T11</em></span></div>
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:12%"></span><span class="vz-funnel-num">12</span><span class="vz-funnel-txt"><strong>where the alert gets through</strong> <em>guess · T9, T19</em></span></div>
  <div class="vz-funnel-row"><span class="vz-funnel-bar" style="width:7.2%"></span><span class="vz-funnel-num">7.2</span><span class="vz-funnel-txt"><strong>where troops act on it</strong> · not ignored as a false alarm <em>guess · T18</em></span></div>
  <div class="vz-funnel-row vz-funnel-us"><span class="vz-funnel-bar" style="width:3.6%"></span><span class="vz-funnel-num">3.6</span><span class="vz-funnel-txt"><strong>where acting avoids the hit</strong> <em>guess · T18</em></span></div>
</div>
<p class="vz-bar-note">Central guesses, each step a share of the one above. A unit that already has a radio detector gains only on fiber-optic FPVs: about 1–2. At a fixed position a minute adds little, since weapons need only seconds; the gain is for people about to move.</p>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">What the estimate covers, and how each input is marked</span></summary>

We estimate what a minute of warning from a forward listening line does for troops' lives, compared with the ~10 seconds a sensor at the position gives, and with the partner systems each could cue. This is a Fermi estimate. Each input is marked **measured**, **claimed** (a source says so, unverified) or **guess** (ours). No source measures what warning does to drone casualties, so the result is a range, not a number. What troops already carry is on [What troops have, and what listening adds]({{ site.baseurl }}{% link research/frontline-kit.md %}). Reviewed 2026-10-15.

</details>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">Position against movement, the central guess, the road guard, partner systems, the three tests</span></summary>

- **At a fixed position, a minute adds little over 10 seconds.** Shotguns, net-guns and turrets have the drone in range for only about 1–4 s, so seconds of warning are enough to have them ready ([A minute against the alternatives]({{ site.baseurl }}{% link research/problem-check.md %}#a-minute-against-the-alternatives)).
- **A minute matters for people about to move:** rotation, resupply, evacuation, recovery. About half of casualties happen in the rear doing exactly this. Ten seconds is too late for them, but a minute lets them hold or change a movement.
- **Our central guess:** the line averts **about 1–4 of every 100 drone casualties** in a unit that uses it. The plausible range is **0.3–14**.
  - The low end is a unit that already has a radio detector, in a sector with few fiber-optic FPVs.
  - The high end is a unit with no radio detector, in a sector where most FPVs are fiber-optic.
- **Guarding the supply road as well roughly doubles it, to about 5–8,** on the roads that are guarded. Posts by the road catch drones waiting in ambush, which the line can't ([below](#adding-a-guard-on-the-supply-road)).
- **Partner systems:**
  - Jammers and interceptors make the line's minute more useful against radio-controlled drones.
  - Against fiber-optic drones, nothing but avoidance works, and only the line gives a minute's warning of them.
- **Three tests decide which end of the range is real:**
  - T18: do troops act on alerts?
  - T9/T21: do the hops along the row hold, and does the light get home down the fiber?
  - T11: does a listener hear an FPV?

</details>

<details class="layer" id="scale" markdown="block">
<summary><span class="layer-title">Scale</span><span class="layer-sub">Casualties, the drone share, the rear share, the fiber-optic share, and what they imply</span></summary>

| Input | Value | Type |
|---|---|---|
| Ukrainian casualties, Feb 2022 – Dec 2025 | 500,000–600,000, of whom 100,000–140,000 killed ([CSIS, Jan 2026](https://www.csis.org/analysis/russias-grinding-war-ukraine)) | claimed (estimate) |
| Share caused by drones | "80% was the most common answer, with a range of 75-95%", from 15+ battalion and brigade commanders ([Rob Lee, ChinaTalk, Oct 2025](https://www.chinatalk.media/p/ukraines-drone-war)) | claimed (interviews) |
| Share taken in the rear | "approximately 50% of their casualties are taken in the rear from Russian FPVs, artillery and glide bombs", during rotation, resupply and recovery ([RUSI, Feb 2025](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)) | claimed (brigade reports) |
| Fiber-optic share of FPVs | 30–50% in some sectors, up to 90% in one Kharkiv sector ([sources]({{ site.baseurl }}{% link research/problem-check.md %}#the-threat-is-real-and-is-the-main-killer)); no front-wide figure | claimed, varies by sector |
| Casualties per company or per km of front | Not found | none |

**What this implies (our arithmetic):**
- Drones account for roughly 9,000–10,000 Ukrainian casualties a month (CSIS total × 80%, spread over about 46 months).
- If every unit fielded a line and the central guess held, that would be on the order of 100–400 casualties a month averted.
- That is an upper bound for the idea, not a forecast. No unit-level casualty rate was found, so we can't yet say what one line saves one battalion.

</details>

<details class="layer" id="the-chain-per-100-drone-casualties" markdown="block">
<summary><span class="layer-title">The chain, per 100 drone casualties</span><span class="layer-sub">The five conditions a minute needs, each with its guess, range and test</span></summary>

A minute of warning only saves someone who meets all five conditions:
1. They are about to be exposed.
2. They are threatened by a drone that flies in across the line.
3. The line hears that drone.
4. The alert reaches them.
5. They act on it in a way that avoids the hit.

| Step | Central guess | Range | Type | What would measure it |
|---|---|---|---|---|
| Drone casualties among people moving in the rear (rotation, resupply, recovery, evacuation) | 50 of 100 | 35–60 | claimed (RUSI: about half, but that figure includes artillery and glide bombs) | unit casualty logs (T18) |
| …from FPVs that fly in across the line, not ones already waiting in ambush or launched inside it | 50% | 30–70% | guess. Fiber-optic FPVs wait by roads for up to 12 h ([Trench Art](https://www.trenchart.us/p/russias-best-drones-lie-in-wait-beside)) and stay silent until launch | T18 |
| …that the line hears | 60% | 40–85% | guess. No FPV has been range-tested acoustically | T11 |
| …where the alert gets through | 80% | 60–95% | guess. Jamming beside the receiver could cut this to near zero unless the last link is wired ([jamming]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)) | T9, T17, T19 |
| …where troops act on it rather than ignoring it (false-alarm fatigue) | 60% | 30–80% | guess | T18 |
| …and acting avoids the hit (holding the run, stopping under trees, delaying the evacuation) | 50% | 30–70% | guess | T18 |
| **Averted, unit with no radio detector** | **≈3.6** | **≈0.4–14** | | |
| **Averted, unit that already has a radio detector** (the line adds only fiber-optic FPVs, 30–50% of them) | **≈1–2** | **≈0.1–7** (up to the full figure where fiber-optic is ~90%) | | |

The ranges multiply the low ends together and the high ends together, so the true value is very unlikely to sit at either extreme.

**Not yet subtracted:**
- **Harm from alerts themselves.** In Israel, people running for shelter after sirens are themselves injured. A front-line false alarm that sends troops into the open would cost lives.
- **Giving away positions.** An alert or a jammer that transmits can reveal the unit's position. The tripwire's listeners only receive at the unit, but a cued jammer transmits.
- **Hours lost.** Movements held on false alarms cost time; whether units would accept that is a T18 question.

</details>

<details class="layer" id="a-minute-against-10-seconds-with-partner-systems" markdown="block">
<summary><span class="layer-title">A minute against 10 seconds, with partner systems</span><span class="layer-sub">What each warning time lets jammers, interceptors and avoidance do</span></summary>

| Partner system | With ~10 s (sensor at the position, or a soldier's ear) | With ~1 min (forward line) | What the minute adds in lives |
|---|---|---|---|
| **Shotgun, rifle, net-gun** | Enough: the drone is in range for about 1–4 s | Same | ≈0 |
| **AI turret** | Enough to slew and track | Same | ≈0 |
| **Cover at the position** | Enough if the dugout is a few yards away | Smoke and dispersal also become possible | small |
| **Holding a movement** (vehicle, resupply, walkers, evacuation) | Too late: they are already in the open | A go/no-go call before setting out. Russia's roadside drone "traffic lights" do this on roads ([Espreso, Dec 2024](https://global.espreso.tv/russia-ukraine-war-russia-installs-traffic-lights-to-counter-ukrainian-fpv-drones)) | **most of the chain above** |
| **Cued jammer** (e.g. CERBAIR MEDUSA, [partners]({{ site.baseurl }}{% link research/competitors.md %}#partners-and-the-budget-we-compete-for)) | Switches on while the drone is already on its final approach | Switches on early and only when a drone is coming, so it transmits less. Also covers radio links its own detector misses | radio FPVs only, and fading: "Jamming no longer works", says a brigade EW commander; **none against fiber-optic** |
| **Interceptor drone** | Can't launch and climb in time | Plausibly the minimum lead time (our inference; no source gives launch-to-intercept times against FPVs) | unknown |
| **Nets, tunnels, cable traps** | Need no warning | Need no warning | ≈0; they compete with the line for the same budget |

**What this shows (inference):**
- Against **radio-controlled FPVs**, a radio detector already gives a minute, and partner jammers already depend on it. The line adds little there beyond cueing jammers for drones the detector misses, and jamming itself is losing ground.
- Against **fiber-optic FPVs**, jammers do nothing and weapons get only seconds whatever the warning. The line's minute is the only early warning available, and its value is entirely in **avoidance by people who are about to move**.
- So the line's value grows with the fiber-optic share in a sector and with how much movement the unit has to make in the open.

</details>

<details class="layer" id="adding-a-guard-on-the-supply-road" markdown="block">
<summary><span class="layer-title">Adding a guard on the supply road</span><span class="layer-sub">How posts by the road catch drones waiting in ambush</span></summary>

The chain above writes off the half of rear casualties caused by drones already waiting by the road: a position's line can't hear something sitting still. A [road guard]({{ site.baseurl }}{% link models/route-guard.md %}) changes that. In the route model, posts along the road hear every drone that lands within 300 ft of it, and keep the alert ("drone waiting near post 17") up for hours. A rough re-run, using the same steps:

| | Central | Range |
|---|---|---|
| Drones flying in, warned by the minute (the chain above) | ≈3.6 | ≈0.2–19 |
| **Drones waiting by the road, caught by the posts:** 50 rear × 50% waiting × 50% caught (30–70%) × 80% alert through × 60% acted on × 70% avoided (50–85%) | **≈4.2** | ≈0.3–19 |
| **Total, unit with no radio detector** | **≈8** | |
| **Total, unit that already has a radio detector** | **≈5–6** | |

- **Caught: 50%, a guess.** Every landing within 300 ft is heard in the model, but only 10–13% of landings 600–1,500 ft out, and drones parked before the guard went in or carried in on foot are missed.
- **No hearing step:** the loudest post is a median ~340 ft from a landed drone. That is from the model, not a measurement (T20).
- **Avoided: 70%, not 50%.** A drone known to sit near one post for hours is easier to avoid or clear than one arriving in a minute.
- **A radio detector barely dents the new row.** Drones waiting by roads are mostly fiber-optic ([Trench Art](https://www.trenchart.us/p/russias-best-drones-lie-in-wait-beside)), and a landed drone isn't transmitting.
- **It applies only to movement on guarded roads.** The last stretch on foot to a position isn't covered. If half a unit's movement casualties happen on its guarded roads, the gain is about half: roughly 4 more per 100, not 8.
- **Without the cable and lamps,** a truck with its jammer on hears nothing on the move ([jamming]({{ site.baseurl }}{% link models/route-guard.md %}#jamming-and-a-wire-along-the-road)).

</details>

<details class="layer" id="is-it-worth-the-cost" markdown="block">
<summary><span class="layer-title">Is it worth the cost?</span><span class="layer-sub">The line's cost against what it might save</span></summary>

The tripwire costs about $2.0–3.1k for a unit's package and about $3–5k a year in re-lays, with a solar panel on every dart ([running cost]({{ site.baseurl }}{% link models/tripwire.md %}#the-running-cost-lines-are-ammunition)).

**Inference (rule of thumb, no source):** if a battalion takes even a few dozen drone casualties a year, averting 1–4% of them is plausibly worth that cost. It is not worth it where:
- most drone casualties come from FPVs already waiting in ambush, or launched inside the line; or
- the roads are already netted.

A guard on a supply road costs more: about $20–30k a year for 4 mi with solar ([costs]({{ site.baseurl }}{% link costs.md %}#guarding-a-road)). It is aimed at the rear, where about half the casualties are.

</details>

<details class="layer" id="the-israeli-analogue" markdown="block">
<summary><span class="layer-title">The Israeli analogue</span><span class="layer-sub">What sirens and shelters teach, including harm from alerts</span></summary>

- **What was found:** Zucker and Kaplan modelled rocket casualties in Sderot and found expected casualties per rocket would be "between three (best-case) and nine (worst-case) times higher" without civil defence ([Studies in Conflict & Terrorism, 2014](https://ideas.repec.org/a/taf/uterxx/v37y2014i3p258-266.html)).
- **Why it doesn't transfer directly:**
  - That civil defence was "safe rooms, bomb shelters, early detection alarms, and missile defense" together, so the share due to warning alone is not separated.
  - Civilians in a town are not soldiers on the move.
- **What it does show:** warning paired with somewhere to go saves many lives. Warning with nowhere to go saves few. The line's minute is worth most where troops have a real alternative to moving.

</details>

<details class="layer" id="what-would-change-this-estimate" markdown="block">
<summary><span class="layer-title">What would change this estimate</span><span class="layer-sub">The findings that would move it up or down</span></summary>

- **T18 (interviews):**
  - What share of a unit's drone casualties happen while moving.
  - How many come from FPVs that wait in ambush.
  - Whether drivers and medics would hold a movement on an alert.
  - How far from the road waiting drones land, and how often trucks run their jammers ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})).
- **T11:** whether a listener hears an FPV at all, and at what distance.
- **T9/T17:** whether the alert gets out of the trees.
- **A unit casualty rate:** with one, the estimate becomes lives per battalion per year, and can be set against the re-lay cost.

</details>
