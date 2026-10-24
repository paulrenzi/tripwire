---
title: "Build: software plan"
nav_order: 1.75
nav_tripwire: 8
---

# Build: software plan, and the open-source parts to build it from
{: .no_toc }

<p class="vz-lede">Which public projects each of the six programs on <a href="{{ site.baseurl }}{% link build-software.md %}">Build: software</a> can be built from, what they change in the design, and the order to build in. <strong>A plan, not progress: no code exists yet.</strong></p>

<div class="vz-cards vz-4">
  <div class="vz-card"><p class="vz-card-num">MIT</p><p>Our firmware stays MIT, built on Batear and RadioLib. Mesh firmwares lend ideas, not code: they beacon, and Meshtastic is GPL</p></div>
  <div class="vz-card"><p class="vz-card-num">Radio does the listening</p><p>The SX1262 runs relay listening windows itself, so the ESP32 sleeps until the radio wakes it</p></div>
  <div class="vz-card"><p class="vz-card-num">Weakest goes first</p><p>A dart that heard a packet faintly relays sooner, so each hop covers the most ground</p></div>
  <div class="vz-card"><p class="vz-card-num">One dataset is out</p><p>The Al-Emadi drone audio is non-commercial only; a CC BY FPV set and Batear's MIT set replace it</p></div>
</div>

### The build, in seven phases

<div class="vz-tiles">
  <div class="vz-tile"><span class="vz-tile-id">Phase 0</span><span class="vz-tile-q">Groundwork</span><span class="vz-tile-cost">laptop only</span><span class="vz-chip vz-size-S">small</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 1</span><span class="vz-tile-q">Radio range</span><span class="vz-tile-cost">T9 · layer 1</span><span class="vz-chip vz-size-S">small</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 2</span><span class="vz-tile-q">Edge receiver and display v0</span><span class="vz-tile-cost">T17 · layer 3</span><span class="vz-chip vz-size-M">medium</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 3</span><span class="vz-tile-q">Battery life</span><span class="vz-tile-cost">T12 · layer 4</span><span class="vz-chip vz-size-M">medium</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 4</span><span class="vz-tile-q">Relaying and the line display</span><span class="vz-tile-cost">layer 5</span><span class="vz-chip vz-size-L">large</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 5</span><span class="vz-tile-q">The learned classifier</span><span class="vz-tile-cost">after layer 2 data</span><span class="vz-chip vz-size-L">large</span></div>
  <div class="vz-tile"><span class="vz-tile-id">Phase 6</span><span class="vz-tile-q">Laying the line</span><span class="vz-tile-cost">T13, T14</span><span class="vz-chip vz-size-M">medium</span></div>
</div>
<p class="vz-bar-note">Each phase goes with a test or an MVP layer. Size is the work, not the cost. One assumption is unproven: that an Android tablet can read the wired display adapter in the browser. A laptop works either way.</p>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">The page's introduction and the plan-not-progress warning</span></summary>

Which public projects each of the six programs on [Build: software]({{ site.baseurl }}{% link build-software.md %}) can be built from, what each one changes in the design, and the order to build it all in.

{: .warning }
> **A plan, not progress.** No code exists yet. Every repository below was checked on 2026-10-19 for its licence, its last push and, where it matters, its source. Stars and dates move; licences rarely do. Nothing here has been run on our hardware.

</details>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">Licences, three findings that change the design, Batear moving our way, and one unproven assumption</span></summary>

