---
title: Overview
layout: home
nav_order: 1
---

<div class="hero" markdown="1">
<span class="hero-tag">RESEARCH NOTEBOOK · REVIEWED 2026-10-23</span>

# The drone-laid acoustic tripwire

Don't try to make a microphone hear farther. Drop cheap ones about a mile forward, so a front-line unit gets about a minute of warning of an incoming FPV instead of about ten seconds, including fiber-optic FPVs that emit no radio.
</div>

<div class="stats">
  <div class="stat"><p class="stat-num">~1 min</p><p class="stat-label">warning from a row about 1 mi out, against ~10 s from a ring near the unit (est.)</p></div>
  <div class="stat"><p class="stat-num">$38 / $128</p><p class="stat-label">a throwaway dart, and a tip dart with its fiber (small-batch est.)</p></div>
  <div class="stat"><p class="stat-num">160–200 ft</p><p class="stat-label">the only measured cheap-mic range; we plan on 330–980 ft, unproven</p></div>
  <div class="stat"><p class="stat-num">4/5</p><p class="stat-label">feasibility: every part exists and fiber took out the long radio link; the chain is still untested</p></div>
</div>

{: .warning }
> **Nothing here has been built or field-tested yet.** Ranges, costs and warning times are estimates from published sources, labelled as such. The tests that would settle them are cheap, and listed under the [Saturday test]({{ site.baseurl }}{% link weekend-test.md %}) and the [MVP path]({{ site.baseurl }}{% link mvp.md %}).

<p class="kicker">01 · The idea</p>

## Lay a line, listen quietly, report back, warn.

<figure class="vz-figure">
<svg class="vz-hero vz-hero-wide" viewBox="0 0 720 430" role="img" aria-labelledby="vz-hero-t vz-hero-d">
  <title id="vz-hero-t">How the tripwire works</title>
  <desc id="vz-hero-d">Seen from above. A row of listening darts lies across the enemy's approach about a mile out from the unit. A drone crossing the row is heard by the nearest dart; the alert hops along the row and comes home down two fibers to the unit, about a minute before the drone arrives. A ring of microphones at the unit would hear it only about ten seconds out.</desc>
  <rect x="0" y="0" width="720" height="62" fill="#f3e1d8"/>
  <text x="20" y="39" class="vz-t-tag">ENEMY SIDE</text>
  <g fill="#d2451e" fill-opacity=".07" stroke="#d2451e" stroke-opacity=".45" stroke-dasharray="4 4">
    <circle cx="60" cy="140" r="50"/><circle cx="135" cy="140" r="50"/><circle cx="210" cy="140" r="50"/>
    <circle cx="285" cy="140" r="50"/><circle cx="360" cy="140" r="50"/><circle cx="435" cy="140" r="50"/>
    <circle cx="510" cy="140" r="50"/><circle cx="585" cy="140" r="50"/><circle cx="660" cy="140" r="50"/>
  </g>
  <path d="M60 140 Q60 330 316 350" fill="none" stroke="#2f6b3a" stroke-width="3"/>
  <path d="M660 140 Q660 330 404 350" fill="none" stroke="#2f6b3a" stroke-width="3"/>
  <circle cx="360" cy="350" r="52" fill="none" stroke="#6a625a" stroke-width="2" stroke-dasharray="6 5"/>
  <line x1="478" y1="22" x2="372" y2="318" stroke="#151515" stroke-width="2.5" stroke-dasharray="8 6"/>
  <g transform="translate(466 56)" stroke="#151515" stroke-width="3">
    <line x1="-11" y1="-11" x2="11" y2="11"/><line x1="11" y1="-11" x2="-11" y2="11"/>
    <g fill="#fff" stroke-width="2"><circle cx="-11" cy="-11" r="5"/><circle cx="11" cy="-11" r="5"/><circle cx="-11" cy="11" r="5"/><circle cx="11" cy="11" r="5"/></g>
  </g>
  <g fill="#d2451e">
    <circle cx="60" cy="140" r="7"/><circle cx="135" cy="140" r="7"/><circle cx="210" cy="140" r="7"/>
    <circle cx="285" cy="140" r="7"/><circle cx="360" cy="140" r="7"/><circle cx="510" cy="140" r="7"/>
    <circle cx="585" cy="140" r="7"/><circle cx="660" cy="140" r="7"/>
  </g>
  <circle cx="435" cy="140" r="11" fill="#d2451e" stroke="#151515" stroke-width="3"/>
  <text x="494" y="62" class="vz-t">FPV crosses the row</text>
  <text x="90" y="224" class="vz-t-small">darts ~960 ft apart</text>
  <line x1="300" y1="238" x2="300" y2="318" stroke="#151515" stroke-width="2"/>
  <path d="M293 246 L300 234 L307 246 M293 310 L300 322 L307 310" fill="none" stroke="#151515" stroke-width="2"/>
  <text x="288" y="266" class="vz-t-big" text-anchor="end">~1 mi</text>
  <text x="290" y="296" class="vz-t-accent" text-anchor="end" style="font-size:19px">≈ 1 min warning</text>
  <text x="575" y="300" class="vz-t-green" text-anchor="end">fiber home</text>
  <rect x="316" y="332" width="88" height="36" fill="#151515"/>
  <text x="360" y="357" class="vz-t-unit" text-anchor="middle">UNIT</text>
  <text x="360" y="424" class="vz-t-small" text-anchor="middle">a ring at the unit hears it only ~10 s out</text>
