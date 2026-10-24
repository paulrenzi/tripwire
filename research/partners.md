---
title: Partners for the alert
parent: Research Notes
nav_order: 0.4
nav_primary: 3.1
nav_label: Partners
---

# Partners: getting the alert to troops on the move
{: .no_toc }

<p class="vz-lede">The people who need a road alert are walking or driving it. <strong>Put our alert on a device they already trust</strong>, not a new box. First step: ask the Hrafit team whether they take outside sensor feeds.</p>

<div class="vz-ladder">
  <a class="vz-rung" href="#hrafit-and-sova"><span class="vz-rung-n">1</span><span class="vz-rung-q"><strong>Hrafit's Sova</strong> <span class="vz-rung-meta">already pushes FPV alerts to drivers' phones along their route · best fit</span></span><span class="vz-chip vz-chip-done">target</span><span class="vz-rung-tot">first</span></a>
  <a class="vz-rung" href="#delta-and-atak"><span class="vz-rung-n">2</span><span class="vz-rung-q"><strong>TAK, and through it Delta</strong> <span class="vz-rung-meta">a gateway turns each alert into a Cursor-on-Target message</span></span><span class="vz-chip vz-chip-open">fallback</span><span class="vz-rung-tot">next</span></a>
  <a class="vz-rung" href="#meshtastic"><span class="vz-rung-n">3</span><span class="vz-rung-q"><strong>Meshtastic handhelds</strong> <span class="vz-rung-meta">a vehicle receiver re-sends each alert as a text</span></span><span class="vz-chip">maybe</span><span class="vz-rung-tot">later</span></a>
  <a class="vz-rung" href="#chuyka"><span class="vz-rung-n">4</span><span class="vz-rung-q"><strong>Chuyka</strong> <span class="vz-rung-meta">the radio detector we sit beside; no way in today</span></span><span class="vz-chip">partner</span><span class="vz-rung-tot">beside</span></a>
</div>
<p class="vz-bar-note">Our own receiver stays for units with none of these. Goes with <a href="{{ site.baseurl }}{% link models/route-guard.md %}">Guarding a road</a>. Reviewed 2026-10-23.</p>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">Who needs the alert, and the recommendation</span></summary>

The people who need a road alert are the ones walking or driving it, not someone at a checkpoint screen. This page asks what they already carry that our alerts could ride on, so they get one warning on a device they trust instead of a new box. It goes with [Guarding a road]({{ site.baseurl }}{% link models/route-guard.md %}) and [Central API and military integration]({{ site.baseurl }}{% link research/integration.md %}). Reviewed 2026-10-23.

{: .important }
> **Target Hrafit's Sova module first.** It already pushes FPV alerts to drivers' phones along their route, and it is built from radio intelligence, so it should share the fiber-optic blind spot we fill. Build a TAK output as the fallback that also reaches Delta. Keep our own receiver for units with neither. **First step: ask the Hrafit team whether they take outside sensor feeds.**

</details>

<details class="layer" id="the-candidates" markdown="block">
<summary><span class="layer-title">The candidates</span><span class="layer-sub">Each partner: what troops do with it, how our alert gets in, fit, and what's missing</span></summary>

| Partner | What troops do with it | How our alert would get in | Fit | What's missing |
|---|---|---|---|---|
| **Hrafit / Sova** | A phone push alert when an FPV or glide bomb approaches. Sova is for "logistics crews, drivers, and medical evacuation" and moves its watch area with the vehicle | A gateway at a checkpoint, or in a vehicle with Starlink, posts our alerts to Hrafit | **Best.** Same users, same job, and our alert shows against the route on the phone | No public interface found. A partnership, not a plug-in |
| **Delta** | The army's map: air, ground and naval picture, messenger, streams | Through TAK, which Delta already links to, or a direct feed via the Ministry of Defence | Commanders and checkpoints more than a driver in the moment | No developer route found |
| **ATAK** | A map app; takes Cursor-on-Target (CoT) position and alert messages | A small gateway turns each alert into a CoT message. Outside sensors do this routinely | **The realistic technical route,** and a way into Delta | How many Ukrainian units run ATAK itself: not found |
| **Meshtastic handhelds** | Texts and position sharing on cheap LoRa radios | A vehicle receiver re-sends each alert as a Meshtastic text, so anyone on foot with one gets a buzz | Closest to our hardware: our boards are sold as Meshtastic kits | Thin, second-hand evidence of use. The receiver would transmit, breaking "a truck gives nothing away". We'd write our own sender, not use their GPL code |
| **Chuyka** | The most common warning device: sound and light alarm against radio FPVs. Now has a phone app that manages several detectors | Nothing today | A partner in the field, the [second box]({{ site.baseurl }}{% link research/competitors.md %}) beside ours | No wired alarm output or third-party protocol found. Shared alert data in its app is only a stated plan |

