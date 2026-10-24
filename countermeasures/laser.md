---
title: The laser
nav_counter: 3
---

# The laser
{: .no_toc }

<p class="vz-lede">Can a laser burn through a fiber FPV's line "for just a moment"? <strong>Only a strong one, held on a spot you already know.</strong> A fiber is hair-thin, so most of the beam misses it, and it lies slack, so nothing snaps it once the coating is burned off: the beam has to melt the glass. The case that works is <strong>a drone parked by a road</strong>. You can see it, so a beam traced in a loop around it has to cross its line.</p>

<figure class="vz-figure vz-narrow">
<svg viewBox="0 0 480 360" role="img" aria-labelledby="lz-hero-t">
  <title id="lz-hero-t">Seen from above: a road with one of the road guard's posts beside it, carrying a laser. A drone has landed near the road to wait. Its fiber runs from it back to its pilot on the enemy side. The laser traces a loop around the drone, and the loop crosses the fiber, where it burns through.</title>
  <defs><marker id="lz-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#151515"/></marker></defs>
  <rect x="0" y="0" width="480" height="40" fill="#f3e1d8"/>
  <text x="14" y="27" class="vz-t-tag" style="font-size:15px">ENEMY SIDE · TO THE PILOT</text>
  <path d="M250 40 C 240 80, 262 120, 246 160 C 238 180, 250 196, 246 216" fill="none" stroke="#d2451e" stroke-width="2.5"/>
  <circle cx="246" cy="232" r="44" fill="none" stroke="#2f6b3a" stroke-width="2.5" stroke-dasharray="6 5"/>
  <g transform="translate(246 232)" stroke="#151515" stroke-width="2.5">
    <line x1="-11" y1="-11" x2="11" y2="11"/><line x1="11" y1="-11" x2="-11" y2="11"/>
    <g fill="#fff" stroke-width="2"><circle cx="-11" cy="-11" r="5"/><circle cx="11" cy="-11" r="5"/><circle cx="-11" cy="11" r="5"/><circle cx="11" cy="11" r="5"/></g>
  </g>
  <g stroke="#d2451e" stroke-width="3"><line x1="236" y1="180" x2="256" y2="196"/><line x1="256" y1="180" x2="236" y2="196"/></g>
  <text x="300" y="150" class="vz-t" style="font-size:15px">the loop has to</text>
  <text x="300" y="168" class="vz-t" style="font-size:15px">cross the line</text>
  <text x="300" y="230" class="vz-t-small" style="font-size:14px">waiting drone,</text>
  <text x="300" y="248" class="vz-t-small" style="font-size:14px">heard landing</text>
  <rect x="0" y="292" width="480" height="40" fill="#e6e3dc"/>
  <text x="14" y="317" class="vz-t-tag" style="font-size:14px">ROAD</text>
  <rect x="88" y="268" width="14" height="14" fill="#2f6b3a"/>
  <line x1="102" y1="272" x2="208" y2="214" stroke="#2f6b3a" stroke-width="1.5" stroke-dasharray="2 3"/>
  <text x="20" y="262" class="vz-t-small" style="font-size:14px">post + laser</text>
  <text x="14" y="352" class="vz-t-small" style="font-size:13px">not to scale · loop about 2 ft across · post up to 635 ft away</text>
</svg>
<figcaption>Seen from above. Red: the enemy's fiber. Green: our post and the beam's loop. The loop has to go round the whole drone, so the beam never touches the drone or its warhead.</figcaption>
</figure>

<div class="stats">
  <div class="stat"><p class="stat-num">0.1 J</p><p class="stat-label">to burn through each mm of line, at least: about half for the coating, half for the glass (our arithmetic)</p></div>
  <div class="stat"><p class="stat-num">~100 W</p><p class="stat-label">needed for "a fraction of a second": 0.04 s on a 0.08 in spot. A 10 W diode needs 0.4 s on the same spot (model)</p></div>
  <div class="stat"><p class="stat-num">40–200 s</p><p class="stat-label">for a 100 W beam to loop a parked drone from 100–635 ft. That's fine against a drone waiting for hours (model)</p></div>
  <div class="stat"><p class="stat-num">2/5</p><p class="stat-label">feasibility: the physics works up close; cutting at range, aiming, the fire risk and the eye risk are untested</p></div>
</div>

### What the pasted claim gets right and wrong

