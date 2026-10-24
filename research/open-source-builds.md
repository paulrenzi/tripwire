---
title: Open-source projects to build on
parent: Research Notes
nav_order: 1.5
---

# Open-source projects to build on
{: .no_toc }

<p class="vz-lede">Three public projects already cover parts of the tripwire. <strong>None does bearings, fusion, military map output or forward placement</strong>, which is where this project adds something.</p>

<div class="vz-cards">
  <div class="vz-card"><p class="vz-card-num">Batear</p><p>A single-mic detector and LoRa gateway on an ESP32-S3: <strong>our starting firmware</strong></p><p><span class="vz-chip vz-chip-done">MIT</span> <span class="vz-chip">active</span> <span class="vz-chip vz-chip-open">no range published</span></p></div>
  <div class="vz-card"><p class="vz-card-num">VolAnti</p><p>A four-mic unit with a local alarm: <strong>real range data</strong>, 340 ft on a hovering quad, and a tested cheap design</p><p><span class="vz-chip vz-chip-done">Apache / CERN-OHL</span> <span class="vz-chip">active</span></p></div>
  <div class="vz-card"><p class="vz-card-num">AcousticPrint</p><p>Machine-learning code for identifying drones: <strong>method ideas and labelled data</strong></p><p><span class="vz-chip vz-chip-open">no licence</span> <span class="vz-chip">dormant since 2020</span></p></div>
</div>

<p class="vz-done">The last section turns them into a <a href="#weekend-test-kit-start-training-the-detector">weekend test kit</a> for collecting training audio; the steps are on <a href="{{ site.baseurl }}{% link weekend-test.md %}">the Saturday test</a>.</p>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">What the three projects cover, and what none of them does</span></summary>

