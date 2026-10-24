# a road running along the front: 4.00 mi of road

## Plan
posts 21 (one every 1055 ft), fence 6.2 mi in 1 run(s): 35 fence darts, 5 of them tip darts on fiber trunks to a post (5.6 mi of fiber, the longest 5917 ft laid); 35 air-dropped darts in all
per mile of road: 5.3 posts, 8.8 darts; longest route to a post 5 hops; nodes cut off in the plan: 0

## Strike tracks (drone flying in at 60 mph within 60 degrees of the enemy direction, 1000 tracks)
| Guard | Darts | Worst warning | 10th pct | Median | Tracks with a minute (55 s) | 30 s | 10 s |
|---|---|---|---|---|---|---|---|
| Posts only | 21 | 0 s | 2 s | 4 s | 0% | 0% | 3% |
| Posts and fence | 56 | 60 s | 63 s | 72 s | 100% | 100% | 100% |

## Landings within 300 ft of the road (480 spots)
heard by a post 100%, by two or more 13%; distance to the loudest post: median 350 ft, 90th pct 525 ft
landings 600-1,500 ft off the road: heard by a post 10% (the rest only as a drone in, none out)

## One dead node, on the plan
worst single loss leaves 98% of tracks with a minute; 0 of 56 nodes cost more than 2 points
worst single fiber cut leaves 100% of tracks with a minute (the tip still relays to its neighbours by radio)

## Holes between repairs (each dart lost 0.5% a day, each post 1.0%, each fiber cut 1%, found and fixed within 1 day)
dead at a time: mean 0.5; tracks with a minute: mean 100%, worst day 98%; landings heard: mean 99%

## Laying the fence
planned: 35 darts in 13 sorties; 4.2 h with 6 packs and 2 charger channels, 2.5 h with 12 packs and 4
simulated, GPS jammed, confirm, 200 lays: darts 45.9 (9 in 10 within 51), 6.1 of them tip darts (9 in 10 within 8), sorties 18.0, 6.5 h (6 packs) / 3.1 h (12 packs), drones lost 0.32, points left for repair 0.14
tracks with a minute after the lay: mean 100%, lays with at least 97%: 100%

## Costs, ours, small batch (est.)
package: 50 air-dropped darts, 9 tip darts and 5 fiber ends, 25 posts, 14 receivers, outfitted drone with 12 packs and 4 channels: $6517 ($1631 a mile)
one re-lay of the fence: $2550 (46 darts, 6.1 of them tip darts, 0.32 drones, pack wear)
| Power | Fence re-lays a year | Fence | Post cell swaps | Repairs between re-lays | A year | A mile a year |
|---|---|---|---|---|---|---|
| Solar, 4 winter re-lays | 4.0 | $10198 | $0 | $9905 | $20103 | $5031 |
| Solar, 2 winter re-lays | 2.0 | $5099 | $0 | $9905 | $15004 | $3755 |
| No solar, 2-week cells | 26.0 | $66290 | $6688 | $9905 | $82884 | $20743 |
| No solar, 4-week cells | 13.0 | $33145 | $3344 | $9905 | $46394 | $11611 |
| No solar, 12-week cells | 4.3 | $11048 | $1115 | $9905 | $22068 | $5523 |
posts only, solar: $3756 a year in lost posts ($940 a mile); package 25 posts and 14 receivers $1533

## If the planning numbers are wrong (50 lays each)
| Case | Posts | Air-dropped darts | Per mile | Tracks with a minute, plan | Darts used a lay | Sorties |
|---|---|---|---|---|---|---|
| Plan | 21 | 35 | 14.0 | 100% | 45.7 | 17.9 |
| Drones come within 45 degrees, not 60 | 21 | 32 | 13.3 | 100% | 41.8 | 16.2 |
| Drones come within 75 degrees | 21 | 38 | 14.8 | 100% | 50.1 | 19.6 |
| Radio hop 800 ft, not 980 | 21 | 42 | 15.8 | 100% | 55.5 | 20.6 |
| Hearing 500 ft, not 656 | 31 | 41 | 18.0 | 100% | 50.5 | 19.3 |
| A trunk every 3 mi, not 2 | 21 | 35 | 14.0 | 100% | 45.3 | 17.1 |
| Landings 95% upright, not 85% | 21 | 35 | 14.0 | 100% | 41.0 | 16.1 |
| 1 fiber in 5 breaks while laid, not 1 in 20 | 21 | 35 | 14.0 | 100% | 47.5 | 19.4 |
| The last plan: radio relay trunks | 21 | 60 | 20.3 | 100% | 77.7 | 22.9 |
