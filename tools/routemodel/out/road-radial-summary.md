# a road running toward the front: 4.03 mi of road

## Plan
posts 21 (one every 1064 ft), fence 10.2 mi in 1 run(s): 58 fence darts, 7 of them tip darts on fiber trunks to a post (7.8 mi of fiber, the longest 5911 ft laid); 58 air-dropped darts in all
per mile of road: 5.2 posts, 14.4 darts; longest route to a post 6 hops; nodes cut off in the plan: 0

## Strike tracks (drone flying in at 60 mph within 60 degrees of the enemy direction, 1025 tracks)
| Guard | Darts | Worst warning | 10th pct | Median | Tracks with a minute (55 s) | 30 s | 10 s |
|---|---|---|---|---|---|---|---|
| Posts only | 21 | 2 s | 4 s | 9 s | 9% | 16% | 43% |
| Posts and fence | 79 | 61 s | 69 s | 102 s | 100% | 100% | 100% |

## Landings within 300 ft of the road (486 spots)
heard by a post 100%, by two or more 24%; distance to the loudest post: median 340 ft, 90th pct 584 ft
landings 600-1,500 ft off the road: heard by a post 13% (the rest only as a drone in, none out)

## One dead node, on the plan
worst single loss leaves 98% of tracks with a minute; 2 of 79 nodes cost more than 2 points
worst single fiber cut leaves 100% of tracks with a minute (the tip still relays to its neighbours by radio)

## Holes between repairs (each dart lost 0.5% a day, each post 1.0%, each fiber cut 1%, found and fixed within 1 day)
dead at a time: mean 0.6; tracks with a minute: mean 100%, worst day 83%; landings heard: mean 99%

## Laying the fence
planned: 58 darts in 22 sorties; 8.4 h with 6 packs and 2 charger channels, 4.2 h with 12 packs and 4
simulated, GPS jammed, confirm, 200 lays: darts 76.0 (9 in 10 within 82), 8.5 of them tip darts (9 in 10 within 10), sorties 28.4, 11.7 h (6 packs) / 5.1 h (12 packs), drones lost 0.59, points left for repair 0.23
tracks with a minute after the lay: mean 100%, lays with at least 97%: 100%

## Costs, ours, small batch (est.)
package: 80 air-dropped darts, 11 tip darts and 7 fiber ends, 25 posts, 14 receivers, outfitted drone with 12 packs and 4 channels: $7938 ($1969 a mile)
one re-lay of the fence: $4135 (76 darts, 8.5 of them tip darts, 0.59 drones, pack wear)
| Power | Fence re-lays a year | Fence | Post cell swaps | Repairs between re-lays | A year | A mile a year |
|---|---|---|---|---|---|---|
| Solar, 4 winter re-lays | 4.0 | $16540 | $0 | $13052 | $29592 | $7341 |
| Solar, 2 winter re-lays | 2.0 | $8270 | $0 | $13052 | $21322 | $5289 |
| No solar, 2-week cells | 26.0 | $107510 | $6688 | $13052 | $127250 | $31567 |
| No solar, 4-week cells | 13.0 | $53755 | $3344 | $13052 | $70151 | $17402 |
| No solar, 12-week cells | 4.3 | $17918 | $1115 | $13052 | $32085 | $7959 |
posts only, solar: $3756 a year in lost posts ($932 a mile); package 25 posts and 14 receivers $1533

## If the planning numbers are wrong (50 lays each)
| Case | Posts | Air-dropped darts | Per mile | Tracks with a minute, plan | Darts used a lay | Sorties |
|---|---|---|---|---|---|---|
| Plan | 21 | 58 | 19.6 | 100% | 75.2 | 28.1 |
| Drones come within 45 degrees, not 60 | 21 | 53 | 18.4 | 100% | 68.8 | 25.6 |
| Drones come within 75 degrees | 21 | 61 | 20.3 | 100% | 80.2 | 29.5 |
| Radio hop 800 ft, not 980 | 21 | 69 | 22.3 | 100% | 91.8 | 32.0 |
| Hearing 500 ft, not 656 | 31 | 66 | 24.1 | 100% | 82.6 | 30.3 |
| A trunk every 3 mi, not 2 | 21 | 58 | 19.6 | 100% | 76.0 | 26.7 |
| Landings 95% upright, not 85% | 21 | 58 | 19.6 | 100% | 68.8 | 26.1 |
| 1 fiber in 5 breaks while laid, not 1 in 20 | 21 | 58 | 19.6 | 100% | 77.3 | 29.7 |
| The last plan: radio relay trunks | 21 | 93 | 28.3 | 100% | 120.4 | 34.9 |
