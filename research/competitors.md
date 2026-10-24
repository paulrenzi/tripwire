---
title: Competitors to the tripwire
nav_primary: 3
nav_label: Competitors
---

# Competitors to the tripwire
{: .no_toc }

<p class="vz-lede">Everything that competes for the tripwire's job, warning a front-line position of incoming FPVs, ranked by <strong>what it costs against what it's shown to achieve</strong>. Reviewed 2026-10-15.</p>

<figure class="vz-figure vz-narrow">
<svg viewBox="0 0 520 370" role="img" aria-labelledby="co-chart-t">
  <title id="co-chart-t">Price per sensor against seconds of warning of an FPV. Our dart row: 17 to 50 dollars, 45 to 108 seconds, estimated. VolAnti about 65 to 105 dollars and DroneAlert about 211 dollars, about 4 seconds. Zvook NW0 834 to 950 dollars, 6 to 17 seconds on its own claims. Chuyka 584 to 701 dollars, no warning of a fiber-optic FPV.</title>
  <g stroke="#d9d3c7" stroke-width="1"><line x1="60" y1="226" x2="480" y2="226"/><line x1="60" y1="153" x2="480" y2="153"/><line x1="60" y1="79" x2="480" y2="79"/></g>
  <line x1="60" y1="300" x2="480" y2="300" stroke="#151515" stroke-width="1.5"/>
  <line x1="60" y1="30" x2="60" y2="300" stroke="#151515" stroke-width="1.5"/>
  <g class="vz-t-small" style="font-size:13px" text-anchor="end"><text x="52" y="304">0 s</text><text x="52" y="230">30 s</text><text x="52" y="157">60 s</text><text x="52" y="83">90 s</text></g>
  <g class="vz-t-small" style="font-size:13px" text-anchor="middle"><text x="60" y="320">$10</text><text x="270" y="320">$100</text><text x="480" y="320">$1,000</text></g>
  <text x="270" y="346" class="vz-t-small" text-anchor="middle" style="font-size:14px">price per sensor (log scale)</text>
  <text x="14" y="20" class="vz-t-small" style="font-size:14px">warning of an FPV</text>
  <rect x="108" y="35" width="99" height="155" fill="#d2451e" fill-opacity=".85"/>
  <text x="157" y="104" class="vz-t-unit" text-anchor="middle" style="font-size:15px;letter-spacing:0">Our dart</text>
  <text x="157" y="124" class="vz-t-unit" text-anchor="middle" style="font-size:15px;letter-spacing:0">row (est.)</text>
  <line x1="231" y1="290" x2="275" y2="290" stroke="#151515" stroke-width="5"/>
  <text x="252" y="276" class="vz-t" text-anchor="middle" style="font-size:13px">VolAnti</text>
  <circle cx="338" cy="289" r="5" fill="#151515"/>
  <text x="338" y="276" class="vz-t" text-anchor="middle" style="font-size:13px">DroneAlert</text>
  <rect x="463" y="258" width="12" height="28" fill="none" stroke="#151515" stroke-width="2" stroke-dasharray="3 2"/>
  <line x1="469" y1="200" x2="469" y2="256" stroke="#151515" stroke-width="1"/>
  <text x="476" y="194" class="vz-t" text-anchor="end" style="font-size:13px">Zvook NW0 (claimed)</text>
  <path d="M434 294 L444 304 M444 294 L434 304" stroke="#b83a16" stroke-width="2.5"/>
  <line x1="439" y1="232" x2="439" y2="290" stroke="#b83a16" stroke-width="1"/>
  <text x="440" y="226" class="vz-t" text-anchor="end" style="font-size:13px;fill:#b83a16">Chuyka: blind to fiber</text>
</svg>
<figcaption>Warning = how far out a sensor hears ÷ an FPV at 60 mph. Only our row sits forward; everything else sits at the position. VolAnti's range is its author's test; DroneAlert's and Zvook's are their makers' claims; ours is an estimate.</figcaption>
</figure>

<div class="vz-cards vz-4">
  <div class="vz-card"><p class="vz-card-num">No proof</p><p>Nobody has independent evidence of hearing an FPV at a position. Every acoustic FPV range is a maker's claim</p></div>
  <div class="vz-card"><p class="vz-card-num">3–50×</p><p>cheaper per sensor than Zvook's $834–950, which also needs 15–18 W of power</p></div>
  <div class="vz-card"><p class="vz-card-num">$211</p><p>DroneAlert's LoRa module. Our throwaway dart is about 4–12× cheaper (<a href="{{ site.baseurl }}{% link research/build-or-scrap.md %}">build or scrap?</a>)</p></div>
  <div class="vz-card"><p class="vz-card-num">160–200 ft</p><p>the one measured cheap-mic range, on a consumer drone in wind. Ours is unproven until T11</p></div>
</div>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The short version, as first written</span><span class="layer-sub">The page's original summary, with its links</span></summary>

**The job the [tripwire]({{ site.baseurl }}{% link index.md %}) does:** warn a **front-line position** of incoming FPVs, especially fiber-optic ones that radio detectors can't hear. This page ranks everything that competes for that job, or for the same budget, by **what it costs against what it's shown to achieve**. Reviewed 2026-10-15.

