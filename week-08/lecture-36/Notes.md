# Lecture 36: Bi-Temporal Change Detection & Siamese Architectures (Siam-UNet) (Detailed Notes)

This lecture presents **Bi-Temporal Change Detection (CD)** in satellite remote sensing, focusing on **Siamese Network architectures** (Siam-UNet).

---

## 1. What is Change Detection?
Change Detection is the process of identifying differences in the state of an object or geographic phenomenon by observing co-registered satellite images acquired at different times ($T_1$ and $T_2$).

* **Applications:** Urban expansion monitoring, deforestation tracking, post-disaster damage assessment, glacier retreat analysis.

---

## 2. Siamese Network Architectures
A Siamese Network processes dual inputs ($T_1$ image patch and $T_2$ image patch) through two identical encoder branches with shared weights.

```
Image T1 ──► Encoder Branch (Shared Weights) ──┐
                                               ├──► Feature Difference / Concatenation ──► Decoder ──► Change Mask
Image T2 ──► Encoder Branch (Shared Weights) ──┘
```

---

## 3. Siam-UNet Variants
1. **Siam-UNet Concatenation (Siam-UNet-Conc):** Concatenates features from both encoder branches at each skip connection level before passing to the decoder.
2. **Siam-UNet Difference (Siam-UNet-Diff):** Computes the absolute feature difference $|F(T_1) - F(T_2)|$ at each skip connection level, focusing explicit attention on changed areas.

---

## 4. Key Challenges
* **Co-Registration Errors:** Misalignment of even a few pixels between $T_1$ and $T_2$ creates false change artifacts along object edges.
* **Phenological and Illumination Variations:** Seasonal vegetation shifts and solar angle differences cause spectral discrepancies without real land-use change.
