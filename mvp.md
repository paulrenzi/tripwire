---
title: MVP path
nav_primary: 5
---

# The MVP path: $80 to a working line
{: .no_toc }

<p class="vz-lede">The <a href="{{ site.baseurl }}{% link models/tripwire.md %}">tripwire</a> built in five cheap layers. Each answers one question, and its gate decides whether to buy the next. <strong>The MVP is layer 5:</strong> six hand-placed listeners hear a real drone and alert a screen at the base box over fiber, while nothing at the unit transmits.</p>

<div class="stats">
  <div class="stat"><p class="stat-num">$80</p><p class="stat-label">for the first step, the Saturday test</p></div>
  <div class="stat"><p class="stat-num">$545–1,125</p><p class="stat-label">to the MVP, all five layers</p></div>
  <div class="stat"><p class="stat-num">6</p><p class="stat-label">listeners in the MVP line, 0.6–1.2 mi out</p></div>
  <div class="stat"><p class="stat-num">0</p><p class="stat-label">layers run so far: a plan, not a result</p></div>
</div>

{: .warning }
> **A plan, not a result: no layer has been run yet.** Gates marked *proposed* are ours; T9's are the site's. Links were loaded 2026-10-15. Items that wouldn't load are search terms.

## Start with the Saturday test {#weekend-test}

**One day, about $80–90, with a speaker and no drone:** how far a mic near the ground hears a drone, and how far its alarm travels. The steps are on their own page: [the Saturday test]({{ site.baseurl }}{% link weekend-test.md %}).

### Could a speaker stand in for the drone? {#speaker-reasoning}

**For most distances, yes.** A speaker finds the detector's threshold cheaply and precisely. It can't copy what 330 ft of real ground does to the sound, so a real flight at three distances checks it later, in layer 2.

<details class="layer" markdown="block">
<summary><span class="layer-title">The reasoning</span><span class="layer-sub">Source level, spreading, what a speaker gets wrong</span></summary>