{: .important }
> **The short version.**
> - **Nobody has independent evidence** of hearing an FPV at a position. Every acoustic FPV range below is a maker's claim, except the lab and field studies, which used quieter consumer drones.
> - **Zvook NW0 now has a public price: about $834–950 per sensor**, plus 15–18 W of power that the price doesn't include. **We are about 3–50x cheaper per sensor**: $17–50 per tripwire listener, about $125–300 per hand-placed node. We also need no mains or solar power. Cost per *position* depends on real range, which nobody has measured for either of us.
> - **A ~$211 LoRa acoustic module is now listed** (DroneAlert). Our hand-placed node is not cheaper than it; our throwaway listener is about 4–12x cheaper. See [Build or scrap?]({{ site.baseurl }}{% link research/build-or-scrap.md %}).
> - **The one measured cheap-microphone range is about 160–200 ft** (consumer drone, windy field). Our planning figure of 330–980 ft is unproven, and T11 decides it.

</details>

<details class="layer" id="the-priority-list" markdown="block">
<summary><span class="layer-title">The priority list</span><span class="layer-sub">Every competitor ranked: cost, what it achieves at a position, evidence, what it means for us</span></summary>

Ranked by how much each matters to us: how directly it competes for the job, and how much it achieves per dollar. Prices in hryvnia are converted at 45 UAH to the dollar (NBU rate, Oct 2026).

