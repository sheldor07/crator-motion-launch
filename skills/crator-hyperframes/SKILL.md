---
name: crator-hyperframes
description: Create and refine Hyperframes motion videos for Crator and Yajat using the lessons from the Crator launch film. Use for Crator launch videos, feature demos, faceless product films, storyboards, camera choreography, and feedback such as “looks like a PPT,” “not visually interesting,” “scaling is weird,” or “the composition is off.” Captures Yajat's preferences for continuous product stories, native ERPNext UI, dramatic but smooth camera work, readable feed-scale typography, purposeful color and depth, and cohesive endings. Pair with Hyperframes technical skills; do not apply this film direction to unrelated websites, slide decks, or simple talking-head caption edits.
---

# Crator motion direction

Make a short film in which the viewer follows a business action becoming working software. The canvas is larger than the viewport. The camera discovers relevant parts of it. A succession of animated presentation layouts is the principal failure this skill prevents.

This is a creative and review layer over the Hyperframes workflow, not a replacement renderer. Read `/hyperframes` for routing and use its core, keyframes and audio guidance as needed. Use motion-doctrine and seam-craft for continuity mechanics when available. Do not turn their default transition recipes into an identical move at every boundary: Yajat explicitly preferred varied pacing, smooth dissolves where appropriate, and continuity that serves the story. Current user instructions take precedence over these recorded preferences.

## Start from evidence

Read [preferences and corrections](references/preferences.md) before directing a new film. For a narrow edit, read only the relevant section plus the actual scene source. Read [techniques](references/techniques.md) when choosing choreography, [production](references/production.md) when building or checking it, and [source map](references/source-map.md) when you need real implementations and reference frames.

1. Recover the accepted brief, latest render, current source and checkpoint. Re-read edited HTML before rebuilding; Studio may have changed it independently of its generator.
2. Identify the audience, business outcome, aspect ratio, duration, CTA and any confirmed claims. Reuse answers already provided. Ask only for missing information that changes the work; continue independent work while waiting.
3. Distinguish a new film, a broad motion redesign, and a local correction. A request to center a stamp does not authorize redesigning the whole film. A complaint that it feels like a slideshow usually does require rethinking its composition and sequence.
4. For new direction, inspect the user's actual reference footage in motion. Sample promising passages every 0.25–0.5 seconds, then watch those passages at speed. Record what persists, camera targets, depth, background changes, holds and exits. A thumbnail, logo wall or source-code listing does not establish how a video moves. Say when a reference is inaccessible; do not claim to have studied it.
5. Pick one or two relevant references and extract mechanisms, not their branding. Avoid endless reference searches once the missing technique is understood. The historical study and source map let you resume without rediscovering everything.

## Design a causal sequence before styling scenes

Write a short beat map. For each beat record:

| Field | Question |
| --- | --- |
| Message | What single new thing should the viewer understand? |
| Subject | Which real UI fragment, business object, word or mark carries it? |
| Action | What changes? What visibly causes that change? |
| Camera | Where do we start, travel and arrive? What becomes readable there? |
| Composition | What dominates now? What is secondary or intentionally cropped? |
| Field | Which solid color, inversion or pattern supports this action and its neighbor? |
| Handoff | What survives into the next beat, at what position, scale and velocity? |
| Read | When does movement settle enough to understand the result? |

Do not use this table as the on-screen layout. It is a planning aid.

Select different actions for adjacent beats. For example: spreadsheet rows become imported items; the camera follows one item into an assembled product and native BOM; that product's order travels along an approval route; the cursor approves it; the same order returns with its changed state. This is one story. Three repeated title → zoomed screen → green tick sequences are still a slideshow.

Create visual density through relationships: neighboring records, an alternate route, layered product planes, foreground objects and purposeful occlusion. Extra cards, random shapes, a progress counter and an idle wobble do not supply missing narrative.

For a broad redesign, build a short motion sample spanning two or three connected beats before finishing the whole film. Show real timing, UI and camera behavior. Static sketches may help composition but cannot prove motion quality. Continue through already authorized work; do not introduce a new approval stop by default.

## Win recognition, then move the thought forward

The opening needs a recognizable visual idea immediately. Generic “Introducing Crator” and “Implementation takes months” were weak openers for this launch because they gave a cold viewer little reason to stop.

When the brief supports a familiar-product analogy, make the familiar mark **and wordmark** readable from the first beat. Let their animation resolve into the complete comparison, then carry its important word or object into the product story. A tiny “Meet” followed by a delayed logo wastes the strongest attention window. Do not rush into the complete sentence and then park there for seconds.

For the accepted launch, the chain was Lovable lockup → “Meet Lovable for ERP” → the same ERP word with colorful module icons → icons passing the camera → centered “Describe your business.” This is an example, not the template for every future video. The drawn orbit ring was eventually removed; recognition and the icon movement worked without it.

Keep a carried word's font, weight, spacing and color consistent across a transition unless the transformation is intentional and legible. Prior mismatched ERP text made two adjacent scenes feel disconnected even when their positions were close.

## Show the actual product at a useful scale

Use Crator's real composer and ERPNext primitives for product passages. Inspect available frontend code, screenshots or recordings before inventing UI. Preserve recognizable document titles, fields, tabs, rows, badges and action semantics. Remove irrelevant navigation to focus the film; do not replace the product with generic floating dashboard cards.

Show the module you claim: inventory through items, warehouses or stock; manufacturing through BOMs, operations or work orders; accounting through invoices or ledger views. Reusing a sales-order screen under three module labels does not demonstrate three modules.

