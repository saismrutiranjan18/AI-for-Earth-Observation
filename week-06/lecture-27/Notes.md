# Lecture 27: Feature Pyramid Networks (FPN) & Multi-Scale Object Detection (Detailed Notes)

This lecture explores **Feature Pyramid Networks (FPN)** and their critical role in addressing multi-scale object detection challenges in high-resolution Earth Observation imagery.

---

## 1. The Multi-Scale Challenge in Remote Sensing
* **Scale Variance:** Satellite images capture massive spatial scenes where target objects range from small vehicles ($10 \times 10$ pixels) to large industrial complexes or harbors ($500 \times 500$ pixels).
* **Single-Scale Limitations:** Deep layers in standard CNN backbones have large receptive fields and rich semantics, but low spatial resolution (losing tiny objects). Early layers have high spatial resolution, but lack semantic depth (leading to false positives).

---

## 2. Feature Pyramid Network (FPN) Design
FPN creates a pyramid of feature maps with high-level semantics at all spatial resolutions using a top-down pathway and lateral connections.

```
Bottom-Up Pathway (Backbone)         Top-Down Pathway (FPN)
  C5 (Low Res, Rich Semantics)  ──►  P5 (1x1 Conv)
       │                                  │  (2x Upsample + Add)
  C4 ──────────────────────────►  P4 ─────┤
       │                                  │  (2x Upsample + Add)
  C3 ──────────────────────────►  P3 ─────┤
       │                                  │  (2x Upsample + Add)
  C2 ──────────────────────────►  P2 (High Res, Rich Semantics)
```

---

## 3. Benefits of FPN in Earth Observation
* **Small Object Recall:** Small targets (like individual trees or cars) are detected on high-resolution feature maps ($P_2, P_3$) enriched with deep contextual semantics.
* **Large Object Context:** Large geographic structures (airports, agricultural fields) are evaluated on lower-resolution feature maps ($P_4, P_5$).
* **Computational Efficiency:** Adds minimal computational overhead while dramatically boosting multi-scale Detection Precision (mAP).
