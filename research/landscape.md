---
title: "The wider field: eight sensor models"
parent: Research Notes
nav_order: 9
---

<div class="hero" markdown="1">
<span class="hero-tag">RESEARCH NOTEBOOK · REVIEWED 2026-10-15</span>

# Low-cost acoustic drone detection

Can a mesh of cheap microphones detect and locate drones well enough to plot them on a shared map, for a fraction of what military counter-UAS sensors cost today?
</div>

<div class="stats">
  <div class="stat"><p class="stat-num">8</p><p class="stat-label">sensor models rated 3 or higher</p></div>
  <div class="stat"><p class="stat-num">$60</p><p class="stat-label">low end of a purpose-built node</p></div>
  <div class="stat"><p class="stat-num">14k</p><p class="stat-label">nodes in Sky Fortress (upper est.)</p></div>
  <div class="stat"><p class="stat-num">M1</p><p class="stat-label">recommended core</p></div>
</div>

<p class="kicker">01 · The idea</p>

## Listen, classify, report, fuse.

1. Cheap sensor nodes listen for drone sound signatures (engines, propellers).
2. Each node classifies what it hears **on the device** and estimates a **bearing** (direction) to it.
3. Nodes send small detection reports — never raw audio — over a mesh or cellular link.
4. A central service fuses bearings from several nodes into a **position and track**, and publishes it on a map and to military systems (TAK / Cursor-on-Target, SAPIENT).

Software is the comparatively easy part. The hard parts are **range** (how far a node can hear), **direction accuracy**, **false alarms**, and **keeping thousands of nodes alive outdoors** for months.

{: .important }
> The proven model is a dense, fixed network of cheap ground sensors. Ukraine's Sky Fortress runs on ~10,000–14,000 of them at about $400–1,000 each, against Shaheds and cruise missiles. Against FPVs at the front, no acoustic model is proven yet. The most credible way to beat that cost is a **purpose-built mic-array node at roughly $60–120** (a parts estimate at volume, against Sky Fortress's reported field cost), mounted high (masts, rooftops, telecom towers), that reports bearings instead of raw detections. The only airborne option still on the list is lighter-than-air: a tethered aerostat.


## Eight ways to build the network.

<div class="vz-gridwrap">
<p class="vz-grid-ylab">↑ Payoff if it works</p>
<div class="vz-grid">
<span class="vz-grid-y">5</span>
<span class="vz-gcell"></span>
<span class="vz-gcell"></span>
<span class="vz-gcell vz-gcell-hot"><a class="vz-gchip vz-gchip-us" href="{{ site.baseurl }}{% link models/tripwire.md %}" title="Drone-laid tripwire (use case: M3 nodes laid by M7)">Tripwire</a></span>
<span class="vz-gcell vz-gcell-hot"></span>
<span class="vz-grid-y">4</span>
<span class="vz-gcell"></span>
<span class="vz-gcell"><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m07-drone-deployed-nodes.md %}" title="Drone-deployed ground nodes">M7</a></span>
<span class="vz-gcell vz-gcell-hot"><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}" title="Fixed ground mic-array mesh">M1</a><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m04-elevated-nodes.md %}" title="Elevated fixed nodes (towers, masts)">M4</a><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m10-hybrid-cueing.md %}" title="Hybrid: acoustic + passive RF + camera cueing">M10</a></span>
<span class="vz-gcell vz-gcell-hot"></span>
<span class="vz-grid-y">3</span>
<span class="vz-gcell"></span>
<span class="vz-gcell"><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m03-single-mic-tdoa.md %}" title="Single-mic nodes + time-difference">M3</a><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m09-mobile-nodes.md %}" title="Vehicle / soldier-mounted mobile nodes">M9</a></span>
<span class="vz-gcell"></span>
<span class="vz-gcell vz-gcell-hot"><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m02-phone-network.md %}" title="Phone-based sensor network">M2</a></span>
<span class="vz-grid-y">2</span>
<span class="vz-gcell"></span>
<span class="vz-gcell"><a class="vz-gchip" href="{{ site.baseurl }}{% link models/m05-aerostats.md %}" title="Tethered aerostats / balloons">M5</a></span>
<span class="vz-gcell"></span>
<span class="vz-gcell"></span>
<span></span><span class="vz-grid-x">2</span><span class="vz-grid-x">3</span><span class="vz-grid-x">4</span><span class="vz-grid-x">5</span>
</div>
<p class="vz-grid-xlab">Feasible today →</p>
</div>
<p class="vz-bar-note">Each model's two scores, 1 to 5. Tap one to open its page. Top right is where to be: the tripwire has the highest payoff, and is a 4 on feasibility now that fiber has taken out its long radio link; its field tests still have to run. M1 (cheap mic-array nodes), M4 (raising them up) and M10 (adding radio and camera cues) are the solid middle.</p>