- **Our firmware stays MIT, built on Batear and RadioLib.** Both are MIT and active. The mesh firmwares (Meshtastic, MeshCore, LoRaMesher) are used for their ideas, not their code. All three send routine beacons or routing traffic, and a listener must stay silent until it hears a drone. Meshtastic is also GPL, which would change our licence.
- **Three findings change the design:**
  1. **The SX1262 can run the relay listening windows itself.** RadioLib's `startReceiveDutyCycleAuto()` puts the radio into its own sleep–listen cycle, sized from the sender's preamble. The ESP32 can then stay in deep sleep and wake on the radio's DIO1 pin. On the Heltec V3 that is GPIO 14, which can wake the chip from deep sleep. Relaying then costs very little battery.
  2. **Relays should wait by signal strength, not at random.** In Meshtastic's managed flooding, a node that heard the packet *weakly* relays *sooner*, so the farthest node goes first. Nearer nodes hear that relay and stay quiet. Along a line, that means each hop covers as much ground as it can. This replaces the random 100–600 ms wait in rule I2.3.
  3. **The Al-Emadi drone audio set is non-commercial only.** Its licence allows academic research and teaching. A model trained on it can't ship in a sold product without permission. [Training data]({{ site.baseurl }}{% link research/datasets.md %}) is corrected, and two usable sets are added: a CC BY 4.0 FPV set and Batear's MIT set.