</svg>
<svg class="vz-hero vz-hero-tall" viewBox="0 0 360 530" role="img" aria-labelledby="vz-hero2-t">
  <title id="vz-hero2-t">How the tripwire works: a row of darts about a mile out hears the drone and warns the unit about a minute ahead; a ring at the unit hears it about ten seconds out</title>
  <rect x="0" y="0" width="360" height="44" fill="#f3e1d8"/>
  <text x="14" y="29" class="vz-t-tag" style="font-size:15px">ENEMY SIDE</text>
  <g fill="#d2451e" fill-opacity=".07" stroke="#d2451e" stroke-opacity=".45" stroke-dasharray="4 4">
    <circle cx="30" cy="150" r="50"/><circle cx="105" cy="150" r="50"/><circle cx="180" cy="150" r="50"/><circle cx="255" cy="150" r="50"/><circle cx="330" cy="150" r="50"/>
  </g>
  <path d="M30 150 Q30 400 138 425" fill="none" stroke="#2f6b3a" stroke-width="3"/>
  <path d="M330 150 Q330 400 222 425" fill="none" stroke="#2f6b3a" stroke-width="3"/>
  <circle cx="180" cy="425" r="48" fill="none" stroke="#6a625a" stroke-width="2" stroke-dasharray="6 5"/>
  <line x1="270" y1="52" x2="190" y2="400" stroke="#151515" stroke-width="2.5" stroke-dasharray="8 6"/>
  <g transform="translate(262 84)" stroke="#151515" stroke-width="3">
    <line x1="-10" y1="-10" x2="10" y2="10"/><line x1="10" y1="-10" x2="-10" y2="10"/>
    <g fill="#fff" stroke-width="2"><circle cx="-10" cy="-10" r="4.5"/><circle cx="10" cy="-10" r="4.5"/><circle cx="-10" cy="10" r="4.5"/><circle cx="10" cy="10" r="4.5"/></g>
  </g>
  <g fill="#d2451e"><circle cx="30" cy="150" r="7"/><circle cx="105" cy="150" r="7"/><circle cx="180" cy="150" r="7"/><circle cx="330" cy="150" r="7"/></g>
  <circle cx="249" cy="150" r="11" fill="#d2451e" stroke="#151515" stroke-width="3"/>
  <text x="240" y="90" class="vz-t" text-anchor="end" style="font-size:17px">FPV crosses the row</text>
  <text x="56" y="228" class="vz-t-small" style="font-size:16px">darts ~960 ft apart</text>
  <line x1="98" y1="250" x2="98" y2="392" stroke="#151515" stroke-width="2"/>
  <path d="M91 258 L98 246 L105 258 M91 384 L98 396 L105 384" fill="none" stroke="#151515" stroke-width="2"/>
  <text x="110" y="306" class="vz-t-big" style="font-size:28px">~1 mi</text>
  <text x="110" y="336" class="vz-t-accent" style="font-size:19px">≈ 1 min</text>
  <text x="110" y="358" class="vz-t-accent" style="font-size:19px">warning</text>
  <rect x="138" y="408" width="84" height="34" fill="#151515"/>
  <text x="180" y="431" class="vz-t-unit" text-anchor="middle" style="font-size:16px">UNIT</text>
  <text x="350" y="478" class="vz-t-green" text-anchor="end" style="font-size:16px">fiber home</text>
  <text x="180" y="518" class="vz-t-small" text-anchor="middle" style="font-size:16px">a ring at the unit: only ~10 s</text>
</svg>
<figcaption>Seen from above, not to scale. Each dashed circle is one dart's hearing. The alert hops dart to dart and comes home by fiber.</figcaption>
</figure>

