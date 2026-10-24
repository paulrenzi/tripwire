---
title: "The full design"
nav_tripwire: 1
---

# The tripwire: full design
{: .no_toc }

<p class="vz-lede">Don't make a microphone hear farther. <strong>Drop cheap ones a mile forward</strong>, and a unit gets about a minute of warning instead of ten seconds, even against fiber-optic FPVs that emit no radio.</p>

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

<div class="stats">
  <div class="stat"><p class="stat-num">~1 min</p><p class="stat-label">warning from a row about 1 mi out (est.)</p></div>
  <div class="stat"><p class="stat-num">$21–59</p><p class="stat-label">per throwaway listener (est.)</p></div>
  <div class="stat"><p class="stat-num">22</p><p class="stat-label">darts to lay one unit's net, 4 of them tips with fiber (lay model)</p></div>
  <div class="stat"><p class="stat-num">4/5</p><p class="stat-label">feasibility: every part exists, fiber took out the long radio link; field tests still to run</p></div>
</div>

## Warning time

<div class="vz-bars" role="img" aria-label="Seconds of warning against an FPV: about 3 to 4 at the position, 8 to 10 from a ring 980 feet out, 45 to 108 from a row about a mile out">
  <div class="vz-bar-row"><span class="vz-bar-label">A detector at the position <em>(DroneAlert, VolAnti)</em></span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:3.6%"></span></span><span class="vz-bar-val">3–4 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">A ring of mics 980 ft out</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:9%"></span></span><span class="vz-bar-val">8–10 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>Our row, about 1 mi out</strong></span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:54.5%"></span><span class="vz-bar vz-bar-us-light" style="width:43.6%"></span></span><span class="vz-bar-val"><strong>45–108 s</strong></span></div>
  <p class="vz-bar-note">Warning = distance ÷ drone speed. Dark: an FPV at top speed. Light: at its usual 37–50 mph. All estimates; nobody has yet measured how far a cheap mic hears an FPV.</p>
</div>

Ten seconds is enough to raise a shotgun. A minute is enough to stop people walking into the open.

## Lay, listen, report, warn

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

## Where it stands

Every part exists. Nobody has shown the whole chain working. Each link has a cheap test:

<div class="vz-chain">
  <a class="vz-link" href="{{ site.baseurl }}{% link research/open-questions.md %}"><span class="vz-link-title">Hear an FPV</span><span class="vz-link-test">T11 · range of one mic</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back"><span class="vz-link-title">Hop along the row</span><span class="vz-link-test">T9 · T19 near jammers</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box"><span class="vz-link-title">Light home by fiber</span><span class="vz-link-test">T21 · a full spool</span><span class="vz-chip vz-chip-open">untested</span></a>
  <a class="vz-link" href="{{ site.baseurl }}{% link build-hardware.md %}"><span class="vz-link-title">Laid by a drone</span><span class="vz-link-test">T10 · T13 · T14</span><span class="vz-chip vz-chip-open">untested</span></a>
</div>

<p class="vz-done"><span class="vz-chip vz-chip-done">designed</span> a printable dart, a release harness and a printed carrier (<a href="{{ site.baseurl }}{% link build-hardware.md %}">hardware</a>) · the software, part by part (<a href="{{ site.baseurl }}{% link build-software.md %}">software</a>) · each test under $500 (<a href="#open-questions">tests</a>)</p>

## Why it matters

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">~80%</p><p>of casualties at the front come from drones, by analysts' estimates (<a href="https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone">NPR</a>)</p></div>
  <div class="vz-card"><p class="vz-card-num">No radio</p><p>from a fiber-optic FPV, so radio detectors miss it and jammers can't stop it. A microphone hears it</p></div>
  <div class="vz-card"><p class="vz-card-num">Nothing forward</p><p>Cheap acoustic sensors sit at the unit and give seconds (<a href="{{ site.baseurl }}{% link research/competitors.md %}">competitors</a>)</p></div>
</div>