<details class="layer" markdown="block">
<summary><span class="layer-title">The scores as a table</span><span class="layer-sub">Each model's feasibility, payoff, unit cost and status, and how the scores are set</span></summary>

Each model gets two scores. **Feasible** runs from 1 (not feasible now) to 5 (proven, build today). **Payoff** runs from 1 to 5 for how much it would matter to units in the field, against small drones including fiber-optic FPVs, if it works. Models rated below 3 (perch-and-listen drones, flying microphone swarms, and fiber-optic distributed acoustic sensing) have been dropped. See [how ratings work](#how-ratings-work).

| # | Model | Feasible | Payoff | Unit cost | Status |
|---|---|:-:|:-:|---|---|
| UC | [Drone-laid tripwire (use case: M3 nodes laid by M7)]({{ site.baseurl }}{% link models/tripwire.md %}) | <span class="score score-hi">4</span> | <span class="score score-hi">5</span> | ~$2.1–3.5k package + ~$1.6–6.3k/yr re-lays | Highest payoff; fiber replaced the radio link home |
| M1 | [Fixed ground mic-array mesh]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}) | <span class="score score-hi">4</span> | <span class="score score-hi">4</span> | $60–120 | Recommended core |
| M2 | [Phone-based sensor network]({{ site.baseurl }}{% link models/m02-phone-network.md %}) | <span class="score score-hi">5</span> | <span class="score score-mid">3</span> | $100–500 | Proven at scale (Ukraine) |
| M3 | [Single-mic nodes + time-difference]({{ site.baseurl }}{% link models/m03-single-mic-tdoa.md %}) | <span class="score score-mid">3</span> | <span class="score score-mid">3</span> | $30–50 | Cheapest, harder to make work |
| M4 | [Elevated fixed nodes (towers, masts)]({{ site.baseurl }}{% link models/m04-elevated-nodes.md %}) | <span class="score score-hi">4</span> | <span class="score score-hi">4</span> | $80–300 + mount | Recommended placement for M1 |
| M5 | [Tethered aerostats / balloons]({{ site.baseurl }}{% link models/m05-aerostats.md %}) | <span class="score score-mid">3</span> | <span class="score score-lo">2</span> | $5k–50k+ | Niche, gap-filler |
| M7 | [Drone-deployed ground nodes]({{ site.baseurl }}{% link models/m07-drone-deployed-nodes.md %}) | <span class="score score-mid">3</span> | <span class="score score-hi">4</span> | node + delivery | Deployment method for M1 |
| M9 | [Vehicle / soldier-mounted mobile nodes]({{ site.baseurl }}{% link models/m09-mobile-nodes.md %}) | <span class="score score-mid">3</span> | <span class="score score-mid">3</span> | $150–1,000 | Being trialled (Zvook) |
| M10 | [Hybrid: acoustic + passive RF + camera cueing]({{ site.baseurl }}{% link models/m10-hybrid-cueing.md %}) | <span class="score score-hi">4</span> | <span class="score score-hi">4</span> | $100–2,000 / site | Phase 2 add-on |
{: .matrix }

Each model's page says what it works best against. Reference point: commercial acoustic arrays such as Squarehead **Discovair G2** (Norway) detect small drones at several hundred yards and are sold inside full counter-UAS systems at far higher prices. See [Existing systems]({{ site.baseurl }}{% link research/existing-systems.md %}).

</details>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="whats-out-there-what-works-what-failed" markdown="block">
<summary><span class="layer-title">What's out there, what works, what failed.</span><span class="layer-sub">The camps in counter-drone sensing, what each is good at, and its blind spot</span></summary>

