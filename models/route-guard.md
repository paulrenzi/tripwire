---
title: Guarding a road
nav_primary: 2.15
---

# Guarding a supply road
{: .no_toc }

<p class="vz-lede">About half of casualties come in the rear, on rotation and resupply, and fiber-optic FPVs now land beside roads to wait. A road guard gives trucks <strong>a minute's warning</strong> of a drone coming in, and <strong>finds the ones waiting</strong>.</p>

<figure class="vz-figure vz-narrow">
<svg viewBox="0 0 480 430" role="img" aria-labelledby="rg-hero-t">
  <title id="rg-hero-t">A road guard seen from above: a fence of darts about a mile out sends alerts down fibers to posts beside the road. A drone flying in is heard at the fence, at least a minute before it reaches the road. A drone that lands near the road to wait is heard by the nearest post.</title>
  <rect x="0" y="0" width="480" height="40" fill="#f3e1d8"/>
  <text x="14" y="27" class="vz-t-tag" style="font-size:15px">ENEMY SIDE</text>
  <g fill="#d2451e" fill-opacity=".07" stroke="#d2451e" stroke-opacity=".45" stroke-dasharray="4 4">
    <circle cx="40" cy="95" r="32"/><circle cx="90" cy="95" r="32"/><circle cx="140" cy="95" r="32"/><circle cx="190" cy="95" r="32"/><circle cx="240" cy="95" r="32"/><circle cx="290" cy="95" r="32"/><circle cx="340" cy="95" r="32"/><circle cx="390" cy="95" r="32"/><circle cx="440" cy="95" r="32"/>
  </g>
  <path d="M90 95 L120 286" stroke="#2f6b3a" stroke-width="3"/>
  <path d="M390 95 L360 286" stroke="#2f6b3a" stroke-width="3"/>
  <rect x="0" y="300" width="480" height="30" fill="#d9d3c7"/>
  <text x="470" y="320" class="vz-t-small" text-anchor="end" style="font-size:14px">supply road</text>
  <g fill="#151515"><rect x="34" y="282" width="12" height="12"/><rect x="114" y="282" width="12" height="12"/><rect x="194" y="282" width="12" height="12"/><rect x="274" y="282" width="12" height="12"/><rect x="354" y="282" width="12" height="12"/><rect x="434" y="282" width="12" height="12"/></g>
  <line x1="296" y1="14" x2="286" y2="268" stroke="#151515" stroke-width="2.5" stroke-dasharray="8 6"/>
  <path d="M279 256 L286 270 L293 257" fill="none" stroke="#151515" stroke-width="2.5"/>
  <g fill="#d2451e"><circle cx="40" cy="95" r="6"/><circle cx="140" cy="95" r="6"/><circle cx="190" cy="95" r="6"/><circle cx="240" cy="95" r="6"/><circle cx="340" cy="95" r="6"/><circle cx="440" cy="95" r="6"/></g>
  <g fill="#d2451e" stroke="#2f6b3a" stroke-width="3"><circle cx="90" cy="95" r="8"/><circle cx="390" cy="95" r="8"/></g>
  <circle cx="292" cy="95" r="10" fill="#d2451e" stroke="#151515" stroke-width="3"/>
  <text x="240" y="152" class="vz-t-small" text-anchor="middle" style="font-size:15px">fence of darts, ~1 mi out</text>
  <text x="274" y="196" class="vz-t" text-anchor="end" style="font-size:16px">flying in: heard</text>
  <text x="274" y="216" class="vz-t" text-anchor="end" style="font-size:16px">at the fence</text>
  <text x="274" y="242" class="vz-t-accent" text-anchor="end" style="font-size:18px">≥ 60 s warning</text>
  <text x="98" y="205" class="vz-t-green" text-anchor="end" style="font-size:15px">fiber</text>
  <g transform="translate(200 360)" stroke="#151515" stroke-width="2.5">
    <line x1="-8" y1="-8" x2="8" y2="8"/><line x1="8" y1="-8" x2="-8" y2="8"/>
    <g fill="#fff" stroke-width="2"><circle cx="-8" cy="-8" r="3.5"/><circle cx="8" cy="-8" r="3.5"/><circle cx="-8" cy="8" r="3.5"/><circle cx="8" cy="8" r="3.5"/></g>
  </g>
  <circle cx="200" cy="360" r="24" fill="none" stroke="#151515" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="234" y="356" class="vz-t" style="font-size:16px">landed to wait:</text>
  <text x="234" y="376" class="vz-t-small" style="font-size:15px">"drone near post 3"</text>
  <text x="14" y="418" class="vz-t-small" style="font-size:14px">■ posts 40 ft off the road, ≤ 1,100 ft apart</text>