The evidence, the open risks and the front-line fixes are in [the short version, in full](#the-short-version-in-full) below.

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The short version, in full</span><span class="layer-sub">Ratings, the four steps with numbers, the evidence it matters, where it stands, and front-line problems in plain terms</span></summary>

### Ratings

| Feasibility | Payoff | Technical readiness | Cost per sq mi | Persistence | Deployability |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **4/5** | **5/5** | 3/5 | 4/5 | 4/5 | 4/5 |

### The idea in four steps

1. **Lay a line.** A small drone with no pilot drops 4 throwaway listeners per flight in a row across the enemy's approach, about 1 mi out, with two FPV fibers from the row back to the unit ([How it works]({{ site.baseurl }}{% link models/line-layout.md %})).
2. **Listen quietly.** Each listener sleeps until it hears something drone-like, and transmits nothing while it waits.
3. **Report back.** A few-byte alert hops listener to listener to one of two tip darts, which send it home down a fiber the drone laid.
4. **Warn.** Warning time is distance ÷ drone speed, so a row about 1 mi out gives about 45–60 seconds against an FPV at top speed, and 1.3–1.8 minutes at its usual 37–50 mph. A ring of microphones 980 ft out gives 8–10 (both estimates).

### Why it matters: the evidence

- **Drones cause about 80% of casualties** at the front, by analysts' estimates ([NPR, Oct 2026](https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)).
- **Units cope by not moving:** underground, under nets, taking hours to cover half a mile. Every trip out is exposure (same source).
- **Fiber-optic FPVs, the fastest-growing threat, emit no radio**, so the detectors units carry miss them, and jamming does nothing to them. A microphone hears them ([what troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})).
- **Nothing cheap fills the gap yet.** Camera systems like WISP aren't at the front and can't see through tree lines; Zvook's acoustic FPV sensor, the NW0, sits at the unit, not forward: it needs 15–18 W of power and a link. It's on sale at about $834–950 per sensor, but its range and fiber-optic claims are the maker's only ([details]({{ site.baseurl }}{% link research/competitors.md %}#zvook-nw0--direct-competitor-claims-only)). Denmark's Komodo already sells a sensor variant that drones can drop, built for Shaheds rather than FPV lines ([details]({{ site.baseurl }}{% link research/competitors.md %}#komodo--the-drone-dropped-sensor-already-exists)).

Full evidence: [Is the problem worth solving?]({{ site.baseurl }}{% link research/problem-check.md %})

### Where it stands, in detail

- **Rated 3 out of 5.** Every part exists, but nobody has shown the whole chain working: a dart that hears an FPV, hops along the row, and light home down a fiber.
- **The deciding tests are the hops along the row (T9), light down the fiber (T21) and radio near jammers (T19).** Fiber carries alerts the last mile, so the old question, whether radio could get out of the trees to the unit, is gone. Radio is left only dart to dart along the row, about 980 ft a hop. Published measurements say open ground probably works; a tree belt between two darts can still break a hop. [Evidence and test plan]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back).
- **Jamming covers our band, but distance decides it.** On our estimate a trench jammer blinds a dart only within about 390 ft; in the worst case, about a mile. The unit's own jammers were the first threat to a receiver at the position, so alerts now come home by fiber and reach the positions by wire ([jamming]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)).
- **The last mile is fiber.** Two tip darts in the row send alerts down FPV fiber the drone pays out as it lays them, to a base box behind the unit, so nothing at the position emits or receives by radio ([design]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)). Untested ([T21](#open-questions)). Where fiber can't go, the fallback is a listen-only receiver at the edge of the unit's tree line ([fallback](#getting-alerts-out-of-the-trees)).
- **The payoff is a guess, not a doubt.** Fiber-optic FPVs get no warning today. Our central guess is about 1–4 of every 100 drone casualties averted, almost all among people about to move ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})). Front-line interviews would narrow it ([T18]({{ site.baseurl }}{% link research/problem-check.md %}#the-next-step-ask-before-building-t18)); they are not a gate.
- **Next steps cost little.** The first five tests each cost under $500; see [Parts and first build](#components-and-mvp).
- **Designs exist now:** a printable dart, an X500 release harness and a printed carrier ([Build: hardware]({{ site.baseurl }}{% link build-hardware.md %})), and the software laid out component by component ([Build: software]({{ site.baseurl }}{% link build-software.md %})).

### Front-line problems, in plain terms

From [what the front actually looks like]({{ site.baseurl }}{% link research/field-conditions.md %}). Each fix adds no cost, and each also gathers information the unit can use. These are proposals, not tested yet.

| Problem | What it means day to day | Our fix | What the line learns |
|---|---|---|---|
| **GPS is jammed** | The drone may not put listeners where planned | Fly on compass, optical flow and lidar from an origin set at launch, in daylight, and confirm every dart by radio as it lands ([how]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net)). Listeners carry no GPS, which saves money. Troops walking in can also place them by hand | Where GPS fails along the unit's routes |
| **Friendly drones everywhere** | A line that alarms on every drone gets switched off | Alarm only for drones heading **in**, outside the unit's own flight times | Enemy drone habits: when, where and how fast |
| **Tree lines** | Lines follow the tree belts, where radio range is short | Drop listeners at belt edges, not inside, and plan each hop along open ground so no belt sits between neighbours. Alerts come home by fiber, so the unit's own tree line no longer blocks them. Space them closer, paid for by dropping GPS | When leaf fall changes radio range |
| **Jammers on both sides cover 868–915 MHz** | Radios beside a working jammer can't receive | Keep every radio that must receive a few hundred feet from jammers; wire or fiber where it can't be ([how]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)) | Where the radio fails, from the daily roll call |
| **Cold** | Batteries die sooner in winter | Listeners report battery and temperature; re-lay a line when it runs low | Real winter battery life |

</details>


<details class="layer" id="how-it-works" markdown="block">
<summary><span class="layer-title">How it works</span><span class="layer-sub">Warning time, why lines beat coverage, the listeners, the drone, getting alerts home</span></summary>

### Warning time comes from distance

A microphone hears a small FPV at roughly **330–980 ft** ([working estimate]({{ site.baseurl }}{% link research/range-and-cost.md %})). Better hardware barely moves that, so move the listeners forward instead.

{: .warning }
> **The only measured range for cheap microphones is lower: about 160–200 ft** against a consumer drone in a windy field ([what's measured]({{ site.baseurl }}{% link research/competitors.md %}#what-is-actually-measured)). FPVs are probably louder, but no study has flown one at distance. If 160–200 ft holds, listeners sit about 330 ft apart and a 1.9 mi line needs about 30, not 12. T11 decides it.

| Where the listeners sit | Warning against an FPV at top speed, 67–89 mph | At its usual speed with a warhead, 37–50 mph |
|---|---|---|
| Ring placed by hand, ~980 ft out | ~8–10 seconds | ~13–18 seconds |
| Row laid by drone, about 1 mi out ([the modelled net]({{ site.baseurl }}{% link models/line-layout.md %})) | ~45–60 seconds | ~1.3–1.8 minutes |
| A deeper row, 2.5 mi out | ~1.5–2 minutes | ~3–4 minutes |

{: .warning }
> FPV speeds and detection ranges are planning estimates, not field measurements ([how fast and how high the drones fly]({{ site.baseurl }}{% link research/threat-profile.md %})). The ratio is what matters: ten times the distance is roughly ten times the warning.

Ten seconds is enough to get a shotgun or net-gun up; weapons have only about 1–4 seconds of the drone's flight in range, so a minute adds little for them. What a minute adds is a go/no-go call on exposure: get people under cover, don't start a vehicle run, hold a resupply pickup. Only a line forward gives that against fiber-optic FPVs. Interceptor drones are built mostly for other targets so far. [A minute against the alternatives]({{ site.baseurl }}{% link research/problem-check.md %}#a-minute-against-the-alternatives).

### Lines, not coverage

Covering a whole area against small drones would take thousands of nodes ([the density problem]({{ site.baseurl }}{% link research/range-and-cost.md %}#worked-examples)). Attacking drones mostly come from one side, so a tripwire only covers the approaches.

- **One row**, about a mile out, says *something crossed here, at this time*. That is the [modelled net]({{ site.baseurl }}{% link models/line-layout.md %}).
- **Where it crossed, for free:** the alert names the dart that heard it, and comparing loudness with its neighbours places the crossing between two darts: about ±5° as seen from the unit (estimate).
- **Which way it's heading, for free in firmware:** each dart notes the moment the drone passed closest, from the loudness peak and the drop in pitch as it goes by. A drone flying straight in passes neighbouring darts at the same moment; one at an angle passes them seconds apart, so 1 s of timing error is about ±5° of heading (estimate). It costs a few bytes an alert and clocks that agree to about 0.1 s, not 1–2 s. Untested on an FPV, whose changing throttle blurs the pitch; T11 measures it.
- **A second row** a few hundred yards behind adds in-or-out, speed and heading when only one dart heard it, for about a dozen more darts. It is an option, not in the model, and worth it only if T11 shows the timing method doesn't hold up.
- A listener only has to hear the drone, not locate it, so listeners sit about one detection range apart: every 660–980 ft against FPVs, or closer under trees. A 1.9 mi front takes about 12 per line ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}) works out a net for one unit: 15 listening darts a mile out with two fibers home, 16 on real ground and about 22 used in laying them; [Projected costs]({{ site.baseurl }}{% link costs.md %}) prices it).
- Pinpointing the drone is left to the dense ring near the unit ([M1]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}) on [M4]({{ site.baseurl }}{% link models/m04-elevated-nodes.md %}) placements).

### Throwaway listeners

Single-microphone nodes ([M3]({{ site.baseurl }}{% link models/m03-single-mic-tdoa.md %}) class) built to be dropped, not placed:

- A **dart** that sticks upright in soil and holds the microphone about 20 in up on a rigid fiberglass rod ([v3 design]({{ site.baseurl }}{% link build-hardware.md %}#1-v3-three-parts-per-dart)). A microphone lying in grass hears much worse.
- **Wake on sound:** the processor and radio wake only when something drone-like is heard. Target: **weeks on a small battery**.
- **No recovery.** Lost or dead listeners are replaced by the next flight, like ammunition.

Open-source starting points exist: [Batear]({{ site.baseurl }}{% link research/open-source-builds.md %}#batear) (MIT licence) already runs a single-mic detector with encrypted LoRa alerts on an ESP32-S3, and [VolAnti]({{ site.baseurl }}{% link research/open-source-builds.md %}#volanti) has published a 340 ft range test.

### The delivery drone

- **Flies itself.** A pre-planned mission on open-source autopilot software (ArduPilot), with a drop at each point and every radio link off, so nothing broadcasts while the line is laid. Six flights lay two lines across a 1.9 mi front.
- **Reusable**, but cheap enough to lose. At the end of its life it can be left on high ground as a relay.
- Airframes, software and GPS jamming: [Delivery drone]({{ site.baseurl }}{% link research/delivery-drone.md %}).

### Getting alerts home

A listener sends a few bytes only when it hears something: time, its ID, what it heard, how sure it is, a short description of the sound and its battery level. Alerts hop along the row to a tip dart and home by fiber to a base box behind the unit, and a wire takes them to each position ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)). The base box feeds the shared map, TAK and [Lattice]({{ site.baseurl }}{% link research/integration.md %}#anduril-lattice). Where fiber can't go, a raised receiver at the unit is the [fallback](#getting-alerts-out-of-the-trees).

As more units lay lines that report to the same map, they add up to a wider network that nobody had to plan or fund centrally.

</details>

<details class="layer" id="getting-alerts-out-of-the-trees" markdown="block">
<summary><span class="layer-title">The fallback: an edge receiver where fiber can't go</span><span class="layer-sub">Before fiber, this was how alerts got out of the trees. Kept for where a tip dart can't be laid</span></summary>

**Alerts now come home by fiber** ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)), so the question this section used to answer, whether radio can get from the row through the unit's tree line, no longer decides the tripwire. Radio is left only between darts along the row, about 980 ft a hop (T9).

Where a fiber can't be laid, or keeps being cut, the old design still works:

- **A listen-only receiver at the edge of the unit's own tree line,** raised 16–33 ft on a pole or hoisted into the canopy, with a small Yagi aimed at the line for about 6–9 dB (est.). Two or three on one wire get round fading and a single blocked path.
- **It never transmits.** RS-485 over twisted pair, rated to about 0.7 mi ([TI](https://www.ti.com/document-viewer/SN65HVD72/datasheet/typical-application-sllse118349)), carries alerts, and power on a second pair, to the dugout.
- **Its weakness is why fiber replaced it:** it must sit at least about 1,000 ft from the unit's own jammers. On our estimate a 20 W trench jammer deafens a raised receiver within about 1,030 ft ([jamming]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)).
- **Range on paper:** a listener at 3.3 ft reaching a receiver at 33 ft, 1.9 mi away over open ground, leaves about 40 dB of an SX1262's roughly 159 dB. That is room for about four windbreak belts at 4–5 dB each ([Weissberger's model](https://en.wikipedia.org/wiki/Weissberger%27s_model), estimates). 660 ft of forest costs about 29 dB at 915 MHz, so deep forest doesn't fit.
- **Cost:** about $100–250 for a receiver, its Yagi and its wire (est.).
- **Tests:** T17, and T9 run E across windbreaks. Build steps are [MVP layer 3]({{ site.baseurl }}{% link mvp.md %}#layer-3-the-edge-receiver-t17).

</details>

<details class="layer" id="solving-the-field-limits-at-no-extra-cost" markdown="block">
<summary><span class="layer-title">Front-line problems: the full fixes</span><span class="layer-sub">GPS jamming, friendly drones, tree lines and cold, solved at no extra cost while gathering information</span></summary>

{: .warning }
> A design proposal, not a tested system. The tests that would check it are at the end of this section.

### The fixes

| Problem | Fix | What the line learns | Extra cost |
|---|---|---|---|
| **GPS is jammed** ([source]({{ site.baseurl }}{% link research/field-conditions.md %}#electronic-warfare)) | No GPS on the listener. Its position is the planned drop point, corrected by where the drone's flight log says it released. Its clock is set when it is loaded and kept in step with neighbours whenever they relay. Its own GPS would be jammed in the same places as the drone's anyway. The drone flies on compass, optical flow and lidar from an origin set at launch, and confirms each dart by radio as it lands, so drops a few hundred feet off still make a net (T14, [how]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net)). Troops walking in at night can also place listeners by hand (an inference) | ArduPilot's flight log records GPS fix quality on every flight, so each sortie maps where GPS failed or jumped along the unit's routes | **Saves $8–15 per listener** |
| **Friendly drones** ([source]({{ site.baseurl }}{% link research/field-conditions.md %}#what-infantry-use-to-hear-drones-today)) | A drone heading in trips the outer line first; one heading out trips the inner line first. The unit enters its own flight times on the receiving tablet. An inbound drone outside those times is an alarm; everything else is logged quietly | Each alert carries a few bytes describing the sound (main tone, loudness, duration). Alerts during friendly flights label themselves, so the line builds training examples for the next batch's classifier | None: a few more bytes per alert |
| **Tree lines** ([source]({{ site.baseurl }}{% link research/field-conditions.md %}#where-infantry-actually-sit-tree-lines)) | Lay lines across the tree belts and the gaps between them, spaced closer under canopy. The money that bought 12 listeners with GPS buys about 15–17 without. Plan each hop along open ground so no belt sits between neighbours; alerts come home by fiber ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)) | Every received packet comes with its signal strength. Logged per link, it shows when leaf fall or growth changes range and which links are about to fail | None |
| **Cold** ([source]({{ site.baseurl }}{% link research/field-conditions.md %}#seasons)) | No pricier cold-rated cells up front. Listeners add battery voltage and chip temperature to packets they already send, plus a rare stand-alone check-in | Measured winter battery life, which no source we found has published, and a forecast of when each line needs re-laying | None on boards that already read their battery, such as the Heltec V3 (Meshtastic reports its level); two resistors, a few cents, on a custom board. The ESP32-S3 has a [built-in temperature sensor](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/temp_sensor.html), which reads close to air temperature only while the listener sleeps |

### What the unit gets

Over weeks, a line becomes a record of drone traffic on the unit's approach:

- **Enemy drone habits:** time of day, which tree lines and gaps they use, and speed from the time between the two lines. That says when to stay under cover and where to point a camera or interceptor. On the shared map, many units' lines show the pattern across a sector.
- **Friendly traffic:** a count of the unit's own flights, useful for checking against neighbouring units' drones.
- **A jamming map**, updated every sortie.
- **A radio and season map**, showing where lines need closer spacing and when.
- **Winter battery data**, measured where it matters.
- **Lost listeners as a signal (an inference):** one that goes quiet while its battery was healthy was probably destroyed or found. Where and when that happens is itself a sign of activity.

### Rules that keep it cheap and quiet

- **No new transmissions to gather data.** Summaries ride on alerts and relays already being sent. A stand-alone check-in goes out at most once or twice a day, and the unit can switch it off. Keep the extra summary to roughly 10–15 bytes (an estimate), since every byte adds air time.
- **No audio leaves a listener.** LoRa is far too slow. Training recordings come from the [weekend test kit]({{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector) and test ranges.
- **Classifier updates ship in the next batch of listeners**, not over the air.
- **The record lives at the unit's receiver and on the shared map**, not in the listeners.

### What has to be proven

- **Clocks without GPS.** Telling direction from which line trips first needs neighbouring clocks to agree within about 1–2 seconds for weeks. A drone at 67–89 mph crosses lines a few hundred yards apart roughly 5–15 seconds apart, and ordinary microcontroller clocks drift a few seconds a day (both estimates). Neighbour syncing has to keep up (T15).
- **Heading from timing** needs two darts to hear the drone. Head-on that happens on only about a third of crossings, at 30° off about half, at 60° nearly all (estimates from 960 ft spacing and 635 ft hearing). The one-dart cases are the drones flying straight at the unit.
- **Direction alone doesn't sort friend from foe.** Friendly drones fly home inbound, and enemy scouts leave outbound. Until T15 shows whether sound can tell them apart, the unit's flight times do most of the work.
- **Positions from the drop plan** are only as good as the drone's navigation (T14).
- **Battery life in cold**, with the extra bytes counted (T12).

### Considered: anchoring to a central node

A reader suggested one central node with a known position, and listeners that measure their distance to it, instead of GPS on every node.

- **The tripwire already works this way.** Listeners carry no GPS; the delivery drone's release point is the reference. The anchor wouldn't need GPS either, since it would be jammed at the unit too: make it a point fixed from a map or a one-off survey.
- **A central time beacon** is simpler than neighbours syncing with each other, and is now one of the options in T15. The catch is that a regular transmission marks the unit (T8), so it would have to be rare or sent from somewhere else.
- **Dead reckoning** is for things that move. A dropped listener doesn't; the drone already dead-reckons (T14).
- **Radio ranging doesn't pay here.** With listeners 330–980 ft apart, 66–160 ft of position error doesn't change "a drone crossed near listener 7". The current radio (SX1262) can't measure distance; the SX1280 can, but on 2.4 GHz, which reaches less far. A published outdoor test reached 0.9 mi over open farmland with an average error of 150 ft, worst where a forest shadowed the link ([Müller et al., 2021](https://digitalcollection.zhaw.ch/bitstream/11475/22769/3/2021_Mueller-etal_Outdoor-ranging-and-positioning-based-on-LoRa-modulation.pdf)). A listener 1.2–2.5 mi out under trees would probably not reach an anchor at all, and every ranging exchange is another emission.
- **Where it could pay:** [M1]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}) and [M3]({{ site.baseurl }}{% link models/m03-single-mic-tdoa.md %}), which locate a drone from several nodes and need positions and clocks to a few yards and milliseconds. That is [T16]({{ site.baseurl }}{% link research/open-questions.md %}#t16-positions-and-clocks-without-gps).

</details>

<details class="layer" id="components-and-mvp" markdown="block">
<summary><span class="layer-title">Parts and first build</span><span class="layer-sub">What goes in one listener, five cheap build steps, and photos of the starter parts</span></summary>

### What goes in one listener

| Part | Example | Est. cost | Why it's there |
|---|---|---|---|
| Microcontroller | ESP32-S3 | $4–10 | Runs the drone / no-drone classifier on the device, so only a few bytes are sent |
| Microphones | 4 analog MEMS mics on the fin tips, about 4 in apart, an ES7210 4-channel audio chip and a compass chip | $3–8 | Each dart takes its own bearing, which fixes the head-on, one-dart case. One mic listens; the other three wake on a detection. Timing across neighbouring darts still works without it ([costs]({{ site.baseurl }}{% link costs.md %}#per-component)) |
| LoRa radio | SX1262, 915 MHz in the US | $6–25 | Sends alerts and relays neighbours' alerts toward the unit |
| GPS | none | $0 (was $8–15) | Dropped: it would be jammed where it matters most ([why](#solving-the-field-limits-at-no-extra-cost)) |
| Battery | small LiPo cell | ~$3–8 (estimate) | Weeks, not days, only if the listener sleeps until it hears something |
| Solar | a 2.4 × 2.4 in panel lying flat on the pod, and a charger chip that stops charging below 32°F | ~$2–4 (estimate) | Covers a dart's daily use from March to October, so cells run flat only in midwinter ([running cost](#the-running-cost-lines-are-ammunition)) |
| One printed body and a head pod on a fiberglass rod | 3D-printed, plus a ~$1.10 rod | $1–2 in filament | Sticks upright and holds the mic about 20 in up |
| Windscreen | fur or foam cover | ~$1–3 (estimate) | Wind is the biggest range-killer in [VolAnti's tests]({{ site.baseurl }}{% link research/open-source-builds.md %}#volanti) |
| **Total** | | **~$21–59** | Against a **$30–60 target** (~$25–65 with GPS) |

{: .warning }
> Part prices come from [Hardware]({{ site.baseurl }}{% link research/hardware.md %}); the battery and windscreen figures are estimates. All are hobby-grade, small-volume prices. A board that already combines the ESP32-S3 and LoRa radio, such as the Heltec WiFi LoRa 32 V3, costs about $25–30 and is the easiest way to build the first ones. A unit's package, 22 darts, 4 tip darts with their fiber, a base box and an outfitted delivery drone, costs us about **$2,900** in a small batch ([Projected costs]({{ site.baseurl }}{% link costs.md %})).

### The running cost: lines are ammunition

The package price is only the start. Listeners aren't recovered, so every net is re-laid when its batteries run out. A small solar panel on every dart keeps that to midwinter. All figures below are estimates from [Projected costs]({{ site.baseurl }}{% link costs.md %}#keeping-it-up), built on an unmeasured battery life and winter solar harvest (T12):

- **One re-lay** of a unit's net: about 22 darts and 7 drone sorties at up to 4 darts each ([lay model]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net)), **≈ $810–1,590** at our cost with drone wear.
- **With solar:** a dart's panel covers its daily use from March to October, and about half to two-thirds of it from December to January, so the net goes flat only in midwinter: about 2–4 re-lays a year, **≈ $1.6–6.3k a year** per unit. A second cell in every dart might cut that to 0–1 re-lays (an option, [costs]({{ site.baseurl }}{% link costs.md %}#keeping-it-up)).
- **Without solar,** at four weeks per battery, it would be 13 re-lays and **≈ $10.6–20.6k a year**.
- **Plus** listeners lost to shelling, and the occasional delivery drone.

So the tripwire is a consumable, not a one-off purchase. It costs less than a radar but more than a radio detector bought once. What shrinks the bill now is a panel that collects more in winter, a cell that lasts longer in the cold, and fewer listeners lost. Test T12 decides which bill is real.

### Five build steps

Each step answers one question before money goes into the next. They match the [tests](#open-questions). The [MVP path]({{ site.baseurl }}{% link mvp.md %}) lays the same steps out as layers you can order parts for today, starting with an $80 radio test.

| Step | What you build | What it proves | Rough cost |
|---|---|---|---|
| **1. Weekend test kit** | 2 Heltec V3 boards running [Batear]({{ site.baseurl }}{% link research/open-source-builds.md %}#batear), 3 INMP441 mics, windscreens, phones as recorders | A cheap mic hears a drone at known distances; first labelled training audio; a first radio range figure | **~$80–90** with a borrowed drone, tripods and power banks; ~$360–480 buying everything |
| **2. Radio range test (T9)** | The same two boards, one carried away from a raised receiver | Whether a row a mile out can report back at all. **The deciding question** | < $300 |
| **3. Listener on a mast (T10, T11)** | One listener on a 1.6–3.3 ft spring mast, plus a drop-tested printed dart body | Detection range at listener height (sets spacing), and whether listeners land upright | < $500 |
| **4. Battery and solar test (T12)** | One listener with wake-on-sound, a small classifier and its solar panel | Whether "weeks on a small battery" is real, and how much a panel collects in winter | < $250 |
| **5. Drop flight (T13)** | A printed quad that lays 4 listeners on planned points | Placement accuracy and payload | < $500 |

### Parts for step 1

{: .warning }
> Prices are rough US figures checked in October 2026 and change often. Parts marked "ships from China" won't arrive in days. The "step 2" recorder board below is the kit's own later upgrade, not build step 2.

{% include kit-parts.html %}

Buying advice: [weekend test kit]({{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector). The steps: [the Saturday test]({{ site.baseurl }}{% link weekend-test.md %}).

</details>

<details class="layer" id="compared-with-the-alternatives" markdown="block">
<summary><span class="layer-title">Compared with the alternatives</span><span class="layer-sub">Radio detectors, cameras, radar, phone networks, and why not just drop phones</span></summary>

The claim is narrow: **for early warning of low drones approaching a unit, including drones that emit no radio.** It works best alongside the others: a radio detector still catches radio-controlled FPVs at long range, and the tripwire tells a camera where to look.

| | Fiber-optic FPV | Behind trees or a ridge | Warning time vs FPV | Emits while watching | Rough cost | A unit can carry it |
|---|:-:|:-:|---|:-:|---|:-:|
| **Drone-laid tripwire** | ✅ | ✅ | **~1–2 min** | ❌ | **~$2.0–3.1k package, then ≈ $3–5k a year in re-lays with solar** ([est.](#the-running-cost-lines-are-ammunition)) | ✅ |
| Hand-placed acoustic ring | ✅ | ✅ | ~10 s | ❌ | similar | ✅ |
| Radio detector (e.g. Chuyka) | ❌ | partly | long, if it emits | ❌ | ~$584–701 | ✅ |
| Camera (e.g. WISP) | ✅ if in sight | ❌ | depends on sight lines | ❌ | far higher | ❌ |
| Radar | ✅ if in sight | ❌ | long, if in sight | **✅** | $40k–160k | ❌ |
| Phone network (Sky Fortress) | ✅ | ✅ | ~10 s for FPVs near the unit | **✅** (cellular) | $400–1,000 per sensor | ❌ |

**The same assumptions on every row.** The warning times are our estimates from where each sensor sits, not measurements. Every acoustic row, ours included, assumes the sensor actually hears an FPV, which nobody has measured ([what's measured]({{ site.baseurl }}{% link research/competitors.md %}#what-is-actually-measured)). The tripwire's minute comes from distance, not from a better microphone; if T11 finds short range, it needs more listeners, not less warning.

**Trees hurt every option, in different ways.** A windbreak belt weakens a radio link by a few dB ([estimate](#getting-alerts-out-of-the-trees)), and sound gets through too, but a belt blocks a camera's or radar's view outright. A radio detector at the unit isn't stopped by trees, but can't hear fiber-optic FPVs. Phones need cell coverage. Any sensor pushed forward, of any kind, has to get its report home through the same trees: the tripwire's radio problem is shared, not unique to it.

### Why not just drop phones?

Phones are the [best-proven acoustic sensor there is]({{ site.baseurl }}{% link models/m02-phone-network.md %}) and still win for fixed networks with power and cell coverage, and as the display at the unit. For a line dropped 1.2–2.5 mi forward, purpose-built listeners win:

| | Purpose-built listener | Phone |
|---|---|---|
| **Emissions** | Silent until it hears something, then one short burst | Keeps checking in with the cell network, so it can be located; with radios off it can't report |
| **Network** | Its own mesh; no cell towers | Needs cell coverage, which near the front is jammed, destroyed or watched |
| **Battery** | Wake-on-sound: weeks (target) | Running a mic and classifier non-stop: about a day (estimate) |
| **Weight** | Target well under 3.5 oz, so a small drone carries 3–4 | ~4.5 oz with its rod (v3 estimate) |
| **Cost** | $17–50 (estimate) | ~$50–100 for the cheapest phone, plus mount and protection |
| **Survives a drop** | Designed for it | Isn't |
| **Brains** | Only needs "drone-like sound: yes or no" | Can run much bigger classifiers |

The phone's one real advantage is computing power. A listener only has to answer *was that a drone?*, a small-classifier job of the kind that already runs on microcontrollers. That still has to be proven on real recordings.

</details>

<details class="layer" id="questions-weve-weighed" markdown="block">
<summary><span class="layer-title">Questions we've weighed</span><span class="layer-sub">Hands or a drone, whether it's worth it, getting listeners back, a central anchor, predicting radio range</span></summary>

### Why not have people place the listeners?

**For the first builds, they should.** Placing listeners by hand tests what decides everything (radio range, detection range and battery: T9, T11, T12) without also depending on the drop and no-GPS flights (T13, T14). People also place them better: upright, hidden, and at belt edges where the radio carries.

The drone earns its place later. A row a mile out sits inside the drone kill zone, which units describe as 3.1–4.3 mi deep or more ([source]({{ site.baseurl }}{% link research/field-conditions.md %}#the-drone-kill-zone)). Every walk out risks people and takes hours, and lines need re-laying as listeners die. A drone sortie takes minutes and risks a drone. Placing by hand stays the right tool near the unit: the inner ring, the [edge receiver](#getting-alerts-out-of-the-trees), and nights when the drone can't fly.

### Is it worth it if it works exactly as specified?

For warning time, probably: about a minute instead of about ten seconds, including against fiber-optic FPVs that radio detectors miss. Even working perfectly, it has limits:

- It only catches drones that cross a line. Launches from inside it, or routes round its ends, are missed.
- It says *something crossed here*, not where it will strike.
- A minute is only worth what the unit can do with it. Against fiber-optic FPVs that is mostly avoidance (hold a movement, get under cover). Weapons need only seconds ([a minute against the alternatives]({{ site.baseurl }}{% link research/problem-check.md %}#a-minute-against-the-alternatives)).
- The enemy adapts, by flying round the ends or hunting listeners.

How many lives a minute saves is for front-line users to refine, not a test bench. [Is the problem worth solving?]({{ site.baseurl }}{% link research/problem-check.md %}) sets out the evidence and the questions (T18).

### Should listeners be retrievable, for example by a magnet on the drone?

**Not in the field (an inference).** A listener costs $17–50. Picking one up means the drone hovering low over each listener, inside the kill zone, exposed just as it was when it dropped it. Finding a listener would also need better than the 66–160 ft the drop plan gives, so it would need a homing signal: another emission. A magnetic pickup is buildable; it just doesn't pay.

**Yes on test ranges,** where boards are reused across dozens of trials. A buzzer or light that turns on when commanded, and a person walking out, is enough.

### A central anchor instead of GPS on every node?

A reader's suggestion; considered [here](#solving-the-field-limits-at-no-extra-cost). The tripwire already works that way. It matters more for M1 and M3 ([T16]({{ site.baseurl }}{% link research/open-questions.md %}#t16-positions-and-clocks-without-gps)).

### Can the radio question be answered before the field test?

Partly, by simulation calibrated to the published measurements. Nothing published settles it. [Method and nearest research]({{ site.baseurl }}{% link research/open-questions.md %}#predicting-it-before-the-field-test).

</details>

<details class="layer" id="limits-and-risks" markdown="block">
<summary><span class="layer-title">Other risks</span><span class="layer-sub">Radio range, tracing, noisy laying, gaps, false alarms, litter, export rules</span></summary>

- **The hops along the row.** Fiber carries alerts home, but darts still relay to a tip by radio. Published measurements with antennas near the ground show over 2.5 mi in open country, but only 160–820 ft in most forest tests. In woods a row would need hops of perhaps 330–660 ft, so more darts. The tip's laser and the fiber are untested too (T21). [Evidence and test plan]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back).
- **Jamming.** Jammers on both sides cover our band. On our estimate a jammer near the ground blinds a dart only within a few hundred feet, so jamming becomes a question of where darts and roots go; in the worst case it blinds darts out to about a mile, and a radio net can't work near the front. T19 decides which ([model]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)).
- **The relay chain can point home.** A chain of bursts leading back to the unit could be traced. Keep bursts short and rare, bend the chain instead of running it straight, and treat listeners as disposable.
- **Laying the line is noisy.** The drone can be heard and seen, so the enemy may learn roughly where the line is. Lay at night or under other noise when GPS works; with GPS jammed, the optical-flow navigation needs daylight. Expect losses.
- **Only drones that cross the line are caught.** A drone launched from inside the line, or routed around its ends, is missed. The inner ring is still needed.
- **False alarms with nobody to check.** Wind, vehicles and birds can trip a single listener. Requiring two neighbours, or a front dart then a trunk dart, to agree is the main filter.
- **Litter.** Throwaway listeners are electronic waste. Consider biodegradable printed bodies and batteries that can't leak.
- **Export controls.** A counter-drone sensor kit may fall under ITAR/EAR once built for military use.

GPS jamming, friendly drones, tree lines and cold are covered [above](#solving-the-field-limits-at-no-extra-cost).

</details>

<details class="layer" id="why-3d-print-the-drones-and-the-nodes" markdown="block">
<summary><span class="layer-title">Why 3D-print the drone and listeners</span><span class="layer-sub">It barely cheapens the drone, but it makes the system easier to field</span></summary>

| Part of a small delivery quad | Estimated cost |
|---|---|
| Motors (4) | $40–80 |
| Electronic speed controllers | $25–40 |
| Flight controller | $20–40 |
| GPS / compass | $10–20 |
| Control receiver | $10–20 |
| Battery | $20–40 |
| Frame: carbon fiber | $20–40 |
| Frame: 3D-printed | **$3–8** in filament |

{: .warning }
> Rough estimates for hobby-grade parts at small volume. Parts for military use may face supply-chain and country-of-origin rules.

Electronics are about 85–90% of the drone's cost, so a printed frame saves only about $15–35 per drone. Printing pays off elsewhere:

- **The listeners.** Each needs a dart body, mast mount and battery housing: a dollar or two printed, no tooling, and they are used by the hundred.
- **The drop mechanism.** Release clips and cargo racks are small custom parts, exactly what printers are good at.
- **Making and fixing kits near the front** from a file, without waiting on a supply chain. Ukraine already prints drone parts at scale.
- **Fast design changes.** When a dart breaks in drop tests, the fix ships as a new file that day.

A **printed fixed-wing** carrier is worth testing too: it flies much farther on the same battery and doesn't need to hover.

</details>

<details class="layer" id="open-questions" markdown="block">
<summary><span class="layer-title">Tests</span><span class="layer-sub">Ten cheap tests, from radio range and jamming to friendly drones and the fiber home</span></summary>

| Test | What it answers | Rough cost |
|---|---|---|
| **T9** Radio range at 1.2–1.9 mi, open ground and trees, raised receiver at the unit ([test plan]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back)) | Can a forward line report back at all? Probably yes in the open; trees unproven | < $300 |
| **T10** Drop-test printed dart bodies onto soil, sand, mud and grass | Do listeners land upright with the mic clear? | < $200 |
| **T11** FPV detection range for one mic on a 1.6–3.3 ft spring mast. Record raw audio on every mic and the test drone's GPS log | How far apart listeners can be, and whether the moment of closest pass is sharp enough to give heading | < $300 |
| **T12** Wake-on-sound battery life with a small classifier, including in cold, and a winter of solar harvest on a dart and a post | Is "weeks" real, how much shorter in winter, and how many winter re-lays does solar leave? | < $250 |
| **T13** Drop flight: 4 listeners on planned points from a printed quad | Placement accuracy and payload | < $500 |
| **T14** The same flight with GPS unavailable | Can a line be laid under jamming? | < $300 |
| **T15** Record friendly drones; test whether sound, which line trips first and flight times can sort friend from foe, with clocks kept in step without GPS | Will the line cry wolf? | < $200 |
| **T17** Build a [listen-only edge receiver](#getting-alerts-out-of-the-trees) raised at a tree-belt edge, wired 980–3,300 ft to the dugout | The fallback where fiber can't go: can a unit hear its lines from inside a tree line without transmitting from its position? | < $300 |
| **T19** The best T9 link beside a working ELRS jammer, then 300 ft to 1 mi from it | How far from a jammer does a link near the ground still work? | < $300 |
| **T21** A tip dart with a laser on a full 1.2 mi spool of FPV fiber, into a base box ([design]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)) | Does enough light get home, what does the heartbeat cost the battery, how much does a tip weigh, and how often does fiber break when a drone lays it? | < $300 |

All are tracked in [Open questions]({{ site.baseurl }}{% link research/open-questions.md %}).

</details>

<details class="layer" id="rating-history" markdown="block">
<summary><span class="layer-title">Background and rating history</span><span class="layer-sub">The Vietnam-era precedent, and why the rating is where it is</span></summary>

### Precedent

In the Vietnam War, **Operation Igloo White** air-dropped acoustic and seismic sensors (including the ACOUBUOY and SPIKEBUOY) along the Ho Chi Minh Trail and relayed their detections back by aircraft. What's new is that the sensor, the delivery drone and the classifier are now cheap enough to throw away.

### How the rating changed

| Date | Rating | Why |
|---|---|---|
| 2026-10-15 | 3 | Each part exists (cheap nodes, autonomous drop drones, LoRa mesh), but nobody has proven forward lines can report back over 1.2–2.5 mi. Rises to 4 if the radio range test passes. |
| 2026-10-15 | 3 (unchanged) | Reviewed published LoRa range measurements: over 2.5 mi in the open with antennas at 4.9 ft, but 0.6 mi or less in forest. The open-ground case looks likely; the forest case needs the [T9 field test]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back), which now has pass/fail criteria. |
| 2026-10-15 | 3 (unchanged) | Reviewed front-line conditions. Fiber-optic FPVs, which radio detectors can't see, and predictable approach routes along tree lines support the payoff. GPS jamming, friendly drones and the forest radio case add work; they are now tests T14, T15 and T9. |
| 2026-10-15 | 3 (unchanged) | Proposed [no-extra-cost fixes](#solving-the-field-limits-at-no-extra-cost) for those limits: drop the node's GPS, sort friend from foe by line order and flight windows, and report battery and temperature. The fixes also turn the line into a record of drone traffic. All untested; rating moves only on test results. |
| 2026-10-15 | 3 (unchanged) | Page reorganised into layers: summary, front-line problems in plain terms, then fold-out detail. No change to the evidence. |
| 2026-10-15 | 3 (unchanged); payoff 5 confirmed | [Front-line evidence]({{ site.baseurl }}{% link research/problem-check.md %}) supports the payoff: drones cause about 80% of casualties, fiber-optic FPVs beat the radio detectors units carry, and no cheap system fills the gap. Feasibility is unchanged: radio out of the trees (T9, T17) and whether warning changes behaviour (T18) are still unproven. |
| 2026-10-15 | 3 (unchanged) | Proposed an engineering answer to the radio question: a listen-only receiver at the edge of the unit's tree line, wired back. Windbreak belts are 10–49 ft wide, not forests, and cost a few dB each on paper. Untested (T9, T17). |
| 2026-10-23 | 3 (unchanged) | A [jamming model]({{ site.baseurl }}{% link models/line-layout.md %}#jamming): a jammer near the ground blinds a dart only within a few hundred feet on our estimate, about a mile in the worst case. The unit's own jammers deafen receivers at the positions, so the position's links go by wire or fiber. T19 now measures at range, and decides between the two cases. |
| 2026-10-23 | 3 (unchanged) | Alerts now come home on [two FPV fibers]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box) from tip darts in the front row, and each position is covered ±60°. The lay model's net drops from 35 darts a lay to 22, and nothing at the unit uses radio. Untested: the fiber link is T21. |
| 2026-10-23 | **4** (up from 3) | The rating was 3 because nobody had shown a forward line could report back 1.2–2.5 mi by radio, and it was to rise to 4 once that was solved. The two FPV fibers from the tip darts now carry every alert home, so that link is gone, and FPV fiber is flown every day at the front. What remains is short radio hops between darts about 960 ft apart, and tests not yet run: a laid fiber lasting on the ground (T21), landing upright (T10), winter power (T12) and whether warning changes what troops do (T18). A failure in any of them drops it back. |
</details>
