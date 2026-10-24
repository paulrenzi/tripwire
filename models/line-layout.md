---
title: How it works
nav_primary: 2.1
---

# How it works
{: .no_toc }

<p class="vz-lede">A row of listening darts about a mile out. The dart that hears a drone radios its neighbours, the alert hops along the row to one of two <strong>tip darts</strong>, and each tip sends it home down a fiber the drone laid.</p>

<div class="stats">
  <div class="stat"><p class="stat-num">15</p><p class="stat-label">darts on open, flat ground; about 22 used in laying them</p></div>
  <div class="stat"><p class="stat-num">960 ft</p><p class="stat-label">between darts: the radio hop sets it, not the ear</p></div>
  <div class="stat"><p class="stat-num">1.01 mi</p><p class="stat-label">out: the front row, 5,316 ft from the unit</p></div>
  <div class="stat"><p class="stat-num">≥ 65 s</p><p class="stat-label">warning for any drone heading for the unit (est.)</p></div>
</div>

### The planning numbers, none measured yet

<div class="vz-cards vz-4">
  <div class="vz-card"><p class="vz-card-num">656 ft</p><p>a dart's hearing. A drone 165 ft up is heard about 635 ft away along the ground. <a href="{{ site.baseurl }}{% link mvp.md %}#layer-2-hear-a-drone-from-near-the-ground-t11">T11</a> measures it</p></div>
  <div class="vz-card"><p class="vz-card-num">980 ft</p><p>a radio hop near the ground. <a href="{{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back">T9</a> measures it</p></div>
  <div class="vz-card"><p class="vz-card-num">60 mph</p><p>drones, up to 165 ft up: above an FPV's usual 37–50 mph, below its 75 mph loaded top (<a href="{{ site.baseurl }}{% link research/threat-profile.md %}">the drones</a>)</p></div>
  <div class="vz-card"><p class="vz-card-num">+5 s</p><p>for recognising the drone and relaying the alert, on top of the minute</p></div>
</div>

### Why the row sits a mile out

<figure class="vz-figure vz-narrow">
<svg viewBox="0 0 420 440" role="img" aria-labelledby="ll-deep-t">
  <title id="ll-deep-t">The worst case: a drone flying midway between two front darts 960 feet apart is first heard about 400 feet before the row. With the row 5,316 feet out, it is heard 5,720 feet from the unit, 65 seconds at 60 mph.</title>
  <g fill="#d2451e" fill-opacity=".07" stroke="#d2451e" stroke-opacity=".5" stroke-dasharray="5 4">
    <circle cx="60" cy="200" r="198"/><circle cx="360" cy="200" r="198"/>
  </g>
  <line x1="0" y1="200" x2="420" y2="200" stroke="#6a625a" stroke-width="1.5" stroke-dasharray="3 5"/>
  <line x1="210" y1="8" x2="210" y2="345" stroke="#151515" stroke-width="2.5" stroke-dasharray="8 6"/>
  <path d="M202 333 L210 347 L218 333" fill="none" stroke="#151515" stroke-width="2.5"/>
  <g fill="#d2451e"><circle cx="60" cy="200" r="8"/><circle cx="360" cy="200" r="8"/></g>
  <circle cx="210" cy="71" r="9" fill="#fff" stroke="#d2451e" stroke-width="4"/>
  <text x="226" y="58" class="vz-t" style="font-size:18px">first heard</text>
  <line x1="196" y1="71" x2="196" y2="200" stroke="#151515" stroke-width="1.5"/>
  <text x="188" y="142" class="vz-t-small" text-anchor="end" style="font-size:17px">~400 ft</text>
  <text x="60" y="232" class="vz-t-small" text-anchor="middle" style="font-size:16px">dart</text>
  <text x="360" y="232" class="vz-t-small" text-anchor="middle" style="font-size:16px">dart</text>
  <line x1="72" y1="262" x2="348" y2="262" stroke="#151515" stroke-width="1.5"/>
  <path d="M82 256 L70 262 L82 268 M338 256 L350 262 L338 268" fill="none" stroke="#151515" stroke-width="1.5"/>
  <rect x="166" y="250" width="88" height="24" fill="#fff"/>
  <text x="210" y="268" class="vz-t" text-anchor="middle" style="font-size:17px">960 ft</text>
  <text x="222" y="310" class="vz-t-small" style="font-size:16px">5,316 ft to the unit</text>
  <rect x="166" y="352" width="88" height="32" fill="#151515"/>
  <text x="210" y="374" class="vz-t-unit" text-anchor="middle" style="font-size:15px">UNIT</text>
  <text x="210" y="420" class="vz-t-accent" text-anchor="middle" style="font-size:18px">5,720 ft ÷ 88 ft/s = 65 s of warning</text>
</svg>
<figcaption>The worst case: a drone passing exactly between two front darts. Dashed circles are each dart's hearing; drawn to scale except the distance home.</figcaption>
</figure>

## The net

<figure style="margin:12px 0 8px;max-width:600px">
<div id="line-layout"></div>
<figcaption style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px">
<button type="button" id="line-layout-play" class="btn btn-sm">Play</button>
<button type="button" id="line-layout-replay" class="btn btn-sm">Replay</button>
<span id="line-layout-status" aria-live="polite" style="font-weight:600;flex:1 1 220px"></span>
</figcaption>
<p id="line-layout-net" aria-live="polite" style="margin:6px 0 0;font-size:0.9em"></p>
</figure>
<script src="{{ '/assets/js/line-layout.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>

