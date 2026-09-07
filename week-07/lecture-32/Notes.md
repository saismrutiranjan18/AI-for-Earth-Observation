# Lecture 32: Contrastive Learning (SimCLR, MoCo) for Satellite Imagery (Detailed Notes)

This lecture covers **Contrastive Self-Supervised Learning** algorithms (SimCLR, MoCo, BYOL) adapted for multi-spectral and multi-temporal satellite imagery.

---

## 1. Principles of Contrastive Learning
Contrastive learning maps augmented views of the same image patch to nearby points in a feature embedding space, while pushing embeddings of different patches far apart.

* **Augmentation Strategy for EO:**
  * Spatial transforms: Random cropping, rotation ($90^\circ, 180^\circ, 270^\circ$), horizontal/vertical flips.
  * Spectral transforms: Channel dropping, band noise addition, solar angle adjustment.
  * Temporal augmentations: Pairing patches from the same location taken on different dates.

---

## 2. Key Frameworks
### A. SimCLR (Simple Framework for Contrastive Learning)
* Uses **InfoNCE Loss**:
  $$\mathcal{L}_{i,j} = -\log \frac{\exp(\text{sim}(z_i, z_j)/\tau)}{\sum_{k=1}^{2N} \mathbb{I}_{[k \neq i]} \exp(\text{sim}(z_i, z_k)/\tau)}$$
* Requires large batch sizes (e.g., $4096$) to provide sufficient negative samples.

### B. MoCo (Momentum Contrast)
* Maintains a dynamic **dictionary queue** of negative samples and updates a key encoder using momentum:
  $$\theta_k \leftarrow m \theta_k + (1-m) \theta_q$$
* Eliminates the need for massive GPU batch sizes, making it popular for remote sensing labs.

---

## 3. Remote Sensing Considerations
* **False Negatives in Earth Observation:** Two satellite patches from different coordinates might contain identical land cover (e.g., two pine forests). Naive negative sampling penalizes them, motivating specialized geographic contrastive losses (e.g., GeoCLR, SeCo).
