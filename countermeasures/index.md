---
title: Countermeasures
nav_primary: 3.2
permalink: /countermeasures/
---

# Countermeasures
{: .no_toc }

<p class="vz-lede">The tripwire warns. This section asks what the warning can <em>do</em>, without anyone standing up to shoot. <strong>Today a fiber-optic FPV is often stopped with a shotgun at close range.</strong> Its weak point is the hair-thin line it leaves lying on the ground behind it.</p>

<div class="stats">
  <div class="stat"><p class="stat-num">1.9–13 lbf</p><p class="stat-label">what it takes to break the fiber: about 2 lbf at its proof test, up to 13 lbf on vendors' claims</p></div>
  <div class="stat"><p class="stat-num">Goes dark</p><p class="stat-label">a fiber FPV with no radio backup when its line is cut; with a backup, it falls to jammers</p></div>
  <div class="stat"><p class="stat-num">2</p><p class="stat-label">Ukrainian cutting fences already fielded: a rotating barbed wire, and Logika's Chaharnyk</p></div>
  <div class="stat"><p class="stat-num">0</p><p class="stat-label">of our countermeasures tested: everything here is research and models</p></div>
</div>

### What troops use against a fiber FPV today

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Shotgun</p><p>At the drone itself, at close range. It "requires a mix of skill and luck", and someone has to be up and exposed.</p></div>
  <div class="vz-card"><p class="vz-card-num">Scissors</p><p>Troops cut every fiber they find, friend or foe. That works on lines already lying around, not on a drone that's on its way in.</p></div>
  <div class="vz-card"><p class="vz-card-num">Cutting fences</p><p>A barbed wire that turns, or hooks pulled along a fence 31 in tall. Each hears the drone and breaks the line where it lies. They're fielded, but not independently tested.</p></div>
</div>

### Pages in this section

<div class="vz-cards vz-2">
  <div class="vz-card"><p class="vz-card-num"><a href="{{ site.baseurl }}{% link countermeasures/fiber-cutter.md %}">The fiber cutter</a></p><p>A moving loop of polyester packing strap about 32 in up, with a plastic fin every 4 ft. When the tripwire hears a drone, the strap moves, a fin's V slot grabs the slack fiber lying across it, and a guarded blade at the next rod cuts it, within 17 s. About $995 a mile in parts. Its best job is on a road, cutting the line of a drone parked and waiting.</p></div>
  <div class="vz-card"><p class="vz-card-num"><a href="{{ site.baseurl }}{% link countermeasures/laser.md %}">The laser</a></p><p>Can a laser burn through the line "for a moment"? Only about 100 W, held on a spot you already know. It works against a drone parked by a road: a beam looped around it must cross its line. It takes 40–200 s from a road post, and it brings fire and eye risks. Blinding the drone's camera with a $120 diode is a cheaper first step.</p></div>
  <div class="vz-card"><p class="vz-card-num">More to come</p><p>Handing a drone whose line has been cut over to the unit's jammers, and anything else the alert can trigger without putting a person in the open.</p></div>
</div>

## The details

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="why-the-fiber" markdown="block">
<summary><span class="layer-title">Why go after the fiber</span><span class="layer-sub">Why the line is the weak point, and what a cut does</span></summary>

