---
title: Sensor Models
nav_order: 2
has_children: true
permalink: /models/
---

# Sensor Models

{: .note }
> **The notebook now centres on one use case, the [drone-laid tripwire]({{ site.baseurl }}{% link index.md %}).** The models below are the survey it came out of. They are kept for reference and are not being developed.

Each page describes one way of deploying listeners, with a feasibility rating, an estimated cost, how it works, what limits it, and the open questions that would change the rating.

The [overview matrix]({{ site.baseurl }}{% link research/landscape.md %}#eight-ways-to-build-the-network) compares them side by side.

## Recommended combination (current view)

1. **Core:** [M1 fixed mic-array nodes]({{ site.baseurl }}{% link models/m01-ground-array-mesh.md %}) mounted per [M4 elevated placement]({{ site.baseurl }}{% link models/m04-elevated-nodes.md %}).
2. **Bootstrap / surge:** [M2 phones]({{ site.baseurl }}{% link models/m02-phone-network.md %}) where speed matters more than unit quality.
3. **Phase 2:** [M10 hybrid cueing]({{ site.baseurl }}{% link models/m10-hybrid-cueing.md %}) — add passive RF and camera confirmation at key sites.
4. **R&D bet:** the [drone-laid tripwire]({{ site.baseurl }}{% link models/tripwire.md %}), built on [M7 drone-deployed nodes]({{ site.baseurl }}{% link models/m07-drone-deployed-nodes.md %}) for fast placement in contested areas.

Every model here is **passive**: nothing emits while it listens, and nothing depends on radar. Models rated below 3 (perch-and-listen drones, flying microphone swarms, fiber-optic distributed acoustic sensing) were dropped on 2026-10-15.
