# Lecture 30: Evaluation Metrics & Aerial Detection Challenges (Detailed Notes)

This lecture outlines quantitative metrics used to benchmark object detection algorithms in satellite imagery and details the domain-specific challenges faced in operational deployments.

---

## 1. Quantitative Evaluation Metrics
* **Intersection over Union (IoU):** Measures spatial overlap between predicted box $B_p$ and ground truth $B_g$:
  $$\text{IoU} = \frac{\text{Area}(B_p \cap B_g)}{\text{Area}(B_p \cup B_g)}$$
* **Precision & Recall:**
  $$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}$$
* **Average Precision (AP) & mAP:** Area under the Precision-Recall curve calculated for each class and averaged across all categories at a given IoU threshold (e.g., $\text{IoU} = 0.5$).

---

## 2. Key Challenges in Remote Sensing Object Detection
1. **Extreme Scale Variation:** Vehicles ($5-10$ meters) vs. Airports ($2,000$ meters) in the same geographic region.
2. **Dense Small Targets:** Hundreds of small cars or solar panels closely packed in urban scenes.
3. **Imbalanced Classes:** Massive background clutter (water, desert, forest) relative to rare foreground objects (e.g., damaged bridges).
4. **Atmospheric & Shadow Interference:** Shadow projections from tall buildings or clouds alter object geometry and spectral signatures.
