# v42 — centered approval and closing, tighter bill

- Center the Approved checkmark and text as one group at the canvas center.
- Remove 0.5 seconds of the implementation estimate hold, preserving the dissolve duration. All later scenes shift earlier; total duration is 27.5 seconds.
- Move the closing logo, headline and destination down 64 pixels as one group. Match the incoming headline and mask geometry so the transition stays continuous.
- Recut the same music source with its one-second source offset and a smooth ending fade.

Validation: full Hyperframes check passes with zero errors or warnings. Five seam checks pass. Layout info findings are the existing intentional off-canvas text exits.
