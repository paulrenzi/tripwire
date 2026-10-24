## Plan
front darts 16 (open-ground plan 13), relays per trunk [0, 0], total 16
planned net with no errors: worst warning 60 s, 16 of 16 darts reach the unit
the last plan (radio trunks, +/-45): 13 front darts and 12 relays

| Sortie | Darts | Miles | Minutes | Battery used |
|---|---|---|---|---|
| 1 | F2 F1 F3 | 2.9 | 8.0 | 70% |
| 2 | F4 F5 F6 F7 | 2.9 | 8.4 | 69% |
| 3 | F8 | 2.2 | 5.4 | 52% |
| 4 | F15 F16 F14 F13 | 2.8 | 8.2 | 69% |
| 5 | F12 F11 F10 F9 | 2.7 | 8.2 | 66% |
planned lay: 1.0 h with 6 packs and a 2-channel charger; 3.3 h with 2 packs and 1 channel

## Wind: sorties needed for the planned darts (wind toward the enemy, plus the gust margin)
- 0 mph: 4
- 5 mph: 4
- 9 mph: 5
- 12 mph: 5
- 15 mph: 7
- 18 mph: 12

## Simulated lays (1000 each)
| Case | Whole | Survives any one loss | Darts used | 90th pct darts | Sorties | Hours | Worst warning, 10th pct | Drones lost | Survives a fiber cut |
|---|---|---|---|---|---|---|---|---|---|
| Last plan: radio trunks, +/-45, GPS jammed, confirm | 99% | 93% | 34.9 | 40 | 9.3 | 2.2 h | 58 s | 0.20 | - |
| This plan, GPS working, no confirm | 8% | 2% | 16.0 | 16 | 5.1 | 1.0 h | none (a track no dart hears) | 0.12 | 31% |
| This plan, GPS working, confirm | 100% | 94% | 20.3 | 23 | 6.6 | 1.3 h | 60 s | 0.13 | 99% |
| This plan, GPS jammed, confirm | 98% | 91% | 22.2 | 26 | 7.1 | 1.4 h | 58 s | 0.15 | 98% |
|   landings 95% upright | 100% | 93% | 19.8 | 23 | 6.3 | 1.2 h | 58 s | 0.12 | 99% |
|   radio hop 800 ft, not 980 | 99% | 91% | 26.7 | 31 | 8.0 | 1.7 h | 58 s | 0.16 | 97% |
|   compass 4 degrees, not 2 | 89% | 82% | 22.7 | 27 | 7.2 | 1.5 h | none (a track no dart hears) | 0.16 | 97% |
|   1 fiber in 5 breaks while laid | 98% | 87% | 23.3 | 28 | 7.8 | 1.7 h | 58 s | 0.14 | 93% |
|   15 mph wind | 99% | 91% | 22.1 | 26 | 8.1 | 1.7 h | 58 s | 0.17 | 97% |
|   14 F, packs not warmed | 98% | 89% | 22.5 | 27 | 17.0 | 6.0 h | 58 s | 0.35 | 97% |

demo lay (seed 7013): 22 darts, 8 sorties, 1.5 h, worst warning 61 s