<div class="vz-steps">
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><g fill="none" stroke="#151515" stroke-width="3"><line x1="10" y1="10" x2="22" y2="18"/><line x1="38" y1="10" x2="26" y2="18"/><circle cx="8" cy="8" r="4"/><circle cx="40" cy="8" r="4"/></g><line x1="24" y1="22" x2="24" y2="44" stroke="#d2451e" stroke-width="4"/><path d="M18 38 L24 46 L30 38" fill="none" stroke="#d2451e" stroke-width="3"/></svg>
    <p class="vz-step-num">1 · Lay</p>
    <p>A drone with no pilot drops 4 darts a flight in a row about 1 mi out (<a href="{{ site.baseurl }}{% link models/line-layout.md %}">how</a>).</p>
  </div>
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="14" cy="24" r="5" fill="#d2451e"/><g fill="none" stroke="#151515" stroke-width="3"><path d="M24 14 Q30 24 24 34"/><path d="M31 8 Q41 24 31 40"/></g></svg>
    <p class="vz-step-num">2 · Listen</p>
    <p>Each dart sleeps until it hears something drone-like. It sends nothing while it waits.</p>
  </div>
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><g fill="#d2451e"><circle cx="6" cy="30" r="4"/><circle cx="24" cy="30" r="4"/><circle cx="42" cy="30" r="4"/></g><g fill="none" stroke="#151515" stroke-width="3"><path d="M8 24 Q15 12 22 24"/><path d="M26 24 Q33 12 40 24"/></g><line x1="42" y1="34" x2="42" y2="46" stroke="#2f6b3a" stroke-width="3"/></svg>
    <p class="vz-step-num">3 · Report</p>
    <p>A few-byte alert hops dart to dart, then home down a fiber the drone laid.</p>
  </div>
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6 L44 42 H4 Z" fill="#d2451e"/><rect x="22" y="18" width="4" height="13" fill="#fff"/><rect x="22" y="34" width="4" height="4" fill="#fff"/></svg>
    <p class="vz-step-num">4 · Warn</p>
    <p>The unit knows a drone crossed, and where, about a minute before it arrives.</p>
  </div>
</div>

**The same darts can guard a supply road,** where about half of casualties happen:

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Posts</p><p>along the verge, about 5 a mile, hear drones that land to wait in ambush. Alone, about $940 a mile a year</p></div>
  <div class="vz-card"><p class="vz-card-num">A fence</p><p>of darts a mile out, home on fiber, gives every drone flying in at least 60 s in the model</p></div>
  <div class="vz-card"><p class="vz-card-num">With the troops</p><p>receivers in vehicles, lamps on posts, and partners' phone systems (<a href="{{ site.baseurl }}{% link models/route-guard.md %}">Guarding a road</a>)</p></div>
</div>

<details class="layer" markdown="block">
<summary><span class="layer-title">The idea in full</span><span class="layer-sub">The four steps with their numbers and links, and the road guard</span></summary>

1. **Lay a line.** A small drone with no pilot drops 4 throwaway listeners per flight in a row across the enemy's approach, about 1 mi out, and two FPV fibers from the row back to the unit ([How it works]({{ site.baseurl }}{% link models/line-layout.md %})): about 22 darts a lay.
2. **Listen quietly.** Each listener sleeps until it hears something drone-like, and transmits nothing while it waits.
3. **Report back.** A few-byte alert hops listener to listener to one of two tip darts, which flash it home down the fiber to a base box behind the unit, and a wire takes it to each position. Nothing at the unit transmits or receives by radio, so the unit's own jammers can't deafen it ([jamming]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)).
4. **Warn.** Warning time is distance ÷ drone speed. A row about 1 mi out gives about 45–60 seconds against an FPV at top speed, and 1.3–1.8 minutes at the 37–50 mph it usually flies with a warhead ([the drones]({{ site.baseurl }}{% link research/threat-profile.md %})); a ring of microphones 980 ft out gives 8–10 (both estimates).

The idea is to buy warning with distance rather than with sensitivity. A better microphone gains tens of yards; laying the line forward gains miles.

**The same darts can guard a supply road,** where about half of casualties happen ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})):

- **Posts along the verge,** about 5 a mile, hear drones that land to wait in ambush, which nothing else on sale does. On their own they cost about $940 a mile a year.
- **A fence of darts a mile out,** home on fiber like a position's line, gives every drone flying in at least 60 s in the model.
- **The alert travels with the troops:** receivers in their vehicles, lamps on the posts, and, if a partner takes it, the phone systems they already carry ([Partners]({{ site.baseurl }}{% link research/partners.md %})).

</details>

<p class="kicker">02 · Why it matters</p>