Counter-drone sensing has split into a few camps. Each one is good at something, and each has a blind spot.

**What works.** Ukraine settled half the question. Cheap acoustic networks work in war **against Shaheds and cruise missiles over the rear**. Nobody has shown they work against FPVs at the front. The US Army's 2026 review says they do, but its sources are about Shaheds ([why that matters]({{ site.baseurl }}{% link research/competitors.md %}#two-markets-only-one-of-them-ours)). Sky Fortress runs about 14,000 phone-and-microphone sensors on poles at $400–1,000 each, roughly $5M for the whole network, and tracks Shaheds and cruise missiles with them. Zvook puts microcomputers on radio towers and is trialling a vehicle version with NATO. At the top end, Squarehead's Discovair and Microflown's AVISA show what premium acoustic arrays claim without line of sight: a few hundred yards against small drones. Soldiers already buy cheap radio detectors in numbers; BlueBird's Chuyka 3.0 costs $584–701 and picks up analog FPV video at up to 2.5 mi. Anduril's WISP cameras and Lattice software sit at the expensive end and are becoming the US Army's backbone.

**What falls short, and why.** The blind spots are exactly where drones are moving.

- **Radio detectors** hear radio, not drones. Fiber-optic FPVs and pre-programmed drones are invisible to them, and they rarely give a position to put on a map.
- **Radar** is accurate, but it transmits all the time, so it can be found and targeted. It also needs line of sight and costs $40k–160k a unit.
- **Cameras**, even WISP, can't see a low drone behind trees, buildings or a ridge.
- **Premium acoustic arrays** work, but they are single expensive sensors sold through prime contractors. Even they top out at a few hundred yards, so better hardware alone doesn't buy more range.
- **Sky Fortress** is built for national coverage of loud engine drones over cellular networks, not for portable kits that units can carry against FPVs.

**What the front tells us.** The evidence makes a strong case that the gap is real, and that it is where units are dying ([full review]({{ site.baseurl }}{% link research/problem-check.md %})):