**The arithmetic.** EASA lists the DJI Mini 4 Pro and Mini 5 Pro at a sound power of **81 dB(A)** ([EASA](https://www.easa.europa.eu/en/node/143951)). Spreading over a sphere, that is about 70 dB(A) at 3.3 ft, 36 at 160 ft, **30 at 330 ft**, 24 at 660 ft and 20 at 980 ft (6 dB less each time the distance doubles). A quiet field is often 30–40 dB(A). So at 330 ft a consumer drone is about as loud overall as the background, and detection depends on its rotor tones standing out in narrow bands. That fits the only measured cheap-mic range, 160–200 ft. Air absorption hardly matters at these distances: under about 1 dB at 980 ft below 1 kHz (ISO 9613-1, 68 °F, 70% humidity), rising to several dB above 2 kHz.

**Two ways to use a speaker:**

| | A. Speaker near the mic, turned down | B. Speaker at the real distance, on a pole |
|---|---|---|
| Set-up | Speaker 16 ft from the mic. Play the drone clip quieter by 20·log₁₀(distance ÷ 16 ft) dB: 26 dB for 330 ft, 32 dB for 660 ft | Speaker 10–33 ft up at the real distance, playing at the drone's own level (about 70 dB(A) at 3.3 ft for a Mini-class drone) |
| Captures | The detector's threshold against your real background noise, in 1 dB steps, as often as you like | Also the real ground, wind and trees along the path |
| Misses | Everything along the path: ground interference near a 20 in mic, wind bending the sound (upwind can lose 10 dB or more), turbulence | The drone's height and motion, and its own directivity |
| Needs | Any Bluetooth speaker, a basic sound level meter | A speaker that plays loud without distorting; FPV levels are unknown and probably much louder |

**What makes it work:**
- **Calibrate loud, then attenuate exactly.** Cheap sound meters can't read 20–30 dB(A). Measure the clip at the mic at a comfortable level, then make the quieter versions by digital gain, not by guessing with the volume knob.
- **Know the source level.** Recordings online aren't level-calibrated. For a Mini-class drone, use EASA's 81 dB(A). For an FPV, borrow one for ten minutes and measure it at 16 ft: no published measurement turned up.
- **Watch for distortion.** A speaker driven hard adds harmonics, and harmonics are what Batear's detector listens for, so distortion would flatter the result. Keep the speaker well below full volume, and compare the h2 and h3 values in the detector's log for the speaker and the real drone at the same level.
- **Check the low end.** Small speakers lose output in the low hundreds of hertz, where consumer-drone rotor tones sit. Look at the clip's spectrum before trusting a small speaker.
- **Log it as a speaker.** Use the logger's *Speaker* run type. Its results get their own line in the range table, and the clip cutter labels them `speaker_100m`, never mixed with real flights.

**What it buys.** Each 6 dB of detector sensitivity doubles the range. A speaker can measure that threshold in an afternoon, without a pilot, airspace rules or an FPV. It can also run at night, in wind, and next to a road, and it builds training data at known levels. One real flight at 160, 330 and 490 ft then shows whether the threshold-plus-spreading estimate holds over real ground. If it does, later tests can lean on the speaker. If not, the gap is the near-ground effect T11 exists to measure.

These are standard acoustics estimates, not measurements of our kit.
</details>

## The five layers to the MVP

<div class="vz-ladder">
  <a class="vz-rung" href="#layer-0"><span class="vz-rung-n">0</span><span class="vz-rung-q"><strong>Where does a minute help most?</strong> <span class="vz-rung-meta">T18 · $0 · gate: None: sizes the payoff</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:0.6%"></span><span class="vz-bar vz-bar-us-light" style="width:0%"></span></span><span class="vz-rung-tot">$0</span></a>
  <a class="vz-rung" href="#layer-1-the-radio-test-t9"><span class="vz-rung-n">1</span><span class="vz-rung-q"><strong>Do dart-to-dart hops hold at 660–980 ft?</strong> <span class="vz-rung-meta">T9 · ~$65–80 · gate: T9's marks</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:7.1%"></span><span class="vz-bar vz-bar-us-light" style="width:0.0%"></span></span><span class="vz-rung-tot">~$80</span></a>
  <a class="vz-rung" href="#layer-2-hear-a-drone-from-near-the-ground-t11"><span class="vz-rung-n">2</span><span class="vz-rung-q"><strong>How far does a mic near the ground hear a drone?</strong> <span class="vz-rung-meta">T11 · ~$50 · gate: ≥ 330 ft</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:11.6%"></span><span class="vz-bar vz-bar-us-light" style="width:0.0%"></span></span><span class="vz-rung-tot">~$130</span></a>
  <a class="vz-rung" href="#layer-3-fiber-home-t21"><span class="vz-rung-n">3</span><span class="vz-rung-q"><strong>Does a tip's light get home down the fiber?</strong> <span class="vz-rung-meta">T21 · ~$110–470 · gate: Every frame, 10 dB spare</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:21.3%"></span><span class="vz-bar vz-bar-us-light" style="width:31.999999999999996%"></span></span><span class="vz-rung-tot">~$240–600</span></a>
  <a class="vz-rung" href="#layer-4-battery-and-cold-t12"><span class="vz-rung-n">4</span><span class="vz-rung-q"><strong>Does a listener last weeks, in the cold?</strong> <span class="vz-rung-meta">T12 · ~$55–175 · gate: ≥ 3 weeks</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:26.2%"></span><span class="vz-bar vz-bar-us-light" style="width:42.7%"></span></span><span class="vz-rung-tot">~$295–775</span></a>
  <a class="vz-rung" href="#layer-5-the-mvp-a-six-listener-line"><span class="vz-rung-n">5</span><span class="vz-rung-q"><strong>Does the whole chain work?</strong> <span class="vz-rung-meta">MVP · ~$250–350 · gate: 18 of 20 crossings in 10 s</span></span><span class="vz-rung-track"><span class="vz-bar vz-bar-us" style="width:48.4%"></span><span class="vz-bar vz-bar-us-light" style="width:51.6%"></span></span><span class="vz-rung-tot">~$545–1,125</span></a>
</div>
<p class="vz-bar-note">Bars: total spent by the end of each layer, dark the low end and light the high end, out of $1,125. Tap a layer to open it.</p>

<details class="layer" markdown="block">
<summary><span class="layer-title">The layers as a table</span><span class="layer-sub">Every layer's question, spend, running total and gate in full</span></summary>

| Layer | Question | Spend | Total | Gate |
|---|---|---|---|---|
| [0](#layer-0) T18 | Where does a minute help most, and how would troops place a line? | $0 | $0 | None: sizes the payoff, shapes placement |
| [1](#layer-1-the-radio-test-t9) T9 | Do dart-to-dart hops hold at 660–980 ft, in the open and across trees? | ~$65–80 | ~$80 | T9's marks, or margins that predict them |
| [2](#layer-2-hear-a-drone-from-near-the-ground-t11) T11 | How far does a mic at 1.6–3.3 ft hear a drone? | ~$50 | ~$130 | ≥330 ft (sets spacing, so cost per km) |
| [3](#layer-3-fiber-home-t21) T21 | Does a tip's light get home down the fiber, and what does it cost the battery? | ~$110–470 | ~$240–600 | Every frame with 10 dB to spare; battery cost measured |
| [4](#layer-4-battery-and-cold-t12) T12 | Does a listener last weeks, in the cold, and what does its solar panel collect? | ~$55–175 | ~$295–775 | ≥3 weeks, cold loss and winter harvest measured |
| [5](#layer-5-the-mvp-a-six-listener-line) MVP | Does the whole chain work? | ~$250–350 | ~$545–1,125 | 18/20 crossings in 10 s, <1 false alarm/day, silent |

</details>

Assumed owned: laptop, phone, USB power banks, soldering iron.

## Layer 0: ask alongside (T18, $0, not a gate) {#layer-0}

Earlier warning against a threat nothing else detects (fiber-optic FPVs), at lower cost, is worth having; that is not tested here. 5–10 interviews ([questions]({{ site.baseurl }}{% link research/problem-check.md %}#the-next-step-ask-before-building-t18)) only tune the build: which moments matter most (sizes the [lives estimate]({{ site.baseurl }}{% link research/lives-model.md %})), and how troops would place listeners and a receiver.

<details class="layer" id="layer-1-the-radio-test-t9" markdown="block" open>
<summary><span class="layer-title">Layer 1: radio test (T9), ~$80</span><span class="layer-sub">Two boards at 1.6–3.3 ft, dart to dart, across open ground, woods and hedgerows</span></summary>

**Why first:** the hop along the row sets dart spacing, and so the cost of a line ([how]({{ site.baseurl }}{% link models/line-layout.md %})). It needs no drone, and every later layer reuses the boards. Alerts come home by fiber (layer 3), so the long radio leg to the unit is tested only for the fallback, run F.

| Item | Buy | Alternatives |
|---|---|---|
| **2 × LoRa board**, 915 MHz | **Bought:** Seeed XIAO ESP32S3 + Wio-SX1262 kit, [Rokland, $15.97 each](https://store.rokland.com/products/seeed-studio-xiao-esp32s3-wio-sx1262-kit-for-meshtastic-lora) | Heltec V3 2-pack, [Amazon, $44.98](https://www.amazon.com/dp/B0CW6151WJ); [Rokland, $29.97 each](https://store.rokland.com/products/heltec-wifi-lora-32v3); [Heltec direct, $17.90–19.90](https://heltec.org/project/wifi-lora-32-v3/) + China shipping; [RAK WisBlock kit, $34.97](https://store.rokland.com/products/rak-wireless-wisblock-meshtastic-starter-kit); [LILYGO T3S3, $72.99](https://www.tindie.com/products/yihang/915mhz-meshtastic-kit-t3s3-s3-sx1262/) |
| **u.FL→SMA cable** (neither board has SMA) | Proxicast, [Amazon, $7.94](https://www.amazon.com/dp/B09GJGNPQX) | [Adafruit 851, $3.95](https://www.adafruit.com/product/851) |
| **10 dB attenuator** (margin method) | MWRF, [Amazon, $12.49](https://www.amazon.com/dp/B07MRG9RDV) | [Inmet AHC-10, RF Parts, $15.91](https://www.rfparts.com/ahc-10.html); [L-com 20 dB, $92.09](https://www.l-com.com/coaxial-2w-20db-rf-fixed-attenuator-sma-male-to-sma-female-passivated-stainless-steel-body-up-to-6-ghz) |
| **Mast**, 20–33 ft (run F only) | **Free:** upstairs window, roof edge, tree | Mifoci 23 ft, [Amazon, $59.99](https://www.amazon.com/dp/B0GYYL3S6C) (16 ft [$39.99](https://www.amazon.com/dp/B0GYXPXCNY)); [Spiderbeam 39 ft HD, $109.99](https://moonrakeronline.com/us/spiderpole-12hd-telescopic-pole-12m-heavy-duty-fibreglass) |
| **Antenna** (run D) | 915 MHz omni with u.FL lead, [Amazon, $16.95](https://www.amazon.com/dp/B0GSB5XKLF) | [8 dBi omni, Newegg Business, $16.99](https://www.neweggbusiness.com/p/9B-2VT-04FG-00029); [Rokland 5.8 dBi kit, $49.97](https://store.rokland.com/products/meshtastic-compatible-6-dbi-n-female-omni-outdoor-915-mhz-antenna-kit-with-6-10-or-15-cable-choice) |

**Minimum:** 2 boards + cable, $53. With the attenuator, $65.

**Firmware**
- **Quick walk:** Meshtastic [Range Test](https://meshtastic.org/docs/configuration/module/range-test/), region US. Logs `rangetest.csv` with GPS. It sends one packet every 15–60 s, so it finds where the link dies but can't count delivery.
- **Counted points:** a [RadioLib](https://github.com/jgromes/RadioLib) ping sketch sending one packet every 1–2 s, 100 per point. It sets output power directly, which the margin method needs.

**Margin method:** lets a small woodlot stand in for deeper forest.
1. At each point, step power down 22 → 17 → 12 → 7 → 2 dBm, then add the attenuator, until delivery drops below 80%. The power you cut is the margin. Each spreading-factor step (SF12 → SF7) adds about 2.5 dB.
2. Repeat 150, 300 and 2,000 ft into forest. Margin lost per 330 ft predicts where the link dies.
3. This is an extrapolation ([Weissberger](https://en.wikipedia.org/wiki/Weissberger%27s_model)), so one real hop inside deep forest is still needed.

| Run | Place | Node | Receiver |
|---|---|---|---|
| A | Field or farm road, node to node | 20 in and 3.3 ft, 660–1,600 ft apart | Same height |
| C | Woodlot, node to node | 3.3 ft, 330–980 ft apart | Same height |
| E | Hedgerows (US stand-in for [windbreak belts]({{ site.baseurl }}{% link research/field-conditions.md %}#where-infantry-actually-sit-tree-lines)), node to node | One either side of 1, then 2 belts, 490–980 ft apart | Same height |
| F | Fallback only: woodlot or hedgerows to a raised receiver at the edge | 3.3 ft, 0.6–1.2 mi | 16–33 ft |

Run with leaves on now and leaves off in December.

**Gate:** [T9's marks]({{ site.baseurl }}{% link research/open-questions.md %}#the-test-t9), e.g. 90% at 980 ft between two boards at 3.3 ft in the open, and 80% node to node at 660 ft in woods. If open ground passes but woods fail, plan rows along open ground and belt edges, with closer darts under trees.
**Not testable at home:** jamming (T19), which is illegal in the US. 915 MHz at legal power is licence-free.

</details>

<details class="layer" id="layer-2-hear-a-drone-from-near-the-ground-t11" markdown="block">
<summary><span class="layer-title">Layer 2: hear a drone from the ground (T11), ~$50</span><span class="layer-sub">Mic range at 1.6–3.3 ft sets spacing, and so the cost of a line</span></summary>

**Why:** the site assumes listeners every 660–980 ft against FPVs, but the [only measured range]({{ site.baseurl }}{% link models/tripwire.md %}#warning-time-comes-from-distance) for cheap mics is 160–200 ft. Kit: the [weekend kit]({{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector) with the mic lowered, running Batear on layer 1's boards.

| Item | Buy | Alternatives |
|---|---|---|
| **3 × I2S mic** | INMP441 5-pack (Batear's wiring), [Amazon, $12.51](https://www.amazon.com/dp/B09G4RNT3G) | Adafruit SPH0645: [Amazon, $12.62](https://www.amazon.com/dp/B06XNL2GBW), [Adafruit, $6.95](https://www.adafruit.com/product/3421); INMP441 at [Vetco, $4.95](https://vetco.net/products/omnidirectional-microphone-module-inmp441-high-precision-i2s) |
| **Fur windscreens** | eBoot 5-pack, [Amazon, $8.99](https://www.amazon.com/dp/B01E4ZMTEG) | [Movo WS10n 5-pack, $14.95](https://www.movophoto.com/products/ws10n-universal-furry-outdoor-microphone-windscreen-lavalier) |
| **Breadboard + jumpers** | BOJACK kit, [Amazon, $9.99](https://www.amazon.com/dp/B08Y59P6D1) | [Adafruit 3314, $9.95](https://www.adafruit.com/products/3314); [SparkFun 140 pcs, $8.95](https://www.sparkfun.com/jumper-wire-kit-140pcs.html) |
| **Recorder** | XIAO ESP32S3 Sense, [Amazon, $23.99](https://www.amazon.com/dp/B0C69FFVHH) | Phone in a windscreen (free); [Seeed direct, $13.99](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html) |
| **Stake** | 48 in fiberglass, 20-pack, [Amazon, $23.99](https://www.amazon.com/dp/B0DF58T198) | Garden stake |
| **Drone** | **Borrow a 5–7 in FPV:** [AMA clubs](https://www.modelaircraft.org/club-finder), [MultiGP](https://www.multigp.com/chapters/) | [Potensic ATOM SE, $249.99](https://store.potensic.com/products/atom-se); DJI Mini 4K ~$299 (search); [DJI Neo, $169](https://store.dji.com/product/dji-neo), out of stock |
| **Wind** | Phone weather app | Anemometer, [Amazon, $12.99](https://www.amazon.com/dp/B0D7Z43M9S) |

**Run** ([weekend plan]({{ site.baseurl }}{% link research/open-source-builds.md %}#the-saturday-test), mic at 20 in and 3.3 ft)
- Hover 60 s at 80, 160, 330, 490, 660 and 980 ft, at two altitudes. Then fly straight passes.
- Log wind on every run.
- Record 30+ min with no drone: traffic, mowers, birds.
- Repeat along a [tree line]({{ site.baseurl }}{% link research/field-conditions.md %}#where-infantry-actually-sit-tree-lines).
- Fly under FAA TRUST or Part 107.

**Gate (proposed):**
- **Pass:** 9 of 10 passes heard at ≥330 ft with a consumer drone, or ≥490 ft with an FPV, in light wind. 660 ft spacing holds.
- **Fail, under 200 ft:** a line needs 3–4× the listeners per km. Redo the [cost]({{ site.baseurl }}{% link costs.md %}) first.

</details>

<details class="layer" id="layer-3-fiber-home-t21" markdown="block">
<summary><span class="layer-title">Layer 3: fiber home (T21), ~$110 on the bench, ~$470 with a real spool</span><span class="layer-sub">A board's alerts sent as light down FPV fiber to a base box, what it costs the battery, and whether a laid spool survives</span></summary>

**Why:** alerts come home by fiber, so the line's way home is a tip dart's light, not a radio the unit has to receive beside its own jammers. This proves a tip can send a few bytes down a full spool on a dart's battery ([design]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)). Nothing at the base box transmits, so the silence check that layer 3 used to need comes free.

{: .warning }
> **Less firm than the other layers.** The sellers' pages wouldn't load on 2026-10-23, so these prices are from search listings, unconfirmed. The likely cheap light source is a fiber-to-the-home modem's laser at $5–9, from one unconfirmed listing. Until one arrives, the bench uses FPV fiber transceivers that already carry serial data, and swaps in that laser when it does.

| Item | Buy | Alternatives |
|---|---|---|
| **Reference link, ×2:** FPV fiber transceivers that carry serial data | NanoHD F3, "video + UART serial/CRSF", [Unmanned Tech, £29.69 each](https://www.unmannedtechshop.co.uk/collections/fibre-optic) | Sky and ground modules, [GetFPV, $110 each](https://www.getfpv.com/commercial-industry-drones/fiber-optics.html); Sky TX kit with 3 km of fiber, [Sigmanortec, ~€421](https://sigmanortec.ro/en/fiber-optic-fpv-kit-3km-with-sky-tx-module) |
| **Bench fiber** | A short single-mode patch cord in the transceivers' connector, plus a fixed optical attenuator (search terms) | – |
| **A real spool** (step 4 only) | 1 km canister, [GetFPV, about $360](https://www.getfpv.com/commercial-industry-drones/fiber-optics.html) | [2 km canister, GetFPV](https://www.getfpv.com/commercial-industry-drones/fiber-optic-canister-v2-2km.html); bulk G657A2 at about $30 a km, with a large minimum order ([Alibaba](https://electronics.alibaba.com/product/fiber-drone-cable)) |
| **The cheap tip's light source** | The 1310 nm laser from a fiber-to-the-home modem, already joined to a lead of single-mode fiber, $5–9, buy-one minimum ([GoldSupplier](https://www.goldsupplier.com/provide/p100619675.html), one listing, unconfirmed). It is the part a $122 tip dart assumes | Branded pigtailed 1310 nm laser diodes, from about $328 ([MKS](https://np.d1.mks.com/f/fiber-pigtailed-laser-diodes)); the FPV fiber module makers' bare transmitter |
| **Current meter** | Layer 4's PPK2 | – |

**Run**
1. Pair the two transceivers on the patch cord. Feed a board's serial output, the 44-byte frame from [Build: software]({{ site.baseurl }}{% link build-software.md %}) at 9,600 baud, into one end and read it on a laptop at the other. Count frames for an hour.
2. Add attenuation until frames drop. That is the margin. The fiber itself loses under 1 dB over 1.2 mi on paper.
3. Measure the sending end's current: always on, and keyed only for alerts and the 10 s heartbeat, if it can be.
4. Lay the real spool from the drone over plough, grass and a hedgerow, with the home end plugged in first. Count breaks (1 in 20 assumed).

**Gate (proposed):** every frame arrives with at least 10 dB to spare; a cut shows dark within 30 s; the light and heartbeat add little to a tip's daily use (about 25 µA averaged, est.), so its solar panel still covers it outside midwinter. If the reference link draws too much for a dart, that is the gap a cheap light source has to close. If none can, use the fallback below.

</details>

<details class="layer" id="layer-3-the-edge-receiver-t17" markdown="block">
<summary><span class="layer-title">Fallback: silent edge receiver (T17), ~$90–130</span><span class="layer-sub">Only where fiber can't go: a receive-only board at the tree-line edge, wired to the dugout, proven silent with an SDR</span></summary>

**Why:** where a tip dart can't be laid, or its fiber keeps being cut, the unit has to hear the line by radio without transmitting. This proves it can ([fallback design]({{ site.baseurl }}{% link models/tripwire.md %}#getting-alerts-out-of-the-trees)). Skip it if layer 3 passes.

| Item | Buy | Alternatives |
|---|---|---|
| **3rd LoRa board** | Heltec V3, [Amazon, $34.99](https://www.amazon.com/dp/B0D1H1FN9Y) | [Rokland, $29.97](https://store.rokland.com/products/heltec-wifi-lora-32v3); as layer 1 |
| **RS-485, edge** | MAX3485 (3.3 V) 5-pack, [Amazon, $8.99](https://www.amazon.com/dp/B0FTFXT876) | [SparkFun breakout, $12.50](https://www.sparkfun.com/sparkfun-transceiver-breakout-rs-485.html). Not the 5 V MAX485 |
| **USB→RS-485, laptop** | FT232RL adapter, [Amazon, $16.31](https://www.amazon.com/dp/B081MB6PN2) | [Waveshare (B), ~$7.99](https://www.waveshare.com/product/iot-communication/wired-comm-converter/usb-to-rs485-b.htm) |
| **Wire** | Old Ethernet cable (one pair) | 980 ft run: burial Cat5e 1000 ft, [Amazon VIVO, $89.99](https://www.amazon.com/dp/B0092TJ4K2) or [TRUE CABLE, $228.99](https://www.amazon.com/dp/B01JAVNWOK) |
| **Directional antenna** | **DIY** wire Yagi on a wooden boom, a few dollars | 7 dBi Yagi, N-female, [Amazon, $24.99](https://www.amazon.com/dp/B0CPFT1V9L) (needs N→SMA); [Pasternack 9 dBi, $254.99](https://www.pasternack.com/single-antenna-880-960-mhz-9-dbi-gain-n-pe51ya1018-p.aspx) |
| **Into the canopy** | Tennis ball + paracord | Throw line kit, [Amazon, $21.68](https://www.amazon.com/dp/B0DH2SV5XK) |
| **SDR** | RTL-SDR Blog V3 + dipoles, [Amazon, $47.95](https://www.amazon.com/dp/B0BMKB3L47) | Dongle only, [Amazon, $37.95](https://www.amazon.com/dp/B0BMKZCKTF); Nooelec SMArt v5, [Amazon, $44.95](https://www.amazon.com/dp/B01HA642SW) |

**Run**
1. Raise the receive-only board 16–33 ft at a woodlot edge and cable it in to a laptop.
2. Send from layer 1's passing points and log delivery.
3. Watch 902–928 MHz on the SDR for 1 h, at the edge and at the laptop.
4. Once the short run works, prove 980 ft of cable. RS-485 is rated to ~3,900 ft at low data rates.

**Gate (proposed):** delivery matches layer 1, the SDR sees **no transmission**, and alerts reach the laptop within 2 s. If the board emits anything in receive mode, fix the firmware first.

</details>

<details class="layer" id="layer-4-battery-and-cold-t12" markdown="block">
<summary><span class="layer-title">Layer 4: battery, cold and solar (T12), ~$55–175</span><span class="layer-sub">Weeks on one cell? The kitchen freezer is the cold chamber, and a winter outdoors measures the panel</span></summary>

**Why:** listeners are disposable, so battery life and how much a solar panel collects in winter set the [running cost]({{ site.baseurl }}{% link models/tripwire.md %}#the-running-cost-lines-are-ammunition). With a panel, cells should run flat only in midwinter; this measures whether they do. It needs the classifier trained on layer 2's audio.

| Item | Buy | Alternatives |
|---|---|---|
| **Current meter** | [Nordic PPK2, Adafruit, $99.95](https://www.adafruit.com/product/5048) (reads µA sleep current; Amazon $189.99) | FNIRSI FNB58, [Amazon, $49.99](https://www.amazon.com/dp/B0BJ253W31). Average current only |
| **Cells** (not on Amazon) | [Molicel P28A, $5.99](https://www.18650batterystore.com/products/molicel-p28a) | [Samsung 30Q, $6.99](https://www.18650batterystore.com/products/samsung-30q); [Battery Junction P28A, ~$6.70](https://batteryjunction.com/molicel-inr18650-p28a) |
| **Holder** | 2-pack with leads, [Amazon, $5.99](https://www.amazon.com/dp/B092TGQ7PB) | [SparkFun 1×18650, $1.25](https://www.sparkfun.com/battery-holder-1x18650-wire-leads.html) (backordered) |
| **Plug** | Solder the V3's included SH1.25 lead to the holder | LiPo with "Micro JST 1.25" ([Rokland V3 page](https://store.rokland.com/products/heltec-wifi-lora-32v3)). Adafruit LiPos (JST-PH) don't fit |
| **Solar charger** | Adafruit bq24074 Universal USB/DC/Solar charger, [Adafruit, $14.95](https://www.adafruit.com/products/4755), with a 10K thermistor on the cell so it stops charging below 32°F | A TP4056-class module with a thermistor input (search terms), cheaper but less tested |
| **Panels** | A dart's: 2.4 × 2.4 in epoxy panel, [Kunkune, £1–2.55](https://kunkune.co.uk/shop/uncategorized/small-solar-epoxy-panel-polycrystalline-solar-panel). A post's: 6 V 1 W, [Adafruit, $19.95](https://adafruit.com/product/3809) | 110 × 60 mm 6 V 1 W, [Low Power Lab, $4.95](https://lowpowerlab.com/shop/product/166) (out of stock) |
| **Freezer logger** | Inkbird IBS-TH2 Plus, [Amazon, $24.99](https://www.amazon.com/dp/B08TM67HJH) (only the probe goes in; the body is rated to 14 °F) | [GoveeLife R1, $39.99](https://us.govee.com/products/goveelife-smart-thermometer-r1) |

**Run**
1. Measure the current asleep, listening and sending, then work out days per cell.
2. Run one listener on a cell at room temperature until it dies, with a speaker playing a drone clip on a timer.
3. Repeat in the freezer (0 °F), with the board reporting its voltage and temperature as in the [cold fix]({{ site.baseurl }}{% link models/tripwire.md %}#solving-the-field-limits-at-no-extra-cost).
4. Put one listener with its flat panel outdoors on a stake, and one post with its tilted panel, from November to February, logging cell voltage, charge current and temperature every 10 minutes. Note snow, frost and shade. Check that the charger never charges below 32°F.

**Gate (proposed):** at least **3 weeks** at room temperature, with the cold loss measured, and a winter shortfall that matches the plan's 2–4 re-lays a year (the panel collecting about half a dart's daily use in December, est.). If it fails, recompute the running cost; a one-week listener may still pay.

</details>

<details class="layer" id="layer-5-the-mvp-a-six-listener-line" markdown="block">
<summary><span class="layer-title">Layer 5: the MVP, six listeners, ~$250–350</span><span class="layer-sub">Hand-placed line 0.6–1.2 mi out, home on layer 3's fiber, real drone crossings</span></summary>

**Proves:** drone crosses → listener hears → alert hops along the row → the tip sends it down the fiber → the screen at the base box shows it, in time. One of the six carries layer 3's link as the tip; where fiber failed, the edge receiver stands in.

| Per listener | Source | Cost |
|---|---|---|
| Heltec V3 | [Amazon 2-pack](https://www.amazon.com/dp/B0CW6151WJ), or [Heltec direct](https://heltec.org/project/wifi-lora-32-v3/) | $18–23 |
| Mic + windscreen | Layer 2 packs | $4–5 |
| Cell + holder | Layer 4 | $9 |
| Box | uxcell IP65 3.9×2.7×2 in, [Amazon, $15.69](https://www.amazon.com/dp/B07FKN8SZG); [Newegg Business, $10.99](https://www.neweggbusiness.com/p/9B-072-001K-007A7) | $11–16 |
| Stake | Layer 2's 20-pack | $1–2 |
| **Total** | | **$45–55** |

Six listeners cost $270–330. Add four if layer 1's forest hops need tighter spacing.

**Run**
1. [Place by hand]({{ site.baseurl }}{% link models/tripwire.md %}#why-not-have-people-place-the-listeners) across a hedgerow gap, at layer 2's spacing, 0.6–1.2 mi from the base box.
2. Fly 20 crossings, varying height, time of day and wind, and GPS-log each one.
3. Leave the line running a week (T5) to count false alarms.

**Measure:**
- detections;
- time from crossing to screen;
- delivery per link;
- false alarms per day;
- battery left at the end.

**Gate (proposed):**
- **18 of 20** crossings on screen, each within **10 s**.
- **Under 1** false alarm per line per day.
- **No transmission** from anything at the unit, checked on the SDR.

A pass shows the idea works at small scale on US ground. It does not show it against jamming, Ukrainian terrain, mass raids or air-dropped placement.

</details>

<details class="layer" id="shopping-list" markdown="block">
<summary><span class="layer-title">Full shopping list, all layers</span><span class="layer-sub">Amazon where it sells the part, prices checked 2026-10-15. Alternatives are in each layer</span></summary>

| Layer | Item | Buy | Price |
|---|---|---|---|
| 1 | Seeed XIAO ESP32S3 + Wio-SX1262 kit, ×2 (bought) | [Rokland](https://store.rokland.com/products/seeed-studio-xiao-esp32s3-wio-sx1262-kit-for-meshtastic-lora) | $31.94 |
| 1 | u.FL→SMA pigtail, Proxicast | [Amazon](https://www.amazon.com/dp/B09GJGNPQX) | $7.94 |
| 1 | 10 dB SMA attenuator, MWRF | [Amazon](https://www.amazon.com/dp/B07MRG9RDV) | $12.49 |
| 1 | 915 MHz omni, N, with u.FL lead (run D) | [Amazon](https://www.amazon.com/dp/B0GSB5XKLF) | $16.95 |
| 1 | Mast, 23 ft fiberglass (optional; a window or tree is free) | [Amazon](https://www.amazon.com/dp/B0GYYL3S6C) | $59.99 |
| 2 | INMP441 I2S mic, 5-pack | [Amazon](https://www.amazon.com/dp/B09G4RNT3G) | $12.51 |
| 2 | Fur windscreens, 5-pack | [Amazon](https://www.amazon.com/dp/B01E4ZMTEG) | $8.99 |
| 2 | Breadboards + jumpers | [Amazon](https://www.amazon.com/dp/B08Y59P6D1) | $9.99 |
| 2 | Seeed XIAO ESP32S3 Sense (recorder) | [Amazon](https://www.amazon.com/dp/B0C69FFVHH) | $23.99 |
| 2 | 48 in fiberglass stakes, 20-pack | [Amazon](https://www.amazon.com/dp/B0DF58T198) | $23.99 |
| 2 | Anemometer (optional) | [Amazon](https://www.amazon.com/dp/B0D7Z43M9S) | $12.99 |
| 3 | NanoHD F3 fiber transceiver, ×2 (listed, unconfirmed) | [Unmanned Tech](https://www.unmannedtechshop.co.uk/collections/fibre-optic) | £59.38 |
| 3 | 1 km FPV fiber canister (step 4 only; listed, unconfirmed) | [GetFPV](https://www.getfpv.com/commercial-industry-drones/fiber-optics.html) | ~$360 |
| 3 fallback | Heltec V3, single | [Amazon](https://www.amazon.com/dp/B0D1H1FN9Y) | $34.99 |
| 3 fallback | MAX3485 RS-485 modules (3.3 V), 5-pack | [Amazon](https://www.amazon.com/dp/B0FTFXT876) | $8.99 |
| 3 fallback | USB→RS-485, FT232RL | [Amazon](https://www.amazon.com/dp/B081MB6PN2) | $16.31 |
| 3, 5 | RTL-SDR Blog V3 + dipole kit | [Amazon](https://www.amazon.com/dp/B0BMKB3L47) | $47.95 |
| 3 fallback | 915 MHz Yagi, 7 dBi (optional; DIY is a few dollars) | [Amazon](https://www.amazon.com/dp/B0CPFT1V9L) | $24.99 |
| 3 fallback | Throw line kit (optional; a tennis ball works) | [Amazon](https://www.amazon.com/dp/B0DH2SV5XK) | $21.68 |
| 3 fallback | Burial Cat5e, 1000 ft (980 ft run only) | [Amazon](https://www.amazon.com/dp/B0092TJ4K2) | $89.99 |
| 4 | Nordic PPK2 current meter | [Adafruit](https://www.adafruit.com/product/5048) (Amazon $189.99) | $99.95 |
| 4 | 18650 cells, Molicel P28A (not on Amazon) | [18650 Battery Store](https://www.18650batterystore.com/products/molicel-p28a) | $5.99 each |
| 4 | 18650 holders with leads, 2-pack | [Amazon](https://www.amazon.com/dp/B092TGQ7PB) | $5.99 |
| 4 | Inkbird IBS-TH2 Plus freezer logger | [Amazon](https://www.amazon.com/dp/B08TM67HJH) | $24.99 |
| 5 | 2 more Heltec 2-packs (6 listeners in all) | [Amazon](https://www.amazon.com/dp/B0CW6151WJ) | $89.96 |
| 5 | IP65 box 3.9×2.7×2 in, uxcell | [Amazon](https://www.amazon.com/dp/B07FKN8SZG) | $15.69 each |

</details>

## After the MVP

| Test | Adds | Why later |
|---|---|---|
| T7 | 20+ listeners, losses in a mass raid | ~$1,000; only matters once a line works |
| T10, T13, T14 | Drone-laid listeners, with and without GPS. Dart, X500 harness and printed carrier: [Build: hardware]({{ site.baseurl }}{% link build-hardware.md %}) | Hand placement proves the rest first |
| T15 | Friend or foe | Needs recordings of friendly drones |
| T19 | Jamming | Illegal in the US; needs a licensed range or Ukraine |
| T6 | Shahed-class engines | Needs a partner |

All tests: [open questions]({{ site.baseurl }}{% link research/open-questions.md %}).
