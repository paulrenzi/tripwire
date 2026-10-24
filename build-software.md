---
title: "Build: software"
nav_order: 1.7
nav_tripwire: 7
---

# Build: software, from listener to dugout
{: .no_toc }

<p class="vz-lede">The <strong>six programs</strong> the <a href="{{ site.baseurl }}{% link models/tripwire.md %}">tripwire</a> needs, how they connect, and how much of each the open-source <a href="{{ site.baseurl }}{% link research/open-source-builds.md %}#batear">Batear</a> already covers. A design, not code: nothing is written or tested yet.</p>

<div class="vz-flow" role="img" aria-label="The chain: mission tooling on a laptop plans the drone's drops; listener firmware on each dart hears and relays by LoRa to a tip dart; the tip sends alerts down fiber to the base box; the base box passes them by RS-485 wire to the dugout display.">
  <div class="vz-node"><span class="vz-node-n">4</span><strong>Mission tooling</strong><span>laptop plans the drops; the drone's log gives each dart's position</span></div>
  <div class="vz-arrow">drone lays</div>
  <div class="vz-node vz-node-hot"><span class="vz-node-n">1</span><strong>Listener firmware</strong><span>each dart hears, alerts, relays once</span></div>
  <div class="vz-arrow">LoRa hops</div>
  <div class="vz-node vz-node-hot"><span class="vz-node-n">1</span><strong>Tip dart</strong><span>flashes alerts down its fiber</span></div>
  <div class="vz-arrow vz-arrow-green">fiber</div>
  <div class="vz-node"><span class="vz-node-n">2</span><strong>Base box</strong><span>never transmits</span></div>
  <div class="vz-arrow">RS-485 wire</div>
  <div class="vz-node vz-node-dark"><span class="vz-node-n">3</span><strong>Dugout display</strong><span>map, alarm, line and fiber health</span></div>
</div>
<p class="vz-bar-note">Offline, around the chain: <strong>5 · the classifier pipeline</strong> trains the model baked into the next batch of darts, and <strong>6 · the test harness</strong> replays audio and simulated flights.</p>

### How much Batear already covers

<div class="vz-bars">
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>1</strong> Listener firmware</span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:50%"></span></span><span class="vz-bar-val">~half</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>2</strong> Base box firmware</span><span class="vz-bar-track"><span class="vz-bar vz-bar-us" style="width:50%"></span></span><span class="vz-bar-val">~half</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>3</strong> Dugout display</span><span class="vz-bar-track"></span><span class="vz-bar-val">none</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>4</strong> Mission tooling</span><span class="vz-bar-track"></span><span class="vz-bar-val">none</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>5</strong> Classifier pipeline</span><span class="vz-bar-track"><span class="vz-bar vz-bar-us-light" style="width:8%"></span></span><span class="vz-bar-val">recordings</span></div>
  <div class="vz-bar-row"><span class="vz-bar-label"><strong>6</strong> Test harness</span><span class="vz-bar-track"></span><span class="vz-bar-val">none</span></div>
  <p class="vz-bar-note">Batear has the mic front end, a harmonic detector, LoRa, encryption and a receive-only gateway. It lacks wake-on-sound, relaying, the fiber link, a wired output and a nonce scheme safe with more than one detector. Rough shares, from reading its source on 2026-10-15.</p>
</div>

### What gets built when

<div class="vz-steps vz-4">
  <div class="vz-step"><p class="vz-step-num">1 · now</p><p>Flash Batear as is for the radio test. Log signal strength.</p></div>
  <div class="vz-step"><p class="vz-step-num">2–3 · layer 3</p><p>Base box: fiber inputs, transmit compiled out, wired output, the nonce fix. A first display: a list and a beep.</p></div>
  <div class="vz-step"><p class="vz-step-num">4–5 · layers 4–5</p><p>Wake-on-sound and the new packet; then relaying, the map and line health for the MVP.</p></div>
  <div class="vz-step"><p class="vz-step-num">6–7 · later</p><p>A learned classifier once there's field audio; laying tools once T13 flies.</p></div>
</div>

## The details

Each section opens for the full reasoning, numbers and sources.

<button type="button" class="layer-toggle" data-layers-toggle>Open all sections</button>

<details class="layer" id="the-short-version-in-full" markdown="block">
<summary><span class="layer-title">The opening, as first written</span><span class="layer-sub">The page's original introduction and the design-not-code warning</span></summary>