</svg>
<figcaption>Seen from above, not to scale. Green: the fibers from two tip darts in the fence to posts by the road.</figcaption>
</figure>

<div class="stats">
  <div class="stat"><p class="stat-num">≥ 60 s</p><p class="stat-label">warning of every drone flying in to strike, in the model; median 72–102 s</p></div>
  <div class="stat"><p class="stat-num">4–9 s</p><p class="stat-label">from posts alone, without the fence</p></div>
  <div class="stat"><p class="stat-num">14–20</p><p class="stat-label">darts and posts a mile of road</p></div>
  <div class="stat"><p class="stat-num">$4.7–6.7k</p><p class="stat-label">a mile a year, with solar (est.)</p></div>
</div>

### The two alerts

<div class="vz-cards vz-2">
  <div class="vz-card"><p class="vz-card-num">Inbound</p><p>A fence dart hears a drone. Says <strong>"Hot: mile 0.7 to 2.7"</strong>, the stretch it could reach. Clears when it's heard leaving, or after a set time.</p></div>
  <div class="vz-card"><p class="vz-card-num">Waiting</p><p>A post hears a drone close by, then nothing. Says <strong>"Drone waiting near post 17"</strong>. Stays up until a team clears it. Nothing else on sale gives this.</p></div>
</div>

### What it is made of

<div class="vz-cards vz-4">
  <div class="vz-card"><p class="vz-card-num">$38</p><p><strong>Dart:</strong> four mics, a LoRa radio and a cell in a finned body, dropped point-first in the fence</p></div>
  <div class="vz-card"><p class="vz-card-num">$128</p><p><strong>Tip dart:</strong> a dart with 1.2 mi of FPV fiber and a small laser, sending alerts to a post</p></div>
  <div class="vz-card"><p class="vz-card-num">$49</p><p><strong>Post:</strong> a dart's board on a stake by the road, 4 cells, a tilted solar panel, a 2 ft whip</p></div>
  <div class="vz-card"><p class="vz-card-num">Listen only</p><p><strong>Receivers</strong> in every vehicle and at checkpoints only listen, so a truck gives nothing away</p></div>
</div>

<p class="vz-done"><span class="vz-chip vz-chip-open">untested</span> a working model (<a href="https://github.com/paulrenzi/tripwire/blob/main/tools/routemodel/route_model.py"><code>route_model.py</code></a>) run on two invented 4 mi roads. Nothing in it is measured yet.</p>

## The guard

<figure style="margin:12px 0 8px;max-width:600px">
<div id="route-model" data-src="{{ '/assets/data/route-demo.json' | relative_url }}"></div>
<figcaption style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px">
<button type="button" id="route-play" class="btn btn-sm">Play</button>
<button type="button" id="route-replay" class="btn btn-sm">Replay</button>
<span id="route-status" aria-live="polite" style="font-weight:600;flex:1 1 220px"></span>
</figcaption>
</figure>
<script src="{{ '/assets/js/route.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>

The model's example road, to scale, with the enemy to the right: 4 mi running toward the front, from a depot 5.7 mi back to 1.7 mi behind our positions. Every position, hearing and warning comes from the model; time runs ten times faster, except in the last scene.

<details class="layer" markdown="block">
<summary><span class="layer-title">How an alert gets to the trucks</span><span class="layer-sub">Hear, get it to the road, spread it along the road, show it, count in and out</span></summary>

1. **Hear.** Every dart and post listens all the time. A fence dart that hears a drone passes "drone, heading in" to its neighbour.
2. **Get it to the road.** The alert hops along the fence to the nearest tip dart, at most 6 hops, and the tip sends it down its fiber to a post as flashes of a small laser. Light only goes one way, home, and a heartbeat every 10 s shows the fiber is whole.
3. **Spread it along the road.** Posts relay every alert along the road. Their 2 ft whips on stakes should reach about 2,500 ft, more than two posts' spacing, so one dead post breaks nothing (an estimate; T9 measures it). Proposed: a cable along the verge as well, so posts share alerts where radio is jammed ([below](#jamming-and-a-wire-along-the-road)).
4. **Show it.** Every vehicle carries a receiver that never transmits, so a truck gives nothing away. It and a board at each checkpoint show which stretches are hot. Drivers check before setting out; anyone on a hot stretch stops under cover.
5. **Count in and out.** A drone heard crossing the fence inward stays on the count until it is heard leaving, heard landing, or cleared.

</details>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">Why a road, as first written</span><span class="layer-sub">The page's original opening, with its sources</span></summary>

