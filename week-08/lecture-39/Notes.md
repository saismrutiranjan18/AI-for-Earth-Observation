# Lecture 39: Disaster Monitoring & Damage Assessment (Floods, Earthquakes, Wildfires) (Detailed Notes)

This lecture highlights **AI applications in Natural Disaster Response**, focusing on automated flood extraction, earthquake infrastructure damage classification, and wildfire burn severity mapping.

---

## 1. Rapid Flood Mapping using SAR
* **Specular Reflection Mechanism:** Smooth open water reflects radar pulses away from the antenna, yielding low backscatter (dark pixels).
* **Thresholding & U-Net Mapping:** Deep segmentation models trained on Sentinel-1 VV/VH backscatter produce automated inundation maps even through heavy cloud cover.

---

## 2. Earthquake Building Damage Assessment (xBD Dataset)
* **Categorization Standard:** Evaluates pre-disaster and post-disaster VHR optical images to classify structures into 4 damage tiers:
  1. *No Damage*
  2. *Minor Damage*
  3. *Major Damage*
  4. *Destroyed / Collapsed*
* **Ordinal Loss & Imbalance Mitigation:** Utilizes Focal Loss and Ordinal Regression to handle severe class imbalance between intact buildings and rare collapsed targets.

---

## 3. Wildfire Tracking & Burn Severity
* **Normalized Burn Ratio (NBR):**
  $$\text{NBR} = \frac{\text{NIR} - \text{SWIR}}{\text{NIR} + \text{SWIR}}$$
* **Delta NBR ($\Delta\text{NBR}$):** Difference between pre-fire and post-fire NBR maps to delineate burn severity zones for post-fire ecological recovery planning.
