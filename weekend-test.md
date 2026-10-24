---
title: Saturday test
nav_primary: 4
---

# The Saturday test
{: .no_toc }

<p class="vz-lede">How far does a mic 20 in off the ground hear a drone, and how far does its alarm travel by radio? <strong>One day, about $80–90, and no drone.</strong></p>

<div class="stats">
  <div class="stat"><p class="stat-num">1 day</p><p class="stat-label">in a yard or park; the laptop work is done the day before</p></div>
  <div class="stat"><p class="stat-num">$80–90</p><p class="stat-label">for the kit (<a href="{{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector">list and prices</a>)</p></div>
  <div class="stat"><p class="stat-num">16 ft</p><p class="stat-label">speaker to mic, playing a drone turned down to 80–1,000 ft</p></div>
  <div class="stat"><p class="stat-num">3 of 3</p><p class="stat-label">plays heard at 330 ft is a pass</p></div>
</div>

<div class="vz-bars" role="img" aria-label="Pass or fail by distance: not heard reliably at 200 feet is a fail, heard 3 of 3 at 330 feet is a pass, in between is short of a pass">
  <div class="vz-scale">
    <span class="vz-scale-seg vz-scale-fail" style="width:20%">fail</span><span class="vz-scale-seg vz-scale-mid" style="width:13%">short</span><span class="vz-scale-seg vz-scale-pass" style="width:67%">pass</span>
  </div>
  <div class="vz-scale-ticks"><span style="left:0">0</span><span style="left:20%">200</span><span style="left:33%">330 ft</span><span style="left:100%">1,000 ft</span></div>
  <p class="vz-bar-note"><strong>Fail:</strong> not heard in 3 of 3 plays at 200 ft. <strong>Pass:</strong> heard in 3 of 3 at 330 ft. In between is short of a pass, not a fail. Every distance plays three times; the logger only rules on a distance with 3 or more plays. The radio range is walked for real.</p>
</div>