Three drones fly in at 60 mph: one straight at the middle position, exactly between two front darts (the worst case), one from 30° to the left, and one from 60° to the right. **Tap any dart to knock it out, or a fiber to cut it,** and see which darts can still get an alert home.

<div class="vz-steps vz-3">
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="14" cy="24" r="5" fill="#d2451e"/><g fill="none" stroke="#151515" stroke-width="3"><path d="M24 14 Q30 24 24 34"/><path d="M31 8 Q41 24 31 40"/></g></svg>
    <p class="vz-step-num">1 · Hear</p>
    <p>Every dart listens in every direction and answers one question: <em>is that a drone?</em></p>
  </div>
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><g fill="#d2451e"><circle cx="6" cy="30" r="4"/><circle cx="24" cy="30" r="4"/><circle cx="42" cy="30" r="4"/></g><g fill="none" stroke="#151515" stroke-width="3"><path d="M8 24 Q15 12 22 24"/><path d="M26 24 Q33 12 40 24"/></g><line x1="42" y1="34" x2="42" y2="46" stroke="#2f6b3a" stroke-width="3"/></svg>
    <p class="vz-step-num">2 · Pass it back</p>
    <p>A few bytes hop dart to dart, 0.05–1 s a hop, to a tip dart, which flashes it home down its fiber.</p>
  </div>
  <div class="vz-step">
    <svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6 L44 42 H4 Z" fill="#d2451e"/><rect x="22" y="18" width="4" height="13" fill="#fff"/><rect x="22" y="34" width="4" height="4" fill="#fff"/></svg>
    <p class="vz-step-num">3 · Warn</p>
    <p>Both fibers end at a base box behind the unit, wired to a phone at each position. Nothing at the unit uses radio.</p>
  </div>
</div>

<details class="layer" markdown="block">
<summary><span class="layer-title">The three steps in full</span><span class="layer-sub">Tip darts, hop times, the base box, and why it's a tripwire, not an array</span></summary>