## The threat nothing cheap detects.

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">~80%</p><p>of casualties at the front come from drones, by analysts' estimates (<a href="https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone">NPR</a>)</p></div>
  <div class="vz-card"><p class="vz-card-num">No radio</p><p>from a fiber-optic FPV, so radio detectors miss it and jammers can't stop it. A microphone hears it</p></div>
  <div class="vz-card"><p class="vz-card-num">Nothing forward</p><p>Cheap acoustic sensors sit at the unit and give seconds (<a href="{{ site.baseurl }}{% link research/competitors.md %}">competitors</a>)</p></div>
</div>

<div class="stats">
  <div class="stat"><p class="stat-num">1–4</p><p class="stat-label">of every 100 drone casualties averted by a position's line, our central guess</p></div>
  <div class="stat"><p class="stat-num">5–8</p><p class="stat-label">with the supply road guarded too, on guarded roads</p></div>
  <div class="stat"><p class="stat-num">30–50%+</p><p class="stat-label">of FPVs are fiber-optic in some sectors</p></div>
  <div class="stat"><p class="stat-label" style="margin:0"><a href="{{ site.baseurl }}{% link research/problem-check.md %}" style="color:#fff">Is the problem worth solving? →</a></p></div>
</div>

<details class="layer" markdown="block">
<summary><span class="layer-title">Why it matters, in full</span><span class="layer-sub">Casualties, fiber-optic FPVs, what Sky Fortress does and doesn't show, and the lives estimate</span></summary>

- **Drones cause about 80% of casualties** at the front, by analysts' estimates ([NPR, Oct 2026](https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)). Units cope by not moving, and every trip out is exposure.
- **Fiber-optic FPVs emit no radio**, so the radio detectors units carry miss them and jamming does nothing. In some sectors they are 30–50% or more of FPVs. A microphone hears them ([what troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})).
- **Acoustic detection works at scale, against a different target.** Ukraine's Sky Fortress hears Shaheds and cruise missiles over the rear with thousands of cheap pole-mounted sensors. Loud, low-pitched engines carry for miles; small electric FPVs don't. Against FPVs at the front, no acoustic system has an independent test yet.
- **Our central guess is 1–4 of every 100 drone casualties averted** by a position's line, almost all among people about to move. **Guarding the supply road as well roughly doubles it, to about 5–8,** on the roads that are guarded, because the posts also catch drones waiting in ambush ([estimate]({{ site.baseurl }}{% link research/lives-model.md %}#adding-a-guard-on-the-supply-road)). Both are guesses, not measurements.

Full evidence: [Is the problem worth solving?]({{ site.baseurl }}{% link research/problem-check.md %})

</details>

<p class="kicker">03 · How to assess it</p>

## What decides whether the tripwire is worth building.

<div class="assess">
<a class="assess-card" href="{{ site.baseurl }}{% link build-3d.md %}">
<span class="assess-num">02</span>
<span class="assess-title">3D models and downloads</span>
<span class="assess-q">Can a printed dart and harness carry, release and stand a listener?</span>
<span class="assess-body">Rotate the dart, the harness and the loaded X500, and watch them come apart. STL and STEP files for every printed part.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link models/line-layout.md %}">
<span class="assess-num">03</span>
<span class="assess-title">How it works</span>
<span class="assess-q">How many darts give a unit a minute, and how do alerts get home?</span>
<span class="assess-body">About 22 darts a lay, a row a mile out, and two FPV fibers to a base box behind the unit, wired to each position.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link models/route-guard.md %}">
<span class="assess-num">04</span>
<span class="assess-title">Guarding a road</span>
<span class="assess-q">Can the same darts protect a supply road?</span>
<span class="assess-body">Posts on the verge hear drones waiting in ambush; a fence a mile out gives a minute. About $4.7–6.7k a mile a year in full with solar, $940 for posts alone.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link costs.md %}">
<span class="assess-num">05</span>
<span class="assess-title">Projected costs</span>
<span class="assess-q">What does it cost to buy, and to keep laid?</span>
<span class="assess-body">Parts per dart, a unit's package at about $2.0–3.1k, and re-lays at about $3–5k a year with solar: lines are ammunition.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link research/competitors.md %}">
<span class="assess-num">06</span>
<span class="assess-title">Competitors</span>
<span class="assess-q">Who else warns a position of FPVs, and at what cost?</span>
<span class="assess-body">Zvook NW0 at $834–950 a sensor, RADD, Komodo's drone-dropped sensor, DroneAlert. All claims, no independent FPV range.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link research/partners.md %}">
<span class="assess-num">07</span>
<span class="assess-title">Partners</span>
<span class="assess-q">How does an alert reach troops on the move?</span>
<span class="assess-body">Hrafit's Sova module first, which already alerts drivers' phones; a TAK output as the fallback and a way into Delta.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link weekend-test.md %}">
<span class="assess-num">08</span>
<span class="assess-title">Saturday test</span>
<span class="assess-q">How far does a mic near the ground hear a drone?</span>
<span class="assess-body">One day and an $80–90 kit, in ten numbered steps. A phone and a Bluetooth speaker do most of the distances.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link mvp.md %}">
<span class="assess-num">09</span>
<span class="assess-title">MVP path</span>
<span class="assess-q">Can a line of listeners report home without being found?</span>
<span class="assess-body">Five gated layers to a six-listener line, about $600–750 in total.</span>
</a>
<a class="assess-card" href="{{ site.baseurl }}{% link models/tripwire.md %}">
<span class="assess-num">+</span>
<span class="assess-title">The full design</span>
<span class="assess-q">How each piece works, what it costs, and what could kill it.</span>
<span class="assess-body">Warning time, the listener, the delivery drone, getting alerts home by fiber, field limits and risks.</span>
</a>
</div>