<div class="vz-cards vz-2">
  <div class="vz-card"><p class="vz-card-num">Right</p><p>A pointer or rangefinder does nothing to the line. Light shone on the side of a fiber can't get into its core to scramble the signal. And a strong enough beam does ruin a fiber.</p></div>
  <div class="vz-card"><p class="vz-card-num">Wrong</p><p>"Snaps under the tension of the drone pulling it." The line lies slack on the ground behind the drone. Burning off the coating leaves bare glass that still carries the signal, so the beam has to melt the glass. And "a moment" is only true for about 100 W held on a spot you already know.</p></div>
</div>

### Where it could fit

<div class="vz-cards vz-2">
  <div class="vz-card"><p class="vz-card-num">A drone waiting by a road</p><p><strong>The only case that works.</strong> The road posts hear it land. A camera on the post finds it, and the laser traces a 2 ft loop around it. The loop has to cross the line, and aim errors only bend the loop. It needs no fence wire, and the beam never touches the warhead. A video from March 2026 seems to show exactly this.</p></div>
  <div class="vz-card"><p class="vz-card-num">A drone flying in</p><p><strong>No.</strong> No camera can see a line 0.01 in wide in the air or on the ground at range, so there is nothing to aim at. The <a href="{{ site.baseurl }}{% link countermeasures/fiber-cutter.md %}">fiber cutter</a> needs no aiming, and stays the answer for this case.</p></div>
</div>

<p class="vz-done"><span class="vz-chip vz-chip-open">model</span> energy, dwell, spot and loop times from <a href="https://github.com/paulrenzi/tripwire/blob/main/tools/lasermodel/laser_model.py"><code>laser_model.py</code></a>, ignoring heat loss, so every time is a lower bound · <span class="vz-chip vz-chip-open">unverified</span> the March 2026 video, and every laser price · <span class="vz-chip vz-chip-open">est.</span> the post laser is a design, not priced from quotes</p>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">The whole page in seven bullets</span></summary>

- **A laser can ruin the line, but not "for just a moment" unless it is strong and well aimed.** A 100 W beam on a 0.08 in spot needs about 0.04 s. A 10 W blue engraving diode on the same spot needs about 0.4 s, and 10 s on a 0.4 in spot (model, a lower bound).
- **Nothing snaps the line.** It lies slack, so the beam has to burn off the coating and then melt the glass.
- **Seeing the line is the hard part, and you can't.** It's 0.01 in wide. Ukraine's General Staff says the same of lasers against drones: the laser is easy, aiming it is hard.
- **A parked drone gets round that.** You can see the drone, and its line runs from it to its pilot. So a loop traced around it must cross the line. That takes a 100 W beam about 40 s from 100 ft and about 200 s from 635 ft, the farthest a landing can be from a road post (model).
- **A video from March 2026 seems to show this,** from Russian sources: a laser burning the line of a drone waiting by a road. Nobody has confirmed it.
- **A cheaper first step is blinding its camera.** A few watts from a $120 blue diode, focused by the drone's own lens, is above the reported damage level for a camera sensor (model). That is allowed against optics under the treaty on blinding lasers.
- **The risks are fire and eyes.** 100 W sets dry grass alight. A beam along a road is an eye hazard to our own troops and to anyone else on it.

1. TOC
{:toc}

</details>

<details class="layer" id="the-arithmetic" markdown="block">
<summary><span class="layer-title">The arithmetic</span><span class="layer-sub">How much energy it takes, and how long the beam has to stay on the line</span></summary>

**The line** is 0.01 in (0.25 mm) of acrylate coating over 0.005 in (0.125 mm) of glass. To burn through 1 mm of it, the beam has to:
- **burn off the coating:** heat it to about 500 °F, where acrylate breaks down ([patent on medical laser fibers](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10405923)), and break it down: about 56 mJ;
- **soften the glass:** heat it to about 2,900 °F: about 43 mJ.

**That's about 0.1 J for each mm, at least.** A line this thin loses heat fast, and that loss isn't counted, so every time below is a lower bound.

**Most of the beam misses.** A line 0.01 in wide catches only part of a round spot: 16% of a 0.08 in spot, 3% of a 0.4 in one. How much of what hits it is absorbed is the biggest unknown. We assume 30%.

| Laser | Spot | Line catches | Dwell | Fastest sweep |
|---|---|---|---|---|
| 10 W blue engraving diode, close up | 0.08 in | 16% | 0.41 s | 0.19 in/s |
| 10 W blue engraving diode, wide spot | 0.39 in | 3% | 10 s | 0.04 in/s |
| **100 W fiber laser, tight spot** | **0.08 in** | **16%** | **0.04 s** | **1.9 in/s** |
| 100 W fiber laser | 0.20 in | 6% | 0.26 s | 0.76 in/s |