**You need:** two XIAO ESP32S3 + Wio-SX1262 radio kits (one is the *detector*, the other the *gateway*), an INMP441 mic, two phones with mobile data, a Bluetooth speaker, two power banks, a tape measure, and a laptop with Chrome for the day before ([kit and prices]({{ site.baseurl }}{% link research/open-source-builds.md %}#weekend-test-kit-start-training-the-detector)).

**On the day there are two ends** ([layout](#field-layout)):
- **The sound end stays put:** the detector and the *mic phone* side by side, 20 in up, and the speaker on a chair 16 ft away.
- **You are the other end:** the gateway in your pocket and the *logger phone* in your hand. The logger phone runs everything.

## The steps

### At home, the day before

1. **Flash both boards** from [the flasher]({{ site.baseurl }}/tools/flasher/), antennas on: the detector, then the gateway. Nothing to type.
2. **Wire the mic** to the detector: SCK to D3, WS to D4, SD to D5, L/R to GND, VDD to 3V3, GND to GND.
3. **Set the mic phone's meter** from the detector, on the laptop ([how](#phone-meter)).
   <span class="tw-see">You should see: the mic phone reads within about 1 dB of the detector.</span>
4. **Connect the gateway to the logger phone.** Open [the logger]({{ site.baseurl }}/tools/weekend/logger.html) on it, tap **Logger phone**, and follow the three steps under *Connect* ([more](#phone-setup)).
   <span class="tw-see">You should see: *gateway online*, and *last packet* resetting about once a minute.</span>

### In the park

{:start="5" style="counter-reset: step-counter 4"}
5. **Set out the sound end:** the detector 20 in up in its windscreen, the mic phone beside it, the speaker 16 ft away facing it. Both phones on Do Not Disturb, screens never locking.
6. **Connect:** logger phone hotspot on, gateway powered, tap the gateway. On the mic phone, tap **Mic phone**, then the logger.
7. **The sound test, about 21 minutes, hands off.** Follow the two steps under *Sound test* in the logger: set the volume, then **Start sequence** and walk 65 ft or more away. Afterwards, tap **Save recording** on the mic phone ([more](#speaker-test)).
8. **The radio walk.** Walk away from the detector with the gateway. At 330, 660, 1,300 ft and on, enter the distance under *Radio walk*, tap **Start run**, and stop it when a packet arrives. Turn back when none comes in two minutes.

**The result** is the logger's *Range so far* table. The logger saves everything online as it goes, so there's nothing to export.

<p><a class="btn btn-primary" href="{{ site.baseurl }}/tools/weekend/logger.html">Open the logger</a></p>

A speaker can't copy what 330 ft of real ground and wind does to the sound. A real flight checks that later, in [layer 2]({{ site.baseurl }}{% link mvp.md %}#layer-2-hear-a-drone-from-near-the-ground-t11).

## Details

<details class="layer" id="screens" markdown="block">
<summary><span class="layer-title">What each phone shows</span><span class="layer-sub">Each phone asks which one it is: the logger phone runs the test, the mic phone sits by the mic</span></summary>

The logger is one web page that opens as two different screens. Open it on each phone from the **Open the logger** button above, or send the link from one phone to the other. Its first screen asks *Which phone is this?*. Your answer decides which screen you get, and the title at the top then says which one you're on. Nothing to scan, and no laptop on the day.

<div style="display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 16px">
<figure style="margin:0;flex:1 1 220px;max-width:280px"><img src="{{ site.baseurl }}/assets/images/weekend/pick-view.png" alt="The logger's first screen on a phone: Which phone is this? with three big buttons, Logger phone, Mic phone and Just watching, each with a line saying what that phone does" width="280" style="border:1px solid rgba(128,128,128,.4);border-radius:8px"><figcaption class="note">The first screen, on every phone.</figcaption></figure>
<figure style="margin:0;flex:1 1 220px;max-width:280px"><img src="{{ site.baseurl }}/assets/images/weekend/logger-view.png" alt="The trip/wire logger screen on a phone: Connect with three steps, boxes for the hotspot name and password and a Send to gateway button, then the alarm box reading quiet and the four radio readings" width="280" style="border:1px solid rgba(128,128,128,.4);border-radius:8px"><figcaption class="note"><b>trip/wire logger</b>, on the logger phone, at the top: <i>Connect</i>, then the alarm and radio.</figcaption></figure>
<figure style="margin:0;flex:1 1 220px;max-width:280px"><img src="{{ site.baseurl }}/assets/images/weekend/logger-tests.png" alt="Further down the logger: Sound test with two steps, a sound picker, Play calibration, Measure at the mic, Start sequence and Stop; then Radio walk with one distance box, Start run and Stop run" width="280" style="border:1px solid rgba(128,128,128,.4);border-radius:8px"><figcaption class="note">Further down the logger: <i>Sound test</i> (step 7) and <i>Radio walk</i> (step 8).</figcaption></figure>
<figure style="margin:0;flex:1 1 220px;max-width:280px"><img src="{{ site.baseurl }}/assets/images/weekend/mic-view.png" alt="The trip/wire mic screen on a phone: one big sound level, the Mic phone panel saying it is connected to the logger with a Save recording button, and the Speaker panel saying the logger phone starts the speaker" width="280" style="border:1px solid rgba(128,128,128,.4);border-radius:8px"><figcaption class="note"><b>trip/wire mic</b>, on the mic phone. It reads a raw level until its meter is set (step 3), then dB(A).</figcaption></figure>
</div>

- **The logger phone, at the receiving end, shows *trip/wire logger*.** Tap **Logger phone**, then your gateway: it shows up under *Connect* by itself once the hotspot is on and the gateway has power. The first time, you give the gateway this phone's hotspot from *Connect* too. Top to bottom it shows *Connect*, the alarm and radio, *Sound at the mic*, *Sound test*, *Radio walk* and *Range so far*. Anything you won't need on the day sits in a closed *More* or *Settings* box.
- **The mic phone, at the sound end, shows *trip/wire mic*.** Tap **Mic phone**, then the logger, which shows up by itself while the logger is open. That one tap starts the mic. After that you touch it once more, to **Save recording** at the end. In between the logger runs it, starting and stopping the recording and the speaker, and its big number is the sound at the mic. Its *More* boxes are for home and for spares.
- **The gateway has no screen.** It shows on the logger as the chip under the title, which reads *gateway online*, and as *last packet* resetting about once a minute.
- **The laptop opens *trip/wire logger* too**, for step 3 at home only. Plugged into the detector by USB, it also shows *detector mic, dB(A)* and the button that sets the mic phone's meter. It stays home on the day.

Anyone else can follow along from anywhere by tapping **Just watching**, a third, watch-only screen, *trip/wire watch*. If either phone ends up on the wrong screen, tap **Change phone** at the top.

</details>

<details class="layer" id="field-layout" markdown="block">
<summary><span class="layer-title">Where everything goes</span><span class="layer-sub">Two ends: the sound end stays put, and the receiving end goes wherever you go</span></summary>

The test uses two boards and two phones:

- **Board 1, the detector,** has the mic. It decides whether it hears a drone and sends each alarm by LoRa radio.
- **The mic phone** sits beside the mic. It measures and records the sound there, and plays the test sound to the speaker by Bluetooth.
- **Board 2, the gateway,** has no mic. It receives the detector's radio messages and passes them to the logger phone over its hotspot.
- **The logger phone** runs the logger and the hotspot, and tells the mic phone what to play and when.

**The distances are played, not walked.** The speaker is always 16 ft from the mic. For 330 ft, the mic phone plays the drone as quietly as it would sound from 330 ft away: 26 dB quieter than at 16 ft, since every doubling of distance takes 6 dB off. So Bluetooth only ever has to cover 16 ft. The one thing that goes far is the radio, from board 1 to board 2.

So the test has two ends. The **sound end** (board 1, the mic, the mic phone and the speaker) never moves. The **receiving end** (board 2 and the logger phone) is you, and goes wherever you go. The only link between the ends is the one under test, LoRa; the two phones keep in touch over mobile data. A real system is the same chain: one gateway listening to detectors spread across a field.

<figure class="field-layout" style="margin:12px 0 16px;max-width:420px">
<svg viewBox="0 0 360 600" width="100%" role="img" aria-labelledby="flTitle flDesc" style="color:inherit;font-family:inherit">
<title id="flTitle">Field layout for the Saturday test</title>
<desc id="flDesc">Seen from above, not to scale. A callout explains that the speaker never moves: it sits 16 feet from the mic and the mic phone plays the drone quieter to stand in for 80 to 1,000 feet. The sound end: board 1, the detector, wired to the mic 20 inches up, with the mic phone beside it, and the speaker on a chair 16 feet away, which the mic phone plays by Bluetooth. A LoRa radio link runs from board 1 to the receiving end, 65 feet or more away during the sound test and walked out to 1,300 feet and beyond for the radio walk. The receiving end: you, carrying board 2, the gateway, with its power bank, and the logger phone, whose hotspot the gateway joins by WiFi a pocket away. The two phones talk over their own mobile data, through the internet.</desc>
<rect x="6" y="6" width="348" height="88" rx="10" fill="#c2562c" fill-opacity="0.08" stroke="#c2562c" stroke-opacity="0.6"/>
<text x="18" y="27" font-size="12" font-weight="700" fill="#c2562c">HOW 330 FT FITS IN A YARD</text>
<text x="18" y="46" font-size="12" fill="currentColor">The speaker never moves: it stays 16 ft from</text>
<text x="18" y="62" font-size="12" fill="currentColor">the mic and plays the drone quieter, as quiet</text>
<text x="18" y="78" font-size="12" fill="currentColor">as it sounds from 330 ft. Only the radio walks.</text>
<rect x="6" y="106" width="348" height="228" rx="10" fill="#6a9a3a" fill-opacity="0.08" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="4 4"/>
<text x="18" y="126" font-size="12" font-weight="600" fill="currentColor" fill-opacity="0.7">SOUND END: STAYS PUT, ON GRASS</text>
<line x1="48" y1="152" x2="48" y2="136" stroke="#534ab7" stroke-width="1.6"/>
<rect x="18" y="152" width="36" height="36" rx="5" fill="#534ab7" fill-opacity="0.15" stroke="#534ab7"/>
<text x="36" y="176" font-size="16" font-weight="700" text-anchor="middle" fill="#534ab7">1</text>
<line x1="54" y1="170" x2="66" y2="170" stroke="currentColor" stroke-width="2"/>
<circle cx="82" cy="170" r="16" fill="#1d9e75" fill-opacity="0.18" stroke="#1d9e75"/>
<text x="82" y="174" font-size="11" font-weight="600" text-anchor="middle" fill="currentColor">Mic</text>
<rect x="110" y="148" width="24" height="44" rx="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
<line x1="118" y1="186" x2="126" y2="186" stroke="currentColor" stroke-width="1.4"/>
<text x="148" y="152" font-size="13" font-weight="600" fill="#534ab7">Board 1: detector,</text>
<text x="148" y="168" font-size="13" fill="currentColor">wired to the mic, 20 in up</text>
<text x="148" y="188" font-size="13" font-weight="600" fill="currentColor">Mic phone beside it:</text>
<text x="148" y="204" font-size="13" fill="currentColor">meter, recorder, player</text>
<line x1="122" y1="194" x2="122" y2="266" stroke="#c2562c" stroke-width="2" stroke-dasharray="1 4" stroke-linecap="round"/>
<text x="130" y="236" font-size="12" font-weight="600" fill="#c2562c">Bluetooth, 16 ft: plays</text>
<text x="130" y="251" font-size="12" fill="#c2562c">the drone, turned down</text>
<rect x="87" y="268" width="70" height="46" rx="8" fill="#c2562c" fill-opacity="0.1" stroke="#c2562c"/>
<rect x="102" y="274" width="40" height="34" rx="6" fill="none" stroke="currentColor" stroke-width="1.4"/>
<circle cx="122" cy="291" r="9" fill="none" stroke="currentColor" stroke-width="1.2"/>
<text x="168" y="287" font-size="13" font-weight="600" fill="#c2562c">Speaker on a chair,</text>
<text x="168" y="303" font-size="13" fill="currentColor">facing the mic</text>
<line x1="36" y1="190" x2="36" y2="452" stroke="#534ab7" stroke-width="2" stroke-dasharray="6 4"/>
<text x="48" y="356" font-size="12" font-weight="600" fill="#534ab7">LoRa radio, board 1 to board 2:</text>
<text x="48" y="372" font-size="12" fill="currentColor">65 ft or more for the sound test,</text>
<text x="48" y="388" font-size="12" fill="currentColor">then walked out to 1,300 ft and on.</text>
<text x="48" y="404" font-size="12" fill="currentColor">The only link that goes the distance.</text>
<rect x="6" y="420" width="348" height="100" rx="10" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.5"/>
<text x="60" y="440" font-size="12" font-weight="600" fill="currentColor" fill-opacity="0.7">RECEIVING END: YOU, CARRYING</text>
<rect x="18" y="452" width="36" height="36" rx="5" fill="#534ab7" fill-opacity="0.15" stroke="#534ab7"/>
<text x="36" y="476" font-size="16" font-weight="700" text-anchor="middle" fill="#534ab7">2</text>
<rect x="58" y="458" width="14" height="24" rx="3" fill="none" stroke="currentColor" stroke-opacity="0.6"/>
<line x1="76" y1="470" x2="96" y2="470" stroke="#1a7fa8" stroke-width="2" stroke-dasharray="2 3"/>
<rect x="100" y="448" width="24" height="44" rx="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
<line x1="108" y1="486" x2="116" y2="486" stroke="currentColor" stroke-width="1.4"/>
<text x="136" y="462" font-size="13" font-weight="600" fill="#534ab7">Board 2: gateway</text>
<text x="136" y="478" font-size="13" fill="currentColor">+ power bank, WiFi to</text>
<text x="136" y="494" font-size="13" font-weight="600" fill="currentColor">logger phone (hotspot),</text>
<text x="136" y="510" font-size="13" fill="currentColor">a pocket apart</text>
<text x="8" y="546" font-size="12" fill="currentColor" fill-opacity="0.8">The two phones never connect to each other: each</text>
<text x="8" y="562" font-size="12" fill="currentColor" fill-opacity="0.8">uses its own mobile data, so the logger phone can</text>
<text x="8" y="578" font-size="12" fill="currentColor" fill-opacity="0.8">order plays from anywhere. Not to scale.</text>
</svg>
</figure>

- **The mic phone sits at the mic,** at the same height, so what it measures and records is what the detector hears. It plays to the speaker by Bluetooth, which reaches about 33 ft, less through a body or a bag, so nobody stands between them.
- **Carry the gateway with the logger phone.** It talks to the phone by WiFi, and a phone hotspot reaches about 30 ft, so keep them together: a pocket each is fine. The detector reaches the gateway by LoRa, which goes hundreds of yards; the radio walk measures how far.
- **Each board gets its own power bank.** If *last packet* stops resetting, the detector's power bank may have switched itself off: some do when a board draws too little. Use another one.
- **Stay 16 ft or more from walls, cars and fences,** on grass. A hard surface behind the mic adds up to 3 dB and flatters the result.
- **Check for a cell signal** where you set up. Both phones need mobile data: the hotspot needs it, and the mic phone reaches the logger over the internet. Give the mic phone its own data, not the hotspot, which won't reach it once you walk away.
- **Do Not Disturb matters, on both phones.** A notification on the mic phone plays through the speaker at test volume and gets logged as drone sound, and a call stops the audio. Airplane mode won't work, because both phones need data.
- **Give the gateway the logger phone's hotspot, not your home WiFi.** Otherwise it works in the garden and goes silent in the field. On an iPhone, switch on **Maximize Compatibility**: the board only sees 2.4 GHz.
</details>

<details class="layer" id="phone-setup" markdown="block">
<summary><span class="layer-title">Set up the phones</span><span class="layer-sub">The gateway joins the logger phone's hotspot, and both phones meet through a public MQTT broker</span></summary>

1. Know the logger phone's hotspot name and password, from its hotspot settings. On an iPhone the name is the phone's name (Settings, General, About). Switch on **Maximize Compatibility**: the board only sees 2.4 GHz.
2. [The flasher]({{ site.baseurl }}/tools/flasher/) asks for nothing: it makes up a gateway ID and fills in the broker. Flash both boards from the same computer, since they need the same network key.
3. On the logger phone, open the logger, tap **Logger phone**, and type the hotspot's name and password under *Connect*. The logger keeps them on this phone.
4. Power the gateway. If it doesn't know this phone's hotspot, it opens its own WiFi network, *tw-… setup*, within a minute. With the hotspot off, join that network from the logger phone, go back to the logger and tap **Send to gateway**. A new tab says *Saved*. (Without the logger, type the hotspot into the gateway's own page at *192.168.4.1* instead.) The gateway remembers it, and the one before it. Then turn the hotspot on. The gateway shows up under *Connect* about 30 s later, by the ID the flasher gave it: tap it. To change logger phones later, do the same from the new one. The chip turns to *gateway online* when the board checks in. An iPhone only shows its hotspot while the Personal Hotspot screen is open, so keep it open until then.
5. On the other phone, on its own mobile data, open the logger, tap **Mic phone**, then tap the logger, and allow the microphone. That tap starts the mic and also lets it play the speaker. *Sound at the mic* in the logger then shows *live* under *mic phone*.

Readings pass through a free public broker, and the saved sessions can be read by anyone with the link: fine for a test, not for anything sensitive. Keep both screens on, since readings that arrive while the logger is locked are lost, and a locked mic phone stops its mic and the speaker.

**Only one phone?** Tap *Only one phone: use this phone's mic* instead. It works, but that phone has to stay at the mic and play the speaker, and the gateway has to stay within 30 ft of it, so the radio walk can't happen while the speaker plays.

With a laptop and a cable, use **Connect USB** instead. Phones can't read a USB board from a web page. Plugging in the detector as well adds its confidence score.

The gateway hears from the detector when it alarms, when it clears, and once a minute in between. That once-a-minute check-in is what the radio walk counts. Leave **Beep on alarm** off while recording.
</details>

<details class="layer" id="phone-meter" markdown="block">
<summary><span class="layer-title">Set the phone's meter from the detector, and check the speaker</span><span class="layer-sub">Once, at home; no meter app needed</span></summary>

A phone's mic can measure sound, but phone mics differ by several dB, so its raw reading needs one known level to turn into dB(A). The detector's INMP441 mic gives it: its sensitivity is rated to within 1 dB, and over USB the detector reports its A-weighted level once a second. So the phone is set against the detector, once, and remembers it.

1. **Plug the detector into the laptop,** open the logger there from the flasher's link (it then has the same gateway ID) and tap **Connect USB**. *Sound at the mic* shows *detector mic, dB(A)*. In a quiet room it reads about 30–40.
2. **Put the mic phone right beside the detector's mic,** at the same height. Open the logger on it, tap **Mic phone**, then tap the laptop's logger.
3. **Play the calibration.** Pair the speaker with the mic phone, set it 3 ft away facing both mics, and tap **Play calibration** on the laptop. Turn it up until the detector reads 60–75 dB(A).
4. **Tap Set the mic phone's meter from the detector.** The button only works once the sound is loud enough and steady. A few seconds later the mic phone reads within about 1 dB of the detector, and the logger shows the gap between them. Tap the calibration off.
5. **Check the speaker.** It should sound the same with the mic on as it did with the mic off.

Every 6 dB halves or doubles the distance the speaker emulates, which is why this matters. Setting the phone from the detector also means the levels in the results are in the detector's own terms. The detector mic's 1 dB rating is the maker's figure for the chip; a clone board could be further off, and nothing in this kit can check it. The recording weighs about 45 MB an hour.

**If the detector shows "reads this as silence",** the room is quieter than its silence gate, about 37 dB at the mic, and it won't alarm. A quiet room can be. A field almost never is, and the logger shows the same warning there.

**If the speaker sounds thin once the mic is on,** like a phone call, the phone has switched it into call mode, which cuts the high notes the detector listens for. Some speakers with a built-in mic do this. Use a speaker without a mic, or an aux cable from the mic phone.
</details>

<details class="layer" id="speaker-test" markdown="block">
<summary><span class="layer-title">Run the speaker test</span><span class="layer-sub">Run from the logger phone; the mic phone plays the sound, measures it and records it</span></summary>

1. **Set up.** Silent mode off on the mic phone, and the speaker paired with it. Speaker on a chair 16 ft from the mic, facing it. The mic phone beside the mic, with its mic on.
2. **Calibrate.** In the logger's *Sound test*, pick a sound and tap **Play calibration**. Use the volume buttons, on the mic phone or the speaker, until *Sound at the mic* reads 60–65 dB(A). Then tap **Measure at the mic**: the mic phone reads 10 s with the speaker off and 10 s of calibration, and both readings fill in. Don't touch the volume again. Without the mic phone, type the two readings from any sound meter.
3. **Start sequence.** The logger sends the whole sequence to the mic phone, which waits 60 s while you walk away (*Walk away, s*), then starts the recording, plays the ladder of distances three times over, each play 30 s with 10 s of quiet between, records 4 minutes of background with the speaker off, and stops the recording: about 21 minutes in all. The default, eight distances from 80 ft to 1,000 ft, takes about 16 minutes of plays. The logger logs every play as a *Speaker* run and the background as a *No drone* run. The mic phone keeps its own time, so the sequence carries on if the logger phone loses signal. Fewer than 3 plays at a distance and the *Range so far* table won't rule on it; to save time, trim the distances rather than *Plays each*.

Each run keeps the level it aimed for, the level the mic phone measured and the detector's own level, so a play that came out wrong shows in the *Runs* table. That check only works for the loud plays: beyond about 160 ft the drone is quieter than a typical field, so *Measured* reads the background instead, and that's expected. Those plays rest on the calibration.

**Check the background run too.** A play counts as heard if any alarm arrives during it. If the 4-minute *No drone* run also alarms, far-distance "heard" results may be the field, not the speaker.

**Why not louder:** near full volume a small speaker distorts, and distortion adds the harmonics the detector listens for. The loudest step needs only 42 dB(A) at the mic.

The sounds are a DJI Mini 4 Pro and a 5-inch FPV from [batear-datasets](https://github.com/batear-io/batear-datasets) (MIT), or your own recording. Why a speaker can stand in for most distances, and what it misses: [the reasoning]({{ site.baseurl }}{% link mvp.md %}#speaker-reasoning).
</details>

<details class="layer" id="weekend-downloads" markdown="block">
<summary><span class="layer-title">Downloads and training clips</span><span class="layer-sub">The logger as one file, its sounds and the clip cutter</span></summary>

| File | What it's for | Get it |
|---|---|---|
| Logger | One file that also works offline over USB | <a href="{{ site.baseurl }}/tools/weekend/logger.html" download>logger.html</a> |
| Drone sounds | Built into the logger | <a href="{{ site.baseurl }}/tools/weekend/sounds/mini.mp3" download>mini.mp3</a> · <a href="{{ site.baseurl }}/tools/weekend/sounds/fpv.mp3" download>fpv.mp3</a> |
| Clip cutter | Fetches the saved session, lines the phone's recording up with the logger and cuts each run into labelled 1 s clips, noting whether Batear was alarming | <a href="{{ site.baseurl }}/tools/weekend/cut_clips.py" download>cut_clips.py</a> · <a href="{{ site.baseurl }}/tools/weekend/test_cut_clips.py" download>tests</a> |

Optional, afterwards (Python 3.11+, and [ffmpeg](https://ffmpeg.org/) for a phone's `.m4a`):

```bash
python cut_clips.py --session latest --recording S20261025-1003-mic.m4a --mic --tag mic05 --rate 16000 --out clips
```

`--mic` uses the start time the phone logged, good to a few tenths of a second, which is fine for 1 s clips. For a recording made any other way, clap next to it while tapping **Sync clap** and use `--sync`.

Hold out whole runs for testing, never clips from a run you trained on.
</details>
