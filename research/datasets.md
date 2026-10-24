---
title: Training data and sound libraries
parent: Research Notes
nav_order: 5
---

# Training data and sound libraries
{: .no_toc }

1. TOC
{:toc}

## Public datasets found

| Dataset | Contents | Licence / access | Use |
|---|---|---|---|
| **DroneAudioset** | 23.5 h annotated recordings, wide SNR range (down to −57 dB) | MIT; Hugging Face `ahlab-drone-project/DroneAudioSet` | Drone-mounted mics; ego-noise research |
| **RWDA** (rotary-wing drone acoustic) | Drone sounds + natural environmental noise, open field | IEEE DataPort | Robust detection in noise |
| **Multiclass acoustic drone dataset** (2025) | 3,200 recordings from 32 UAV types, ~16,000 s | arXiv 2509.04715 | Multi-class identification |
| **Drone Sound Audio Detection** | Binary drone / unknown | Kaggle | Baseline classifier |
| **Sara Al-Emadi drone audio dataset** | Early drone audio corpus | **Academic and non-commercial use only** (the repo's licence, read 2026-10-19). Fine for benchmarking; a model trained on it can't ship in a sold product without permission | Baseline |
| **FPV drone audio classification dataset** (Saarmets, 2026) | Public WAV recordings of FPV drones, about 660 MB ([GitHub](https://github.com/saarmets/fpv-drone-audio-classification-dataset)) | CC BY 4.0 | FPV positives, the target the tripwire cares about most; contents not yet audited |
| **batear-datasets** | Mavic recordings, clips captured on Batear boards, and urban and rural negatives ([GitHub](https://github.com/batear-io/batear-datasets)) | MIT | Clips from the same chip and mic family as our listener |
| **AcousticPrint** | 5 commercial drones recorded at ~66 ft, 4 more from YouTube, plus vehicles, bees and speech as negatives | No licence stated; ask the authors before reuse | Open-set rejection of unknown sounds; see [Open-source projects]({{ site.baseurl }}{% link research/open-source-builds.md %}#acousticprint) |
| **Western Sydney 24-mic localization** | Multi-mic recordings with GPS flight logs | Research release | Testing bearings and triangulation offline |

## The real gap

{: .warning }
> The original framing mentions an open-source drone sound library from **Ukraine and Norway**. We have **not** yet found it. Candidates to check: Squarehead (Norway) publications, Ukrainian volunteer projects (Zvook, Sky Fortress), NATO/DIANA challenges. **Add the link here once found.**

- Public datasets are mostly small hobby/commercial quadcopters.
- **Shahed/Geran, Lancet and fiber-optic FPV recordings** are what a military customer cares about, and they are scarce publicly. This is likely the true data bottleneck; partnering with a Ukrainian or Baltic program for recordings matters more than any model architecture.
- **Collecting our own:** the open-source [Batear]({{ site.baseurl }}{% link research/open-source-builds.md %}#batear) detector can save the audio around each alarm to an SD card, a cheap way to gather labelled field recordings.
- **Negative data** (mopeds, chainsaws, generators, tractors, aircraft, wind, rain) from the actual deployment region is just as important, to keep false alarms down.

## Sources

- [DroneAudioset — arXiv 2510.15383](https://arxiv.org/pdf/2510.15383)
- [RWDA — IEEE DataPort](https://ieee-dataport.org/documents/rotary-wing-drone-acoustic-dataset-rwda-dataset)
- [Multiclass acoustic dataset — arXiv 2509.04715](https://arxiv.org/pdf/2509.04715)
- [Kaggle — Drone Sound Audio Detection](https://www.kaggle.com/datasets/amineipad/drone-sound-audio-detection)
- [Sara Al-Emadi — Drone Audio Dataset](https://saraalemadi.com/2019/01/12/drone-audio-dataset/)