So "a fraction of a second" holds only for about 100 W on a tight spot. Sweeping the beam across a field cuts nothing: it moves far faster than 2 in/s.

**Spot size at range.** Even a perfect beam from a 2 in lens spreads. A fiber laser (1 µm) makes 0.06 in at 100 ft and 0.19 in at 300 ft. A CO₂ laser makes 0.62 in and 1.9 in. Real beams are wider, and a cheap blue diode's much wider. That's why range costs so much time.

</details>

<details class="layer" id="which-laser" markdown="block">
<summary><span class="layer-title">Which laser</span><span class="layer-sub">What each kind of light does to the coating and the glass</span></summary>

- **Near-infrared fiber lasers (about 1 µm)** focus tightly and are made for industry. But the glass lets this light through, and so does clear coating. It heats only what's coloured or dirty, so absorption could be well under 30%. Test L1 measures it.
- **Blue diodes (445 nm)** are what cheap engravers use. A 10 W module costs about $120 ([eBay listing](https://www.ebay.de/itm/285749674639)), though sellers often overstate the power. Acrylate absorbs blue and violet light: there's a patented method for stripping fiber coating that way ([US9791624](https://patents.google.com/patent/US9791624)). But glass passes blue light, and the beam spreads too fast to use at range.
- **CO₂ lasers (10.6 µm)** are absorbed by the glass itself. That's how laser splicers melt fiber ([AFL LZM-100](https://www.aflglobal.com/en/Products/Fusion-Splicing/Specialty-Fusion-Splicing-Equipment/Splicers/LZM-100-LAZERMaster-Laser-Splicing-System)). But the spot is ten times wider at the same range, and the glass tube and water cooling are fragile in the field.

**Best bet: a 100 W fiber laser,** for its range, if L1 shows the coating absorbs enough. A CO₂ laser only if it doesn't.

</details>

<details class="layer" id="aiming" markdown="block">
<summary><span class="layer-title">Aiming: the loop around a parked drone</span><span class="layer-sub">Why a loop has to cross the line, and how long it takes</span></summary>

**The problem:** no camera sees a line 0.01 in wide in grass at range. Ukraine's General Staff says the hard part of a laser against drones is the guidance, not the laser ([LIGA](https://news.liga.net/en/politics/news/ukraine-is-working-on-means-to-counter-uavs-on-fiber-optics---source-in-the-general-staff)).

**The way round it** is the same reasoning as the fiber cutter's wire. The line runs without a break from the drone to its pilot. So **any closed loop around the drone has to cross it.** We don't need to see the line, only the drone. The beam traces a loop about 2 ft across, wide enough to clear a 7–10 in FPV and its arms. If the post sways, the loop bends, but it still goes round the drone. Knowing roughly where the pilot is, half a loop on that side is often enough, and halves the time.

**How long a full loop takes** with a 100 W fiber laser, at the slowest sweep that still burns through (model):

| From the post | Spot (perfect beam) | Sweep | Full 2 ft loop |
|---|---|---|---|
| 100 ft | 0.08 in | 1.9 in/s | 40 s |
| 300 ft | 0.19 in | 0.8 in/s | 95 s |
| 635 ft, the farthest a landing can be from a post | 0.40 in | 0.4 in/s | 200 s |

A drone waiting by a road can wait for hours, so minutes are fine. At 300 W, the 635 ft loop drops to about 70 s.

**What the post needs:**
- a camera to find the drone. The posts' microphones already say where it landed ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})).
- a rangefinder to focus the beam.
- a pan-tilt mount steady to about 0.1 in at the drone.
- its own battery. A 100 W fiber laser draws roughly 330 W, so a 200 s loop uses about 18 Wh, far beyond the post's four cells.

</details>

<details class="layer" id="reported-use" markdown="block">
<summary><span class="layer-title">Reported use</span><span class="layer-sub">The March 2026 video, and Ukraine's lasers</span></summary>

- **March 2026: a video from Russian sources** seems to show a laser burning the line of a Russian fiber FPV waiting by a road, after which the drone lost its link. It was shared on 10 March 2026. Ukraine's army has not confirmed it, and no laser, power, platform or range was given ([United24](https://united24media.com/es/latest-news/rusia-afirma-que-ucrania-utilizo-un-laser-para-quemar-el-cable-de-fibra-optica-de-un-dron-es-real-16707)). David Axe suggests an aerial laser may be sweeping roads for these drones, and says damaging the line is possible "only in certain cases" ([Trench Art](https://www.trenchart.us/p/is-ukraine-sweeping-roads-with-lasers)). That case fits this page's physics: a drone you can see, holding still.
- **Tryzub**, Celebra Tech's laser, is a different job: it burns the drone itself. Its maker claims FPV kills at 2,600–3,000 ft from a trailer. Its power isn't published ([TechSpot](https://www.techspot.com/news/112357-ukraine-testing-ai-guided-laser-weapon-can-destroy.html)). One expert guess put it at about 50 kW ([Espreso](https://global.espreso.tv/russia-ukraine-war-ukrainian-laser-weapon-tryzub-could-rival-us-and-uk-systems)). Cutting a parked drone's line takes about 100 W, a few hundred times less.

</details>

<details class="layer" id="blinding-the-camera" markdown="block">
<summary><span class="layer-title">The cheaper option: blinding its camera</span><span class="layer-sub">Why a few watts may be enough, and what it does and doesn't do</span></summary>

**A camera's own lens does most of the work.** It focuses whatever enters it onto a spot a few pixels wide. Say a cheap diode's beam is 0.8 in wide at 100 ft, and the FPV's lens is 3 mm. Then 1 W puts about 22 mW through the lens, about 29,000 W/cm² on the sensor; 5 W puts about 143,000 W/cm² (model, rough guesses for beam and lens). A colour camera sensor is reported to take damage at about 40,000–60,000 W/cm² in a quarter second ([laserpointersafety.com](https://laserpointersafety.com/ilda-camera-info-old.html), summarising [Schwarz et al., 2017](https://www.spiedigitallibrary.org/journals/Optical-Engineering/volume-56/issue-3/034108/Laser-induced-damage-threshold-of-camera-sensors-and-micro-optoelectromechanical/10.1117/1.OE.56.3.034108.full); not checked against the paper).

**So a $120, 5–10 W blue diode on the post may kill a waiting drone's camera.** The camera points at the road, so it often faces the post.

**What it does:** the pilot loses the picture and can't time the ambush. **What it doesn't:** the drone stays on its line, armed. The pilot can still fly it blind, or set it off where it sits. It's a cheap first step, not a kill. Test L3.

</details>

<details class="layer" id="cost" markdown="block">
<summary><span class="layer-title">What it would cost</span><span class="layer-sub">A rough price for a laser on a road post</span></summary>

All estimates. No quote was found for a 100 W continuous fiber laser, and the listings found disagree widely.

| Part | Each (est.) |
|---|---|
| 100 W continuous fiber laser source. Marketplace listings run $450–4,500 for sources of various powers ([Accio](https://www.accio.ai/find-supplier/raycus-source)); one vendor blog implies far more ([Alibaba blog](https://seller.alibaba.com/blogs/2026/southeast-asia/machinery/fiber-laser-cutting-machine-source-guide-alibaba-b2b)) | $1,500–4,500 |
| Pan-tilt mount, camera and rangefinder | $500–1,100 |
| A battery for about 330 W bursts, and its charger | $150–300 |
| Enclosure, output lens and window | $200–400 |
| **A laser post** | **$2,400–6,300** |
| *Or:* a 10 W blue diode on a small pan-tilt, for the camera only | *$200–400* |

**About 5 posts a mile of road** ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})), so **$12k–32k a mile in parts** for lasers that cut the line. That's three to nine times the fiber cutter's parts, about $3.6k a mile. Lasers that only blind the camera cost about $1–2k a mile.

</details>

<details class="layer" id="safety-and-law" markdown="block">
<summary><span class="layer-title">Safety and the law</span><span class="layer-sub">Fire, eyes, and the treaty on blinding lasers</span></summary>

- **Fire.** 100 W held on dry grass or leaves can set them alight. On a paved or gravel shoulder it's much safer. The post should check the ground with its camera before firing, and hold when it's dry.
- **Eyes.** Every laser here is Class 4: the direct beam, and its reflections, can blind. A post firing low along a road can hit our own troops and anyone else on it. It must fire only on a target the camera has confirmed, with nobody in the arc, and log every shot.
- **The treaty.** Protocol IV of the Convention on Certain Conventional Weapons bans lasers designed to blind people permanently. It allows lasers used against optical equipment, such as a drone's camera, and requires users to take precautions against blinding anyone ([Protocol IV text](https://nuke.fas.org/control/ccw/text/protocol4.htm)). A laser that cuts lines or blinds a drone's camera is on the allowed side, as long as it is never aimed at people.
- **Never at our own fiber.** The same rule as the cutter: hold while our own fiber drones are out. Our own lines must not run across a loop.

</details>

<details class="layer" id="what-has-to-be-tested" markdown="block">
<summary><span class="layer-title">What has to be tested</span><span class="layer-sub">Three tests that decide whether to build it</span></summary>

These are proposed, numbered L1–L3, apart from the tripwire's T-tests and the cutter's C-tests.

| Test | What | Pass | Cost |
|---|---|---|---|
| **L1. Does the line absorb it?** | On a bench, 3 ft away, hold beams of known power on real FPV fiber lying on asphalt and on grass. 10 W blue, then a rented or borrowed 100 W fiber laser. Measure the time until the light through the fiber is lost | The line is ruined within 3× the model's dwell, on both surfaces | One spool, about $200–500; the 10 W diode, about $120; the 100 W laser borrowed |
| **L2. Can a post loop a parked drone?** | A dummy FPV with fiber on a road shoulder, a laser on a post 100 ft and 300 ft away, a camera and pan-tilt tracing the loop. 20 runs, with wind on the post | The line is cut in 18 of 20 runs, the beam never touches the dummy, nothing catches fire | Pan-tilt, camera and rangefinder, about $500–1,100 |
| **L3. Does a blue diode blind an FPV camera?** | A real FPV camera and lens on a stand, a 5 W blue diode at 100 ft and 300 ft | The camera shows lasting damage, not just dazzled, within 1 s | One camera, about $30; the diode from L1 |

**What would scrap it:** in L1, the coating barely absorbs 1 µm light and the glass survives a long hold. Then only a CO₂ laser works, and its spot is too wide at range. Or in L2, grass hides the line from the beam or keeps catching fire.

</details>

<details class="layer" id="sources" markdown="block">
<summary><span class="layer-title">Sources</span><span class="layer-sub">Every source for this page, loaded 2026-10-23</span></summary>

- The video: [United24 (in Spanish)](https://united24media.com/es/latest-news/rusia-afirma-que-ucrania-utilizo-un-laser-para-quemar-el-cable-de-fibra-optica-de-un-dron-es-real-16707), [Trench Art](https://www.trenchart.us/p/is-ukraine-sweeping-roads-with-lasers)
- Aiming and Ukraine's lasers: [LIGA, General Staff source](https://news.liga.net/en/politics/news/ukraine-is-working-on-means-to-counter-uavs-on-fiber-optics---source-in-the-general-staff), [TechSpot, Tryzub](https://www.techspot.com/news/112357-ukraine-testing-ai-guided-laser-weapon-can-destroy.html), [Espreso, Tryzub](https://global.espreso.tv/russia-ukraine-war-ukrainian-laser-weapon-tryzub-could-rival-us-and-uk-systems)
- Coating and glass: [patent on medical laser fibers (acrylate at 500 °F)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10405923), [US9791624, stripping coating with blue light](https://patents.google.com/patent/US9791624), [AFL LZM-100, CO₂ laser splicing](https://www.aflglobal.com/en/Products/Fusion-Splicing/Specialty-Fusion-Splicing-Equipment/Splicers/LZM-100-LAZERMaster-Laser-Splicing-System)
- Camera damage: [laserpointersafety.com](https://laserpointersafety.com/ilda-camera-info-old.html), [Schwarz et al., Optical Engineering 2017](https://www.spiedigitallibrary.org/journals/Optical-Engineering/volume-56/issue-3/034108/Laser-induced-damage-threshold-of-camera-sensors-and-micro-optoelectromechanical/10.1117/1.OE.56.3.034108.full)
- Prices: [eBay, 10 W 445 nm module](https://www.ebay.de/itm/285749674639), [Accio, Raycus sources](https://www.accio.ai/find-supplier/raycus-source), [Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/machinery/fiber-laser-cutting-machine-source-guide-alibaba-b2b)
- The law: [Protocol IV on blinding laser weapons](https://nuke.fas.org/control/ccw/text/protocol4.htm)
- Model: [`tools/lasermodel/laser_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/lasermodel/laser_model.py). Run `py laser_model.py --range 635` for the farthest landing, or `--absorb 0.1` for a clear coating.

</details>
