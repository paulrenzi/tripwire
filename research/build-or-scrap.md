---
title: Build or scrap?
parent: Research Notes
nav_order: 0.1
nav_tripwire: 2
---

# Build or scrap?
{: .no_toc }

<p class="vz-lede">Does the case for the tripwire hold, after a fresh sweep of competitors, FPV acoustics, forward sensors, enemy counters and whether warning helps? <strong>Verdict: don't scrap, but narrow.</strong> Reviewed 2026-10-15.</p>

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Keep</p><p><strong>The forward-laid tripwire.</strong> Nobody sells it, physics favours it, and it buys a go/no-go minute for people about to move</p></div>
  <div class="vz-card"><p class="vz-card-num">Drop</p><p><strong>The hand-placed node as a product.</strong> A Ukrainian LoRa module already lists at about $211, inside our $125–300 band</p></div>
  <div class="vz-card"><p class="vz-card-num">Test</p><p><strong>Not bulletproof yet.</strong> Two field tests under $300 each, T9 and T19, decide what could kill it; desk research won't</p></div>
</div>

### A 1.9 mi line, if every sensor hears an FPV at 330 ft

<div class="vz-bars">
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>Our listeners</strong> ($17–50 each)</span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:1.8%"></span><span class="vz-bar vz-bar-us-light" style="width:3.4%"></span></span><span class="vz-bar-val"><strong>$510–1.5k</strong></span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">DroneAlert ($211 each)</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:21.7%"></span><span class="vz-bar vz-bar-them-light" style="width:0.0%"></span></span><span class="vz-bar-val">~$6.3k</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">Zvook NW0 ($834–950, plus power)</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:86.2%"></span><span class="vz-bar vz-bar-them-light" style="width:13.8%"></span></span><span class="vz-bar-val">$25–29k</span></div>
  <p class="vz-bar-note">30 sensors each, the same range for everyone, arithmetic on listed prices. <strong>About 4–12× cheaper than DroneAlert and 17–56× cheaper than NW0</strong> at any equal range; re-lays are extra.</p>
</div>

### The three risks left

<div class="vz-tiles">
  <div class="vz-tile"><span class="vz-tile-id">1 · T18</span><span class="vz-tile-q">How many lives a minute saves is a guess</span><span class="vz-chip">sizes it, not a gate</span></div>
  <div class="vz-tile"><span class="vz-tile-id">2 · T9, T19</span><span class="vz-tile-q">The radio link along the row gets jammed or found</span><span class="vz-chip vz-chip-open">untested</span></div>
  <div class="vz-tile"><span class="vz-tile-id">3 · T11</span><span class="vz-tile-q">The real hearing range is very short</span><span class="vz-chip vz-chip-open">untested</span></div>
</div>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The verdict, as first written</span><span class="layer-sub">Keep, drop, and what isn't bulletproof, with its links</span></summary>

A review of whether the case for our model holds, after a fresh sweep of competitors' prices and capabilities, FPV acoustics, forward ground sensors, enemy counters and whether warning helps. Reviewed 2026-10-15.

{: .important }
> **Verdict: don't scrap, but narrow.**
> - **Keep the forward-laid tripwire.** It is the one part nobody sells, and the one part that physics favours. What it buys is a go/no-go minute for people about to move: about 1–4 of every 100 drone casualties averted, on our central guess ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})).
> - **Drop the hand-placed node as a product.** A Ukrainian LoRa acoustic module is already listed at about $211, inside our $125–300 band.
> - **The case is not bulletproof, and more desk research won't make it so.** Two things could still kill it, and two field tests under $300 each (T9, T19) decide them. Interviews (T18) size the payoff but don't gate it.

</details>

<details class="layer" id="why-the-forward-line-holds" markdown="block">
<summary><span class="layer-title">Why the forward line holds</span><span class="layer-sub">What nobody else sells, and why physics favours distance</span></summary>

**Warning time is distance divided by speed.** No microphone changes that. Take an FPV at about 62 mph (63 mph; an assumption, and FPVs fly slower and faster), and take off 1–2 s to classify the sound:

