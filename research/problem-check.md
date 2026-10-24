---
title: Is the problem worth solving?
parent: Research Notes
nav_order: 0.25
nav_tripwire: 3
---

# Is the problem worth solving?
{: .no_toc }

<p class="vz-lede">Before building more, check the premise: are units' current methods failing, would earlier warning change anything, and is someone already solving it? <strong>The case for the problem is strong; the size of the payoff is a guess.</strong></p>

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Failing? Yes</p><p>Drones are the biggest killer at the front. Troops survive by hiding and not moving, and fiber-optic FPVs defeat the detectors they carry</p></div>
  <div class="vz-card"><p class="vz-card-num">Worth it? A guess</p><p>About <strong>1–4 of every 100</strong> drone casualties averted (range 0.3–14), almost all among people about to move (<a href="{{ site.baseurl }}{% link research/lives-model.md %}">estimate</a>)</p></div>
  <div class="vz-card"><p class="vz-card-num">Solved? Not forward</p><p>A Ukrainian firm sells acoustic FPV sensors, but at the position, giving seconds. Camera systems aren't at the front</p></div>
</div>

### Warning against a fiber-optic FPV

<div class="vz-bars">
  <div class="vz-bar-row"><span class="vz-bar-label">Nothing: seen at the last moment</span><span class="vz-bar-track"></span><span class="vz-bar-val">0 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">A sentry's ear</span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:2.7%"></span><span class="vz-bar vz-bar-them-light" style="width:0.7%"></span></span><span class="vz-bar-val">4–5 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">An acoustic sensor at the position <em>(makers' claims)</em></span><span class="vz-bar-track"><span class="vz-bar vz-bar-them" style="width:2.0%"></span><span class="vz-bar vz-bar-them-light" style="width:8.7%"></span></span><span class="vz-bar-val">3–16 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label">A radio detector <em>(hears only radio-controlled FPVs)</em></span><span class="vz-bar-track"></span><span class="vz-bar-val">0 s</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>A forward listener row</strong></span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:30.0%"></span><span class="vz-bar vz-bar-us-light" style="width:70.0%"></span></span><span class="vz-bar-val"><strong>45 s–2.5 min</strong></span></div>
  <p class="vz-bar-note">Warning = how far out the drone is detected ÷ its speed, at the worst-case 63–87 mph. A radio detector gives 1.5–2.5 min against radio-controlled FPVs, but nothing against fiber-optic ones. <strong>A minute isn't new; a minute against fiber-optic FPVs is.</strong> All estimates; the row's figure needs T11.</p>
</div>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">The three questions this page checks</span></summary>

Before building more, check the premise: are units' current methods failing, would earlier warning change anything, and is someone already solving it? Every point is sourced; where nothing was found, this page says so. Reviewed 2026-10-15.

</details>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">The case for the problem, and how many lives a forward line might save</span></summary>

**The case for the problem is strong.** Drones are the biggest killer at the front. Troops survive mainly by staying hidden and not moving, which is coping, not protection. The fastest-growing part of the threat, fiber-optic FPVs, defeats the cheap detectors units carry, and the expensive camera systems are not at the front. A Ukrainian firm is now building acoustic FPV sensors for positions, which supports the approach.

**Fiber-optic FPVs arrive unwarned.** Radio detectors can't hear them, so any earlier warning, at lower cost, fills a gap. How many lives that saves is a guess. Our central estimate: our estimate is that a forward line averts about **1–4 of every 100 drone casualties** (range 0.3–14), almost all among people about to move: rotation, resupply, evacuation ([estimate]({{ site.baseurl }}{% link research/lives-model.md %})). Weapons need only seconds, so at a fixed position a minute adds little. Interviews (T18) would firm up that number; they are not a gate.

</details>

<details class="layer" id="what-the-evidence-says" markdown="block">
<summary><span class="layer-title">What the evidence says</span><span class="layer-sub">Drones as the main killer, how units cope, the fiber-optic gap, and who else is working on it</span></summary>

### The threat is real and is the main killer

