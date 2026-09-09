# Crator motion launch video

Standalone source for the latest Crator launch film: **v42**, 27.5 seconds, 1920 × 1080 at 30 fps. Extracted from checkpoint `ca641c2` of the original launch-video project.

[Watch the included reference render](renders/crator-v42-centered-and-tighter.mp4)

## Run

Requirements: Node.js 22+, npm, Python 3.12+ for source regeneration, and FFmpeg for rendering. The Hyperframes CLI is pinned to 0.8.31; npm fetches it on first use. Network access is needed for initial setup and the GSAP CDN.

```sh
npm run dev
```

For an agent-managed persistent preview:

```sh
npx --yes hyperframes@0.8.31 preview --background
```

## Edit and render

The checked-in HTML works immediately. Edit the Python generators, then rebuild and validate:

```sh
npm run build
npm run check
npm run render
```

The new export is written to `renders/crator-motion-launch.mp4`. The included v42 reference stays intact. No original frontend checkout, reference videos, API credentials or external source folders are required.

| Source | Scene |
| --- | --- |
| `scripts/opening-scenes.py` | Lovable recognition, ERP modules and icon camera pass |
| `scripts/describe-motion.py` | Furniture-business prompt and spreadsheet import |
| `scripts/build-montage.py` | Data migration and manufacturing |
| `scripts/workflow-journey.py` | Approval workflow and centered Approved confirmation |
| `scripts/offer-motion.py` | Traditional estimate, weeks comparison and trial transition |
| `scripts/close-motion.py` | Final Crator lockup and trial destination |
| `scripts/build-timeline.py` | Scene timing and music placement |

`scripts/source-ui/` contains the captured UI markup and styles needed by the generators. `assets/` contains local fonts, logos, ERPNext icons and the selected music edit. `ledger.json` records continuity checks at scene boundaries.

## Current cut

Lovable → ERP modules → describe your business → migrate data → customize manufacturing → build an approval workflow → traditional implementation estimate → Crator takes weeks → free trial at cratorlabs.ai.

The implementation estimate exits half a second earlier than v41. The Approved group is centered; the closing lockup, headline and URL are moved down together with matching incoming transition geometry.

## Asset attribution

Crator logos are supplied brand assets. Lovable's mark is sourced from SVGL. Module icons come from Frappe ERPNext desktop icons; the UI is an illustrative reconstruction using furniture-business demo records. The soundtrack is the user-selected **Get Down — Rex Banner**, with a one-second source offset, -3 dB gain and a closing fade. Third-party media, fonts and marks retain their respective rights; this repository does not assign them a new license.

Hyperframes remains on 0.8.31 because the existing clip-visibility implementation failed validation under 0.8.33 during the original project. Validate before upgrading.