<p class="kicker">04 · Where it stands</p>

## Four links to prove, each test under $500.

<div class="vz-chain">
  <a class="vz-link" href="{{ site.baseurl }}{% link research/open-questions.md %}"><span class="vz-link-title">Hear an FPV</span><span class="vz-link-test">T11 · range of one mic</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back"><span class="vz-link-title">Hop along the row</span><span class="vz-link-test">T9 · T19 near jammers</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box"><span class="vz-link-title">Light home by fiber</span><span class="vz-link-test">T21 · a full spool</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link build-hardware.md %}"><span class="vz-link-title">Laid by a drone</span><span class="vz-link-test">T10 · T13 · T14</span><span class="vz-chip vz-chip-open">untested</span></a>
</div>

<details class="layer" markdown="block">
<summary><span class="layer-title">The five questions in full</span><span class="layer-sub">Why each decides the tripwire, its test and cost, and where it stands</span></summary>

| Question | Why it decides the tripwire | Test | Status |
|---|---|---|---|
| **Do the hops along the row hold?** | Fiber carries alerts the last mile home, so radio is left only between darts along the row, about 980 ft a hop. A tree belt or a ridge between two darts can break a hop | [T9]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back), ~$80 | Open ground probably works on published figures; across tree belts, unproven |
| **Does a tip dart get its light home?** | The fiber is the line's only way home. A small laser has to put enough light into 1.2 mi of FPV fiber on a dart's battery, and the fiber has to survive being laid | [T21]({{ site.baseurl }}{% link research/open-questions.md %}), < $300 (est.) | Not started. The fiber loses under 1 dB over 1.2 mi on paper; 1 in 20 assumed to break while laid |
| **How far does a mic at 1.6–3.3 ft hear an FPV?** | Range sets listener spacing, so the cost of a line. Under about 130 ft the idea stops making sense | [T11]({{ site.baseurl }}{% link mvp.md %}#layer-2-hear-a-drone-from-near-the-ground-t11), ~$50 | Only measured cheap-mic range is 160–200 ft, on a consumer drone |
| **Do the row's hops work near enemy jammers?** | With fiber home, the unit's own jammers can't deafen the line. What's left is enemy jammers near the row, a mile out. On our estimate a jammer blinds a dart only within a few hundred feet; in the worst case, about a mile | [T19]({{ site.baseurl }}{% link research/open-questions.md %}), ~$300, needs a licensed range or Ukraine | [Modelled]({{ site.baseurl }}{% link models/line-layout.md %}#jamming), not measured |
| **Does a dropped dart land upright and working?** | Drone laying is what puts the row a mile out | A weighted dummy dropped from the drone | Modelled, not printed or dropped |

</details>

Ratings are working judgements, not test results. [Build or scrap?]({{ site.baseurl }}{% link research/build-or-scrap.md %}) sets out what result would stop the project.

<p class="kicker">05 · The rest of the notebook</p>

## Other models, kept for reference.

This notebook started as a survey of eight ways to build a cheap acoustic sensor network: fixed mic-array meshes, phone networks, elevated nodes, aerostats and more. The tripwire came out of that survey as the use case worth testing first. The survey is still here: [the wider field]({{ site.baseurl }}{% link research/landscape.md %}) and [all sensor models]({{ site.baseurl }}{% link models/index.md %}).

## How to add to this

Each page is a Markdown file in the [repository](https://github.com/paulrenzi/tripwire). Record rating changes and new research in the [changelog]({{ site.baseurl }}{% link changelog.md %}).