The six programs the [tripwire]({{ site.baseurl }}{% link models/tripwire.md %}) needs, the interfaces between them, and how much of each [Batear]({{ site.baseurl }}{% link research/open-source-builds.md %}#batear) (MIT licence) already covers. Hardware: [Build: hardware]({{ site.baseurl }}{% link build-hardware.md %}). The open-source parts to build each one from, and the build plan: [Build: software plan]({{ site.baseurl }}{% link build-software-plan.md %}).

{: .warning }
> **A design, not code.** Nothing here is written or tested yet. Batear's behaviour was read from its source and docs on 2026-10-15 (last push 2026-10-06). Every byte count and timing below is a proposal or an estimate unless a source is linked.

</details>

<details class="layer" id="short-answer" markdown="block">
<summary><span class="layer-title">Short answer</span><span class="layer-sub">Six components, alerts home by fiber, what Batear covers, the one interface that carries the design</span></summary>

- **Six components.** Listener firmware (including the tip dart's fiber output), base box firmware, dugout display, mission tooling, classifier pipeline, test harness.
- **Alerts come home by fiber.** The net on [How it works]({{ site.baseurl }}{% link models/line-layout.md %}) has two tip darts that send alerts down FPV fiber to a base box behind the unit ([design]({{ site.baseurl }}{% link models/line-layout.md %}#the-fibers-and-the-base-box)). The base box is the old edge receiver's board with light detectors in place of the radio as its main input, and writes the same serial frame.
- **Batear covers about half of the two firmwares.** It has the audio front end, a harmonic detector, LoRa transmit and receive, encryption, battery reads and a receive-only gateway. It lacks wake-on-sound, relaying, a fiber link, a wired output, line awareness, and a nonce scheme that is safe with more than one detector (below).
- **Batear covers none of the other four.** Mission tooling and the display are new. The classifier pipeline and test harness reuse public datasets and ArduPilot's simulator.
- **One interface carries the design:** the alert packet. Its contents fix what the display can show, what relays must do, and how many bytes each alert costs on air.
- **Order:** fork Batear for layers 1–3 of the [MVP]({{ site.baseurl }}{% link mvp.md %}), fix its nonce, add the fiber link and the serial output, then add relaying and wake-on-sound for layers 4–5. Mission tooling waits for T13.

</details>

<details class="layer" id="the-chain" markdown="block">
<summary><span class="layer-title">The chain</span><span class="layer-sub">Plan, field and unit as one diagram, from the laptop to the dugout display</span></summary>

```
 PLAN (laptop)                 FIELD                                   UNIT
 ─────────────                 ─────                                   ────
 line.geojson ──► lay_line ──► mission.waypoints ──► ArduPilot drone
                    │                                   │ drops, logs release points
                    │          drop log (.bin) ◄────────┘
                    ▼
               listeners.json ─────────────────────────────────────► dugout display
               (id → position)                                            ▲
                                                                          │ RS-485
 listener ──LoRa──► listener ──LoRa──► … ──► tip dart ──fiber──► base box ┘
 (hears, alerts)   (relays once)          (laser, one way)   (never transmits)
```

</details>

<details class="layer" id="components-and-what-batear-covers" markdown="block">
<summary><span class="layer-title">Components and what Batear covers</span><span class="layer-sub">Each program: what it runs on, its inputs and outputs, what exists, what's new</span></summary>

| # | Component | Runs on | In → out | Batear covers | New work |
|---|---|---|---|---|---|
| 1 | **Listener firmware** | ESP32-S3 + SX1262 (Heltec V3 now, custom board later) | sound → alert packet; neighbours' packets → one relay; on a tip dart, every alert → the fiber | I²S mic, 1024-point FFT harmonic detector, hysteresis, AES-128-GCM packet, battery read, heartbeat ([source](https://github.com/batear-io/batear/blob/main/docs/architecture.md)) | Wake-on-sound sleep, learned classifier stage, relay with dedup, temperature, safe nonce, check-in at most 1–2 a day by radio; on a tip, the fiber link (I2a) and a heartbeat every 10 s |
| 2 | **Base box firmware** | Same board; two light detectors on two serial inputs; radio, if fitted, receive only | fiber frames → serial frames | LoRa receive, decrypt, per-device replay check. Its gateway already never transmits on LoRa: no ACKs, by design ([protocol](https://github.com/batear-io/batear/blob/main/docs/protocol.md)) | Two fiber inputs, the heartbeat watch, Wi-Fi and MQTT off and compiled out, RS-485 output, a reboot-safe replay check |
| 3 | **Dugout display** | Phone or tablet over a USB–RS-485 adapter, or a laptop, at each position | frames + `listeners.json` → map, alarm, line health, fiber health | Nothing (Batear goes to Home Assistant) | All |
| 4 | **Mission tooling** (`lay_line`) | Laptop, Python | planned line → ArduPilot mission; flight log → `listeners.json` | Nothing | All |
| 5 | **Classifier pipeline** | Laptop or cloud GPU, offline | labelled audio → model file baked into the next batch's firmware | Its SD-card alarm recordings collect field audio ([config](https://github.com/batear-io/batear/blob/main/docs/configuration.md)) | Dataset assembly, training, on-device export, scoring against Batear's detector |
| 6 | **Test harness** | Laptop + bench boards + SDR | recorded audio, simulated flights → pass/fail | Nothing | SITL drop missions, audio replay into a listener, RF silence check |

Owner for all six: us. ArduPilot, pymavlink and the public datasets are upstream dependencies, not components.

</details>

<details class="layer" id="interfaces" markdown="block">
<summary><span class="layer-title">Interfaces</span><span class="layer-sub">The alert packet, its nonce, relay rules, the fiber link, the serial frame and the files</span></summary>

### I1. The alert packet (listener → air)

Keep Batear's envelope: **36 bytes on air**, `[4 B nonce][16 B ciphertext][16 B GCM tag]`, about 0.5 s at SF10/BW125 ([Batear protocol](https://github.com/batear-io/batear/blob/main/docs/protocol.md)). Replace its 16-byte plaintext, which spends 7 bytes on firmware version, uptime and free heap, with fields the line uses:

| Bytes | Field | Notes |
|---|---|---|
| 2 | `listener_id` | 0–65,535. Batear's 1-byte ID caps a network at 256, too few once lines from many units share a map |
| 1 | `type` | ALARM, CLEAR, CHECKIN |
| 2 | `age_ds` | Tenths of a second since the sound began, **updated by each relay**. Replaces clock sync (below) |
| 1 | `hops` | Incremented by each relay |
| 1 | `f0_bin` | Main tone, as Batear |
| 1 | `rms_db` | Loudness, as Batear |
| 1 | `conf` | Classifier confidence, 0–255 |
| 1 | `dur_s` | How long the sound lasted, for CLEAR |
| 1 | `vbat_cv` | As Batear: V = 2.50 + 0.01 × value |
| 1 | `temp_c` | Chip temperature + 40 |
| 1 | `rssi_hint` | Weakest link RSSI on the way in, for line health |
| 2 | `tag` | The origin's boot and counter, low byte of each. Names the alert after relays re-encrypt it, so relays can drop duplicates (I2 rule 2) |
| 1 | spare | Classifier version, flags |

**Why age, not clocks:** a relay already decrypts the packet to check it, so it can add its own holding time to `age_ds` and re-encrypt. The receiver then dates the sound as *arrival time − age − airtime × (hops + 1)*. Airtime is fixed for a fixed spreading factor. That gives each crossing a time good to well under a second without any listener knowing the time of day. The 1–2 s neighbour-sync problem in [T15]({{ site.baseurl }}{% link models/tripwire.md %}#what-has-to-be-proven) goes away for line-order direction (an inference, to be checked on the bench).

### I1a. The nonce: a defect in Batear to fix first

Batear builds the 12-byte GCM IV from the first 8 bytes of the network key plus a packet counter ([`lora_crypto.h` L79–95](https://github.com/batear-io/batear/blob/main/main/lora_crypto.h)). That counter is a `uint16_t` that starts at 0 on every boot ([`lora_task.cpp` L80, L290](https://github.com/batear-io/batear/blob/main/main/lora_task.cpp)), and every detector shares the key. So:

- **Two detectors reuse the same IV under the same key.** Detector 1's packet 5 and detector 2's packet 5 are encrypted identically. In GCM, a reused nonce leaks the XOR of the two plaintexts and lets an attacker who collects such pairs recover the authentication key and forge packets ([NIST SP 800-38D §8](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf) requires unique IVs per key).
- **A reboot silences a detector.** The gateway drops any packet whose counter is at or below the last one it saw from that device ([`gateway_task.cpp` L246](https://github.com/batear-io/batear/blob/main/main/gateway_task.cpp)). After a detector reboots, every alert is rejected as a replay until the counter climbs past the old value. The same happens when the counter wraps at 65,536.

**Fix:** IV = `listener_id` (2 B) + boot count stored in flash (2 B) + 32-bit packet counter (4 B), with 4 B of key prefix. On air the nonce grows from 4 to 8 bytes, so a packet is 40 bytes. All little-endian; the counter moves to the next boot rather than wrapping. The receiver keys its replay check on (sender ID, boot, counter) from the nonce. A relay re-encrypts under **its own** ID and counter, so relays never reuse an IV either. **Built 2026-10-19** in `tripwire-firmware` (`components/tw_codec`, and Batear's own detector and gateway) and `tripwire-tools` (`tripwire/codec.py`), both tested against one vector file. Not yet offered upstream.

### I2. Relay rules (listener → listener)

Managed flooding with duplicate suppression, the scheme Meshtastic uses ([Meshtastic docs](https://meshtastic.org/docs/overview/mesh-algo/)), cut down:

1. **Listen in short windows only.** A sleeping listener can't hear neighbours. It wakes the radio in receive mode briefly on a fixed cycle, using LoRa channel-activity detection ([Semtech AN1200.85](https://www.semtech.com/products/wireless-rf/lora-connect/sx1262)), so an alert is preceded by a preamble long enough to span one cycle. Cycle and preamble length trade battery against delay; T12 sizes them.
2. **Relay each alert once,** keyed on (origin `listener_id`, `tag`) from the plaintext, since a relayed copy carries the relay's nonce, not the origin's. Keep the last 32 seen in RAM.
3. **Wait before relaying, shorter the weaker the alert was heard,** as Meshtastic does: the farthest listener relays first, so each hop covers the most ground. **Stay quiet only after hearing two more copies** of the alert while waiting, not one as Meshtastic does: on a line, the copy a listener hears first often comes from a neighbour *behind* it, and cancelling on that one strands everyone ahead. In the relay simulator, waiting for two adds 7–19 points of delivery for about 1.5 times the transmissions (decided 2026-10-19). The window (100–600 ms proposed) comes from the relay simulator ([plan, phase 0]({{ site.baseurl }}{% link build-software-plan.md %}#phase-0-groundwork-laptop-only-s-0)).
4. **No hop limit is needed** on a line of 12–30, since each listener relays each alert once. Cap `hops` at 63 or more, not 15: the relay simulator shows a 30-listener line in dense forest needs more than 15 hops (`tripwire-tools/reports/relay-sim-phase0.md`).
5. **CHECKIN packets are not relayed by default**, so a quiet line stays quiet. The unit can turn relaying on for one day's check-in to get a health map.

### I2a. The fiber link (tip dart → base box)

One way, tip to home. The tip sends **the same 40-byte encrypted packet** it would send by radio, framed for the wire: a sync byte, a length byte, the packet and a CRC-16, 44 bytes in all. Its serial output drives a small laser on and off at 9,600 baud (proposed), so a frame takes about 46 ms of light. The base box's light detector feeds the board's serial input directly.

- **Every alert the tip sends or relays goes down the fiber,** and, like any relay, also out by radio to its neighbours.
- **A heartbeat every 10 s:** a CHECKIN sent down the fiber only, never by radio. Light inside a fiber can't be picked up, so this gives nothing away. The base box marks a fiber dark after 30 s without one.
- **Nothing comes back.** The base box never answers, so the tip needs no light detector, and nothing at home can be made to transmit.
- **To measure (T21):** whether a small laser couples enough light into FPV fiber, which is single-mode, and what the heartbeat costs the tip's battery.

### I3. Serial frame from the base box to the display

One line of ASCII per received packet at 9,600 baud, so any serial terminal can read it if the display fails:

```
$TW,<listener_id>,<type>,<age_ds>,<hops>,<f0_bin>,<rms_db>,<conf>,<vbat_cv>,<temp_c>,<rssi>,<snr>,<rx_id>*<crc8>
```

`rx_id` names how the packet came home: fiber `A`, fiber `B`, or the base box's own radio if one is fitted. `rssi` and `snr` are the last radio hop's, as the tip heard it. A line `$TWF,<fibre>,<LIT|DARK>*<crc8>` reports each change in a fiber's heartbeat. One shared RS-485 pair runs from the base box to a display at each position; the base box is the only sender and the displays only listen. The base box decrypts, so it holds the key; the displays need none.

### I4. `listeners.json` (mission tooling → display)

```json
{"line": "A", "laid": "2026-11-02T03:10Z", "sortie": 4,
 "listeners": [{"id": 1031, "planned": [48.512, 37.991],
                "released": [48.5122, 37.9913], "fix": "3D", "hdop": 0.9}]}
```

`released` comes from the drone's log at the moment the servo moved. If the log shows no GPS fix there, `released` is the dead-reckoned estimate and `fix` says so. The display draws an error circle from it.

### I5. Mission file (mission tooling → drone)

Standard QGroundControl plain-text waypoint format, loaded with MAVProxy or pymavlink ([format](https://mavlink.io/en/file_formats/)). The file's first line is `QGC WPL 110`, then one tab-separated line per item: index, current, frame, command, params 1–4, lat, lon, alt, autocontinue. Per listener: `NAV_WAYPOINT` (16) to the drop point at drop height, with param 1 = 2 s hold to settle; `DO_SET_SERVO` (183) with param 1 = the output number and param 2 = the release PWM in µs; then the next waypoint. `RETURN_TO_LAUNCH` (20) at the end ([ArduPilot mission commands](https://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html)).

On a Pixhawk 6C, the [v2 harness]({{ site.baseurl }}{% link build-hardware.md %}#2-v2-one-rod-one-servo) uses **AUX 1** only, with `SERVO9_FUNCTION = 0`: each drop is a `DO_SET_SERVO` to that dart's step on the rotor, so the PWM rises by one step per listener. ArduPilot needs an unassigned output for `DO_SET_SERVO`, and advises against servos on the 400 Hz MAIN outputs ([ArduPilot servo docs](https://ardupilot.org/copter/docs/common-servo.html)). The v1 harness used AUX 1–4, one servo per dart, so a stuck servo cost one listener. With v2, a jammed rotor keeps the rest of the sortie's darts on board.

</details>

<details class="layer" id="the-components-in-detail" markdown="block">
<summary><span class="layer-title">The components in detail</span><span class="layer-sub">Listener and base box firmware, display, mission tooling, classifier, test harness</span></summary>

### 1. Listener firmware

**States:** `ARMED-WAIT` → `SLEEP` ⇄ `LISTEN` → `CLASSIFY` → `ALARM` → `CLEAR` → `SLEEP`.

- **`ARMED-WAIT`.** Loaded into the harness powered on, the listener stays silent for a set time (default 10 minutes) so it can't transmit from the drone or over the unit's position. It then counts its boot and starts.
- **`SLEEP`.** The processor and radio are off except for the wake source and the relay receive windows (I2). The wake source is the main open choice:

The digital mic can't be the wake source by itself: in deep sleep the ESP32-S3 powers down its I²S block, and its low-power coprocessor can poll only the ADC, touch pins and GPIO ([Espressif sleep modes](https://docs.espressif.com/projects/esp-idf/en/v5.1/esp32s3/api-reference/system/sleep_modes.html)).

| Wake source | How | Cost | Risk |
|---|---|---|---|
| **A. Duty-cycled FFT** | Wake from deep sleep every 1–2 s, start I²S, sample 64 ms, run Batear's harmonic test, sleep | No extra parts | A drone is audible for tens of seconds, so a look every 2 s should catch most crossings (estimate). Average current is set by wake-up overhead |
| **B. Analog energy gate** | An analog mic, a band-pass (150–3,000 Hz) and a comparator on an RTC GPIO wake the processor | ~$1–2 | Wind trips it; needs filtering |
| **C. Wake-on-sound MEMS mic** | Vesper VM1010: about 10 µA in wake-on-sound mode, raising a pin on sound ([datasheet](https://www.mouser.com/datasheet/2/960/vesper_tech_06182019_VM1010-1605563.pdf)) | ~$2–5 | Single source |

Start with **A**, because it needs no hardware change and T12 measures it. **The board, not the method, may set the floor:** Heltec quotes under 10 µA in deep sleep for the V3 ([Heltec](https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/)), but its regulator, charger, USB chip and display keep Heltec ESP32 LoRa boards well above the chip's datasheet figure in practice ([The Things Network forum](https://www.thethingsnetwork.org/forum/t/is-there-a-esp32-lorawan-board-for-battery-operation/35266)). One Meshtastic user saw about 2 mA on a V3, possibly while it was on USB power. At 2 mA, a 3,000 mAh cell lasts about 2 months before any listening. Measure the bare board's sleep current in T12 first. If it is in milliamps, the custom board is what makes "weeks" possible, and B or C becomes worth its cost.

- **`CLASSIFY`.** Stage 1 is Batear's harmonic detector, which is cheap and always on while awake. Stage 2 is a small learned model run only when stage 1 fires, which cuts false alarms (pipeline below). Alarm needs both.
- **`ALARM` / `CLEAR`.** Send ALARM at once and CLEAR when the sound has gone. One retry, as Batear does. A listener that alarms more than N times an hour with low confidence mutes itself for an hour and says so in its next CHECKIN, so a listener next to a generator can't flood the line.
- **No GPS, no over-the-air updates.** Position comes from I4. A new classifier ships in the next batch of listeners ([why]({{ site.baseurl }}{% link models/tripwire.md %}#rules-that-keep-it-cheap-and-quiet)).
- **From Batear, unchanged:** I²S set-up, FFT and harmonic scoring, battery divider gating, the RadioLib HAL. **From Batear, changed:** the packet (I1), the nonce (I1a), the heartbeat (every 30 min in Batear; at most 1–2 a day here, since every transmission can give a listener away).

### 2. Base box firmware

Batear's gateway role minus Wi-Fi and MQTT, with fiber in place of the radio as its main input, plus:

- **Two fiber inputs (I2a),** one per UART, each with its own frame check and heartbeat watch.
- **A build-time guarantee that it cannot transmit:** the transmit functions are compiled out, not just unused, and an SDR check confirms nothing is emitted.
- RS-485 output (I3) through a MAX3485-class transceiver on a spare UART.
- The reboot-safe replay table from I1a, stored in flash, so a reboot doesn't accept old replays. It also drops the second copy when both tips pass on the same alert.
- **Optionally, its own radio, receive only,** to hear darts near the launch point if both fibers are cut. The [jamming model]({{ site.baseurl }}{% link models/line-layout.md %}#jamming) says the unit's own jammers deafen it within about 1,000 ft, so it logs the noise floor every minute: a jammer shows as a raised floor, which gives T19 field data.

The same firmware, with the radio as its only input, is the edge receiver that hears a [line]({{ site.baseurl }}{% link models/tripwire.md %}#getting-alerts-out-of-the-trees) from the edge of a tree belt.

### 3. Dugout display

**Shows:** a map of each line, listeners as dots coloured by last contact, a full-screen alarm naming the listener and its line, **time since crossing** counting up, confidence, and direction when both lines have tripped (outer first = inbound).

**False-alarm policy (proposed):**

| Condition | Display does |
|---|---|
| One listener, confidence high | Alarm |
| One listener, confidence low | Quiet log entry; alarm if a neighbour or the other line confirms within 30 s |
| Inside a friendly flight window the unit entered | Log only, labelled "friendly window" |
| Listener muted itself (I1 flags) | Grey dot, no alarms from it |

**Line health:** last check-in and battery per listener, listeners silent for over a day (possibly destroyed, [a signal in itself]({{ site.baseurl }}{% link models/tripwire.md %}#what-the-unit-gets)), weakest-link RSSI, and a re-lay forecast from battery trends. **Fiber health:** each fiber lit or dark, from its heartbeat; a dark fiber is a repair sortie, first.

**Build:** a single offline HTML page, served from the device and reading the serial port through the browser's Web Serial API, is the least code. It runs in Chrome on a laptop. Chrome on Android has Web Serial over Bluetooth; whether it reads a **wired** USB serial adapter was not settled from public sources on 2026-10-19, so test it on the actual tablet ([plan, phase 2]({{ site.baseurl }}{% link build-software-plan.md %}#phase-2-edge-receiver-and-display-v0-t17-layer-3-m)). Offline map tiles are loaded before deployment. A TAK output (CoT messages) comes later ([integration]({{ site.baseurl }}{% link research/integration.md %})).

### 4. Mission tooling: `lay_line`

```
lay_line plan   sector.json --per-sortie 4                            →  sortie-1.waypoints, sortie-2.waypoints, …
lay_line sitl   sortie-1.waypoints                                    →  simulated flight + release positions
lay_line ingest 00000042.BIN --sortie 1                               →  listeners.json (I4)
```

- **plan:** places the drop points by the rules on [How it works]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net) (one radio hop apart, off trees and ravine floors, short of the enemy edge, the ends past the 60° lines), orders them outward from each tip dart so each new dart is confirmed by the one before, puts each tip first on its sortie, groups them into sorties that pass the battery check in the forecast wind, and writes I5 files.
- **ingest:** reads the ArduPilot DataFlash log with pymavlink, finds each servo output change, and takes the position and GPS quality at that moment. The same pass writes the jamming map the [tripwire describes]({{ site.baseurl }}{% link models/tripwire.md %}#the-fixes).
- **IDs:** each listener's ID is printed on its body and scanned or typed into the sortie at loading time, so the harness slot maps to an ID.
- **A working prototype of `plan`** is [`tools/laymodel/lay_model.py`](https://github.com/paulrenzi/tripwire/blob/main/tools/laymodel/lay_model.py) ([How it works]({{ site.baseurl }}{% link models/line-layout.md %}#laying-the-net)). It checks drop points against trees, ravines and the enemy edge, picks a ground speed for each leg, checks each sortie against the battery in the wind, and writes terrain-relative missions. **Still to build for flight:** an ArduPilot Lua script that reads the confirm radio over serial and inserts re-drops, the 2-byte relayer ID in each relayed packet, and setting the origin and declination before a sortie flown with GPS jammed.

### 5. Classifier pipeline

1. **Data:** the public sets on [Training data]({{ site.baseurl }}{% link research/datasets.md %}), the layer 2 recordings, and Batear's alarm recordings from field listeners. Negatives (wind, vehicles, generators, birds, voices) carry as much weight as drone clips.
2. **Features:** log-mel spectrogram at 16 kHz, matching Batear's sample rate, so one front end serves both stages.
3. **Model:** a small convolutional network, int8-quantised, sized to run in tens of milliseconds on the ESP32-S3 with Espressif's ESP-DL or TensorFlow Lite Micro (both support the S3; timing is an estimate until benchmarked).
4. **Score:** detections per hour against false alarms per hour, at each distance, against Batear's harmonic detector alone. A model that doesn't beat it doesn't ship ([the weekend test's bar]({{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector)).
5. **Ship:** the model file is compiled into the firmware of the next batch, with its version in the packet's spare byte so the display knows which model raised an alarm.

### 6. Test harness

| Test | Tool | Pass |
|---|---|---|
| Drop missions | ArduPilot SITL running `lay_line` output ([SITL](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)) | Every `DO_SET_SERVO` fires at its point; the mission continues with the radio failsafe triggered |
| Classifier on the board | Recorded clips played through a speaker at a listener in a box, at set levels | Same detections as on the laptop, within the time budget |
| Relay and dedup | 6 bench listeners at low power, one alarm source | Every alert reaches the base box once; no listener relays twice |
| Fiber link | A tip dart on a full spool into the base box (T21) | Every frame arrives; a cut fiber shows dark within 30 s; the laser's battery cost is measured |
| Silence | SDR next to the base box and an armed-wait listener (T17, T8) | Nothing above the noise floor |
| Reboot and nonce | Reboot a listener mid-test | Its next alert is accepted; no two packets share an IV |

</details>

<details class="layer" id="order-of-work" markdown="block">
<summary><span class="layer-title">Order of work</span><span class="layer-sub">Seven steps, each tied to an MVP layer or test</span></summary>

| Step | Goes with | Work |
|---|---|---|
| 1 | MVP layer 1 (T9) | Flash Batear as is. Log RSSI and SNR |
| 2 | Layer 3 (T17, T21) | Base box: fiber inputs, transmit compiled out, RS-485 output, the nonce fix. The tip's fiber output and heartbeat |
| 3 | Layer 3 | Display v0: serial log to a list and a beep |
| 4 | Layer 4 (T12) | Wake-on-sound option A, temperature, the new packet; measure battery |
| 5 | Layer 5 (MVP) | Relay rules, display map and line health |
| 6 | After layer 2 data | Classifier stage 2 |
| 7 | T13 | `lay_line`, SITL first |

</details>