- **Drones cause about 80% of casualties**, according to analyst Rob Lee and others. Most casualties fall in the kill zone, a band roughly 10–20 miles deep on each side of the line ([NPR, 5 Oct 2026](https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)).
- **Tree-line positions are targets in themselves.** Incendiary drones are flown along tree lines to burn away the foliage troops hide in ([RUSI](https://www.rusi.org/news-and-comment/in-the-news/ukraines-fire-dropping-drones-can-find-shock-russian-troops-experts)). Night is no refuge: FPVs carry thermal cameras (same NPR report).
- **Fiber-optic FPVs are a large share in some sectors.** Estimates run from 30–50% of FPV operations in some sectors ([drone-warfare.com](https://drone-warfare.com/research/fpv-drone-warfare/), rated medium confidence there) to a claim of 90% of Russian attacks in one Kharkiv-region sector by a Ukrainian operator ([Gwara Media](https://gwaramedia.com/en/russians-expand-area-for-using-fiber-optic-drones-in-kharkiv-oblast-in-2026-military-says/)). No front-wide figure was found.

### What units do today, and how well it works

There is no single "current model", only coping measures. Against fiber-optic FPVs the baseline is **ears, eyes and a firearm**: they are detected "by ear and visually" and "You can only shoot it down" ([Gwara Media, Feb 2025](https://gwaramedia.com/en/border-guards-russian-troops-actively-use-fiber-optic-drones-resistant-to-jamming-north-of-kharkiv-oblast/)).

- **Hiding and not moving** is the main defence. One group took four hours to cover 0.6 mi, and some infantry have gone more than a year without rotation ([NPR](https://www.tpr.org/news/2026-10-05/drones-buzz-overhead-troops-hunker-underground-in-ukraines-hellish-kill-zone)).
- **Radio detectors**, the most common warning device, are blind to fiber-optic drones.
- **Jamming is failing.** A brigade EW company commander says "Jamming no longer works".
- **Nets** leak and burn.
- **Shotguns** now need 130–160 ft of distance against heavier FPVs.
- **An AI turret** that tracks fiber-optic drones is in more than 10 units.
- **Interceptor drones** are bought mostly against recon drones and Shaheds.
- **Cameras like Anduril's WISP** aren't at the front. The only published deployment is US domestic ([DroneXL](https://dronexl.co/2026/08/06/anduril-wisp-washington-national-guard-drones-birds/)), and they need line of sight, which tree lines block.

Item by item, with sources and what a listener adds to each: [What troops have, and what listening adds]({{ site.baseurl }}{% link research/frontline-kit.md %}).

### Is ten seconds enough?

**No published figure answers this.** No source we found says how many seconds of warning troops need, or measures what a detector's warning saves. Detector makers describe the value as seconds to find cover. The serious analyses argue for warning but don't measure it:
- **RUSI (Oct 2024)** says smoke against FPVs and Lancets is "highly effective" if the unit is warned promptly, and only with a low false-alarm rate. Neither claim has a footnote ([Watling & Bronk](https://afghanistan.wilsoncenter.org/sites/default/files/media/uploads/documents/protecting-the-force-from-uncrewed-uas.pdf), p.17).
- **RUSI (Feb 2025):** Ukrainian brigades report about half their casualties in the rear, during rotation, resupply and recovery ([Watling & Reynolds](https://static.rusi.org/tactical-developments-third-year-russo-ukrainian-war-february-2205.pdf)). Warning that covers only the position misses those.
- **An Israeli vendor's CEO** says "we just need 30 seconds warning" to take defensive action ([Ynet](https://www.ynetnews.com/article/s1oz79p011x)). That is a vendor's view, not a measurement.

How much each defence actually needs is worked through [below](#a-minute-against-the-alternatives).

### Someone is already building the near-unit layer

**ZVOOK NW0** (January 2026) is a Ukrainian acoustic FPV sensor for positions, on sale at about $834–950. It claims 490–1,500 ft range and fiber-optic detection, and draws 15–20 W. Every figure is the maker's; we found no independent test and no unit reported using it ([profile]({{ site.baseurl }}{% link research/competitors.md %}#zvook-nw0--direct-competitor-claims-only)). That's weak validation that a credible team thinks the approach is worth building, and it's competition. The US Army's March 2026 review says Ukrainian acoustic networks detect FPVs, but its sources cover Shaheds over the rear ([details]({{ site.baseurl }}{% link research/competitors.md %}#two-markets-only-one-of-them-ours)). Against FPVs at a position, acoustic detection is still unproven, for us and for Zvook alike.

</details>

<details class="layer" id="a-minute-against-the-alternatives" markdown="block">
<summary><span class="layer-title">A minute against the alternatives</span><span class="layer-sub">How much warning each defence needs, and what each source of warning gives</span></summary>

How much warning each defence needs, and so what a minute adds over the few seconds that other sources of warning already give.

### How much warning each source gives

Warning is the distance at which the drone is detected, divided by its speed. FPVs reach a top speed of about 87 mph ([ERR, Nov 2025](https://news.err.ee/1609861089/err-in-ukraine-up-close-with-ukraine-s-counter-drone-air-defense-teams)), so the figures below take 63–87 mph, the worst case. Loaded FPVs usually fly at 37–50 mph ([Kyiv Post](https://www.kyivpost.com/post/39057)), which makes every warning about 1.5–2 times longer ([the drones]({{ site.baseurl }}{% link research/threat-profile.md %})). They are our arithmetic, not measurements, and they ignore the second or two needed to recognise the sound.

| Source of warning | Detects at | Warning vs an FPV (est.) | Against fiber-optic FPVs? |
|---|---|---|---|
| None: drone seen at the last moment | — | 0 s | — |
| A sentry's ear | ~490 ft (Mavic-class, quiet field, [measured](https://www.mdpi.com/2076-3417/10/16/5501)) | ~4–5 s | Yes, if it is heard |
| Acoustic sensor at the position | 390 ft (DroneAlert) to 1,500 ft (NW0), both makers' claims | ~3–16 s | Yes, on the makers' claims |
| Radio detector (Chuyka 3.0) | Up to 2.5 mi, scanning every "4 to 8 seconds" ([Militarnyi, May 2025](https://militarnyi.com/en/news/ukraine-develops-chuyka-3-0-drone-video-signal-detector/)) | ~1.5–2.5 min | **No**: it hears only analog video |
| **Forward listener row** | About 1 mi out, deeper if wanted | **~45 s–2.5 min** | Yes, if the listeners hear it (T11) |

**A minute is not new. A radio detector already gives one against radio-controlled FPVs.** What is new is a minute against fiber-optic FPVs, where every other source drops to seconds.

### What each defence needs, and what each window buys

The middle column is sourced. The four right-hand columns are our inference from it. ✅ the window is enough; 🟡 helps partly; ❌ not enough; — makes no difference.

| Defence | What it needs (sourced) | 0 s | ~5 s | ~15 s | ~1 min |
|---|---|:-:|:-:|:-:|:-:|
| **Net-gun** | Range up to 82 ft, net open "within 0.2 seconds" ([MITLA-1, Ukrainska Pravda, Jul 2025](https://www.pravda.com.ua/eng/news/2025/07/12/7521456/)); up to 98 ft, 2 s reload ([Ptashka 2.0, Mezha](https://oboronka.mezha.ua/en/ptashka-drones-predstavila-sitkomet-ptashka-2-0-310877/)). At FPV speed that is about one second of flight in range | 🟡 last ditch | ✅ in hand, facing it | ✅ | — |
| **Shotgun or rifle** | 33–49 ft from a large FPV is "life-threatening"; shoot from at least 130–160 ft, rifles at 160–330 ft ([Militarnyi, Jun 2026](https://militarnyi.com/en/news/shotguns-ineffective-15-inch-fpv-drones/)). That is about 1–4 s of flight in range | 🟡 reflex | ✅ weapon up | ✅ facing the right way | 🟡 team moves to the threatened side |
| **AI turret** | Detects and tracks itself; the operator "only needs to confirm engagement with a single button press" ([Ukrinform, May 2026](https://ukrinform.net/rubric-ato/4121457-ukraines-defense-minister-shows-ai-turret-used-in-combat-to-intercept-drones-on-battlefield.html)). In more than 10 units by May 2026. Scan Horizon, a net-firing demonstrator, hears drones at up to 66 ft ([Defense Post](https://thedefensepost.com/2026/05/08/ukraine-autonomous-net-turret/amp/)). Reaction time and whether it takes outside cues: not published | 🟡 on its own sensors | — | — | 🟡 only if it accepts cues |
| **Smoke** | "highly effective if the unit being targeted can be warned promptly"; no seconds given ([RUSI, Oct 2024](https://static.rusi.org/protecting-the-force-from-uncrewed-uas.pdf)). It "risks drawing Russia's attention" ([Business Insider, Dec 2025](https://www.aol.com/articles/hunted-drones-ukrainian-forces-hide-113401181.html)) | ❌ | 🟡 a screen may not be up in time | ✅ probably | ✅ |
| **Get under cover** | No published distance to shelter or time to reach it. On foot at 7–11 mph (our assumption), 5 s covers ~49–82 ft and 1 min ~660–980 ft | ❌ | 🟡 next to a dugout | 🟡 within ~160–250 ft | ✅ off a path and under cover |
| **Hold a movement** (vehicle run, resupply pickup) | Russian roadside "traffic lights" (yellow means "a distant drone detection") let drivers "navigate risky areas at safer times" ([Espreso, Dec 2024](https://global.espreso.tv/russia-ukraine-war-russia-installs-traffic-lights-to-counter-ukrainian-fpv-drones)) | ❌ | ❌ | ❌ | ✅ don't set off; stop under cover |
| **Casualty evacuation** | Troops "often have to wait for nighttime, fog, or rain" to evacuate; the golden hour has become a "golden day" ([Business Insider, Dec 2025](https://www.aol.com/articles/hunted-drones-ukrainian-forces-hide-113401181.html)) | ❌ | ❌ | ❌ | 🟡 may let a team move between drones rather than wait for dark; unproven |
| **Interceptor drone** | Piloted "using VR goggles", over 99 mph, built for Shaheds ([Militarnyi, Oct 2024](https://militarnyi.com/en/news/ukrainian-engineers-launch-sting-interceptor-against-shahed-drones)). No published time from cue to launch, and no verified kill of an FPV attacking a position | ❌ | ❌ | ❌ | 🟡 only with one on the pad and a pilot ready; also needs a track, which a line crossing doesn't give |
| **Laser** (Tryzub) | FPVs at around 2,600–3,000 ft, with radar integration ([Euromaidan Press, May 2026](https://euromaidanpress.com/2026/05/08/tryzub-laser/)). Time needed on target: not published. Rare at the front | ❌ | ❌ | 🟡 | 🟡 cue to slew, if one is present |
| **Nets, net tunnels, cable traps** | Always up. Ukraine plans another 2,500 mi of net-covered road by the end of 2026 ([Liga.net, Feb 2026](https://news.liga.net/en/politics/news/another-4000-km-of-roads-will-be-covered-with-anti-drone-tunnels-in-ukraine-by-the-end-of-the-year-photo)) | ✅ | — | — | — |
| **Jamming** | Triggers the drone's own fail-safe by drowning its radio and GNSS links. Crews use detectors to decide when to switch jammers on ([Foreign Policy, Aug 2024](https://foreignpolicy.com/2024/08/05/ukraine-russia-war-drone-detectors-jamming-tsukorok/)); site jammers such as CERBAIR MEDUSA are built to be switched on by a detector's cue ([spec sheet](https://comsecfl.com/wp-content/uploads/2022/04/Specsheet_Medusa.pdf)). **No effect on fiber-optic FPVs**, and losing ground against radio ones: "Jamming no longer works" (EW company commander, [Euromaidan Press, Jun 2025](https://euromaidanpress.com/2025/06/26/is-the-electronic-warfare-era-over-a-frontline-ew-officers-story-of-ukraines-drone-tug-of-war)) | ❌ | 🟡 radio FPVs only | ✅ radio FPVs only | ✅ radio FPVs only; less time transmitting |

### What this shows (inference)

- **Weapons need seconds, not a minute.** A net-gun, shotgun or rifle has about 1–4 seconds of the drone's flight in range. A few seconds' warning gets the weapon up and facing the right way; more adds little. A sensor at the position, if it works and gives a bearing, already covers most of that. **The minute is not a weapons cue.** The tripwire should not be pitched as one.
- **The minute buys one thing nothing else gives against fiber-optic FPVs: a go/no-go call on exposure.** Don't set off, stop the vehicle under cover, hold the resupply pickup, get the walkers off the path. Seconds can't do this; only something 0.6–2.5 mi out can.
- **Someone already pays for this.** Russia's roadside traffic lights exist to time movement around drones. That is the same job as a forward line, done for roads.
- **Above a minute, units fall back on hours.** Evacuations wait for night, fog or rain. A minute's warning competes with that free, slow default. Whether units would trade it for faster moves between drones is exactly what T18 must ask.
- **Always-on defences need no warning at all.** Nets, net tunnels and cable traps are scaling fast, and anything a minute protects must be outside them.

**Pairing, not replacing:** a forward line for go/no-go decisions, and the ear, a radio detector or a sensor at the position for the last seconds a weapon needs.

**In lives:** our central guess is that the line averts about 1–4 of every 100 drone casualties in a unit that uses it (range 0.3–14), almost all among people about to move. See [What the line gains in lives]({{ site.baseurl }}{% link research/lives-model.md %}) and [what troops already have]({{ site.baseurl }}{% link research/frontline-kit.md %}).

{: .warning }
> Almost every timing here is inference. No source gives the seconds of warning a defence needs, the time to reach cover, the time to build a smoke screen, or the time from cue to interceptor launch. A shallow search also found nothing on Scan Horizon or Sky Sentinel reaction times. These are T18 questions.

</details>

<details class="layer" id="what-would-make-it-a-waste" markdown="block">
<summary><span class="layer-title">What would make it a waste</span><span class="layer-sub">Four findings that would kill or re-aim the tripwire</span></summary>

Any of these, found by asking users or by testing:

1. **Warning doesn't change behaviour.** Troops stay hidden by default, hear drones themselves in time, and would not act differently with a minute.
2. **Exposure is mostly on the move, not at positions.** Then the tripwire must be re-aimed: lines along approach paths and covered footpaths to warn walkers, not around a position. That is a change of aim, not a dead end (inference).
3. **A cheap enough sensor is already in units' hands**, such as the NW0 at scale.
4. **Radio can't get out of the trees**, even with a [wired edge receiver]({{ site.baseurl }}{% link models/tripwire.md %}#getting-alerts-out-of-the-trees) (T9, T17).

</details>

<details class="layer" id="the-next-step-ask-before-building-t18" markdown="block">
<summary><span class="layer-title">Questions for front-line users (T18)</span><span class="layer-sub">Who to ask, and the questions, before building more</span></summary>

Talk to 5–10 people with recent front-line experience: soldiers, the volunteers who equip units, Brave1, and Ukrainian drone and EW firms. Ask:

1. When are you most exposed to FPVs: in position, on rotation, at resupply pickups, observing?
2. How do you know a drone is coming now, and how much warning does that give? Which of radio detector, jammer, shotgun team, turret and interceptor do you have, and which do you trust?
3. What would you do differently with 10 seconds, one minute, three minutes? Would you hold a resupply pickup, a vehicle run or an evacuation? Would shooters or a turret be ready?
4. Roughly what share of FPVs attacking you are fiber-optic?
5. Would you place 10 listeners by hand, or accept a receiver on a pole at your tree-line edge?
6. Who decides what kit a unit gets, and who pays: the unit, volunteers, or the state?
7. Is your position in a windbreak, a forest, a field or ruins?
8. Roughly how far is it from the tree edge that faces open ground?
9. What share of your drone casualties happen on the move, and how many come from drones already waiting by the road?

**Not a gate.** Warning of a threat nothing else detects is worth having. The answers size the [lives estimate]({{ site.baseurl }}{% link research/lives-model.md %}) and shape placement.

</details>