| # | Who | Cost | What it achieves at a position | Evidence | What it means for us |
|:-:|---|---|---|---|---|
| 1 | **A soldier's own ears** | $0 | Hears a drone close in; troops already hide when they do | Lab and field studies on consumer drones only ([below](#what-is-actually-measured)) | **The baseline to beat.** On consumer drones it's weak; for FPVs in combat, unmeasured |
| 2 | **Radio detector** (Chuyka 3.0) | **$584–701** each | Warns of radio-controlled FPVs up to 2.5 mi (claimed). Blind to fiber-optic | Strong demand: the most-requested e-point item, per the maker | **Partner, and the price anchor.** We're the second box beside it |
| 3 | **Zvook NW0** (Ukraine) | **$834–950** per sensor, plus a 15–18 W power supply. Zvook advises 1,300–2,000 ft spacing, based on its own claimed range | Claimed 490–1,500 ft, 360°, fiber-optic included. Needs 15–18 W from mains, 12–48 V DC or solar | Maker's claims only. On public sale | **The direct competitor.** Same price as a Chuyka, already on sale |
| 3a | **DroneAlert** (Ukraine, sold by Flash Army) | **~$211** per module (9,500 UAH), gateway ~$56; 3-module kit ~$670 | Claimed 390 ft radius with a bearing, up to 500 h on a 3.7 V battery, LoRa up to 6.2 mi, IP55. Fiber-optic not mentioned | Seller's claims only. Out of stock, no maker named, no reviews ([Flash Army](https://flasharmy.com.ua/dronealert-lora-merezha-akustychnyi-modul-vyiavlennia-droniv)) | **Our architecture, already listed.** Our listener is ~4–12x cheaper; our hand-placed node is not. Buy a kit to test beside ours |
| 3b | **VolAnti** (UK, open source, one student's project) | **£50–80** a unit (about $65–105), £35–45 on a breadboard; the design is free to build | Four summed mics, local alarm, LoRa alerts between units, a bq24074 charger like our dart's. Hunts propeller harmonics, so fiber-optic FPVs included. No bearing: its 3.1 in board is too small | **Author's test: 340 ft** on a hovering quad in light wind on a busy street. Nine units sent to an unnamed site, Sep 2026 ([our notes]({{ site.baseurl }}{% link research/open-source-builds.md %}#volanti), [Circuit Digest, Sep 2026](https://circuitdigest.com/news/volanti-an-open-source-esp32-s3-device-that-detects-fibre-optic-drones-with-no-rf-control-link-using-sound)) | **A free design anyone can build at listener price.** It sits at the position, so seconds of warning, and its author won't make it for any military. Its range figures are our best anchor |
| 4 | **RADD GLADIUS** (US) | Not published | Soldier-worn, about a week on a battery, alerts over a mesh to a squad leader and TAK | "100%" of drones in range, best about 1,600 ft, at a US Army exercise: **maker's account** | **The second direct competitor**, with US Army access. One sensor per soldier, so no forward reach |
| 5 | **Komodo "star"** (Denmark) | Not published | 8-mic sensor; the star variant **can be dropped by drone**, with shorter range | Maker says Shahed detections in Ukraine; no FPV figure | **The nearest thing to our tripwire.** Proof the idea isn't new, and a reason to move fast |
| 6 | **Fiber catchers and nets** (Zvook "Shipshyna") | **~$3,470** per 1,600–2,000 ft of perimeter | A timer-driven spinning barbed-wire unit snags and cuts the fiber. No warning | Maker's claims | **Competes for the same budget.** Sold alongside NW0, which can trigger it |
| 7 | **Russian and Belarusian acoustic detectors** | Not published | Phone, helmet and dugout units at the position. Belarus's SKANER 2.1 claims 330–980 ft against FPVs, fiber-optic included, 2.6 lb, 12 h ([Militarnyi, May 2026](https://militarnyi.com/uk/news/bilorus-predstavyla-akustychnyj-radar-skaner-2-1-dlya-vyyavlennya-fpv-droniv-na-optovolokni/)) | Claimed 460–820 ft, 230–330 ft in strong wind | **The other side uses the idea too.** The only published range-against-wind figures |
| 8 | **Other new entrants** | ZVOOK Tracking ~$2,670; others not published | Arcani HARK (UK) for FPVs, Ukraine test planned May 2026 ([Janes](https://www.janes.com/osint-insights/defence-news/c4isr/arcani-plans-to-test-hark-acoustic-sensor-in-ukraine)); Neuron Soundware Sound Shield (Czechia), under 1 W, reported €100–150 production cost, for borders ([dev.ua](https://dev.ua/news/sound-shield-1781192277)) | Claims only; no results found | **The field is filling up.** Nobody sells forward lines |

Everything else is either in the other market or out of reach for a platoon: see [Not our competitors](#not-our-competitors).

**What the list says (inference):**
- **Per sensor we are much cheaper than NW0.** An NW0 is $834–950, plus the power it needs. A tripwire listener is $17–50 (estimate) and a hand-placed node about $125–300 (a $1,500–2,500 kit of 8–12 nodes, local fusion included). That is roughly 3–50x less.
- **Per position, nobody knows yet.** It depends on real range. Comparing NW0 at its claimed 1,500 ft with us at our cautious measured range would make NW0 look cheaper; that is a best case against a worst case. At equal range we are cheaper per position too. T11 and any independent NW0 test decide the real figure.
- **What NW0 and RADD can't do is reach forward.** NW0 needs 15–18 W and a link, so it lives at a post. RADD is worn. Neither is laid a mile out, which is where a minute of warning comes from.
- **Komodo's star variant shows that dropping sensors by drone works as a product idea.** It's sold for Shaheds and long range, not as cheap FPV lines.

</details>

<details class="layer" id="what-is-actually-measured" markdown="block">
<summary><span class="layer-title">What is actually measured</span><span class="layer-sub">Every range figure we found, sorted by how much it can be trusted</span></summary>

Range decides warning time and how many sensors a line needs. Here is every figure we found, sorted by how much it can be trusted.

| Source | Drone | Sensor | Range | Kind |
|---|---|---|---|---|
| Li et al., *Applied Sciences* 2020 | DJI Mavic Air hovering at 130 ft, 52 dB background | **24 people listening** | At 490 ft, 2 of 24 heard it faintly; at 820 ft and beyond, nobody. All saw it first (50% at 1,000 ft) | **Measured** |
| Ghouli, *Acta Acustica* 2026 | DJI Phantom, coastal field | **8 cheap MEMS mics** (INMP441) on an ESP32-S3 | 91.6% accuracy to about 160 ft; effective range about 200 ft; 5–8% false positives | **Measured**, small test |
| Jekateryńczuk & Piotrowski, *Sensors* 2025 | A speaker playing a 1 kHz tone, not a drone | Studio and shotgun mics | 230–310 ft in low wind; 120–150 ft in high wind | **Measured**, tone only |
| VolAnti (open source) | Hovering quad, street with traffic, light wind | Four cheap mics, summed | 340 ft | Author's test |
| Kudriashov et al., *Sensors* 2020 | Phantom 4 and larger | 30-mic MEMS array | Tested to 1,200 ft; about 490 ft for small drones | **Measured**, expensive array |
| Pobeditel (Russia), via TASS | Light FPV and Mavic at 160 ft altitude | Phone mic | 460 ft hovering, 820 ft moving; 230–330 ft in wind above 22 mph | Maker's claim |
| Zvook NW0 | FPV, fiber-optic included | Unknown | 490–1,500 ft | Maker's claim |
| ARes (Ukraine) | FPV | Phased array, ~$10k | 660–980 ft | Maker's claim |
| RADD GLADIUS | 6- and 8-rotor quads | Soldier-worn | Best about 1,600 ft | Maker's account of a US Army exercise |
| NATO ACT challenge, 2025 | 7–10 inch FPV, 6.6–8.8 lb | Any | **Requirement:** 980 ft minimum, 1,600 ft target, night and bad weather | What NATO asks for |

**What this means:**
- **No study has flown an FPV at distance.** Every measured result uses a consumer drone or a tone. FPVs are probably louder, but nobody has measured by how much (reports disagree on whether fiber-optic FPVs are louder).
- **The soldier's ear is weaker than we feared** in quiet conditions: people heard a Mavic-class drone faintly at 490 ft and not at all at 820 ft. A cheap microphone heard a Phantom to about 200 ft. At the position, ears and a cheap microphone may be roughly even. Forward placement is what beats the ear.
- **Wind halves range** in every source that measured it.
- **The ICMCIS 2026 paper by Zvook staff** used real front-line recordings, including FPVs, and reached an F1 score (accuracy balancing misses and false alarms) of 78.6–82.2%. It has no distance labels, so it says nothing about range. It does show real front-line noise is the hard part.
- **A Brave1 trial** of about two dozen acoustic and optical makers against fiber-optic drones (Snake Island Institute, Third Army Corps, AB3.Tech) found acoustic range of up to several hundred yards, depending on system size. Wind and rain hurt it, and sounds like mowers, vehicles and voices overlap. No results by product were published.

So **T11, our own range test with a real FPV, is the most valuable test on the site.** If cheap listeners hear an FPV at only 160–200 ft, a 1.9 mi line needs about 30 of them, not 12 ([tripwire]({{ site.baseurl }}{% link models/tripwire.md %})).

</details>

<details class="layer" id="two-markets-only-one-of-them-ours" markdown="block">
<summary><span class="layer-title">Two markets, only one of them ours</span><span class="layer-sub">Rear-area air defence against protecting front-line positions</span></summary>

"Acoustic drone detection in Ukraine" covers two jobs. Reporting, including the US Army's own review, blurs them.

| | Rear-area air defence | Protecting front-line positions |
|---|---|---|
| **Threat** | Shaheds and cruise missiles: loud, slow, flying across the country | FPVs, including fiber-optic: quiet, fast, final 0.6–1.2 mi |
| **Acoustic players** | Sky Fortress, Zvook stations, FENEK, Komodo, ARes; city perimeters (Vidar, Soloma) | Zvook NW0, RADD, Russian equivalents |
| **Evidence it works** | Yes: reported by US commanders and Ukrainian press, though never independently tested | **None found** |
| **Who buys** | The state, cities, at scale | Units, volunteers, Brave1 Market |
| **Us** | Not our market | **The gap** |

**The US Army review doesn't close the gap.** "Listening to the Sky" (CALL, March 2026) says Ukrainian acoustic networks detect FPVs. It's a 12-page desk review citing news articles and company sites. Its Sky Fortress and Zvook sources are about Shaheds and cruise missiles, and its FPV range figure cites a vendor page that now redirects elsewhere ([CALL](https://api.army.mil/e2/c/downloads/2026/04/30/af450e75/no-26-1115-listening-to-the-sky-acoustic-drone-detection-in-ukraine-mar-26.pdf)).

</details>

<details class="layer" id="the-direct-competitors" markdown="block">
<summary><span class="layer-title">The direct competitors</span><span class="layer-sub">Zvook NW0, RADD GLADIUS, Komodo and the Russian equivalents</span></summary>

### Zvook NW0 — direct competitor, claims only

- **What it is:** an acoustic FPV sensor for positions, frontline towns and logistics routes, announced January 2026 ([Militarnyi](https://militarnyi.com/en/news/ukraine-develops-acoustic-detector-for-fpv-drones/)).
- **On sale** at MAMO, a Ukrainian online shop. Three versions are listed: Ethernet 37,550 UAH, LTE 40,196 UAH, LoRa 42,757 UAH, so about **$834–950** ([MAMO](https://mamo.com.ua/akustychnyj-sensor-zvook-nw0-lte-vyyavlennya-fpv-droniv-za-zvukom-iz-peredacheyu-danyh-po-lte/)).
- **Claimed:**
  - 490–1,500 ft and 360°, fiber-optic FPVs included.
  - 15–18 W, from mains, 12–48 V DC or solar panels.
  - IP67 (dust-tight and waterproof).
  - An optional siren, plus a live map of tens to hundreds of sensors.
  - It integrates with EW and with fiber-catching barbed-wire units.
- **Spacing:** Zvook advises 1,300–2,000 ft between sensors.
- **Not found:** an independent test, or any unit reported using it. Zvook's own vehicle sensor trial at NATO's BATT26 exercise "worked. Not perfectly", by Zvook's account.
- **Plausibility (inference):** 490 ft is in line with measured results. 1,500 ft is above anything measured with a cheap sensor.
- **It can report by wire.** The Ethernet version, and the fiber and twisted-pair links Zvook's maker describes, can't be jammed ([dev.ua](https://dev.ua/en/news/ukrainska-kompaniia-zvook-stvoryla-akustychnyi-sensor-dlia-vyiavlennia-fpv-droniv-za-zvukom-1769187556)). Our darts rely on radio, which jammers on both sides cover ([jamming]({{ site.baseurl }}{% link models/line-layout.md %}#jamming)).
- **On roads it is the direct rival to our posts.** A wired line of NW0s every 1,300–2,000 ft along a road is what our [road guard]({{ site.baseurl }}{% link models/route-guard.md %}) does with its posts, at about $49 a post against $834–950. What NW0 lacks is the fence a mile out that gives the minute.
- **Where we differ:**
  - We run for weeks on a battery, not 15–18 W.
  - Our listeners are cheap enough to lose.
  - We lay a row about a mile forward instead of placing sensors at the post.
  - Per sensor we cost roughly 3–50x less, and need no power supply.

### RADD GLADIUS — soldier-worn, US

- **What it is:** a TurbineOne spin-out that came out of stealth in March 2026 ([Tectonic](https://www.tectonicdefense.com/exclusive-acoustic-drone-sensing-startup-radd-emerges-from-stealth/)). It's pitched squarely at fiber-optic FPVs.
- **Claimed:**
  - The prototype is tissue-box size. The goal is personal-radio size, about 20% lighter than a rifle magazine.
  - About a week on a battery.
  - Alerts go over a mesh to a node with the squad leader, and into TAK.
- **Tested** at the US Army's EXTiC 26-01 exercise in New Mexico, with DIU and CENTCOM. The founders say it detected every drone that came in range, the farthest pushing 1,600 ft. Targets were 6- and 8-rotor quads. No false-alarm figure or flight count is given, and the article is an "exclusive" based on the founders' account.
- **Not found:** a price or a customer. It's in talks for low-rate production.
- **Where we differ:** one sensor per soldier gives no reach beyond the soldier. Lines laid forward give earlier warning. We could feed the same TAK picture.

### Komodo — the drone-dropped sensor already exists

- **What it is:** an 8-microphone passive sensor from Bionic System Solutions (Denmark), developed with Danish Defence. It comes as a pole on a tripod or as a **"star" variant that drones can drop in remote places, with shorter range** ([Defence-Network, Aug 2025](https://defence-network.com/dalo-passives-c-uas-system-aus-daenemark/)).
- **Claimed:** up to 3.1 mi on drones. The maker says it's in use in Ukraine and detected two Shaheds in July 2025. It took part in NATO trial SET-348 in Denmark, with no published metrics ([Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/komodo-acoustic-c-uas-tested-at-nato-trial-in-denmark/)).
- **Not found:** a price, power figures, or any FPV result.
- **Where we differ:** Komodo sells a capable 8-mic sensor for Shaheds and artillery. We sell cheap single-mic listeners in lines, for FPVs. If Komodo built cheaper star variants for FPVs, it would compete head-on.

### Russian equivalents

- **Pobeditel training centre:** a phone-based acoustic detector. It claims 460 ft against a hovering FPV and 820 ft against a moving one at 160 ft altitude, falling to 230–330 ft in wind above 22 mph. It can't yet tell a Mavic from an FPV. Networked phones give a rough bearing ([CNews/TASS, Sep 2025](https://www.cnews.ru/news/top/2025-09-11_v_rossii_sozdali_detektor)).
- **Farvater "1K"** is helmet-worn, and **Malik** comes in dugout and body-armour versions. Both are prototypes with claimed ranges only.
- **Why it matters:** the other side is building the same thing, and its published wind figures match the Western studies.

</details>

<details class="layer" id="partners-and-the-budget-we-compete-for" markdown="block">
<summary><span class="layer-title">Partners and the budget we compete for</span><span class="layer-sub">Radio detectors, fiber catchers, jammers we could cue, and how units buy with e-points</span></summary>

- **Radio detectors.** Chuyka 3.0 costs $701 with VAT, or $584 for defence buyers. It weighs up to 1.4 lb and runs up to 6 h, with sound and light alerts ([BlueBird](https://blue-bird.tech/en/products/chuyka-3-0/)). Its maker calls it the most-requested item units buy with e-points ([Militarnyi, Jan 2026](https://militarnyi.com/uk/news/dron-detektor-chujka-3-0-zrobyly-dostupnym-za-e-baly/)). Units carry several kinds, and none hears fiber-optic drones. **We sell beside it.**
- **Fiber catchers.** Zvook's Shipshyna kits cost 156,357–379,401 UAH ($3.5–8.4k). The top kit adds sensors and server control ([MAMO](https://mamo.com.ua/kompleks-shypshyna-zahyst-vid-optovolokonnyh-fpv-droniv-komplektacziya-a/)). Nets and cable traps are everywhere. They need no warning, so they compete for money, not for the job.
- **Jammers we could cue: CERBAIR MEDUSA (France).** A radio and GNSS jammer for protected sites. It is built to be switched on automatically by an outside detector: today CERBAIR's own HYDRA radio detector, over Gigabit Ethernet, with "smart mode" jamming only the threatened band. MEDUSA 100 claims a 0.6 mi average range and weighs 71 lb; MEDUSA 200 claims 1.2 mi at 88 lb. It jams 2.4 and 5.8 GHz, GNSS and optionally 433/900 MHz at 35–140 W per band, runs on 10–32 V DC, and works by triggering the drone's own fail-safe ([spec sheet, 2020](https://comsecfl.com/wp-content/uploads/2022/04/Specsheet_Medusa.pdf), maker's claims). **What our network could add (inference):** an acoustic cue hears any drone, whatever its radio link, so it could switch a jammer on only when something is actually inbound. That cuts the time a jammer transmits and gives itself away, and could cover drones HYDRA can't hear on radio. **Limits:** jamming still does nothing to a fiber-optic FPV, and CERBAIR does not publish whether MEDUSA accepts a third party's cue. **A possible partner component**, not a competitor. **But jamming is losing ground at the front:** a brigade EW commander says "Jamming no longer works" ([Euromaidan Press, Jun 2025](https://euromaidanpress.com/2025/06/26/is-the-electronic-warfare-era-over-a-frontline-ew-officers-story-of-ukraines-drone-tug-of-war)), so this pairing is a fading benefit ([what troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})).
- **How units buy.** Units earn e-points for confirmed hits and spend them on the Brave1 Market. Orders go through DOT-Chain Defence and arrive in about 10 days ([MoD](https://mod.gov.ua/en/news/how-the-military-can-obtain-equipment-through-dot-chain-defence-under-the-army-of-drones-bonus-program-step-by-step-guide)). Being listed isn't enough. One EW maker says only about 7% of Ukrainian EW listed there can be bought with e-points. Volunteer appeals fund single devices: one battalion asked for a Chuyka plus antenna at 35,200 UAH ([Mezha](https://mezha.ua/en/blogs/pidtrimayte-zbir-na-pristriy-rer-chuyka-3-0-dlya-zsu-306257/)).

</details>

<details class="layer" id="not-our-competitors" markdown="block">
<summary><span class="layer-title">Not our competitors</span><span class="layer-sub">Systems for the rear, too dear for a platoon, or deaf to fiber-optic drones</span></summary>

They serve the rear, cost too much for a platoon, or don't hear fiber-optic drones. Several are systems to **feed data into** later.

| Who | What | Cost | Why not ours |
|---|---|---|---|
| Sky Fortress, Zvook stations, FENEK (Ukraine) | National acoustic networks | Sky Fortress $400–1,000 per sensor | Built for Shaheds and cruise missiles over the rear ([Defense One](https://www.defenseone.com/defense-systems/2024/07/ukraines-cheap-sensors-are-helping-troops-fight-waves-russian-drones/398204/)) |
| Vidar Systems, Soloma (Ukraine) | City perimeters, e.g. Sumy | $230–575k for 20 mi (Vidar); $466k for 56 sensors (Soloma) | City-scale; Soloma needs 1–2 weeks of retraining per site ([Tsukr, Jul 2026](https://cukr.city/city/2026/iak-vyiavyty-fpv-drony-na-optovolokni-v-sumakh/)) |
| ARes (Ukraine) | Phased array for mobile fire groups and ground robots | ~$10k | Claimed FPV range 660–980 ft; mainly Shaheds ([Oboronka](https://oboronka.mezha.ua/en/ares-sistema-dlya-viyavlennya-shahediv-fpv-droniv-306793/)) |
| Squarehead, Microflown (Europe) | Premium acoustic arrays | High, through prime contractors | Several hundred yards; one big sensor, not many cheap ones |
| Anduril WISP, Pulsar, Lattice | Infrared camera, RF, fusion | Six to seven figures per site | Not at the front; needs line of sight. **Lattice is a target to feed** |
| Echodyne and other radars | Small radar | $40–160k | Emits, so the enemy can find it; needs line of sight |
| Surtr (US) | Fusion software for acoustic and optical sensors | Not published | Tested by Brave1 ("good technological maturity"). **A possible partner** |
| Heaviside MOTH, MyDefence Wingman (US/Denmark) | Body-worn RF detectors for the US Army | MOTH under $5k ([Tectonic](https://www.tectonicdefense.com/heaviside-wins-99m-us-army-idiq-for-body-worn-drone-detector/)); Wingman kits with jammer about $54k each ([Euro-SD](https://euro-sd.com/2026/03/articles/armed-forces/49834/infantry-portable-anti-drone-options/)) | Radio only, so blind to fiber-optic |

</details>

<details class="layer" id="ideas-worth-borrowing" markdown="block">
<summary><span class="layer-title">Ideas worth borrowing</span><span class="layer-sub">Feed existing alarms, trigger something physical, train on front-line noise, publish false alarms</span></summary>

- **Feed the alarm into what units already use:** a siren plus a live map (NW0), and TAK (RADD). RUSI proposes a simple "warning indicator" flag on the company radio net, not audio ([RUSI, Oct 2024](https://afghanistan.wilsoncenter.org/sites/default/files/media/uploads/documents/protecting-the-force-from-uncrewed-uas.pdf), p.32).
- **Trigger something physical.** NW0 can start fiber catchers and EW. A tripwire alert could do the same.
- **Train on front-line noise, and split recordings by site and time** so tests aren't fooled (Zvook's ICMCIS paper). Soloma retrains for 1–2 weeks per site.
- **Publish a false-alarm rate.** RUSI says warning only helps "with a sufficiently low false-positive rate". Nobody publishes one for FPVs. Ghouli's 5–8% shows how high it can run.
- **Copy the fair test designs:**
  - *Sensors* 2025 used a calibrated speaker as a repeatable target.
  - Li 2020 used a listener protocol we can run with soldiers.
  - Poland tested seven acoustic systems side by side at Ustka in April 2026. No results are public yet.
- **Price and sell like Chuyka:**
  - A defence price without VAT, with an end-user certificate.
  - A Brave1 Market listing, then e-point eligibility.
  - A single-device price a volunteer appeal can cover.
- **Copy the drill.** The US Army training centre's "react to UAS" drill runs detect, warn, conceal, break contact ([JMRC, 2025](https://juniorofficer.army.mil/defeating-the-drone-from-jmrcs-skynet-platoon/)). RUSI says smoke works "if the unit… can be warned promptly". Design the alert around one drill.

</details>

<details class="layer" id="how-to-position" markdown="block">
<summary><span class="layer-title">How to position</span><span class="layer-sub">Front-line positions, beside the radio detector; lead on price with the listener</span></summary>

**On the market:** front-line positions facing FPVs, not rear-area air defence. The bar is a soldier's ears, and the product to sit beside is the radio detector.

**On price:** we are much cheaper per sensor than NW0 ($17–50 or about $125–300 against $834–950, plus its power). Say so, with the numbers. Against DroneAlert (~$211), only the throwaway listener is cheaper, so lead with the listener. Don't claim a cost per position until range is measured, for us or for NW0. Price a single listener so a volunteer appeal can cover a line, like a radio detector.

**On capability**, what neither NW0 nor RADD offers:
1. **Weeks on a battery, no wire.** It can sit anywhere, including where nobody can run power.
2. **Placed forward.** A row about a mile out gives about a minute of warning. A sensor at the post gives seconds: about what a sentry's ear gives if its range is near the measured figures, somewhat more if NW0's claimed 1,500 ft holds (an inference).
3. **Throwaway.** Losing a listener costs $17–50.
4. **Passive at the unit:** nothing there transmits.

**On integration:** be a sensor, not a platform. Output to TAK, SAPIENT and Lattice, and trigger what's already there: sirens, fiber catchers, turrets.

**One-line positioning:**
> *An acoustic alarm for front-line positions that hears the FPVs radio detectors can't, especially fiber-optic ones, laid out where the warning is earliest: the second box next to the radio detector.*

**Cost honesty:**
- Per sensor we are roughly 3–50x cheaper than NW0, and it also needs 15–18 W of power. Per position is open until range is measured on both sides.
- The tripwire is a consumable, with an estimated $3–5k a year in re-lays, with a solar panel on every dart ([estimate]({{ site.baseurl }}{% link models/tripwire.md %}#the-running-cost-lines-are-ammunition)). Quote both numbers.

</details>

<details class="layer" id="risks-to-this-positioning" markdown="block">
<summary><span class="layer-title">Risks to this positioning</span><span class="layer-sub">Short mic range, NW0 already on sale, no moat in the architecture, jamming</span></summary>

- **Short cheap-mic range.** The one measured cheap-microphone figure is about 160–200 ft. If FPVs aren't much louder, lines need two to three times as many listeners. T11 decides.
- **NW0 is already on sale at a radio detector's price** (plus its power supply). If it works, units may not want a second acoustic product. Possible answers: we become NW0's forward layer, or we partner with Zvook.
- **The architecture is no moat.** DroneAlert already sells LoRa acoustic modules on a battery at ~$211. If its price falls to listener level, only drone-laying, data and fielding set us apart.
- **The radio link home gets jammed.** Common Russian jammers cover 100 MHz–1.1 GHz, and a LoRa-hunting prototype ("Tishina") is described ([Armada, Sep 2026](https://www.armadainternational.com/2026/09/russia-tishina-software-defined-jammer-electronic-warfare/)). On our [estimate]({{ site.baseurl }}{% link models/line-layout.md %}#jamming) a jammer near the ground blinds a dart only within a few hundred feet, but about a mile in the worst case. A wired NW0 has no such risk. Test T19 decides.
- **Komodo or RADD go cheap and forward.** Komodo already drops sensors by drone, and RADD has US Army access. Our defence is speed and cost per listener.
- **A listening sentry or an AI turret is good enough at the position.** Turrets that carry their own sensor are in more than 10 units ([what troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})). Then only forward placement pays.
- **Warning may not change much.** No source measures what warning saves. Our central guess is about 1–4 of every 100 drone casualties averted, range 0.3–14 ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})). RUSI's brigades report about half of casualties in the rear, during rotation and resupply ([RUSI, Feb 2025](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)). A sensor at the position misses those. A [guard along the road]({{ site.baseurl }}{% link models/route-guard.md %}) would not, on our model.
- **No moat in hardware.** The lasting advantage is front-line training data and fielded integrations.

</details>

<details class="layer" id="sources" markdown="block">
<summary><span class="layer-title">Sources</span><span class="layer-sub">Every source on this page</span></summary>

**Research and reviews**
- [Li, Sun & Li — line-of-sight and hearing of a small drone, *Applied Sciences* 2020](https://www.mdpi.com/2076-3417/10/16/5501)
- [Ghouli — low-cost MEMS array drone detection, *Acta Acustica* 2026](https://acta-acustica.edpsciences.org/articles/aacus/full_html/2026/01/aacus250134/aacus250134.html)
- [Jekateryńczuk & Piotrowski — microphones for drone detection, *Sensors* 2025](https://www.mdpi.com/1424-8220/25/22/7057)
- [Kudriashov et al. — MEMS array drone detection, *Sensors* 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7506852/)
- [Tejera-Berengue et al. — audibility vs machine detection, Forum Acusticum 2025](https://dael.euracoustics.org/confs/fa2025/data/articles/000072.pdf) (modelled, not measured)
- [Vilhurin, Sydorskyi & Shevtsov — front-line acoustic detection, ICMCIS 2026](https://arxiv.org/abs/2608.14287)
- [Watling & Bronk — Protecting the Force from Uncrewed Aerial Systems, RUSI, Oct 2024](https://afghanistan.wilsoncenter.org/sites/default/files/media/uploads/documents/protecting-the-force-from-uncrewed-uas.pdf)
- [Watling & Reynolds — Tactical Developments During the Third Year, RUSI, Feb 2025](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)
- [CALL — Listening to the Sky (Mar 2026)](https://api.army.mil/e2/c/downloads/2026/04/30/af450e75/no-26-1115-listening-to-the-sky-acoustic-drone-detection-in-ukraine-mar-26.pdf)
- [JED — NATO ACT challenge for fiber-optic FPV detection (May 2025)](https://www.jedonline.com/2025/05/15/nato-seeks-solutions-for-fiber-optic-fpv-drones/)
- [Oboronka — Brave1 trial of anti-fiber-optic systems (Jun 2026)](https://oboronka.mezha.ua/en/inzheneri-zasobi-proti-bezpilotnikiv-na-optovolokni-312791/)

**Competitors and prices**
- [MAMO — Zvook NW0 listings](https://mamo.com.ua/akustychnyj-sensor-zvook-nw0-lte-vyyavlennya-fpv-droniv-za-zvukom-iz-peredacheyu-danyh-po-lte/) and [Shipshyna](https://mamo.com.ua/kompleks-shypshyna-zahyst-vid-optovolokonnyh-fpv-droniv-komplektacziya-a/)
- [Militarnyi — Zvook NW0 (EN)](https://militarnyi.com/en/news/ukraine-develops-acoustic-detector-for-fpv-drones/) and [(UK)](https://militarnyi.com/uk/news/v-ukrayini-stvoryly-akustychnyj-detektor-fpv-droniv/)
- [Tectonic — RADD emerges from stealth (Mar 2026)](https://www.tectonicdefense.com/exclusive-acoustic-drone-sensing-startup-radd-emerges-from-stealth/)
- [Defence-Network — Komodo variants (Aug 2025)](https://defence-network.com/dalo-passives-c-uas-system-aus-daenemark/) and [Unmanned Airspace — SET-348](https://www.unmannedairspace.info/counter-uas-systems-and-policies/komodo-acoustic-c-uas-tested-at-nato-trial-in-denmark/)
- [CNews/TASS — Pobeditel acoustic detector (Sep 2025)](https://www.cnews.ru/news/top/2025-09-11_v_rossii_sozdali_detektor)
- [Tsukr — acoustic perimeters in Sumy (Jul 2026)](https://cukr.city/city/2026/iak-vyiavyty-fpv-drony-na-optovolokni-v-sumakh/)
- [Oboronka — ARes](https://oboronka.mezha.ua/en/ares-sistema-dlya-viyavlennya-shahediv-fpv-droniv-306793/)
- [BlueBird — Chuyka 3.0](https://blue-bird.tech/en/products/chuyka-3-0/); [Militarnyi — Chuyka on e-points](https://militarnyi.com/uk/news/dron-detektor-chujka-3-0-zrobyly-dostupnym-za-e-baly/); [Mezha — Chuyka appeal](https://mezha.ua/en/blogs/pidtrimayte-zbir-na-pristriy-rer-chuyka-3-0-dlya-zsu-306257/)
- [MoD — DOT-Chain Defence and e-points](https://mod.gov.ua/en/news/how-the-military-can-obtain-equipment-through-dot-chain-defence-under-the-army-of-drones-bonus-program-step-by-step-guide)
- [Tectonic — Heaviside MOTH](https://www.tectonicdefense.com/heaviside-wins-99m-us-army-idiq-for-body-worn-drone-detector/); [Euro-SD — infantry anti-drone options](https://euro-sd.com/2026/03/articles/armed-forces/49834/infantry-portable-anti-drone-options/)
- [Defense One — Sky Fortress (Jul 2024)](https://www.defenseone.com/defense-systems/2024/07/ukraines-cheap-sensors-are-helping-troops-fight-waves-russian-drones/398204/); [TWZ (Jul 2024)](https://www.twz.com/air/ukraines-acoustic-drone-detection-network-eyed-by-u-s-as-low-cost-air-defense-option); [FENEK](https://fenek.com.ua/en/)
- [DefenseScoop — Anduril $20B Army contract](https://defensescoop.com/2026/03/14/anduril-20-billion-dollar-army-contract/); [Hvylya — Echodyne prices](https://en.hvylya.net/news/1263-bill-gates-backed-radar-firm-claims-10x-cost-edge-over-traditional-air-defense); [Hensoldt — Squarehead in Xpeller](https://hensoldt.net/news/hensoldt-expands-xpeller-counter-uav-product-family); [Unmanned Airspace — Microflown AVISA](https://unmannedairspace.info/?p=17423)
- [NBU exchange rate, 14 Oct 2026](https://kurs.com.ua/en/novost/1483853-dolar-znovu-perevishiv-45-griven-oficiini-kursi-nbu-na-14-zhovtnja)

</details>