Make the input readable on LinkedIn/X. Include a specific, concise business request and recognizable input evidence, such as a spreadsheet icon, a filename and a few representative rows. The example should establish context without unnecessary SKU detail. Let text name the agent's actual work: migrating data, customizing modules, building workflows. Avoid duplicating the same sentence as a title, agent status and bottom caption.

Scale the interface as a coherent object. Compute the camera target from the relevant control or record. Preserve the relative sizes of the input, model label, attachment button, spinner and send control. Camera enlargement is not permission to make every table cell enormous. Establish enough UI to orient the viewer, approach the meaningful action, then reveal its consequence.

Use a cursor when it explains causality. Its tip should reach the real target, the click and reaction should coincide, and it should leave once it has done its job. A wandering cursor over an unchanged screen is decoration.

## Choreograph the camera, depth and color together

Use a pose sequence on one scene world: establish → approach → act → reveal consequence. Mix a slow anticipatory move, acceleration in transit, a readable arrival and a shorter departure. Dramatic means a meaningful change of framing, not constant high velocity. Avoid identical linear sweeps or the same easing duration everywhere. The user explicitly preferred smooth over abrupt when a cut felt accidental.

Use 3D where it explains space or the business: a product assembling, a document with thickness banking through a route, interface planes passing at different depths. Keep readable faces oriented toward the viewer during the read. An arbitrary tilted screen that lands and remains framed under a title is still a presentation layout.

Use color as part of the action: a control expands into a field, a passing object occludes the next space, or the same text reverses contrast. Prefer flat fields, negative black/white and useful grid/dot patterns over soft gradient wallpaper. Preserve the background through a continuous thought unless the change has a visible cause. The Lovable logo's own gradient is an asset, not an excuse to add gradient backgrounds.

Orange is useful punctuation and should not disappear from a lifeless beige/black film. It need not cover every screen. Pastels and other colors are allowed when contrast and subject separation work. “On brand” is not sufficient if the result is dull. Likewise, changing the field color without changing the action will not rescue a weak scene.

The technique reference is a menu, not a quota. Do not add an orbit, a particle field, a whip or a new background solely to check a box. Constantly meaningful development matters more than constant motion.

## Compose the reading holds, not just the entrances

Set one primary message per hold. Define a clear secondary group and attach supporting information to it. Avoid unrelated top labels and a large image occupying the rest of the frame. Text may briefly own the center, then move, be passed by, or become part of the next object.

Diagnose balance before changing fonts. Look at visible ink, container alignment, relative weight, spacing and asymmetric decorative elements. Center the **whole visible group**, not a text container that happens to be centered while its children are left aligned. A checkmark plus “Approved” is one group. Treat the logo, CTA and destination as a composed group rather than three independently centered blocks.

Use Switzer for Crator display text and the product's native faces for UI when those assets are available. Use regular/medium weight by default; large type can carry impact without indiscriminate bold. Deliberate hook emphasis is fine. Do not give “Meet,” “for,” and the comparison arbitrary sizes that make the sentence look broken.

Check at full resolution and around 480–640 pixels wide. Essential copy should read without pausing or zooming the player. Avoid rigid universal font sizes: field labels, interface context, headlines and wordmarks have different jobs.

## Make the comparison and ending intelligible

Use a complete thought: “Traditional implementation takes months” and “Crator takes weeks” communicate more than isolated Months/Weeks labels. Reuse a plan or timeline to make the time comparison visual.

If showing a bill, design a recognizable estimate: document title, relevant scope, subordinate rows and a clearly dominant total. If showing a number, give it a reason to exist in that scene rather than placing it on an empty generic card. Make only confirmed claims. The launch's fixed monthly price was removed because it differed by geography; do not reuse those amounts as evergreen facts.

End with one action and a usable destination. Use the supplied Crator lockup with safe space and no invented tile, arrow or underline unless requested. Group the URL closely with its invitation and subordinate it visually. If a trial headline already arrived, carry it into the final background rather than replaying it as a second CTA.

When moving the closing group, update its incoming matched elements too. Centering only the last scene creates a jump that a static screenshot will miss.

## Review, verify and deliver

Follow the detailed checks in [production](references/production.md). At minimum:

- Watch the current export at speed with sound and muted. Check both comprehension and rhythm; inspect the first frame and the first three seconds separately.
- Inspect full-size and feed-size frames at the opening, each action, each reading hold and the close. Also inspect several frames before/at/after changed transitions.
- Ask of every move: **what new thing becomes visible or happens because of it?** Cut padding, not the time needed to understand the result.
- Check module relevance, consistent record identity, cursor targets, real UI proportions, typography continuity and group centering.
- Run the project's full Hyperframes check. Distinguish intentional off-canvas travel from accidental clipping during reading holds. Passing checks do not prove visual quality.
- For timing edits, update scene durations, subsequent starts, root duration, audio tail and the continuity ledger. For position/scale edits near a boundary, reopen that seam's check.
- Preserve useful local Git checkpoints, keep source and generated composition aligned, and deliver the actual rendered MP4 with an absolute link. Push, publish or share according to the user's authorization, not merely because the skill was invoked.

When the user rejects a pass, name the specific failure and change the responsible mechanism. Do not respond to “PPT” with another title-and-card variation, to “too quick” by slowing every scene equally, or to “not centered” by guessing a global offset without inspecting the visible group.