A net in front of a position protects people who are a few yards from a dugout, where seconds of warning already help. People on a road have nowhere to go in seconds. About half of casualties come in the rear, during rotation and resupply ([RUSI, Feb 2025](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)), and fiber-optic FPVs now hunt roads and land beside them to wait ([Trench Art](https://www.trenchart.us/p/russias-best-drones-lie-in-wait-beside)). This page is a working model of a permanent guard on a road: [`route_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/routemodel/route_model.py), built on the [lay model]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net), run on two invented 4 mi roads. Nothing in it is measured yet.

</details>

<details class="layer" id="the-parts" markdown="block">
<summary><span class="layer-title">The parts</span><span class="layer-sub">Darts, tip darts, posts, what each is connected to, and where alerts go</span></summary>

- **A dart** is a small listening sensor: four microphones on its fins that hear drone motors and take a bearing, a LoRa radio and one battery cell, in a finned body dropped from a drone so it sticks point-first in the ground ([dart model]({{ site.baseurl }}{% link build-3d.md %}#why-it-should-fall-point-first)). It only says "I heard a drone", and its neighbours relay that along the row. A small solar panel on its head keeps the cell topped up from March to October. About $32.
- **A tip dart** is a dart with a spool of FPV fiber, about 1.2 mi, and a small laser. It is dropped first, paying the fiber out from a post, and sends every alert it hears or is passed home as light. About $128, most of it fiber.
- **A post** is a dart's board on a stake, set in by hand from a vehicle at night, 40 ft off the road and at most 1,100 ft apart: about 5 a mile. It has 4 cells instead of 1 and a 1 W solar panel tilted toward the sun, so it should run through winter without a cell swap, and a 2 ft whip antenna, so its radio should reach about 2,500 ft, past the next post (est., T9, T12). About $49.
- **What a post is connected to:** its neighbour posts, by radio and, as proposed, by a twisted-pair cable along the verge ([below](#jamming-and-a-wire-along-the-road)); and, at 5–7 of a road's 21 posts, a tip dart's fiber. Nothing else: no mains power, no network.
- **Where the alerts go:** there is no central box. Every post repeats every alert along the whole road, so anything listening anywhere on it hears all of it. Each vehicle carries a receiver that never transmits. Each checkpoint has one wired to a phone, tablet or laptop that shows the road's map and which stretches are hot. A laptop sees the whole road from a checkpoint within radio reach of the end post, or plugged into the end of the cable. Anywhere further back needs a link this page doesn't design. To put the alert on the phones and radios troops already carry, see [Partners for the alert]({{ site.baseurl }}{% link research/partners.md %}).

</details>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">The whole page in eight bullets: parts, the minute, landings, counts, cost, jamming, nets, gaps</span></summary>

- **A guard has two parts.** Posts stand along the road, placed by hand. A fence of air-dropped darts runs about a mile out on every side a drone can come from. Every 2 mi a **tip dart** in the fence sends its alerts to a post down an FPV fiber, as on the [position net]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box), so nothing between the fence and the road uses radio.
- **The fence gives the minute.** In the model, every drone flying in to strike the road, from anywhere within 60° of the enemy, is heard at least 60 s before it can reach the road; the median is 72–102 s. Posts alone give 4–9 s.
- **The posts catch drones landing to wait.** Every landing within 300 ft of the road is heard, about 340 ft from the post that hears it loudest. The alert, "drone waiting near post 17", stays up until someone clears it.
- **How many:** 21 posts and 35–58 darts for 4 mi of road, **about 14–20 a mile**. A road running toward the front costs more than one running along it, because the fence has to wrap both sides and the forward end. Fiber took out the 25–35 relay darts the radio trunks needed.
- **What it costs us:** a package of about **$6,500–7,900**, then about **$20–30k a year** with solar, **$5,000–7,300 a mile**. Without solar, at four-week cells, it would be $46–70k. Posts alone cost about $1,500 and $3,800 a year; they find landings but give no minute.
- **Jamming: the trucks' own jammers are the threat, and a wire answers it.** A truck's jammer deafens its own receiver and the posts near it, so a radio-only guard tells a jamming truck nothing on the move. Posts on a cable along the verge, each with a hooded lamp facing the road, keep the warning in the model (100% of tracks with a minute) for about $200 a mile more (est.). In the worst case for jamming, the truck's jammer reaches the fence too, and the fibers only partly save it.
- **Against nets and the rest: lead with the posts.** At about $940 a mile a year they hear what nothing else on sale does, a fiber-optic FPV landing to wait. With solar the fence costs less than netting the road for its first 5–16 years, but it only warns; it pays where roads won't be netted, or where trucks have cover to reach in a minute ([comparison](#against-whats-already-on-roads)).
- **What it misses:** drones parked before it was laid, drones carried in on foot, and landings more than about 600 ft from the road. Our own drone crews, who live in this strip, are a risk worse here than at a position.

1. TOC
{:toc}

</details>

<details class="layer" id="two-alerts" markdown="block">
<summary><span class="layer-title">Two alerts</span><span class="layer-sub">Inbound and waiting: what sets each off, what it says, when it clears</span></summary>

| Alert | What sets it off | What it says | When it clears |
|---|---|---|---|
| **Inbound** | A fence dart hears a drone | "Hot: mile 0.7 to 2.7". The stretch a drone could reach | The fence hears it leave, or a set time passes with nothing heard |
| **Waiting** | A post hears a drone close by, then nothing: no strike, nothing heard leaving | "Drone waiting near post 17, mile 3.2" | A team clears it |

**The waiting alert is the one nothing else gives.** A drone waiting with its motors off is silent, but it had to fly there, and it lands within earshot of a post. It then sits on the ground for hours, unable to move fast. That is when to deal with it. In the model, the stretch to search is the post's neighbourhood, about 2,600 ft of road. Two posts hear the landing only 13–24% of the time, so a finer fix needs posts on both sides of the road.

**Landing far from the road is the soft spot.** Only 10–13% of landings 600–1,500 ft out are heard by a post. The fence still heard the drone come in, so the guard knows one drone is inside and unaccounted for, but not where.

</details>

<details class="layer" id="how-many-darts" markdown="block">
<summary><span class="layer-title">How many darts</span><span class="layer-sub">Posts and darts for 4 mi of road, along and toward the front</span></summary>

| Road, 4 mi | Posts | Fence | Fence darts | Of them, tip darts (fiber) | Air-dropped | Per mile, all |
|---|---|---|---|---|---|---|
| Running along the front, 2.3 mi back | 21 | 6.2 mi | 35 | 5 (5.6 mi of fiber) | 35 | **14** |
| Running toward the front, 1.7–5.7 mi back | 21 | 10.2 mi | 58 | 7 (7.8 mi of fiber) | 58 | **20** |

On radio trunks the same fences needed 60 and 93 air-dropped darts: 25–35 of them were relays.

**The rules the planner uses:**

- **Posts every 1,100 ft at most.** Then any landing up to 300 ft off the road passes within 635 ft of a post. Posts stand 40 ft off the road.
- **The fence sits 5,316 ft out,** the same distance as the position net's front row, for the same reason: a drone at 60 mph crossing midway between two darts is heard 65 s out.
- **The fence only goes where a drone heading for the road would cross.** The planner flies tracks at every point of the road from every angle within 60° of the enemy, and puts the fence where they cross 5,316 ft from the road, plus 300 ft at each end. Behind the depot no track crosses, so the back is left open.
- **Fence darts sit about 960 ft apart,** one radio hop, as on the position net. **A fiber every 2 mi** brings alerts to the road, so no fence dart is more than about 6 hops from a tip, and every fence dart has two ways home.
- **Each fiber runs from its tip to the nearest post,** about a mile. A tip's spool holds about 1.2 mi, and the planner allows 10% for the fiber not lying straight, so it moves a tip to the next fence dart if its fiber would be too long.
- **Fiber must not lie across the road,** where trucks would cut it. Posts stand on one side, so where the fence is across the road from them, the fiber ends at a box on the near verge, joined to its post by a short cable buried under the road, laid by hand with the posts (est. a few dollars; not modelled).
- **The planner moves darts off trees.**

</details>

<details class="layer" id="what-the-model-found" markdown="block">
<summary><span class="layer-title">What the model found</span><span class="layer-sub">Warning for every track, landings heard, and what changed with fiber</span></summary>

Every drone flies straight at 60 mph toward a point on the road, from 7.5 mi out, at every 0.1 mi of road and every 5° within 60° of the enemy: about 1,000 tracks a road. Recognising a drone takes 3 s and each hop 0.3 s (assumed).

| Road, 4 mi | Guard | Worst warning | 1 track in 10 below | Median | Tracks with a minute (55 s) |
|---|---|---|---|---|---|
| Along the front | Posts only | 0 s | 2 s | 4 s | 0% |
| Along the front | **Posts and fence** | **60 s** | 63 s | 72 s | **100%** |
| Toward the front | Posts only | 2 s | 4 s | 9 s | 9% |
| Toward the front | **Posts and fence** | **61 s** | 69 s | 102 s | **100%** |

- **Landings within 300 ft of the road: all heard by a post.** The loudest post is a median 340–350 ft from the drone, and 9 in 10 within 525–585 ft.
- **One dead dart or post costs little.** The worst single loss leaves 98% of tracks with a minute.
- **One cut fiber costs nothing in the model.** Its tip still relays by radio along the fence to the next tip, so 100% of tracks keep a minute.
- **Between repairs**, assuming each dart is lost 0.5% of days, each post 1% and each fiber is cut 1% (shelling, traffic, scavenging: guesses), and the daily roll call or the fiber's heartbeat finds a loss within a day: about one node is down at a time. Tracks with a minute average 100%, 83–98% on the worst day sampled (on the road toward the front, a tip and a dart six places along from it down on the same day); landings heard average 99%.
- **Laying the fence, GPS jammed, every dart confirmed,** 200 lays: about 46 darts and 18 sorties for the road along the front, 76 darts and 28 sorties for the road toward it, 6–9 of them tip darts. On radio trunks it was 77–119 darts and 23–35 sorties. The planned net is whole after 100% of lays.

**If the planning numbers are wrong, the fix is more darts,** as on the position net (per mile, posts and darts):

| Case | Along the front | Toward the front |
|---|---|---|
| **Plan** | **14** | **20** |
| Drones come within 45° of the enemy, not 60° | 13 | 18 |
| Drones come within 75° | 15 | 20 |
| Radio hop 800 ft, not 980 | 16 | 22 |
| Hearing 500 ft, not 656 | 18 | 24 |
| A fiber every 3 mi, not 2 | 14 | 20 |
| The last plan: radio relay trunks | 20 | 28 |

A fiber costs no extra darts, since its tip is a fence dart, so fewer fibers save nothing but tip darts. If 1 fiber in 5 breaks while it is laid, not 1 in 20, a lay uses about 2 more darts.

</details>

<details class="layer" id="jamming-and-a-wire-along-the-road" markdown="block">
<summary><span class="layer-title">Jamming, and a wire along the road</span><span class="layer-sub">The trucks' own jammers, and posts on a cable with lamps facing the road</span></summary>

{: .warning }
> From the [jamming model]({{ site.baseurl }}{% link models/line-layout.md %}#jamming) ([`jam_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/jamming/jam_model.py)): estimates, with jammer powers assumed and every jammer on all the time.

**On a road, the jammers that matter are our own.** Trucks carry jammers against radio FPVs, and "most mobile jammers" cover 868–915 MHz ([Armada International, Feb 2026](https://www.armadainternational.com/2026/02/the-curran-papers-no-5-jamming-uninhabited-aerial-vehicle-video-signals-electronic-warfare/)). A 100 W vehicle jammer (assumed) deafens the receiver in its own cab, and posts within about 910 ft on the main estimate, or 2.7 mi in the worst case. So a radio-only guard can't tell a jamming truck anything on the move, which is when it matters. Trench jammers on both sides are too far from these fences to matter on the main estimate; in the worst case they deafen the forward end of the road toward the front.

**Proposed: put the posts on a cable, and give each a lamp.**

- **Twisted pair along the verge,** laid on the same night as the posts. RS-485 runs about 0.7 mi a segment ([TI](https://www.ti.com/document-viewer/SN65HVD72/datasheet/typical-application-sllse118349)), and every post repeats it, so every post knows what any post has heard, with no radio. Posts keep their radios as a backup, so a cut costs nothing unless a jammer is on at the same place.
- **A hooded lamp on each post, facing the road.** Posts on a hot stretch light up. A driver sees them with the jammer on, and a truck needs no receiver at all. It is the Russian roadside traffic light, driven by the guard. The hood has to hide the lamp from drones overhead; not designed.
- **Why copper, not fiber:** both are unjammable, but every post on a fiber would need an optical converter at each end, and copper can also carry power. Fiber is light enough to pay out from a drone, which is why the trunks out to the fence are fiber: nobody walks a mile out to lay them. Along the verge a crew already stops at every post.

| Road, 4 mi | Jammers on | Tracks with a minute, radio guard | Cable and lamps, main estimate | Cable and lamps, worst case |
|---|---|---|---|---|
| Along the front | Trench jammers on both sides | 100% | 100% | 100% |
| Along the front | The truck's own | **0%**: its receiver hears nothing | **100%** | 21% |
| Toward the front | Trench jammers on both sides | 100% | 100% | 82% |
| Toward the front | The truck's own | **0%** | **100%** | 46% |

**In the worst case the truck's jammer also reaches the fence** a mile out and stops its darts relaying. Fiber takes the trunks out of that: 21–46% of tracks keep a minute, against 2–22% on radio trunks. What is left is the fence itself, whose darts relay along the row by radio, and the cable can't fix that. Then a truck has to switch its jammer off on a hot stretch, since it does nothing against fiber-optic FPVs anyway. T19, run at range from a vehicle jammer, decides whether the worst case is real.

**The cable adds about $800 a road, $200 a mile** (est.): about $650 of twisted pair, $2–5 of RS-485 chip and $3 of lamp a post. It saves most of the vehicle receivers.

</details>

<details class="layer" id="laying-it" markdown="block">
<summary><span class="layer-title">Laying it</span><span class="layer-sub">Who lays what, and in what order</span></summary>

- **Posts go in by hand,** from a vehicle at night: 21 stops on a 4 mi road, each post checked with a handheld receiver before the crew moves on. That puts a crew on the shoulder of the road it is guarding. Verges are often mined.
- **The fence goes in by drone,** with the [lay model's]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net) loop: the drone drops 4 darts a sortie and confirms every dart by hearing its neighbour relay it. **Tips go first,** each as the first drop of its own sortie: the crew ties the fiber off at its post, the drone pays it out on the way to the fence, and the tip's heartbeat at the post confirms it. A tip whose fiber breaks is laid again with a new fiber. So every fence dart has a way home before the next one lands.
- **It is a day's work with more packs.** The road toward the front takes about 5.1 h of flying and charging with 12 packs and a 4-channel charger, 11.7 h with the position package's 6 packs and 2 channels; the road along the front 3.1 h or 6.5 h. With GPS jammed it is a daylight job, so the larger kit is the difference between one day and two on the longer fence.
- **The fence is re-laid when its cells run down,** which with solar should happen only in midwinter, 2–4 times a year. Posts aren't re-visited for cells; their tilted panels should carry them through December (T12).

</details>

<details class="layer" id="cost" markdown="block">
<summary><span class="layer-title">Cost</span><span class="layer-sub">Package, re-lays and a year, with and without solar</span></summary>

Small-batch cost to us, from [Projected costs]({{ site.baseurl }}{% link costs.md %}#guarding-a-road). A post is about $49 (est.): the dart's board, 4 cells, a 2 ft whip, a stake and a 1 W solar panel.

| | Along the front | Toward the front |
|---|---|---|
| **Package:** 25 posts, 50 or 80 darts, 9 or 11 tip darts and a fiber end at each fiber's post, 14 receivers (12 vehicles, 2 checkpoints), the outfitted drone with 12 packs and 4 charger channels | **~$6,520** | **~$7,940** |
| One re-lay of the fence: about 46 or 76 darts (6 or 9 of them tip darts), about 0.3–0.6 of a lost drone, pack wear | ~$2,550 | ~$4,140 |
| **A year with solar, 4 winter re-lays:** repairs between re-lays, cut fibers, no post cell swaps | **~$20,100** | **~$29,600** |
| A year with solar, 2 winter re-lays | ~$15,000 | ~$21,300 |
| A year without solar, four-week cells: 13 re-lays, post cells every 16 weeks | ~$46,400 | ~$70,200 |
| A year without solar, two-week cells | ~$82,900 | ~$127,300 |
| **A mile a year with solar, 4 winter re-lays** | **~$5,000** | **~$7,300** |

- **Solar halves the bill.** Without it, battery life set the bill: re-lays were 70–76% of a year at four-week cells. With it, re-lays are a third to a half, and **repairs are the other half**: darts and posts lost to shelling and cut fibers, about $9,900–13,100 a year. Those loss rates are guesses, and now the ones that matter most.
- **Fiber made it cheaper.** A tip dart costs about $128 against a dart's $38, but each fiber replaces about 5 relay darts, and fewer darts means fewer sorties and fewer lost drones.
- **Cut fibers are a running cost:** at the guessed 1% of days each, about 18–26 new tips a year, each on its own sortie, about $2,600–3,800.
- **The drone is the hidden cost again.** At the guessed 2% lost per sortie, a re-lay loses about 0.3–0.6 drones, about $270–500.
- **Posts only:** about $1,500 for 25 posts and 14 receivers, and about $3,800 a year, all of it posts lost; solar ends the cell swaps, and with them most of the night stops on a mined verge. No drone is needed. It finds landings by the road but gives 4–9 s of warning of a strike.
- **The cable and lamps** add about $800 a road ([above](#jamming-and-a-wire-along-the-road)). Repairs to cuts are not costed.

</details>

<details class="layer" id="against-whats-already-on-roads" markdown="block">
<summary><span class="layer-title">Against what's already on roads</span><span class="layer-sub">Nets, guns, jammers and detectors compared</span></summary>

**Lead with the posts. Add the fence only where the minute will be used.** The posts do a job nothing on sale does cheaply. With solar the fence costs less than netting the road for its first 5–16 years, but a net stops drones and the fence only warns. It earns its place on roads that won't be netted, roads that matter for a few weeks, or roads with somewhere to go when the alert comes. Per mile, small-batch costs to us (est.); labour isn't costed:

| Option | To set up, a mile | A year, a mile | Against a fiber-optic FPV |
|---|---|---|---|
| **Our posts alone** | **~$380** | **~$940** | Hear a drone land to wait. 4–9 s of warning of a strike |
| **Our full guard,** posts and fiber fence | ~$1,630–1,970 | **~$5,000–7,300** with solar; ~$3,800–5,300 if winters need only 2 re-lays; ~$11,600–17,400 without solar at four-week cells | A minute's warning of every drone flying in, and the landings |
| Zvook NW0 posts, wired | ~$2,300–4,000 plus power | not known | The posts' job, at about 10–20 times the price a sensor. No minute |
| Net tunnels | **~$29,000–64,000** ($18–40k a km in Kherson) | repairs, not known | Stop many strikes with nobody doing anything. But fiber-optic FPVs fly under them and waiting drones hide under them |
| Interceptor drones | – | ~$1,000–3,000 a shot | Need something to cue them. Nothing found on fiber-optic FPVs specifically |
| Radio detectors (Chuyka, ~$584) | – | – | Can't hear a fiber-optic FPV at all |

Sources: nets, ~1.8 million UAH a km ([Most.ks.ua](https://most.ks.ua/en/news/url/urjad-vidiliv-96-mln-grn-na-antidronovi-koridori-dlja-avtoshljahiv-hersonschini/)); 4,000 km more planned for 2026 ([Liga.net](https://news.liga.net/en/politics/news/another-4000-km-of-roads-will-be-covered-with-anti-drone-tunnels-in-ukraine-by-the-end-of-the-year-photo)), 1,170 km in place by May ([Ukrainska Pravda](https://www.pravda.com.ua/eng/news/2026/05/18/8035246/)); "can also hide under the nets" and flying underneath ([What troops have]({{ site.baseurl }}{% link research/frontline-kit.md %})); interceptors about $1,000–3,000 ([Wikipedia: Sting](https://en.wikipedia.org/wiki/Sting_(drone)), [Euromaidan Press](https://euromaidanpress.com/2026/04/24/ukrainian-p1-sun-drones-down-3000-plus-shaheds-in-2026-at-about-3000-apiece/)); Zvook and Chuyka from [competitors]({{ site.baseurl }}{% link research/competitors.md %}).

**The posts: worth it wherever fiber-optic FPVs hunt a road.**

- Nothing else on sale hears a fiber-optic FPV land by the road and wait, the tactic these drones are now known for ([Trench Art](https://www.trenchart.us/p/russias-best-drones-lie-in-wait-beside)).
- At about $940 a mile a year they cost about one truck a road every three years.
- **Zvook already pitches acoustic sensors for roads,** NW0 networks "protecting… logistics routes" 400–600 m (about 1,300–2,000 ft) apart, over Ethernet, fiber, twisted pair, LTE or LoRa ([Militarnyi](https://militarnyi.com/en/news/ukraine-develops-acoustic-detector-for-fpv-drones/), [dev.ua](https://dev.ua/en/news/ukrainska-kompaniia-zvook-stvoryla-akustychnyi-sensor-dlia-vyiavlennia-fpv-droniv-za-zvukom-1769187556)). That is the posts, wired, at about $834–950 a sensor against our $49. It is the direct rival on the road.
- **Unproven:** whether a post tells a landing from a drone flying out of earshot (T20), and who sets posts on a mined verge.

**The fence: cheaper than a net for years, but not a net.**

- It is 81–87% of the guard's bill, about $4,100–6,400 a mile a year with solar. A net costs $29,000–64,000 a mile once, so it pays back against the fence in about 5–16 years, sooner if its repairs are cheap. Solar made the fence the cheaper choice for a road needed only a few years.
- A net protects without anyone acting on anything. The minute only counts if drivers hold, drive out of the hot stretch or reach cover.
- **Where the fence wins:**
  - **Roads that won't be netted.** Fiber-optic FPVs now reach 12–30 mi, and the whole netting programme is about 2,500 mi of road. There are far more roads inside that reach than that.
  - **Roads that matter for a few weeks.** A fence goes in in a day and moves with the fight; a net stays where it was built.
  - **On top of nets.** It warns of drones flying in to go under a net, and the posts hear the ones that land beneath it.
- **What sets its value is what is built round it:** holding points, cover every half mile (a minute at 30 mph), or an interceptor team the alert can cue. Without them the minute buys a "don't go yet", and little more.
- **Russia's roadside "traffic lights"** already sell that "don't go yet" call ([Espreso](https://global.espreso.tv/russia-ukraine-war-russia-installs-traffic-lights-to-counter-ukrainian-fpv-drones)). Someone already pays for the job.

**Break-even, roughly:** with solar the full guard has to save about one truck every 1.5–2 miles a year, if a used pickup costs about $10k (a guess). The posts alone have to save about one a road every three years. No count of trucks lost per mile of road was found, so whether a given road clears that bar is a judgment.

**What would break the case:**

- **Solar failing in winter (T12).** If panels are buried in snow or shaded, the guard falls back toward four-week cells, $10.7–15.9k a mile a year, and two-week cells would put it at $19–29k: the price of a net, without its armour.
- **Losses higher than guessed.** With solar, repairs are half the bill, so twice the losses to shelling means about half as much again on the year.
- **Labour**, not in the model: a drone crew spends about 3–5 h of flying and charging per 4 mi road on each re-lay, and posts go in by hand on mined verges.
- **The minute going unused (T18).** Then the fence is worth close to nothing. The posts don't depend on it.

</details>

<details class="layer" id="what-it-misses" markdown="block">
<summary><span class="layer-title">What it misses</span><span class="layer-sub">Parked drones, launches on foot, far landings, jammers, cut fibers, our own drones</span></summary>

| Gap | What happens | What helps | Status |
|---|---|---|---|
| **Drones parked before the guard went in** | Never heard: they don't fly again until they strike | Search the road once after laying | Procedure |
| **Drones carried in on foot** and launched near the road | Cross no fence. In the model a post hears it lift off about 1 s before it strikes | Patrols; nothing in the guard | Not fixable by the guard |
| **Landings more than about 600 ft from the road** | Known to be inside, not where | A second row of posts, or posts on both sides | Not modelled |
| **The convoy's own jammer** | A vehicle jammer covering 900 MHz blinds the truck's receiver and posts within about 900 ft, on the move, when it matters | Posts on a cable with lamps facing the road: modelled, 100% on the main estimate | Proposed; T19 at range |
| **The truck's jammer reaching the fence** | In the worst case for jamming, darts a mile out can't relay while it passes | Fiber trunks (now the plan) keep 21–46% of tracks; a jammer off on a hot stretch keeps the rest | Unknown until T19 |
| **A cut fiber** | Shelling, vehicles or people cut a fiber lying a mile across the ground. Guessed at 1% of days each | The tip still relays by radio to the next tip, so no single cut costs a track in the model. The heartbeat shows the cut within 30 s; a new tip is laid on its own sortie | Modelled; T21 |
| **A cut cable** | Shelling or traffic cuts the cable along the verge | Posts fall back to radio; the roll call finds the break | Not costed |
| **Our own drones** | Our drone crews live in this strip and cross the fence both ways all day | A cheap beacon on our drones that darts recognise; flight corridors and times (T15) | Not designed |
| **Traffic noise** | A convoy passing may deafen a post just when a drone lands near it | The fence is far from traffic; landings usually come before the traffic | T20 |
| **Drones from behind,** past 60° | The back of the road is open | Fence at 75° costs about 1 more dart a mile | A choice |
| **Posts on the verge** | Mines, traffic, scavenging. Assumed lost 1% of days | Stakes set back from the edge; the roll call | Guess |
| **A shot-down drone looks like a landing** | A false "waiting" alert | Check it anyway; it is cheap to look | Accepted |

</details>

<details class="layer" id="what-has-to-be-tested" markdown="block">
<summary><span class="layer-title">What has to be tested</span><span class="layer-sub">T20 landings by a road, T21 fiber cuts, T9 whips, T19 vehicle jammers, lamps, drivers</span></summary>

- **T20 (new): hear a landing beside a road.** Fly an FPV-size quad in, land it 50–600 ft from a post, and cut the motors, with and without trucks passing. Does the post tell "landed" from "flew out of range", and how far does a passing truck cut its hearing?
- **T21 on a road:** lay a tip's fiber from a post a mile out across the ground beside a road, and count how often vehicles, people and weather cut it (1% of days assumed).
- **T9 with whips:** the post-to-post hop on 2 ft whips, which this page assumes reaches about 2,500 ft.
- **T19 with a vehicle jammer,** as well as a trench jammer, and at range: how far from a jammer does a post or a dart still receive? That number decides whether the fence works beside a jamming convoy.
- **A lamp drivers can see and drones can't:** how well does a hood hide it from above?
- **T18 with drivers and medics:** would they hold or stop on a "hot" board, and how far from the road do waiting drones actually land?
- T11 and T12 decide the count and the bill, as for the position net. T12 now includes a winter of solar harvest, on a dart's flat panel and on a post's tilted one.

</details>