- **Drones cause about 80% of casualties**, by analysts' estimates ([NPR, Oct 2026](https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)).
- **Troops survive mainly by not moving:** underground, under nets, hiding when they hear a drone, taking hours to cover half a mile and going months without rotation (same source). That is coping, not protection.
- **The fastest-growing threat beats the detectors units carry.** Fiber-optic FPVs send no radio, so radio detectors miss them ([Kyiv Independent](https://kyivindependent.com/as-russias-fiber-optic-drones-flood-the-battlefield-ukraine-is-racing-to-catch-up/)); they are 30–50% or more of FPVs in some sectors.
- **The expensive answer isn't there.** We found no reporting of Anduril's WISP at Ukraine's front ([its published use](https://dronexl.co/2026/08/06/anduril-wisp-washington-national-guard-drones-birds/) is US domestic security), and cameras can't see through tree lines anyway.
- **Ukrainian builders are moving the same way.** Zvook announced an acoustic FPV sensor for front-line positions in January 2026 ([Militarnyi](https://militarnyi.com/en/news/ukraine-develops-acoustic-detector-for-fpv-drones/)). It's now on sale at about $834–950 per sensor, but there's no independent test or reported deployment. A US startup, RADD, is building a soldier-worn version, and Denmark's Komodo already sells a sensor that drones can drop.

- **What troops have doesn't cover it.** Against fiber-optic FPVs the baseline is ears, eyes and a firearm. Jamming is failing ("Jamming no longer works", says a brigade EW commander), nets leak, and an AI turret is in only a handful of units ([what troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})).

**What a minute is worth.** Weapons need only seconds, so at a fixed position a minute adds little. Its value is a go/no-go call for people about to move. Against fiber-optic FPVs, which nothing else detects, our central guess is that a forward line averts about **1–4 of every 100 drone casualties** (range 0.3–14) ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})). Front-line interviews (T18) would narrow that; the next real test is radio under trees (T9).

**The build path.** The [MVP path]({{ site.baseurl }}{% link mvp.md %}) takes the tripwire from an $80 radio test to a six-listener line in five gated layers, about $600–750 in all, with parts you can order today.

**What failed outright.** Microphones on flying drones don't work: the listener's own rotors sit inches from the mic, and published measurements put the target 10–30 times quieter than the drone's own noise. Perching drones (land, stop the motors, listen) fix that, but landing reliably and keeping them powered is still research. Fiber-optic acoustic sensing turns a cable into a long line of microphones, but buried fiber hears airborne sound poorly and has only detected vehicles close to the cable. All three rated below 3 and are no longer on this site.

</details>

<details class="layer" id="the-routes-still-open" markdown="block">
<summary><span class="layer-title">The routes still open.</span><span class="layer-sub">Where a cheap acoustic network could still win</span></summary>

The gap nobody fills cheaply is **passive detection of drones that don't transmit and can't be seen, at a price every unit can carry.** Four practical routes lead there:

1. **Purpose-built mic-array nodes at $60–120, mounted high** ([M1]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}) on [M4]({{ site.baseurl }}{% link models/m04-elevated-nodes.md %}) placements). Many cheap nodes rather than one better sensor, each reporting a bearing rather than a bare alarm. This is the core.
2. **Phones as a fast start** ([M2]({{ site.baseurl }}{% link models/m02-phone-network.md %})). Proven at scale by Sky Fortress. Trade unit quality for speed when coverage is needed this month.
3. **Portable unit kits, and a [drone-laid tripwire]({{ site.baseurl }}{% link models/tripwire.md %}).** 8–12 nodes around a ~1,600 ft perimeter for about $1,500–2,500, placed by hand or dropped by drone ([M7]({{ site.baseurl }}{% link models/m07-drone-deployed-nodes.md %})), with vehicle-mounted nodes ([M9]({{ site.baseurl }}{% link models/m09-mobile-nodes.md %})) for units on the move. This is the form factor Sky Fortress wasn't built for. Dropping cheap listeners about a mile forward turns ~10 seconds of warning into a minute or more. The listeners are consumables, so add an estimated $3–5k a year in re-lays with solar ([running cost]({{ site.baseurl }}{% link models/tripwire.md %}#the-running-cost-lines-are-ammunition)).
4. **Be the sensor, not the platform** ([M10]({{ site.baseurl }}{% link models/m10-hybrid-cueing.md %})). Feed tracks into Lattice, TAK and SAPIENT, and use acoustic bearings to point cameras and RF sensors at drones they would otherwise miss.

The lasting advantage isn't the hardware, which anyone can copy. It's **training data** (real combat recordings and local false-alarm sounds) and integrations that are already in the field. Details and sources are in [Existing systems]({{ site.baseurl }}{% link research/existing-systems.md %}) and the [competitor analysis]({{ site.baseurl }}{% link research/competitors.md %}).

</details>

<details class="layer" id="passive-by-design" markdown="block">
<summary><span class="layer-title">Passive by design.</span><span class="layer-sub">Why listening, not emitting, matters near the front</span></summary>

Many of the counter-drone SBIR topics we are targeting ask for **passive** detection, and for a hard reason: a radar transmits all the time, and an adversary can locate that transmission and send a drone or munition down it. A microphone transmits nothing while it listens.

So every model on this site has to work without an active emitter:

- **Listening is silent.** Nodes detect, classify and take a bearing on the device and emit nothing while they do it.
- **Reports are short and rare.** A node sends a few-byte detection report only when it hears something, at low power, never a continuous signal. Where that is still too much, a node can be wired, use fiber, or store reports and burst them later.
- **No radar in our kit.** We add no emitter of our own. If a site already runs a radar, its track can be fused in, but nothing we field depends on it.
- **Other sensors must be passive too.** Passive RF (receive only) and cameras (visible or thermal) qualify; anything that illuminates the target does not.

</details>

<details class="layer" id="the-layer-the-others-miss" markdown="block">
<summary><span class="layer-title">The layer the others miss.</span><span class="layer-sub">Positioning: the second box beside the radio detector, honest about range, feeding Lattice</span></summary>

For front-line positions: *an acoustic alarm that hears the FPVs radio detectors can't, especially fiber-optic ones: the second box next to the radio detector.*