</details>

<details class="layer" id="hrafit-and-sova" markdown="block">
<summary><span class="layer-title">Hrafit and Sova</span><span class="layer-sub">The phone alert for drivers and medics, and why it shares our blind spot</span></summary>

- **What it does:** "pulls together data from nearly all available radio-technical intelligence and surveillance into a single picture". On the ground, it "comes down to one short push notification", to the observation point, sector command and commander at once ([Euromaidan Press, Sep 2026](https://euromaidanpress.com/2026/09/05/from-hq-to-the-zero-line-ukraines-hrafit-system-answers-one-important-question-on-an-ordinary-phone-in-a-trench-and-on-the-road/)).
- **Who has it:** the army, National Guard, SBU and Border Guard. It runs on Android, iOS and the web, and needs a protected phone and satellite internet such as Starlink.
- **Why it fits:** its alerts already follow a moving vehicle, which is the job the road guard needs done. It also solves "where am I": a road alert names a stretch between posts, and a phone shows that against the route, where a bare receiver can't.
- **The gap we fill (inferred):** it lists FPVs, Mavic-type quadcopters, Molniya and Privet drones and glide bombs, and its sources are radio. The article doesn't mention fiber-optic FPVs. That it can't hear them is our inference from its sources, not a quote.
- **Unknown:** whether it accepts outside sensors, and in what format.

</details>

<details class="layer" id="delta-and-atak" markdown="block">
<summary><span class="layer-title">Delta and ATAK</span><span class="layer-sub">The army's map, and the technical route into it</span></summary>

- **Delta** takes data from drones, sensor networks, satellites and partners, is built to NATO standards, and is reported to link with Virazh, Kropyva, Hrafit and the US **ATAK** system, so an alert fed into Hrafit may reach Delta too ([Wikipedia](https://en.wikipedia.org/wiki/Delta_(situational_awareness_system)), [Ukraine's Arms Monitor](https://ukrainesarmsmonitor.substack.com/p/combat-software-in-the-service-of), [Armada International](https://www.armadainternational.com/2024/10/ukraine-delta-system-milcom/)). No developer route was found; access runs through the Ministry of Defence.
- **ATAK** takes CoT, the format the [integration plan]({{ site.baseurl }}{% link research/integration.md %}) already names. A CoT output is the one piece we can build without anyone's permission, and it is the likeliest door into Delta.

</details>

<details class="layer" id="meshtastic" markdown="block">
<summary><span class="layer-title">Meshtastic</span><span class="layer-sub">Cheap LoRa handhelds, and how much they're used</span></summary>

- Ukrainian units are reported to use Meshtastic for texts and position sharing when other links are down, and a mesh to relay air-raid warnings ([Ukraine War Analytics](https://ukraine-war-analytics.com/cyber/mesh-networking-ukraine.html), [Meshtastic forum](https://meshtastic.discourse.group/t/using-in-ukraine/5685), [Hacker News](https://hn.nuxt.dev/item/47069724)). No official source confirms how widely.
- **The trade:** troops on foot get an alert on a radio some already carry, at no cost. But a vehicle receiver that re-sends is a transmitter, and that's a choice for the unit, not a default.

</details>

<details class="layer" id="chuyka" markdown="block">
<summary><span class="layer-title">Chuyka</span><span class="layer-sub">The radio detector, and why it has no way in today</span></summary>

- It sounds and flashes on radio-drone activity, and its phone app manages several detectors from one screen; syncing trigger data was a plan, not a feature ([BlueBird](https://www.blue-bird.tech/en/products/chuyka-4-0/), [Razom](https://razomua.media/en/news/tekhnolohiyi/smartfon-zamist-okremoho-prystroyu-chuyka-teper-keruyetsya-z-telefonu-i-bachyt-fpv-za-4-km)).
- No alarm output or protocol was found, so there's nothing to integrate today. If its app opens up, our alerts could appear beside its own on the same phone.

</details>

<details class="layer" id="next-steps" markdown="block">
<summary><span class="layer-title">Next steps</span><span class="layer-sub">Who to ask, in order</span></summary>

1. **Ask the Hrafit team** whether Hrafit or Sova takes outside sensor feeds, in what format, and whether fiber-optic FPVs are a known gap for them.
2. **Build a CoT output** on the checkpoint gateway: each alert as a TAK event naming the hot stretch. It needs no partner.
3. **Write a Meshtastic sender** only if a unit asks for it, and only as an option they switch on.
4. **Ask BlueBird** whether the Chuyka app will take outside alerts.

</details>