1. **Hear.** Every dart listens all the time, in every direction. It only answers one question: *is that a drone?*
2. **Pass it back.** The dart that hears it radios a few bytes to its neighbours. Each dart relays an alert once, along the row, until it reaches a **tip dart**: the second or the second-last dart in the row. A tip carries a spool of FPV fiber whose other end is tied off at home, and it sends the alert down the fiber as flashes of a small laser. Each radio hop takes about 0.05–1 s depending on the radio's settings; the fiber adds nothing worth counting.
3. **Warn.** Both fibers end at the **base box** at the launch point behind the unit ([below](#the-fibers-and-the-base-box)). It passes each alert down a wire to a phone or tablet at each position. Nothing at the unit uses radio, so the unit's own jammers can't deafen it ([Jamming](#jamming)). Warning is distance ÷ speed, from wherever the drone was first heard.

**It is a tripwire, not a microphone array.** An array combines its microphones to find a direction, which needs exact spacing and shared timing. Here each dart only says "I heard it", and the net carries that home.

</details>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The planning numbers, as first written</span><span class="layer-sub">The page's original opening, with its sources</span></summary>

How many darts it takes to give a unit a minute's warning of a drone, where they go, and how they get there. Listening darts sit in a row about a mile out. The one that hears a drone radios its neighbours, the row passes the alert along to one of two **tip darts**, and each tip sends it home down an FPV fiber the drone paid out as it laid the tip. The map is drawn to scale, and its animation runs ten times faster than real life.

The planning numbers, none measured yet:

- **Hearing: 656 ft (200 m).** A drone 165 ft up is heard about 635 ft away along the ground. [T11]({{ site.baseurl }}{% link mvp.md %}#layer-2-hear-a-drone-from-near-the-ground-t11) measures it.
- **Radio: 980 ft (300 m) per hop** near the ground. [T9]({{ site.baseurl }}{% link research/open-questions.md %}#t9-can-a-forward-line-report-back) measures it.
- **Drones: 60 mph, up to 165 ft up.** That is above the 37–50 mph an FPV usually flies with a warhead and below its 75 mph loaded maximum. Fiber-optic FPVs fly at 65–165 ft ([the drones]({{ site.baseurl }}{% link research/threat-profile.md %})).
- **Warning: at least a minute,** plus 5 s for recognition and relaying.

</details>

<details class="layer" id="how-deep" markdown="block">
<summary><span class="layer-title">How deep</span><span class="layer-sub">Why the front row sits 5,316 ft out, and why the radio, not the ear, sets the spacing</span></summary>

At 60 mph (88 ft a second), 65 s means hearing the drone **5,720 ft out**.

- **The worst case is a drone passing midway between two front darts.** With darts 980 ft apart, it is 490 ft from each as it crosses the row, and a dart hearing 635 ft along the ground first hears it about 400 ft before that.
- **So the front row sits 5,316 ft (1.01 mi) out.** Every drone heading for the unit is heard at least 5,720 ft away.
- **There are no relay darts.** The fibers carry alerts the last mile, so every dart is a listening dart in the front row.

**The radio sets the spacing, not the ear.** A 656 ft ear alone would allow front darts 1,270 ft apart. But each front dart has to reach its neighbour by radio, so they sit about 960 ft apart. A better ear than this saves almost nothing. A longer radio hop is what would cut darts.

</details>

<details class="layer" id="how-wide" markdown="block">
<summary><span class="layer-title">How wide</span><span class="layer-sub">Three positions, ±60° each, a 2.5 mi row, and sharing it with neighbours</span></summary>

**A unit is small and spread out.** Kofman describes "nine men in three defensive positions" with "250 meters of open ground" between them, and about 15 soldiers per km of front on average ([hvylya](https://en.hvylya.net/news/2036-15-soldiers-per-kilometer-kofman-on-how-europe-s-biggest-war-emptied-the-front-line)). Neighbouring positions are reported 650–3,300 ft apart ([EMPR](https://empr.media/opinion/investigation/widening-gaps-on-the-front-why-ukraines-forces-struggle-to-hold-back-advancing-russians/)). So the map protects **three positions 820 ft apart, 1,640 ft across.**

**Each position gets ±60°.** A drone can be heard coming within 60° of straight on at any of the three positions, so the front row is a 120° arc split open by the unit's width, 2.4 mi long. **The row runs on 300 ft past both 60° lines, 2.5 mi from end dart to end dart,** so a net rotated a few degrees by compass error still covers both edges ([Drop, then confirm](#drop-then-confirm)). Coming in flatter than 60° means starting about 1.7 times as far to the side as in front. A crew a mile forward would have to launch about 1.7 mi to the side, in front of the neighbouring unit. That is our reasoning; we found no source on how far to the side FPV crews launch.

**±60° costs 3 front darts over ±45°** (15 against 12 on open ground). It buys cover against flatter approaches, not margin against bad drops: compass error opens gaps at the joins between sorties in the middle of the row, which the extra width doesn't reach ([What the model found](#what-the-model-found)).

**The net is wider than the unit.** 2.4 mi of front is roughly what 60 soldiers hold at about 24 per mile. Neighbouring units can share one continuous front row, at about 5.5 darts per mile of front, and each adds only its own two fibers.

</details>

<details class="layer" id="two-fibers-for-redundancy" markdown="block">
<summary><span class="layer-title">Two fibers, for redundancy</span><span class="layer-sub">Why two tip darts, what one loss costs, and the fibers and base box</span></summary>

**The net always has two fibers,** one to the second dart at each end of the front row: **15 darts** on open, flat ground, 2 of them tip darts. The last plan carried alerts home on radio trunks and needed 22 (12 in the row, 10 relays) plus a root dart placed by hand. Laying takes more than the plan: on the [lay model](#laying-the-net)'s example sector it plans 16 darts and uses about 22, after bad landings, short hops and broken fibers. The radio trunks used about 35.

- **No single dart can silence it.** Knocking out any one dart cuts off at most 1 other. If a tip dart dies or its fiber is cut, alerts run the other way along the row to the other fiber, and the base box says so within 30 s.
- **One fiber is not offered.** It would save one tip, about $70 of fiber and laser, but one cut would silence the whole net.
- **The longest route home is 6 radio hops and a fiber,** against 11 hops on radio trunks. At 0.05–1 s a hop that adds at most about 6 s (airtime estimate).

### The fibers and the base box

- **A tip dart** is a dart with a spool of about 1.2 mi of FPV fiber and a small laser, about 10 oz against a dart's 4.5 oz (est.). It still hears drones and its neighbours by radio. Light only goes one way, home, so nothing is ever sent out to the row.
- **Laying it.** A tip is the first drop of its sortie. The fiber's home end comes with a connector fitted at the factory: before take-off the crew plugs it into the base box and ties it to a stake. The spool pays out as the drone flies, the way fiber-optic FPVs do.
- **The heartbeat.** A tip checks in down its fiber every 10 s. Light inside a fiber can't be picked up, so this gives nothing away, unlike a radio check-in. If a fiber goes quiet for 30 s the display shows "fiber B dark: cut, or the tip is dead". The heartbeat also proves the connector before take-off and the fiber after the drop: it is how the drone's crew confirms a tip.
- **The base box** is a dart's board with two light detectors, one per fiber, at the launch point. It decrypts each alert, drops the second copy when both tips pass on the same one, and writes the same line of text the radio receiver used to, naming the fiber it came by ([software]({{ site.baseurl }}{% link build-software.md %}#i3-serial-frame-from-the-base-box-to-the-display)). A wire carries it to a phone or tablet at each position. Nothing at the unit transmits or receives by radio.
- **Untested:** whether a small, cheap laser can put enough light into FPV fiber, which carries light in a very thin core, without draining the dart. On paper the fiber itself loses under 1 dB over 1.2 mi. The tip's weight and the fiber-break rate (1 in 20 assumed) are also guesses. One bench test settles all three: a tip dart, a full spool and a base box ([T21]({{ site.baseurl }}{% link models/tripwire.md %}#what-has-to-be-proven)).

What the package costs is on [Projected costs]({{ site.baseurl }}{% link costs.md %}).

</details>

<details class="layer" id="laying-the-net" markdown="block">
<summary><span class="layer-title">Laying the net</span><span class="layer-sub">The lay model: sorties, what it found, the holes fixed, and laying under GPS jamming</span></summary>

Nobody walks a mile forward to plant darts. A small drone does it, with no pilot flying it and no video link ([delivery drone]({{ site.baseurl }}{% link research/delivery-drone.md %})). This section is a working model of that job: a planner and simulator, [`lay_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/laymodel/lay_model.py), that plans a net on a map, checks every sortie against the battery and the wind, writes the ArduPilot missions, and then lays the net 1,000 times with drop errors, bad landings and radio fading.

<figure style="margin:12px 0 8px;max-width:600px">
<video controls muted playsinline loop preload="metadata" poster="{{ '/assets/video/lay-net-poster.png' | relative_url }}" style="width:100%;display:block;border:1px solid #ddd">
<source src="{{ '/assets/video/lay-net.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption style="font-size:0.9em;margin-top:6px">One lay from the model, about 1 min 40 s. An example sector (invented, to scale): two windbreaks, a 50 ft ravine, ground rising 50 ft toward the front, an enemy salient and a 9 mph wind toward it. GPS is jammed. This lay is an unlucky one for the right-hand tip: the first lands silent and the second's fiber breaks, so the third is laid on the next sortie. Every position, battery reading, relay and heartbeat shown comes from the model's output.</figcaption>
</figure>

### How a lay works

1. **Scout.** The unit's own recon drone flies the planned row the day before. Map data is months old; craters, wires and fallen trees are not on it. The crew moves any point the footage puts on bad ground.
2. **Plan.** The crew gives the tool its positions, the **enemy's forward edge as a line** (not just a direction), and the wind forecast. The tool reads a free elevation map (Copernicus GLO-30, about 100 ft grid) and a free land-cover map (ESA WorldCover, about 33 ft grid). It keeps every drop point off trees, off ravine floors and at least 650 ft short of the enemy edge, shortens every hop that crosses a windbreak or a rise, and runs the front row 300 ft past both 60° lines. Then it groups the darts into sorties, each tip first on its own, that pass the battery check and writes one mission per sortie: terrain-relative heights, a ground speed for every leg, a release step for every dart.
3. **Fly.** The drone follows the terrain using its downward lidar, and releases each dart from 33 ft above the ground, not above the launch point. With GPS working it cruises at 100 ft. With GPS jammed it cruises at 35 ft, where its optical-flow sensor stays inside the lidar's 39 ft range, and climbs only to cross the windbreaks the map shows.
4. **Confirm every dart** (table below). A tip is confirmed by its heartbeat reaching the base box. Every other dart sends "landed" with its tilt, its neighbour relays it, and every relay carries the relayer's ID. The dart that closes the front row needs relays from both sides. A point gets at most 3 extra darts; after that it is left for a repair sortie.
5. **Check the battery before every drop.** The drone must be able to release here and still get home into the wind plus a 5 mph gust, with 20% left. If it can't, it flies home with the darts still on board, and they go on the next sortie.
6. **Turn round.** Swap the pack, reload 4 darts, scan their IDs. With 6 packs and a 2-channel charger, the drone never waits for a charge.

**What the drone's receive-only radio hears after each drop, and what it does next:**

| The drone hears | It means | Next |
|---|---|---|
| A relay from the planned neighbour | Linked | Fly on |
| "Landed" but no relay | Out of reach | Next dart 300 ft back toward the neighbour |
| "Landed, tilted" | Lying flat or in a tree | Next dart on the same spot |
| Nothing | A dud | Next dart on the same spot |
| A tip: no heartbeat at the base box | Its fiber broke, or it landed badly | A new tip, with a new fiber, first on the next sortie. In the model the drone flies home with its other darts, since nothing is there to confirm them against |

If a sortie runs out of darts or battery partway through, the points it didn't finish go first on the next sortie.

### What the model found

The example sector, 1,000 lays per row. **"Whole"** means every drone track within 60° of each position is heard at least 55 s out. That is 5 s short of the minute target, which leaves room for small drop errors. **"Survives a fiber cut"** is the share of whole lays that stay whole with either fiber cut.

| Case | Whole | Survives any one dart loss | Survives a fiber cut | Darts used | Darts, 9 lays in 10 | Sorties | Hours |
|---|---|---|---|---|---|---|---|
| The last plan: radio trunks, ±45°, GPS jammed, confirm | 99% | 93% | – | 34.9 | 40 | 9.3 | 2.2 |
| This plan (16 darts), GPS working, no confirm | 8% | 2% | 31% | 16 | 16 | 5.1 | 1.0 |
| This plan, GPS working, confirm | 100% | 94% | 99% | 20.3 | 23 | 6.6 | 1.3 |
| **This plan, GPS jammed, confirm** | **98%** | **91%** | **98%** | **22.2** | **26** | **7.1** | **1.4** |
| … if 95% of darts land upright, not 85% | 100% | 93% | 99% | 19.8 | 23 | 6.3 | 1.2 |
| … if the radio hop is 800 ft, not 980 | 99% | 91% | 97% | 26.7 | 31 | 8.0 | 1.7 |
| … if the compass is off 4°, not 2° | 89% | 82% | 97% | 22.7 | 27 | 7.2 | 1.5 |
| … if 1 fiber in 5 breaks while laid, not 1 in 20 | 98% | 87% | 93% | 23.3 | 28 | 7.8 | 1.7 |
| … in a 15 mph wind | 99% | 91% | 97% | 22.1 | 26 | 8.1 | 1.7 |
| … at 14 °F, with packs not kept warm | 98% | 89% | 97% | 22.5 | 27 | 17.0 | 6.0 |

- **A lay takes about 22 darts and 7 sorties, against 35 and 9 on radio trunks.** The 16 planned darts are the floor. Darts that land badly (15%, assumed), hops that fall short and broken fibers take about 6 more.
- **The fibers are where the saving comes from; ±60° gives some of it back.** Fiber at ±45° would plan 13 darts and use about 18 in 6 sorties. ±60° adds 3 front darts, about 5 darts used and 1.5 sorties a lay ([comparison](https://github.com/paulrenzi/tripwire/blob/main/tools/laymodel/out/fibre-summary.md)).
- **The wider arc doesn't absorb bad drops.** With the compass 4° off, 89% of lays are whole judged at ±60°, and 94% judged at ±45°, against 92% for a net built for ±45°. Compass error opens gaps at the joins between sorties, mid-row, where the extra width doesn't reach.
- **Without confirmation, the net is almost never whole.** 980 ft is the hop that works 9 times in 10. With 15 hops in the row, most lays have one that fails, and nothing on the ground says which.
- **Losing one dart costs a little more than before:** 91% of lays survive any one loss, against 93% on radio trunks, because a tip dart now does a whole trunk's job.
- **Wind:** 5 sorties up to 12 mph, 7 at 15 mph and 12 at 18 mph. Above about 15 mph, don't lay.
- **Cold packs more than double the sorties.** Keep them warm until launch.
- **The drone is a consumable.** At 2% lost per sortie (a guess), a lay costs about 0.15 drones: about 0.6 a year at 4 winter re-lays, with solar.

### Holes found, and the fixes now in the model

| Hole | What it did | Fix | Cost |
|---|---|---|---|
| The plan ignored the ground | Darts in trees and ravines; hops across windbreaks out of reach | Elevation and land-cover checks in the planner | Free data |
| Mission heights were relative to the launch point | Over ground rising 50 ft, a 33 ft release height would put the drone into the ground | Terrain following plus a downward lidar | MTF-01P flow and lidar, ~$42 |
| Optical flow loses its scale above the lidar's range | Jammed-GPS navigation drifts at 100 ft | Cruise at 35 ft when jammed; climb only over mapped belts | None |
| Optical flow needs light | At night with GPS jammed, only the compass is left | When GPS is jammed, lay at dawn or dusk | None |
| Without GPS, ArduPilot has no origin, and so no position to look up magnetic declination | Missions won't run, or headings are off by the local declination | The tool sets the origin and the declination at the launch point before each sortie ([ArduPilot](https://ardupilot.org/copter/docs/common-non-gps-navigation-landing-page.html)) | None |
| Nothing checked that a link worked | 95% of lays broken somewhere | Drop, then confirm, on every dart | Receive-only radio, ~$20 |
| Any relay counted as a confirmation | A dart out of reach of its planned neighbour could pass on a relay from the dart before it | Relays carry the relayer's ID; the closing dart needs both sides | 2 bytes a packet |
| Radio trunks home | 12 relay darts, most of the failed hops, and a receiver beside the unit's own jammers | Two FPV fibers from the base box to tip darts in the front row; a wire from the base box to every position | About $70 a tip (est.), and the relays saved |
| A fiber broken while laid looked like a working one | Alerts down that fiber would be lost without warning | A heartbeat down every fiber every 10 s; a tip with none is laid again | None |
| A bad landing was invisible | A flat or snagged dart checks in normally but hears and radios much worse | An accelerometer in every dart | ~$1–2 a dart |
| The harness drops in a fixed order | A spare is just the next dart, so any dart has to stand in anywhere | Every dart gets a microphone and a tilt sensor. Points a sortie runs out for move to the next one | ~$3 a dart |
| End darts sat 635 ft inside the edge lines | Every drone track along an edge line only grazed a dart, and a rotation of 3° left one edge unheard | Ends 300 ft past the edge lines | One dart |
| A fixed 22 mph cruise | Against 14 mph, the drone couldn't take even one dart to the end of a trunk and get home | Least-energy ground speed per leg (ArduPilot DO_CHANGE_SPEED); battery check with gust margin before every drop | None |
| 2 packs and a 1-channel charger | The planned lay took 3.3 h | 6 packs and a 2-channel charger: about 1 h | ~$340 |
| Cold packs | Up to 25% less capacity (assumed) | An insulated bag | ~$20 |

**Still open, not modelled:**
- The drone's return shows the enemy where it launched from. Launch 300–500 ft from the positions, and vary the spot. Tip sorties have to leave from the base box, where the fibers end; other sorties can launch elsewhere.
- The fibers lead from the front row toward the base box, so a fiber found is a trail. FPV fiber already lies across the front in quantity ([Business Insider](https://www.yahoo.com/news/articles/unjammable-drones-leaving-wires-everywhere-114504509.html)), which may hide ours.
- In the model, a sortie whose tip fails flies home with its other darts. Flying on would save a sortie, if the crew can tell the drone by telemetry.
- A sortie can't be recalled.
- Handing the net over to a relieving unit isn't designed.

### What each test now has to report

The model turns on six numbers. Each test should report a spread, not one figure:

- **T9:** the hop that works 90% of the time, and how much it varies from place to place (4 dB assumed).
- **T10:** the share of drops that land upright in plough, pasture and frozen ground (85% assumed). This is the cheapest saving: at 95%, each lay uses 4 fewer darts.
- **T13:** power against airspeed with 4 darts, and the battery each sortie uses.
- **T14:** compass error with GPS jammed, split into the error shared by a whole day and the change from one sortie to the next (2° and 0.7° assumed). At 4°, 11% of lays leave a gap. Also the lidar's real range over dark plough and snow: the 35 ft cruise assumes the full 39 ft.
- **T12:** pack capacity at 14 °F, warm and cold.
- **T21:** the tip dart: light delivered down a full spool, the battery the laser and heartbeat use, the tip's weight, and how often fiber breaks while laid (1 in 20 assumed).

### What the drone knows

**Coordinates, a few rules and its own sensors.** It knows nothing about north, the enemy or spacing.

- **North and position:** GPS and compass, or with GPS jammed, compass, optical flow and lidar from an origin set at launch (below).
- **The enemy:** only through the plan, which keeps every point 650 ft short of the forward edge the crew drew.
- **Spacing:** proved by radio, one relay at a time, never measured.
- **The darts know nothing.** "Dart 7" is a place only because the drone's log ties that ID to where it was released.

### Finding the drop points when GPS is jammed

GPS is jammed routinely at the front ([field conditions]({{ site.baseurl }}{% link research/field-conditions.md %}#electronic-warfare)). The darts carry no GPS. A dart's position is where the drone's log says it released. The drone needs to know where it is, in this order of cost:

| Method | What it needs | Good enough? |
|---|---|---|
| **Plain GPS** | Nothing extra | Where it isn't jammed. Each flight log records where GPS failed or jumped, so the unit learns its own map of jamming |
| **Compass, barometer and optical flow** from an origin set at launch | The MTF-01P flow and lidar sensor (now in the kit), daylight, a 35 ft cruise | The model's choice under jamming. Drifts with distance, but darts in one sortie drift together, and drop, then confirm repairs the joins ([ArduPilot](https://ardupilot.org/copter/docs/common-non-gps-navigation-landing-page.html)) |
| **Computer vision: matching the camera's view to satellite maps** | A downward camera, a Jetson Orin NX-class computer (several hundred dollars, est.) and stored map tiles | Not used yet; the upgrade if T14 shows a compass error well over 2°. Best open candidate: [NGPS](https://github.com/snktshrma/ngps_flight) (MIT licence, ROS 2, feeds ArduPilot), whose author reports about 10–20 ft error over 5 real flights at 200–490 ft up ([paper](https://arxiv.org/abs/2607.18936)). [gnss-denied-nav](https://github.com/koksalan/gnss-denied-nav) (MIT) reports a 79 ft median on unseen regions and refuses to fix when seasons change the ground; simulation and datasets only. [WildNav](https://github.com/TIERS/wildnav) relies on SuperGlue, whose licence bars commercial use. Ukrainian systems doing this are reported but proprietary |
| **By hand** | Troops walking in at night | The base box and the wire to the positions |

</details>

<details class="layer" id="what-placement-has-to-get-right" markdown="block">
<summary><span class="layer-title">What placement has to get right</span><span class="layer-sub">Drop error against dart count, landing upright, power, the base box, friendly drones</span></summary>

**Accuracy decides the dart count, unless every link is confirmed.** The 15-dart net assumes every dart lands on its point. A dart that lands off its point can end up beyond radio reach of its neighbour. So the plan has to shrink every gap by twice the expected drop error:

| Drop error | Planned spacing | Darts |
|---|---|---|
| none | 980 ft | **15** |
| ±33 ft | 914 ft | **16** |
| ±66 ft | 848 ft | **17** |
| ±160 ft | 660 ft | **22** |

How close a drop lands is test T13. The tripwire page's working figure, that drops 66–160 ft off still make a line, needs revisiting: at 160 ft off, this net needs 22 darts, not 15. The [lay model](#laying-the-net) takes the other route: it plans at the full hop and confirms every link as it is made, which costs fewer darts than planning for the error.

**The other requirements:**

- **Land upright, point first, in soil.** The tip goes in about 2.8 in, holding the microphone about 20 in up. Whether the fins turn a dart nose-down in time is the first drop test ([dart model]({{ site.baseurl }}{% link build-3d.md %}#why-it-should-fall-point-first)).
- **Nothing solid between neighbours.** A ridge, a building or a thick tree belt between two darts can break a hop. Plan hops along open ground and shorten them under trees, which also shortens hearing.
- **Every dart keeps its radio listening.** It has to be awake to catch its neighbours' alerts and pass them on. That costs about 105 mAh a day (est.). A 2.4 in solar panel lying flat on top of the pod, so it works whichever way the dart faces, collects about that much in November and more from March to October, but only about half of it in December. So cells still run flat in midwinter, and the net is re-laid 2–4 times a year instead of 13 (est.). A charger chip stops charging below 32°F, when charging would damage the cell. How long a cell lasts in the cold, and how much the panel collects through a winter, are unknown until the battery test (T12). Tip darts also flash a laser every 10 s for the heartbeat, about 25 µA averaged, a negligible drain (est.).
- **A base box and a wire.** Both fibers end at the base box, placed by hand at the launch point and run on the unit's power. A wire carries alerts from it to a phone or tablet at each position. If the box dies, the unit hears nothing, so it is the first thing the crew checks, and a spare is cheap.
- **Keep the unit's own drones out of the alarm.** Ukrainian FPVs sound like Russian ones. The proposed answer is to alarm only on drones heading inbound, outside the unit's own flight times (test T15).
- **Re-lay before the cells run out,** in practice in midwinter, and replace darts lost to shelling. The darts' battery reports forecast when.

</details>

<details class="layer" id="when-it-breaks" markdown="block">
<summary><span class="layer-title">When it breaks</span><span class="layer-sub">A repair animation and what each failure costs to fix</span></summary>

<figure style="margin:12px 0 8px;max-width:600px">
<div id="repair-model"></div>
<figcaption style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px">
<button type="button" id="repair-play" class="btn btn-sm">Play</button>
<button type="button" id="repair-replay" class="btn btn-sm">Replay</button>
<span id="repair-status" aria-live="polite" style="font-weight:600;flex:1 1 220px"></span>
</figcaption>
</figure>
<script src="{{ '/assets/js/repair.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>

Same map, with time compressed. A shell cuts a fiber, the base box misses the tip's heartbeat, and one sortie lays a new tip and fiber; then a re-lay sortie flown on a compass 3° off is caught by drop, then confirm.

| Failure | What the unit loses | Fix | Our cost |
|---|---|---|---|
| **A front dart** | A blind gap about 660 ft wide: its neighbours end up 1,926 ft apart and each hears 635 ft | One sortie drops a dart on its point | ~$27–31 |
| **A tip dart, or its fiber** | No coverage, but the net is down to one fiber. The base box shows it within 30 s | One sortie from the base box lays a new tip and fiber, first | ~$90–100 (est.) |
| **Two darts** | Both tips, or both fibers, silence the net. Any other two cut off the darts between them | Repair after the first loss | Per dart |
| **The base box** | Everything, until swapped | By hand, at the launch point | ~$60 (est.) |
| **Cells run down** | Darts drop out one by one | A re-lay: about 22 darts, 7 sorties | ~$1,020, with drone wear |
| **The drone** | Any repair or re-lay | A new quad | ~$850–920 |
| **The unit's own jammer on** | Nothing on the main estimate: no link at the unit uses radio. In the worst case it reaches the front row too ([Jamming](#jamming)) | Nothing more to add; T19 decides | none |
| **An enemy jammer near the front row** | Darts within a few hundred feet of it can't relay; a LoRa hunter would open a gap | Pull the row back from it; a second band, 433 MHz (untested) | none |

**The repair model.** The base box lists the darts that have gone quiet and any fiber that's dark, the crew taps "re-drop", and the planning tool writes one mission for up to 4 darts. The flight to the farthest point is about 1.2 mi and about 10 minutes. A dark fiber, a dead tip or a dead front dart goes on the next sortie; anything else waits for the next re-lay. Battery wear is about $0.30 a sortie. **The drone is the hidden cost:** a 2% chance of losing it adds about $20 to every sortie, as much as the dart it carries. So repairs are batched, and a spare drone is worth quoting.

**Roll call: how the unit knows a dart is dead** (a design change). As planned, check-ins aren't relayed ([software plan]({{ site.baseurl }}{% link build-software.md %})), so a dead dart goes unnoticed. Proposed: once a day every dart sends one check-in and every other dart relays it once. That is about 225 short bursts across the net, a second or two of airtime per dart. A dart missing from the roll call is named from the plan within a day. The fibers need no roll call: their heartbeat shows them every 10 s.

### Drop, then confirm

**Compass navigation over a mile is worse than the placement budget.** With GPS jammed, each degree of compass error puts a dart 93 ft sideways at 5,316 ft; 3° is about 280 ft. Inside one sortie that mostly doesn't matter: every drop is off the same way, and consecutive drops about 960 ft apart are only about 50 ft off each other. **The joins between sorties break.** Each sortie starts again from the unit, and the sortie that closes the front row has two joins; at 3°, one closes to about 680 ft and the other opens to about 1,250 ft.

**Proposed fix (untested):** the drone carries a receive-only LoRa board (about $20, transmits nothing).

1. Each dart sends "landed" once it is down, and its neighbour relays it, once.
2. The drone, still hovering, hears that relay. That proves the new dart reached its neighbour.
3. If it hears nothing, or the dart closing the row is relayed from one side only, the drone drops a spare about 300 ft toward the silent neighbour's logged point and listens again.

That measures every link as it is made, so the drone never needs to know where it is to within a hop, and a failed join costs one spare. Absolute error is cheap in the middle of the row, at most about 3 s of warning for 280 ft. **It is not cheap at the ends:** a net rotated 3° moves an end dart about 280 ft along the row, and the first plan's ends, 635 ft inside the edge lines, then left one edge unheard. The lay model puts the ends 300 ft past the edge lines instead, and confirms every dart, not just the joins ([Laying the net](#laying-the-net)).

**If the planning numbers are wrong, the fix is more darts, not a redesign:**

| Radio hop | Darts |
|---|---|
| 650 ft | 22 |
| 800 ft | 18 |
| **980 ft (plan)** | **15** |
| 1,250 ft | 13 |

</details>

<details class="layer" id="jamming" markdown="block">
<summary><span class="layer-title">Jamming</span><span class="layer-sub">How close a jammer has to be to blind a dart, from a link-budget model</span></summary>

{: .warning }
> Estimates from a link-budget model, [`jam_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/jamming/jam_model.py), run on the example sector with every jammer on all the time. Jammer powers and heights are assumed, not measured. [T19]({{ site.baseurl }}{% link research/open-questions.md %}) measures it.

**Jamming is everywhere near the front, and it covers our band.** RUSI counted at least one major Russian jamming system per 6 mi (10 km) of front ([via Wikipedia](https://en.wikipedia.org/wiki/Electronic_Warfare_Troops_of_the_Russian_Federation)). "Most mobile jammers" cover 868–915 MHz, and FPV control links run on the same LoRa chips our darts use ([Armada International, Feb 2026](https://www.armadainternational.com/2026/02/the-curran-papers-no-5-jamming-uninhabited-aerial-vehicle-video-signals-electronic-warfare/)). So the jammers on both sides are already built against our radio. More in [field conditions]({{ site.baseurl }}{% link research/field-conditions.md %}#electronic-warfare).

**What decides it is distance, not how common jamming is.** A jammer is a transmitter like a dart. It spreads its power across the band, about 640 of our 125 kHz channels, so a 20 W trench jammer puts less into our channel than a dart's 0.16 W does. Near the ground its signal fades as fast as ours. So it blinds a dart only from closer than about 0.4 of a hop:

| Jammer (assumed) | Blinds a dart within | Worst case |
|---|---|---|
| Trench jammer, 20 W, 5 ft up | **about 390 ft** | 1.1 mi |
| Vehicle jammer, 100 W, 8 ft up | about 740 ft | 2.2 mi |
| Jammer on a mast, 50 W, 33 ft up | about 1,260 ft | 3.7 mi |
| A LoRa hunter like Tishina, 20 W all in our channel | about 1,970 ft | 5.7 mi |

The worst case assumes the jammer's signal crosses open ground with none of the losses that hold our own hop to 980 ft. That is nearer the truth for a jammer up high than for one in a trench. A jammed dart still hears drones and still transmits. It can't receive, so it can't relay.

**What that does to the net:**

| Jammers on | Main estimate | Worst case |
|---|---|---|
| The enemy's trench jammers, every 1,640 ft along their edge | Net whole, 60 s | Only the two tips report |
| A LoRa hunter every 1,640 ft along their edge | 7 front darts can't relay; gaps in the row | Only the two tips report |
| **Our own trench jammers, at the positions** | **Net whole, 60 s** | Only the two tips report |
| The last plan's radio trunks, with our own jammers on | Receiver deaf: net silent | Net silent |

- **The fibers answer our own jammers.** The last plan put a radio receiver at P2, beside the unit's trench jammers, so whenever those were on, the net was deaf. Now the alerts come home by fiber and go to the positions by wire, so nothing at the unit has to receive by radio. FPV fiber costs about $32–56 a mile today ([DroneXL, May 2026](https://dronexl.co/2026/05/11/ukraine-fiber-optic-spool-price-ai-data-center-demand/)), about $40–70 for a tip's 1.2 mi. In the worst case our jammers reach the front row itself, about a mile out, and only the tips' own ears still count.
- **Enemy jammers matter only near their edge,** on the main estimate. A LoRa hunter would open gaps in the front row. Pulling the row back from a known jammer costs warning; a second band at 433 MHz, which most mobile jammers don't list ([Armada](https://www.armadainternational.com/2026/02/the-curran-papers-no-5-jamming-uninhabited-aerial-vehicle-video-signals-electronic-warfare/)), costs a second radio. Both need T19.
- **Jammers aren't always on.** Crews switch them on when a detector warns ([problem check]({{ site.baseurl }}{% link research/problem-check.md %})). The net's alert comes a minute before the drone, so it may get home before the jammers go on. Not modelled.
- **Why not fiber everywhere?** Fiber can't be jammed and gives off nothing to find. But an air-dropped row can't share one: every dart would need its own run, and a single cut would silence everything beyond it. Fiber fits the long links home: the two tips here, and a tip every 2 mi in a road's fence ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %}#how-many-darts)).
- **Which case is real decides the project.** If the main estimate holds, jamming is a placement problem: keep radios a few hundred feet from jammers. If the worst case holds, a radio net cannot work near the front at all. T19 now has to measure at range from a jammer, not only beside one.

</details>

<details class="layer" id="what-the-net-misses" markdown="block">
<summary><span class="layer-title">What the net misses</span><span class="layer-sub">Parked ambush drones, launches inside the net, very high or flat approaches</span></summary>

- **Fiber-optic FPVs already parked in ambush.** They sit silent by a road and lift off seconds before they strike. A guard on the road itself is the answer: posts that hear them land ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})).
- **Drones launched from inside the net,** drones flying higher than a dart can hear, and drones coming in flatter than 60°.
- **Direction.** A dart hearing a drone can't tell if it is the unit's own, unless the unit's drones fly at set times.

Everything here is geometry on the planning numbers above, not measurements. If a dart hears less than 656 ft, the front row needs more darts. If the radio reaches less than 980 ft, the front row needs more darts too.

</details>