**Who we compete with.** We don't compete with Sky Fortress, Anduril or radar: they serve the rear or aren't at the front. At a position, the bar is a **soldier's own ears**, and nobody has measured how early a sentry hears a fiber-optic FPV. The partner is the **radio detector** the unit already carries. The direct competitors are **Zvook's NW0**, on sale at about $834–950 per sensor but needing 15–18 W of power, and **RADD's GLADIUS**, a soldier-worn US sensor. Both are claims only. **Per sensor we are roughly 3–50x cheaper than NW0**: $17–50 per tripwire listener and about $125–300 per hand-placed node, with no power supply. Cost per position depends on real range, which nobody has measured for either. At the position, AI turrets now reaching units carry their own sensors, so forward warning is where we stand alone. A Ukrainian LoRa acoustic module (DroneAlert) is listed at about $211, so only our throwaway listener is clearly cheaper than the market. We also offer **weeks on a battery and lines laid forward**, which neither NW0 nor RADD does, and only distance gives a minute of warning ([build or scrap?]({{ site.baseurl }}{% link research/build-or-scrap.md %})). [The priority list]({{ site.baseurl }}{% link research/competitors.md %}#the-priority-list).

**Be honest about range.** The only measured range for cheap microphones is about 160–200 ft against a consumer drone. In a quiet field, people heard the same class of drone faintly at 490 ft. No study has flown an FPV at distance ([what's measured]({{ site.baseurl }}{% link research/competitors.md %}#what-is-actually-measured)).

Being passive sets us apart from radar, not from everyone: cameras such as Anduril's WISP are passive too. What sets us apart is **hearing what they can't see**: a small drone flying low behind trees, buildings or a ridge, including fiber-optic FPVs that give off no radio signal for a detector to catch.
Against small quadcopters even premium arrays reach only a few hundred yards, so this is an **early-warning perimeter that cues cameras and other sensors**, At a position that gives seconds of warning; laid 1.2–2.5 mi forward, about a minute. It is not wide-area coverage.

The first integration target is **Anduril Lattice**, which the US Army has picked as its counter-drone backbone. A cheap passive sensor that feeds Lattice makes the expensive systems better instead of competing with them. See [Lattice integration]({{ site.baseurl }}{% link research/integration.md %}#anduril-lattice).

[Read the competitor analysis →]({{ site.baseurl }}{% link research/competitors.md %}){: .btn .btn-primary }

</details>

<details class="layer" id="how-ratings-work" markdown="block">
<summary><span class="layer-title">How ratings work</span><span class="layer-sub">What feasible and payoff mean, and how a model earns each score</span></summary>

**Feasibility** is scored 1–5 on four axes, and the feasibility score is a judgement, not an average:

| Axis | Question |
|---|---|
| **Technical readiness** | Can it be built with parts and methods that exist today? |
| **Cost per sq mi** | What does it cost to cover an area, not just per unit? |
| **Persistence** | Can it run unattended for weeks or months? |
| **Deployability** | Can non-specialists put it out and keep it running at scale? |

**Payoff** is scored separately, 1–5: how much the model would matter for protecting units in the field against small drones, including fiber-optic FPVs, if it works. A model can be easy and unimportant (phones in a rear area) or hard and decisive (the drone-laid tripwire). Read the two together.

The single most important number is **cost per square mile covered = node cost × node density**. Node density is driven by detection range, which differs hugely by target. See [Range and cost-per-square-mile model]({{ site.baseurl }}{% link research/range-and-cost.md %}).

</details>

<details class="layer" id="how-to-add-to-this" markdown="block">
<summary><span class="layer-title">How to add to this</span><span class="layer-sub">How to propose a model or correct a rating</span></summary>

- **New research note:** add a Markdown file to `research/` with `parent: Research Notes` in the front matter.
- **New model:** copy `models/_template.md`, number it `mNN-short-name.md`, and add a row to the matrix above. It must work without an active emitter, it is only listed if its feasibility rates 3 or higher, and it needs both a feasibility and a payoff score.
- **Changed a rating?** Say why in the model page's *Rating history* and in the [Changelog]({{ site.baseurl }}{% link changelog.md %}).
- Mark anything not yet confirmed with an `{: .warning }` callout.

</details>
