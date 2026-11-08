# Build film review

A separate agent watches the build film frame by frame and says what would confuse a viewer: parts passing through each other or flying the wrong way, the product resting upside down or with its face hidden, flicker, a camera inside a part. It can change the film's direction (how the product rests, where the viewer stands, which way parts back out), and the film is re-rendered and watched again. Automatic checks replay every frame against the 3D models as well.

**Verdict:** pass (round 1). A clear, well-paced build film that presents the 8.4-inch Android tablet face-up in its natural orientation, cleanly separates the cover glass, front bezel, touch sensor, display panel, battery, boards, peripheral modules, and unibody aluminium shell in assembly order, and clearly shows the mainboard population and internal FPC cable routing before closing into the finished tablet.

| Severity | Time | Shot | What a viewer sees | Fix |
|---|---|---|---|---|
| P2 | 46.0 s | finale | A small white sliver of the internal touch FPC cable is faintly visible at the right inner bezel edge during the low-angle orbit. | Inset the touch_fpc_cable final waypoint slightly further under the opaque front_bezel mask in rea/spec.yaml. |

