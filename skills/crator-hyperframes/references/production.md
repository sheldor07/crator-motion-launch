# Build and review mechanics

Use the installed Hyperframes contracts for API details. This document preserves practical lessons from the film rather than freezing the framework at one version.

## Source discipline

- Inspect `AGENTS.md`, project context, package scripts and the current render. Keep generated HTML and generator source aligned. A full rebuild can silently overwrite Studio-only changes; reconcile them first or regenerate only the intended scenes.
- Keep local assets and reproducible scene generators. The standalone Crator repository includes native UI source fragments; it does not require the original frontend checkout just to rebuild.
- Register seekable paused timelines under the correct composition IDs. Keep layout/data timing and runtime timelines consistent, and let the framework own media playback.
- If text geometry controls a camera move, measure after fonts are ready. The Lovable handoff required this; fallback-font widths moved the destination.
- Check the current CLI through the normal Hyperframes workflow, but treat an upgrade as a separate verified change. The historical project used 0.8.31 after 0.8.33 failed its existing visibility implementation. That is a compatibility note for this project, not a pin to impose on new projects.

## Camera math and group centering

For a world with transform origin `(0,0)`, viewport `(W,H)`, focal world point `(cx,cy)` and scale `s`, use `x = W/2 - cx*s`, `y = H/2 - cy*s`. A different transform origin requires its own geometry; do not paste this formula onto a center-origin wrapper without adjustment.

For a cursor target inside nested transforms, compute its displayed position after those transforms. Avoid guessed coordinates copied from an earlier camera pose.

For a checkmark plus word, center the flex contents as one group, not just the wide parent. For the closing, inspect the union of the visible logo, headline and URL; balance its top and bottom space. Font ascenders, descenders and transparent SVG padding mean box centers may differ from visible centers. Use the render to verify optical balance.

The final v42 correction centered the Approved group at the 1920×1080 canvas center and moved the whole closing group down 64 pixels. Those values belong to that composition. Compute a new layout for different content or aspect ratios.

## Time edits

When removing half a second from a reading hold, preserve the intended transition duration and move its start earlier. Update the sub-composition duration, all later host start times, root duration, music endpoint/fade and continuity ledger. Do not speed the entire preceding camera move merely to shorten the finished hold.

Separate recognition, travel and reading. A shorter hook does not require shorter UI reading time. Match sound to meaningful events; do not force every animation onto a beat if that destroys comprehension.

## Boundary checks

Record the outgoing and incoming carrier, cut time, position, scale and motion direction. On continuity cuts inspect frames on both sides, not only scene midpoints. Use the existing seam verifier if installed and appropriate for the transition type. A match cut, dissolve and object wipe have different correctness conditions; do not misclassify them just to satisfy a rule.

Protect opaque stage coverage so a transition cannot accidentally reveal white. When the same text changes color through a mask, both copies must share font, weight, size, tracking, width, alignment and position. Suppress overlap checks only for this verified intentional duplication, never broadly.

Any edit near the first/last second of a scene reopens that boundary. A final-frame-only reposition can create a visible jump even though both stills look good in isolation.

## Perceptual checks

Review three ways:

1. **Full moving export with sound:** rhythm, readable arrivals, music relationship, unintended waiting, abrupt cuts.
2. **Muted at feed size:** can a cold viewer recognize the hook, understand the input/action/result and read the destination?
3. **Targeted stills and short transition excerpts:** balance, safe edges, native UI proportions, cursor aim, background continuity, no flashes or doubled text.

When GUI playback is available, play the clip. Frame extraction alone supports composition/continuity review, not claims about having listened to the music or watched realtime playback. Be explicit about any verification limit.

Run the full project check after HTML edits. Fix errors, examine warnings, and inspect informational overflow at its sampled time. Deliberate off-canvas exits are expected on an open canvas; active text disappearing during its read is not.

Save a numbered local checkpoint when useful. Deliver a real MP4 and its path; a clean lint log or a description of improvements is not the deliverable. Preserve existing authorization and avoid repeated permission requests for ordinary reversible edits.