- **Batear has moved toward us.** An open issue ([#51](https://github.com/batear-io/batear/issues/51)) proposes one firmware where every node detects *and* relays. A closed, unmerged draft ([#49](https://github.com/batear-io/batear/pull/49)) wires an int8 CNN into its audio chain on TensorFlow Lite Micro. Our relay and nonce work is worth offering upstream, not keeping in a private fork.
- **One assumption is unproven:** that an Android tablet can read the RS-485 adapter in the browser. Chrome on Android has Web Serial over Bluetooth. Public sources don't settle whether it reads a *wired* USB serial adapter. A laptop works either way. Test the tablet in phase 2.

</details>

<details class="layer" id="the-open-source-parts-layer-by-layer" markdown="block">
<summary><span class="layer-title">The open-source parts, layer by layer</span><span class="layer-sub">For each of the six programs: the projects to build from, and the repositories</span></summary>

**Use** means its code goes into ours. **Tool** means we run it as a separate program, so its licence doesn't touch ours. **Reference** means we read it and write our own.

### 1. Listener firmware and 2. edge receiver firmware

| Project | Licence | Last push | Role | Why |
|---|---|---|---|---|
| [Batear](https://github.com/batear-io/batear) | MIT | 2026-09-24 | **Use: the base fork** | ESP-IDF project for the Heltec V3 and SX1262. I²S mic, harmonic detector, AES-GCM packets, battery read, a receive-only gateway, SD recording of alarms, and CI builds already set up. The nonce defect ([I1a]({{ site.baseurl }}{% link build-software.md %}#i1a-the-nonce-a-defect-in-batear-to-fix-first)) is still in `lora_crypto.h` today |
| [RadioLib](https://github.com/jgromes/RadioLib) | MIT | 2026-10-19 | **Use** (Batear already does) | SX1262 driver. `startReceiveDutyCycleAuto()` and channel-activity detection give the relay windows without waking the processor |
| ESP-IDF UART, RS-485 half-duplex mode | Apache-2.0 | – | **Use** | The edge receiver's RS-485 output, with the driver switching the transceiver's direction. No extra library |
| [Meshtastic firmware](https://github.com/meshtastic/firmware) | GPL-3.0 | 2026-10-19 | **Reference** | The managed-flooding rules: signal-weighted wait, cancel on hearing a duplicate, hop limit ([algorithm](https://meshtastic.org/docs/overview/mesh-algo/)). GPL, and its nodes broadcast node info on a timer, so we don't use its code |
| [MeshCore](https://github.com/meshcore-dev/MeshCore) | MIT | 2026-10-18 | **Reference** | A portable C++ routing library on RadioLib. Only fixed repeaters relay, and routes are learned from floods. Too much machinery for a 12–30 node line that only floods |
| [LoRaMesher](https://github.com/LoRaMesher/LoRaMesher) | MIT | 2026-10-15 | **Skip** | Distance-vector routing sends routing hellos on a timer, which a silent listener can't afford |
| [esp-dsp](https://github.com/espressif/esp-dsp) | Apache-2.0 | 2026-05-11 | **Use if needed** | Optimised FFT and filters for the S3, if Batear's own FFT is too slow for the duty-cycled look in option A |
| [VolAnti firmware](https://github.com/agamrossen/VolAnti) | Apache-2.0 (firmware) | 2026-09-20 | **Reference** | Another ESP32-S3 harmonic detector (2,048-point FFT, 70–2,000 Hz), with a calibration folder and test audio. Its author reports false alarms on music and fan noise. That is useful when choosing the negatives the classifier must reject |
| [Unity](https://github.com/ThrowTheSwitch/Unity) | MIT | 2026-10-19 | **Use** | Unit tests for the packet, nonce and relay logic, run on the laptop as well as the board (ESP-IDF bundles it) |

### 3. Dugout display

| Project | Licence | Role | Why |
|---|---|---|---|
| Web Serial API (Chrome) | – | **Use** | Reads the RS-485 adapter straight into one offline HTML page. Works on a laptop; Android wired support to be tested |
| [Leaflet](https://github.com/Leaflet/Leaflet) | BSD-2 | **Use** | Small, mature map library for listener dots, lines and error circles |
| [PMTiles](https://github.com/protomaps/PMTiles) | BSD-3 (code), CC0 (format) | **Use** | Packs an offline map of the sector into one file the page reads without a tile server. `pmtiles extract` cuts the area out before deployment |
| [pytak](https://github.com/snstac/pytak) | Apache-2.0 | **Tool, later** | Sends Cursor-on-Target messages to TAK, for the [integration]({{ site.baseurl }}{% link research/integration.md %}) step |
| [Meshtastic web](https://github.com/meshtastic/web) | GPL-3.0 | **Reference** | A working Web Serial client for LoRa radios. Worth reading for reconnect and error handling |
| [usb-serial-for-android](https://github.com/mik3y/usb-serial-for-android) | MIT | **Fallback** | If the tablet's browser can't read a wired adapter, a small native app using this library can |

### 4. Mission tooling (`lay_line`)

| Project | Licence | Role | Why |
|---|---|---|---|
| [pymavlink](https://github.com/ArduPilot/pymavlink) | LGPL-3.0 (generator and Python) | **Use** (as an imported library) | Writes the mission, reads DataFlash `.BIN` logs, finds each servo change and the GPS fix at that moment |
| [Shapely](https://github.com/shapely/shapely) + pyproj | BSD-3 / MIT | **Use** | Splits a drawn line into drop points at exact spacing in a local projection |
| [ArduPilot](https://github.com/ArduPilot/ardupilot) SITL | GPL-3.0 | **Tool** | Flies every generated mission in simulation before a real sortie |
| [MAVProxy](https://github.com/ArduPilot/MAVProxy), [QGroundControl](https://github.com/mavlink/qgroundcontrol) | GPL-3.0 | **Tool** | Load and check the mission. Unchanged |
| [MAVSDK-Python](https://github.com/mavlink/MAVSDK-Python) | BSD-3 | **Skip for now** | A cleaner API, but pymavlink is still needed for logs, so one library is enough |

### 5. Classifier pipeline

| Project | Licence | Role | Why |
|---|---|---|---|
| [esp-tflite-micro](https://github.com/espressif/esp-tflite-micro) | Apache-2.0 | **Use, first choice** | TensorFlow Lite Micro with S3 kernels. Batear's draft #49 already feeds it a 40-band log-mel input built from the FFT it computes anyway, so no second FFT. Its CI reported about 114 KB more flash for the detector |
| [ESP-DL](https://github.com/espressif/esp-dl) + ESP-PPQ | MIT | **Use, if faster** | Espressif's own inference engine, which quantises a PyTorch or ONNX model directly. Benchmark both on the S3 with the same model |
| [audiomentations](https://github.com/iver56/audiomentations) | MIT | **Use** | Mixes wind, rain and vehicle noise into drone clips at set signal-to-noise ratios, and simulates distance by gain and filtering |
| [pyroomacoustics](https://github.com/LCAV/pyroomacoustics) | MIT | **Tool** | Simulates sound reaching a mic with a ground reflection and air absorption, for building test sets at known distances |
| [batear-datasets](https://github.com/batear-io/batear-datasets) | MIT | **Use** | Recorded on Batear boards, so its clips have our mic's sound |
| [FPV drone audio set](https://github.com/saarmets/fpv-drone-audio-classification-dataset) | CC BY 4.0 | **Use** (credit the author) | FPV positives, the tripwire's main target. Contents not yet audited |
| [Al-Emadi drone audio](https://github.com/saraalemadi/DroneAudioDataset) | Non-commercial | **Benchmark only** | Comparison with published papers; never in a shipped model |
| DroneAudioset (Hugging Face) | MIT | **Limited** | Recorded from mics *on* the drone, so mostly the drone's own noise. A poor match for a listener on the ground |

### 6. Test harness

| Project | Licence | Role | Why |
|---|---|---|---|
| ArduPilot SITL | GPL-3.0 | **Tool** | Drop missions, the radio-failsafe case, and GPS loss |
| [gr-lora_sdr](https://github.com/tapparelj/gr-lora_sdr) | GPL-3.0 | **Tool** | Decodes LoRa from a software-defined radio, so the silence test can show what an eavesdropper would actually receive, not just whether energy appears |
| rtl-sdr `rtl_power` | GPL-2.0 | **Tool** | Sweeps 915 MHz around an armed-wait listener and the edge receiver for the silence check (T8, T17) |
| [Meshtasticator](https://github.com/meshtastic/Meshtasticator) | none stated | **Reference** | A discrete-event simulator of Meshtastic flooding over LoRa path loss. With no licence we read it, then write our own small simulator |

</details>

<details class="layer" id="the-plan" markdown="block">
<summary><span class="layer-title">The plan</span><span class="layer-sub">Seven phases from groundwork to laying the line, and what comes later</span></summary>

Each phase ends in something that runs, and each lines up with an [MVP]({{ site.baseurl }}{% link mvp.md %}) layer, so software is never ahead of what the hardware tests have shown. Sizes are rough: **S** is a few days, **M** one to two weeks, **L** several weeks. They are estimates, not commitments.

### Repositories

- **`tripwire-firmware`:** a fork of Batear with two new build roles, `listener` and `edge`, beside Batear's own. Keeping the fork lets the nonce fix and the relay go upstream as pull requests and lets us pull Batear's fixes back in.
- **`tripwire-tools`:** Python. The packet codec, `lay_line`, the relay simulator, the classifier pipeline and the test scripts.
- **`tripwire-display`:** one HTML file plus a PMTiles map, with no build step.

The **packet codec** (I1, I1a) is written twice, in C for the firmware and in Python for the tools and display, and both are tested against **one shared file of test vectors**. That file is the contract between the three repositories.

### Phase 0: groundwork, laptop only (S, $0)

- Fork Batear and get its CI building the two new roles.
- Write the I1 packet and the I1a nonce in C and Python. Test vectors cover reboot, counter wrap and a relayed packet re-encrypted under the relay's own ID.
- **Relay simulator (M).** A line of 12–30 nodes, forest path loss from the [T9 literature]({{ site.baseurl }}{% link research/open-questions.md %}), a cycle and preamble length, and the signal-weighted wait. It answers before any hardware: delivery rate, delay to the edge, and transmissions per alert, all against spacing. Its output sets the radio settings for phase 4.
- **Done when:** the codec tests pass in both languages, and the simulator reproduces Meshtastic's published behaviour on a simple case.

### Phase 1: radio range (T9, MVP layer 1; S)

- Flash Batear as it is, adding RSSI and SNR logging on the gateway.
- **Done when:** T9's numbers are in, and they go back into the simulator in place of the literature's path loss.

### Phase 2: edge receiver and display v0 (T17, layer 3; M)

- **Edge role:** the transmit functions compiled out, RS-485 output on ESP-IDF's half-duplex UART mode, the I3 frame, the nonce fix, and a replay table that survives a reboot.
- **Display v0:** a list of alerts and a beep over Web Serial on a laptop.
- **Test the Android tablet with a wired USB–RS-485 adapter.** If it fails, choose then between a laptop at the dugout and a small native app on usb-serial-for-android.
- **Silence test** with `rtl_power`, plus gr-lora_sdr to show nothing decodable leaves the edge receiver.
- **Base box role:** the same build with two fiber inputs (I2a) on two UARTs and a heartbeat watch; the tip's laser output and heartbeat in the listener build. Bench it with a full spool of FPV fiber (T21).
- **Done when:** T17 and T21 pass, and a listener reboot mid-test loses no alerts.

### Phase 3: battery life (T12, layer 4; M)

- Wake-on-sound option A: wake every 1–2 s, take a 64 ms look, run the harmonic test, sleep.
- **Relay windows with the radio's own duty-cycled receive**, with the ESP32 in deep sleep waking on DIO1.
- The new I1 packet, temperature, and check-in at most 1–2 a day.
- Measure the bare board's sleep current first, as the design already says. If the Heltec's regulator and USB chip hold it in milliamps, that is a hardware answer (the custom board), not a software one.
- **Done when:** T12's battery life is measured with relay windows on, not just off.

### Phase 4: relaying and the line display (layer 5; L)

- Flooding per I2, with the **signal-weighted wait** and cancel after two duplicates, `age_ds` updated by each relay, and a dedup cache.
- Six bench listeners at low power, then six in the field.
- **Display:** the line map on Leaflet with an offline PMTiles map, line health, the false-alarm policy, and both-lines direction.
- **Offer the nonce fix and the relay upstream** to Batear, against issue #51.
- **Done when:** the layer 5 test passes, and the field delivery rate matches the simulator's prediction for that spacing.

### Phase 5: the learned classifier (after layer 2 data; L)

- Assemble the training set from sources whose licences allow shipping. Keep Al-Emadi for benchmarking only.
- Train a small CNN on 40-band log-mel at 16 kHz. Batear's #49 draft fixes the input shape, `[1, 32, 40, 1]` int8. Augment it with audiomentations.
- Benchmark esp-tflite-micro against ESP-DL for time and memory on the S3.
- **Done when:** it beats Batear's harmonic detector alone on detections against false alarms per hour, at each distance in the layer 2 recordings. If it doesn't, it doesn't ship.

### Phase 6: laying the line (T13, T14; M)

- `lay_line plan` with Shapely and pyproj, writing I5 missions; `sitl` on ArduPilot SITL; `ingest` from DataFlash logs to I4 with pymavlink.
- **Proposed: a check pass.** After the last drop the drone flies back along the line once. The listeners' alerts against its logged track give each listener's actual hearing range where it landed, flag any that fell badly or went deaf, and check alert delay. Those alerts are logged as friendly because the pass is in the mission's own flight window.
- **Done when:** a SITL sortie fires every drop at its point, and a real T13 sortie produces a `listeners.json` the display draws correctly.

### Later

- TAK output through pytak.
- A tablet app, only if phase 2 forces one.

</details>

<details class="layer" id="risks-the-parts-dont-remove" markdown="block">
<summary><span class="layer-title">Risks the parts don't remove</span><span class="layer-sub">What open-source parts can't fix for us</span></summary>

- **Sleep current on the Heltec board** may decide battery life whatever the software does (phase 3).
- **The classifier's training data** is mostly hobby drones in quiet places. Field recordings from Batear's SD logging are the only route to front-line negatives.
- **Upstream may not want** a military line-relay use in Batear. The fork works on its own either way.
- **Licences:** keep GPL code (Meshtastic, MAVProxy, ArduPilot, gr-lora_sdr) as separate tools and references, never pasted into the firmware or the display.

</details>