| Sensor | Where it sits | Range it relies on | Warning (estimate) |
|---|---|---|---|
| A sentry's ear | At the position | ~490 ft (Mavic-class, quiet field, measured) | ~4 s |
| DroneAlert module | At the position | 390 ft (seller's claim) | ~3 s |
| Zvook NW0 | At the position | 1,500 ft (maker's claim, best case) | ~14 s |
| **Our listener row** | **About 1 mi forward (the [modelled net]({{ site.baseurl }}{% link models/line-layout.md %}))** | **Only needs to hear the drone cross the row** | **~60 s; more from a deeper row** |

Every sensor at the position gives seconds, even on its maker's best figure. Only distance gives a minute. **A listener's range sets how many listeners a line needs, not how much warning it gives.** That makes the tripwire the part of the case least exposed to the range question.

</details>

<details class="layer" id="what-it-costs-at-equal-range" markdown="block">
<summary><span class="layer-title">What it costs at equal range</span><span class="layer-sub">Our listeners against DroneAlert and NW0 at three ranges, and the range nobody has measured</span></summary>

Earlier comparisons gave competitors their claimed ranges. Here every row uses the **same range**, so the comparison is fair. A 1.9 mi line, one sensor per detection range (as the [tripwire]({{ site.baseurl }}{% link models/tripwire.md %}) plans it). Arithmetic on listed prices; the ranges are unmeasured for everyone.

| If every sensor hears an FPV at… | Sensors per 1.9 mi | Our listeners ($17–50) | DroneAlert ($211) | Zvook NW0 ($834–950, plus power) |
|---|---|---|---|---|
| 820 ft | 12 | $200–600 | ~$2,500 | ~$10–11k |
| 330 ft | 30 | $510–1,500 | ~$6,300 | ~$25–29k |
| 160 ft | 60 | $1,020–3,000 | ~$12,700 | ~$50–57k |

**At equal range we are about 4–12x cheaper than DroneAlert and about 17–56x cheaper than NW0.** Add the yearly re-lay cost for a consumable line ([estimate]({{ site.baseurl }}{% link models/tripwire.md %}#the-running-cost-lines-are-ammunition)). A line of 60 listeners re-laid often could cost more than a radio detector bought once.

**How far does a cheap microphone hear an FPV?** Still nobody knows. We found no measured FPV sound level and no controlled FPV range test anywhere. A first-principles estimate (sound falling off with distance, air absorption, rural background noise) puts a single cheap microphone at about **330 ft in wind and 490–820 ft in calm, quiet air**. That assumes an FPV is 85–95 dB(A) at 3.3 ft, which is louder than a Phantom because its props spin about 3x faster at the tips. The same model gives 98–330 ft for a Phantom, which brackets the measured 160–200 ft, so the model is in the right range. **Plan on 20–30 listeners per 1.9 mi line, not 12**, until T11 measures it.

</details>

<details class="layer" id="what-changed-in-the-market" markdown="block">
<summary><span class="layer-title">What changed in the market</span><span class="layer-sub">New prices and products since the last review</span></summary>

- **A cheap LoRa acoustic module exists.** DroneAlert, sold by Flash Army (Ukraine), is listed at 9,500 UAH (~$211) per module, with a 2,500 UAH gateway. The seller claims:
  - a 390 ft detection radius and a bearing;
  - up to 500 hours on a 3.7 V battery;
  - LoRa up to 6.2 mi;
  - IP55.
  
  It's out of stock, names no maker, has no reviews and doesn't mention fiber-optic FPVs ([Flash Army](https://flasharmy.com.ua/dronealert-lora-merezha-akustychnyi-modul-vyiavlennia-droniv), news item Jun 2026). **It has our architecture.** Our listener is still 4–12x cheaper, but the architecture is no moat.
- **Other new entrants, all claims only:**
  - **SKANER 2.1** (Belarus): 330–980 ft against FPVs, fiber-optic included; 2.6 lb; 12 h ([Militarnyi, May 2026](https://militarnyi.com/uk/news/bilorus-predstavyla-akustychnyj-radar-skaner-2-1-dlya-vyyavlennya-fpv-droniv-na-optovolokni/)).
  - **Arcani HARK** (UK): aimed at FPVs, with a Ukraine test planned for May 2026 and no result found ([Janes, Apr 2026](https://www.janes.com/osint-insights/defence-news/c4isr/arcani-plans-to-test-hark-acoustic-sensor-in-ukraine)).
  - **Neuron Soundware Sound Shield** (Czechia): under 1 W per sensor, at a reported €100–150 production cost, for borders ([dev.ua, Jun 2026](https://dev.ua/news/sound-shield-1781192277)).
  - **ZVOOK Tracking**: a bearing-capable array at about $2,670 ([Flash Army](https://flasharmy.com.ua/sensor-zvook-tracking)).
- **Nobody sells forward lines.** Komodo's star is still the only acoustic sensor sold as drone-droppable, and it's priced and pitched as a capable Shahed sensor.
- **No independent test of any acoustic FPV detector** was found: not NW0, RADD, Komodo, DroneAlert or SKANER. Poland's seven-system trial at Ustka (April 2026) published no results.
- **At the front, the kit is shifting** ([inventory]({{ site.baseurl }}{% link research/frontline-kit.md %})). Jamming is failing ("Jamming no longer works", a brigade EW commander). An AI turret that tracks fiber-optic drones is in more than 10 units. Interceptors are the most-ordered category on Brave1 Market. None of it gives a minute's warning of fiber-optic FPVs.
- **Money is moving into acoustic, for the rear.** NATO's procurement agency (NSPA) named a Bionic System Solutions-led consortium as one of five counter-drone framework contractors (July 2026). Lithuania is piloting Sky Fortress, and a Czech fund has invested in Zvook (Oct 2026). None of this is for FPVs at a position.

</details>

<details class="layer" id="what-could-still-kill-it" markdown="block">
<summary><span class="layer-title">What could still kill it</span><span class="layer-sub">Three risks, ranked, each with the test that decides it</span></summary>

Ranked by how likely each is to end the idea, with the test that decides it.

### 1. How many lives a minute saves is a guess (T18)

We found **no study, after-action report or soldier account comparing outcomes with and without warning**. What exists:

- **Seconds of warning are used every day.** Cheap beepers give "seconds to take cover" ([Telegraph, Jul 2025](https://www.yahoo.com/news/inside-ukraine-drone-infested-grey-090000135.html)). Crews use radio detectors to decide when to switch on jammers or run to shelter ([Foreign Policy, Aug 2024](https://foreignpolicy.com/2024/08/05/ukraine-russia-war-drone-detectors-jamming-tsukorok/)).
- **Demand for detectors is high**, but that is a signal of value, not a measurement of lives saved. The Tsukorok developer said demand far outran supply (same source). Ukraine's former defence minister said everyone should carry a Chuyka ([BlueBird, Aug 2026](https://www.blue-bird.tech/en/news-en/everyone-should-have-a-chuyka-from-schoolchildren-to-minibus-drivers-says-mykhailo-fedorov/)).
- **Against:** the Tsukorok designer calls his detector a last warning device that loses value where drones are everywhere (Foreign Policy). Troops already cope by staying put for a month or more and moving at night ([RUSI, Feb 2025](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)).
- **Where the evidence points instead: routes.** About half of casualties are in the rear, during rotation and resupply (RUSI). Fiber-optic FPVs now hunt roads and wait beside them for hours ([Mezha, Nov 2025](https://oboronka.mezha.ua/en/droni-zhduni-yak-pracyuyut-novi-rosiyski-droni-306465/)).

  A line across the approach would warn a convoy of drones flying in. It **would not** warn of one already waiting with its motors off, which is silent until it launches (inference). A guard along the road itself would: in the [route model]({{ site.baseurl }}{% link models/route-guard.md %}), posts beside the road hear every drone that lands within 300 ft of it, and a fence a mile out gives every drone flying in at least 60 s.

**Weapons need seconds; a minute buys go/no-go calls on movement.** Russia's roadside drone "traffic lights" already serve that purpose ([the comparison]({{ site.baseurl }}{% link research/problem-check.md %}#a-minute-against-the-alternatives)). In lives, our central guess is about 1–4 of every 100 drone casualties averted, range 0.3–14 ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})).

**Not a reason to scrap:** fiber-optic FPVs get no warning today, so any warning, cheaper, fills a gap. T18 interviews, especially with drivers, medics and resupply crews, would narrow the estimate.

### 2. The radio link home gets jammed or found (T9, new T19)

- **The bands are already contested.** Russia's Groza-07K jammer covers 100 MHz–1.1 GHz, which includes 433, 868 and 915 MHz ([Armada International, Sep 2026](https://www.armadainternational.com/2026/09/russia-tishina-software-defined-jammer-electronic-warfare/)). Jammers on both sides sit near the line to defeat 900 MHz drone control links.
- **A LoRa-hunting jammer is in development.** The same article, by an analyst from KI Insights, describes "Tishina", a Russian *prototype* designed to detect and suppress LoRa and ELRS signals. No field results are reported.
- **Emitters get struck.** Ukraine has found and hit Russian mesh relay stations by their emissions ([DroneXL, Feb 2026](https://dronexl.co/2026/02/28/ukraine-shahed-drone-relay-stations-belarus)). Those were high-power towers, not small sensors. We found no case of small, rarely-transmitting sensors being hunted, and no case showing they are safe.

Listeners that sit quiet are hard to find. **The receiver at the unit and any relay chain are the parts that are exposed.** The [listen-only edge receiver]({{ site.baseurl }}{% link models/tripwire.md %}#getting-alerts-out-of-the-trees) already keeps the unit's end silent.

**What a jamming model says** ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}#jamming), estimates):

- **Distance decides it.** A jammer spreads its power over hundreds of our channels, so near the ground a 20 W trench jammer blinds a dart only within about 390 ft. That is the main estimate. In the worst case, where the jammer's signal crosses open ground with none of the losses that limit our own hops, it reaches about 1.1 mi.
- **Our own jammers are the first threat.** Receivers at the positions sit beside the unit's trench jammers and go deaf whenever those are on; so do receivers in trucks with vehicle jammers. The fix is a wire: forward roots on fiber at the position, posts on a cable with lamps on a road. Both keep a full minute in the model on the main estimate.
- **Fiber for everything is not the answer.** An air-dropped row can't share one, and every cut silences everything beyond it. Wire or fiber fits the fixed links beside jammers; radio stays for the darts out in the fields.

**Scrap or rethink the back-haul if** T19 shows a near-ground link fails out to about a mile from a working jammer, the worst case. Then a radio net can't work near the front, and only wired links can. **It survives if** links fail only within a few hundred feet of a jammer: then jamming is a matter of where the darts and roots go.

### 3. The real range is very short (T11)

Below about 160 ft, a 1.9 mi line needs 60 or more listeners and each re-lay takes 15–20 drone sorties. The cost per line still beats every competitor at equal range, but the re-lay workload may not be worth it to a unit. **The idea stops making sense below roughly 130 ft** (an inference from the table above). The estimate says 330 ft or more is likely, which keeps this the least likely of the three to kill the idea.

</details>

<details class="layer" id="what-not-to-claim-any-more" markdown="block">
<summary><span class="layer-title">What not to claim any more</span><span class="layer-sub">Claims this review retired</span></summary>

- **"Our hand-placed node is much cheaper than the market."** At $125–300 it isn't cheaper than DroneAlert's ~$211. Only the throwaway listener is.
- **"Nobody sells cheap LoRa acoustic sensors."** DroneAlert does, on paper.
- **"The line is silent."** The listeners are silent until they report. The reports, any relays and any receiver that transmits are not.

</details>

<details class="layer" id="what-would-make-the-case-bulletproof" markdown="block">
<summary><span class="layer-title">What would make the case bulletproof</span><span class="layer-sub">The tests and evidence still missing</span></summary>

1. **T11:** fly a real FPV past one cheap microphone on a mast and log the range in calm and in wind. Under $300.
2. **T19:** run the T9 radio test again next to a working ELRS jammer, and at 300 ft, 0.25 mi, 0.5 mi and 1 mi from it. Under $300.
3. **An independent test of NW0 or DroneAlert alongside ours.** Buying one DroneAlert kit (~$670 for three modules and a gateway) would give the first like-for-like range figure anyone has published.
4. **T18:** 5–10 front-line interviews, including drivers and medics, to narrow the lives estimate. $0.

Desk research has reached diminishing returns. Every remaining unknown is a measurement or an interview.

</details>

<details class="layer" id="sources" markdown="block">
<summary><span class="layer-title">Sources</span><span class="layer-sub">Every source on this page</span></summary>

Beyond those linked above:
- [Jekateryńczuk & Piotrowski, *Sensors* 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12656299/): consumer-drone levels and tones, and range against a calibrated tone in calm and wind.
- [Miguel-Ayala et al., Forum Acusticum 2025](https://dael.euracoustics.org/confs/fa2025/data/articles/000656.pdf): measured hover levels of the Mavic 4, Phantom 4 and Matrice 300.
- [Cabell et al., NASA, NOISE-CON 2016](https://ntrs.nasa.gov/api/citations/20160010139/downloads/20160010139.pdf): small multicopter noise.
- [Tejera-Berengue et al., Forum Acusticum 2025](https://dael.euracoustics.org/confs/fa2025/data/articles/000072.pdf): modelled FPV audibility.
- [Defence-Industry.eu: NSPA counter-drone framework (Jul 2026)](https://defence-industry.eu/nato-procurement-agency-selects-five-suppliers-for-counter-drone-framework-as-allies-seek-faster-access-to-c-uas-systems/)
- [Militarnyi: Lithuania's Sky Fortress pilot (Oct 2026)](https://militarnyi.com/en/news/lit-ukr-skyfortress-acoustic-uav-detection/)
- [Kyiv Post: DEPO Ventures invests in Zvook (Oct 2026)](https://kyivpost.com/post/86941)
- [Defence24: Ustka acoustic trial (Apr 2026)](https://defence24.pl/polityka-obronna/drony-bez-szans-mon-ujawnia-przelomowe-testy)
- [NPR: the kill zone (Oct 2026)](https://www.npr.org/2026/10/05/nx-s1-5925803/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)

</details>