Three public projects already cover parts of what this site proposes. Two are working low-cost detectors on the same chip family we picked; one is academic code for telling drones apart. None of them does bearings, fusion, military map output or forward placement, which is where this project would add something. The last section turns them into a [weekend test kit](#weekend-test-kit-start-training-the-detector) for collecting training audio.

</details>

<details class="layer" id="at-a-glance" markdown="block">
<summary><span class="layer-title">At a glance</span><span class="layer-sub">The three projects side by side: hardware, detection, range, links, licence, activity</span></summary>

| | Batear | VolAnti | AcousticPrint |
|---|---|---|---|
| **What it is** | Single-mic detector node + LoRa gateway | Four-mic detector unit with local alarm | Machine-learning code for drone identification |
| **Hardware** | ESP32-S3 + one MEMS mic (ICS-43434 or INMP441) | ESP32-S3, four digital mics, own 4-layer PCB, printed case | Shotgun mic (RØDE NTG4) for recordings; runs on a PC |
| **Detection** | FFT harmonic ladder | Propeller harmonic pattern | ML classifier that rejects unknown sounds |
| **Range published** | None | **340 ft** (one test, hovering quad) | n/a |
| **Bearing / position** | No | No (mics are summed for gain) | No |
| **Links** | LoRa star to gateway, or Ethernet/PoE; MQTT, Home Assistant | LoRa alerts between units | None |
| **Licence** | **MIT** | Apache-2.0 firmware, CERN-OHL-W-2.0 hardware, CC BY-SA docs | **None stated** |
| **Activity** | Active (last push 2026-10-06), ~425 stars | Active (last push 2026-09-20), ~416 stars | Dormant since May 2020, 5 stars |
| **Best use for us** | Starting firmware for a tripwire node | Real range data and a tested low-cost unit design | Method ideas and labelled data |

</details>

<details class="layer" id="batear" markdown="block">
<summary><span class="layer-title">Batear</span><span class="layer-sub">The MIT single-mic detector we'd fork, and what it lacks for our use</span></summary>

**[github.com/batear-io/batear](https://github.com/batear-io/batear)**: an open-source, edge-only acoustic drone detector built on the ESP32-S3. No cloud and no subscription.

**How it detects:** it samples one microphone at 16 kHz, runs a 1024-point FFT (15.6 Hz per bin) and looks for a fundamental between 180 and 2,400 Hz with matching peaks at 2× and 3× that frequency, the harmonic "ladder" that spinning rotors make. A 0–1 confidence score combines signal-to-noise and harmonic ratios with smoothing. An alarm needs 2 positive frames in a row and clears after 8 negative ones. The whole scan takes well under 10 ms per frame.

**How it reports:** each detector sends an AES-128-GCM-encrypted, 36-byte packet over 915 MHz LoRa to one gateway, which forwards it to MQTT and Home Assistant. A wired version uses Ethernet or PoE, with a REST API and over-the-air updates. It can also record the audio around each alarm to an SD card, and reports battery voltage in every packet.

**What we'd take:**

- It is close to a **[tripwire]({{ site.baseurl }}{% link models/tripwire.md %}) node already**: one cheap mic, an ESP32-S3, LoRa, encryption and tiny packets. The MIT licence means we can build on it commercially with almost no conditions.
- The alarm recordings are a ready-made way to **collect labelled field audio**, which is our real bottleneck ([Training data]({{ site.baseurl }}{% link research/datasets.md %})).
- Its harmonic detector is a sensible first stage before a learned classifier.

**What it lacks for our use:** no direction or position; a star network, not a mesh, so no hop-by-hop relay back from a forward line; no GPS; the ESP32-S3 runs the FFT continuously, which is not a weeks-on-a-battery design; output goes to Home Assistant, not TAK or Lattice; and no published range. Field testing in Ukraine is described as planned, not done.

</details>

<details class="layer" id="volanti" markdown="block">
<summary><span class="layer-title">VolAnti</span><span class="layer-sub">The four-mic unit with a published 340 ft test, and its range against wind</span></summary>

**[volantitech.com](https://volantitech.com/)** · [github.com/agamrossen/VolAnti](https://github.com/agamrossen/VolAnti): an open-hardware acoustic detector designed and tested by Agam Rossen, an engineering student at the University of York. It is one person's project, not a company.

**The unit:** a 3.6 in square, four-layer board with four digital microphones sampled at 16 kHz, in a printed case, with a beeper, light, vibration motor and an e-paper screen that keeps the alert showing with the power off. Units send 18-byte LoRa alerts to each other. The full unit is listed at **£50–80**, a breadboard version at **£35–45**. It looks for the evenly spaced harmonics of propellers, so it works on fiber-optic drones.

**Why it matters to us: it publishes real range numbers.** One unit detected a hovering four-motor airframe at **340 ft** on a street with traffic, without alarming on the cars. Its expected range by wind:

| Wind | Expected range |
|---|---|
| Still air, under 4 mph | 330–660 ft |
| Light breeze | 160–390 ft |
| Breezy | 49–160 ft |
| Strong, upwind, over 18 mph | 16–82 ft |

That backs the low end of our [330–980 ft working estimate]({{ site.baseurl }}{% link research/range-and-cost.md %}) for small quads and shows how hard wind cuts it. For the tripwire it means node spacing may need to be **closer than 660–980 ft** in windy country, or nodes need better windscreens and height.

Nine units were built and sent to an unnamed site in September 2026.

**What we'd take:**

- Its **range-versus-wind table** as a starting point for our own measurements.
- Its **four-mic board** as a sensitivity trick: summing four mics gives about 6 dB for free. It is **not** a bearing board. The author tried beamforming and found that at 3.1 in across it buys nothing, because the array is a tenth of a wavelength at rotor frequencies. Bearings need mics spread much wider, as in [M1]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}).
- Its printed enclosure and local alarm ideas for hand-placed rings.

**Cautions:** the author's own disclaimer says it is not a life-safety product, has had no certification, and that the firmware, written in a month, is the least mature part, with false alarms indoors on some music and fan-like noise. The hardware licence (CERN-OHL-W) asks that changes to the board design be shared under the same licence, which matters if we sell a modified board. The author also says VolAnti was never made for or with any military and will never include countermeasures; the licences still allow reuse, but any military use of a derived design should credit it and keep its name off.

</details>

<details class="layer" id="acousticprint" markdown="block">
<summary><span class="layer-title">AcousticPrint</span><span class="layer-sub">Academic drone-identification code, dormant</span></summary>

**[github.com/AcousticPrint/AcousticPrint](https://github.com/AcousticPrint/AcousticPrint)**: research code from an academic team (Kolamunna, Li, Dahanayake, Seneviratne, Thilakaratne, Zomaya, Seneviratne) that builds acoustic "signatures" for drone classes and flags sounds that match **no known class** as outliers.

**Data:** recordings of five commercial drones (Parrot Bebop 2, DJI Mavic Pro, Phantom 4, Spark, Matrice 100) flown about 66 ft up, plus clips of four more from YouTube, and non-drone sounds (road vehicles, bees, speech, quiet background), with amplitude and time-stretch augmentation.

**What we'd take:** the **open-set idea**. In the field most sounds are neither a known drone nor silence, and a classifier that can say "I don't know this sound" is the right shape for keeping false alarms down. The non-drone recordings are also useful negatives.

**Cautions:** no licence is published, which by default means **we may not reuse the code**; reading it for ideas is fine, and we'd need the authors' permission to copy it. The repository has been dormant since 2020, states no accuracy figures, and covers consumer camera drones, not FPVs or Shaheds.

</details>

<details class="layer" id="what-this-means-for-the-project" markdown="block">
<summary><span class="layer-title">What this means for the project</span><span class="layer-sub">What we take from each, and what nobody has published</span></summary>

- **The single detector node is largely solved in the open.** Two independent projects detect drones on an ESP32-S3 for well under $100. Hardware is not the moat, as the [wider-field overview]({{ site.baseurl }}{% link research/landscape.md %}) already argues.
- **What nobody has published** is what this site is about: bearings from cheap nodes, fusing many nodes into a track, relaying from forward lines, output to TAK and Lattice, and real combat recordings.
- **Fastest path to a prototype:** start tripwire nodes from Batear's MIT firmware, measure range against VolAnti's published numbers, and add open-set rejection along AcousticPrint's lines on our own data.
- These projects are also **free alternatives** a buyer could find. Anything we sell has to do clearly more than they do.

</details>

<details class="layer" id="weekend-test-kit-start-training-the-detector" markdown="block">
<summary><span class="layer-title">Weekend test kit: start training the detector</span><span class="layer-sub">What training needs, the parts, and the recommendation</span></summary>

The aim of a first weekend is not a finished node. It is **labelled recordings** of a drone at known distances, plus plenty of recordings of everything that isn't a drone, a first classifier trained on them, and a free baseline detector (Batear) to beat. Training data is the real bottleneck ([Training data]({{ site.baseurl }}{% link research/datasets.md %})), so the first test should start producing it.

{: .warning }
> Prices are rough US figures checked in October 2026 and change often. Check the listing before buying. Where a part has to ship from China, it won't arrive by this weekend; those parts are marked.

### What training needs, and what each part is for

| Training needs… | Because… | Covered by |
|---|---|---|
| **A drone to record** | No recordings, no model. Distance has to be known to label each clip | The drone, with its app's distance readout |
| **Recordings of everything else** | Most false alarms come from cars, mowers, wind, birds and generators. A model only learns to ignore what it has heard | The same recorders, left running when no drone is up |
| **A microphone at node height, out of the wind** | A mic in the grass hears much less, and wind noise is the biggest range-killer in VolAnti's tests | Tripod or light stand, fur windscreen |
| **A baseline detector to beat** | If a trained model doesn't beat a simple harmonic detector, it isn't worth the power it costs | Batear on two LoRa boards, plus mics |
| **Audio through the same cheap mic the nodes will use** | Phones filter and compress audio differently. A model trained only on phone audio may do worse on a MEMS mic | Step 2: a Batear recorder board (ships from China) |
| **Field power** | Nothing out there has a wall socket | Power banks |

### The parts

{% include kit-parts.html %}

**Free:** the phones you already have (one per recording spot), a laptop, Audacity for cutting and labelling clips, and Python (librosa plus scikit-learn or PyTorch) or Edge Impulse's free tier, which can export a model to run on an ESP32-S3.

### The recommendation

| Kit | What you buy | Cost |
|---|---|---|
| **Cheapest MVP (you have tripods, power banks and a drone to borrow)** | 2 XIAO ESP32S3 + Wio-SX1262 kits (bought; 2 Heltec V3 also work), 3 INMP441 mics, breadboard and jumpers, windscreens | **~$80–90** |
| **Full MVP (buy everything, including a drone)** | The above, plus 2 stands, 2 power banks and a DJI Mini 4K | **~$360–480** |
| Step 2, ordered now for later | T-ETH-Lite S3 and a microSD card | ~$25–35 |

The two LoRa kits are already bought ([Rokland, $15.97 each](https://store.rokland.com/products/seeed-studio-xiao-esp32s3-wio-sx1262-kit-for-meshtastic-lora)). Buy the mics and windscreens from Amazon on Thursday so they arrive by the weekend. Order the T-ETH-Lite at the same time; it will take a week or two.

**Record with phones this weekend.** It is the honest shortcut. Use a recorder app that saves uncompressed WAV and lets you turn off noise reduction, and put a fur windscreen on each phone. When the T-ETH-Lite arrives, repeat a short session through the MEMS mic and check whether the model still works on it.

### The Saturday test

The steps are on one page: [the Saturday test]({{ site.baseurl }}{% link weekend-test.md %}). Two details it links back here for:

1. **Mic wiring.** Solder headers onto the detector board if it has none. Wire one INMP441: VDD to 3V3, GND to GND, SCK to D3, WS to D4, SD to D5, L/R to GND. Those are GPIO 4, 5 and 6, the same pins Batear uses on a Heltec ([Batear hardware](https://github.com/batear-io/batear/blob/main/docs/hardware.md)).
2. **Training a model afterwards.** Cut the recordings into 1-second clips with the test's clip cutter. Split train and test **by flight, not by clip**: clips from the same minute nearly match, and mixing them makes any model look far better than it is. A model is worth keeping only if it beats Batear's own alarms at 330 ft or more, with fewer false alarms per hour.

{: .note }
> **Fly legally.** In the US, recreational pilots must pass the free online TRUST test and fly in permitted airspace (check B4UFLY or a similar app), under 400 ft and within sight. Drones under 8.8 oz flown for fun don't need registering; heavier ones do. Recording drone sound in a field needs no permit, but keep cameras off neighbours' property.

</details>

<details class="layer" id="sources" markdown="block">
<summary><span class="layer-title">Sources</span><span class="layer-sub">Every source on this page</span></summary>

- [Batear — GitHub](https://github.com/batear-io/batear) and its [detection algorithm notes](https://github.com/batear-io/batear/blob/main/docs/how-it-works.md)
- [VolAnti — project site](https://volantitech.com/), [GitHub](https://github.com/agamrossen/VolAnti) and [licence and disclaimer](https://github.com/agamrossen/VolAnti/blob/main/LICENSE.md)
- [AcousticPrint — GitHub](https://github.com/AcousticPrint/AcousticPrint)
- Test kit: [Batear hardware and wiring](https://github.com/batear-io/batear/blob/main/docs/hardware.md), [Batear TF-card recording](https://github.com/batear-io/batear/blob/main/docs/configuration.md), [VolAnti breadboard build](https://github.com/agamrossen/VolAnti/blob/main/docs/breadboard-build.md), [Adafruit ICS-43434 (discontinued notice)](https://www.adafruit.com/product/6049), [Rokland — XIAO ESP32S3 + Wio-SX1262 kit](https://store.rokland.com/products/seeed-studio-xiao-esp32s3-wio-sx1262-kit-for-meshtastic-lora), [Meshtastic — XIAO S3 pin map](https://github.com/meshtastic/firmware/blob/master/variants/esp32s3/seeed_xiao_s3/variant.h), [Rokland — Heltec V3 US915](https://store.rokland.com/products/heltec-wifi-lora-32v3), [CNX Software — T-ETH-Lite S3](https://www.cnx-software.com/2023/09/27/lilygo-t-eth-lite-esp32-s3-board-ethernet-poe/), [The Drive — DJI Mini 4K pricing](https://www.thedrive.com/news/dji-drones-amazon-spring-sale-2026), [FAA — recreational flyers](https://www.faa.gov/uas/recreational_flyers)
- Kit photos, cropped and resized, from Wikimedia Commons: [LILYGO T-Beam](https://commons.wikimedia.org/wiki/File:Meshtastic_T-Beam.jpg) (Chiffre01, CC0), [windshield](https://commons.wikimedia.org/wiki/File:Nicolai_Equipment_Windshield_for_Shotgun_Microphone.jpg) (Nicolai Equipment, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)), [tripod](https://commons.wikimedia.org/wiki/File:(Photography_equipment_Tripod_Photo_Camera_Tripod_photograph_in_a_studio).jpg) (David Adam Kess, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)), [power bank](https://commons.wikimedia.org/wiki/File:USB_power_bank.jpg) (Ronggy, public domain), [DJI Mini 2](https://commons.wikimedia.org/wiki/File:DJI_Mini_2.jpg) (Florian Fuchs, CC BY-SA 4.0), [racing quad](https://commons.wikimedia.org/wiki/File:Racing_Drone.jpg) (Commanderbryce, CC BY-SA 4.0), [ESP32-S3](https://commons.wikimedia.org/wiki/File:ESP32-S3_on_paper.jpg) (VectorVoyager, CC BY-SA 4.0), [microSD](https://commons.wikimedia.org/wiki/File:Size_comparison_of_SD_card,_microSD_card,_and_dime.jpg) (Nashucks, CC0). Breadboard photo from [VolAnti](https://github.com/agamrossen/VolAnti) (Agam Rossen, CC BY-SA 4.0).

</details>