**Jammers can't touch a fiber FPV, but its line can be cut.** It is steered and sees through a glass fiber about 0.01 in thick (0.25–0.28 mm) that it pays out behind it, 6–30 mi of it on a spool ([Made-in-China listing](https://fibconet.en.made-in-china.com/product/VaKRyjNAyCkS/China-Drone-Fiber-Optic-0-27mm-Outer-Diameter-G657A2-Cable-Fpv-Fiber-Optic-Bare-Cable.html), [Zion](https://www.zion-communication.com/90KM-FPV-Drone-Fiber-Optic-Spool-FPV-Drone-Anti-Jamming-Optical-Fiber-Link-pd504050048.html)). The line isn't carried through the air. It lies on the ground and the vegetation behind the drone ([Militarnyi](https://militarnyi.com/en/news/russians-discover-ukrainian-solution-to-fiber-optic-drones/)), so anything low across the drone's path ends up under it.

**It breaks easily.** The glass is proof-tested at about 100 kpsi ([Corning](https://www.corning.com/content/dam/corning/microsites/coc/oem/documents/specialty-fiber/AN7080-Determining-the-Appropriate-Prrof-Test-Level-for-G.pdf)). On a 125 µm fiber that is about 8.5 N, or 1.9 lbf (our arithmetic). Vendors claim 50–60 N, about 11–13 lbf, for their FPV fiber (unverified).

**What a cut does depends on the drone:**
- **With no radio backup, it goes dark.** The crew loses video and control. The drone has no return-to-home, so it comes down where it is, sometimes still carrying its warhead ([DroneXL](https://dronexl.co/2026/03/23/ukraine-fiber-optic-fpv-drones-radio-cable/)).
- **With a radio backup, it switches to radio.** Ukraine has tested a dual-link FPV that costs about $60 more (UAH 2,500), and Logika says many Russian fiber FPVs carry one ([RFE/RL](https://www.rferl.org/a/ukraine-russia-invasion-fpv-drone-defence-cable-cutting-chaharnyk/33867913.html)). On radio, the drone is open to jamming again. A cut and the unit's jammer work together: the cut forces the drone onto the radio, and the jammer takes it down.
- **Too late if it's already diving.** A Chinese assessment of a similar fence noted that a cut doesn't stop the drone's momentum ([RFE/RL](https://www.rferl.org/a/ukraine-russia-invasion-fpv-drone-defence-cable-cutting-chaharnyk/33867913.html)). The cut has to come well before the drone reaches its target. We found no source on fiber FPVs locking onto a target and finishing alone after a cut.

</details>

<details class="layer" id="whats-already-out-there" markdown="block">
<summary><span class="layer-title">What's already out there</span><span class="layer-sub">Every fielded or reported way to cut the line, with its claims</span></summary>

| What | How it works | Size and claims | Source |
|---|---|---|---|
| **Scissors** | Troops cut every fiber they see. Some units require every team member to carry a pair | Cuts lines already lying around: troops can't tell a new line from an old one | [Business Insider via Yahoo](https://www.yahoo.com/news/articles/ukrainian-soldiers-armed-scissors-cut-130657111.html) |
| **Rotating barbed wire** (makeshift, reported Oct 2025) | A barbed wire strung on supports, turned by a motor. Any fiber lying on it winds up and breaks | About 490 ft (150 m), on a battery and a small controller. It runs for a minute, then rests for a minute: 12 h a day. Set up by hand, so it protects rear positions and supply roads, not the front line | [Militarnyi](https://militarnyi.com/en/news/russians-discover-ukrainian-solution-to-fiber-optic-drones/), [Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/ukraine-deploys-rotating-barbed-wire-fences-to-counter-fibre-optic-drones/) |
| **Chaharnyk** ("Shrub"), Logika Design Bureau (announced Sept 2026) | Hears the drone's motors and props, then motors pull hook-studded wires through a break zone | 31 in (80 cm) tall, like a livestock fence. Up to 330 ft (100 m) a unit and about 0.6 mi (1 km) linked. Reacts in 1 s. Claims at least 95% cuts after contact, from demonstrations. Run from a tablet in the Kropyva suite. "Dozens" sent to the front by Oct 1. Price, weight and power not published | [UNN](https://unn.ua/en/news/in-ukraine-the-chahar-barrier-was-created-which-cuts-fpv-drones-fiber-optic-cables-in-one-second), [RFE/RL](https://www.rferl.org/a/ukraine-russia-invasion-fpv-drone-defence-cable-cutting-chaharnyk/33867913.html) |
| **Shotgun** | Shoots the drone itself | Needs someone up and in the open, at close range | [Business Insider via Yahoo](https://www.yahoo.com/news/articles/ukrainian-soldiers-armed-scissors-cut-130657111.html) |

**What critics say about cutting fences.** A pilot who knows where one stands can fly around it. A single fence shows where the defenders are, and is a target itself. It can also get in the way of the defenders' own movement. Logika's head says: "We're not claiming that Chaharnyk will keep everyone safe" ([RFE/RL](https://www.rferl.org/a/ukraine-russia-invasion-fpv-drone-defence-cable-cutting-chaharnyk/33867913.html)).

</details>

<details class="layer" id="where-the-tripwire-fits" markdown="block">
<summary><span class="layer-title">Where the tripwire fits</span><span class="layer-sub">What our alert adds to a cutter, and what a cutter adds to our alert</span></summary>

- **The cutting itself is not new.** Chaharnyk and the rotating wire already break the line. A cutter of our own has to beat them on cost, or on doing something they can't.
- **What our alert adds: about a minute of warning, and knowing a drone is parked and waiting.** Chaharnyk hears a drone only as it reaches the fence. The tripwire hears it about a mile out, so the cutters on the right stretch can be ready before it arrives. On a road, the posts hear a drone land and wait ([Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %})). Its line is then lying across any cutter between it and its pilot, with no rush, and cutting it is a sure thing.
- **What a cutter adds to our alert: something it can trigger with nobody exposed.** "Drone waiting near post 17" now leads to the cutter between the drone and its pilot running, not to a team going out with a shotgun.

</details>
