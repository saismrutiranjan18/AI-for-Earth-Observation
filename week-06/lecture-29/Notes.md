# Lecture 29: Oriented Object Detection (OBB) & Rotated Bounding Boxes (Detailed Notes)

This lecture discusses **Oriented Object Detection (OBB)**, specialized bounding box representations, and benchmark datasets (e.g., DOTA, FAIR1M) for Earth Observation.

---

## 1. Why Oriented Bounding Boxes in Remote Sensing?
* **Top-Down Perspective:** Satellite and aerial sensors view Earth from a bird's-eye perspective. Objects (ships, airplanes, harbor docks, harbor containers) appear at arbitrary orientation angles $\theta \in [-90^\circ, 90^\circ]$ or $[0, 2\pi)$.
* **Drawback of Horizontal Bounding Boxes (HBB):** Horizontal boxes cause massive IoU overlap between adjacent elongated objects aligned diagonally, confusing non-maximum suppression (NMS).

---

## 2. Mathematical Formulations for OBB
1. **5-Parameter Representation $(x, y, w, h, \theta)$:** Predicts center coordinates $(x, y)$, width $w$, height $h$, and rotation angle $\theta$.
2. **8-Parameter Representation $(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)$:** Predicts the exact 4 corner coordinates of the rotated quadrangle.

---

## 3. Boundary Discontinuity Problems
* **Periodicity of Angle:** Small physical rotations near the angle boundary (e.g., $-90^\circ$ vs $+90^\circ$) can cause abrupt loss spikes in regression.
* **Solutions:**
  * Modulated losses (e.g., Smooth L1 with periodic angle mapping).
  * Probabilistic IoU / Gaussian Bounding Box representations (GWD, KLD loss) that represent rotated boxes as 2D Gaussian distributions.

---

## 4. Benchmark Datasets
* **DOTA (Dataset for Object DeTection in Aerial images):** Contains thousands of high-resolution aerial images annotated with oriented bounding boxes across 18 object categories.
* **FAIR1M:** Fine-grained object recognition dataset for remote sensing images with oriented annotations.
