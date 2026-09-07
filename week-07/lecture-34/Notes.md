# Lecture 34: Geospatial Foundation Models (Prithvi, Scale-MAE, Clay) (Detailed Notes)

This lecture discusses the emerging paradigm of **Geospatial Foundation Models**, large-scale AI models pre-trained on multi-terabyte earth observation archives.

---

## 1. What is a Geospatial Foundation Model?
* **Definition:** A large neural network (typically Vision Transformer architecture) trained on vast uncurated planetary data using self-supervised objectives.
* **Core Capabilities:** Serves as a versatile backbone that can be zero-shot evaluated or efficiently fine-tuned for diverse downstream tasks (land cover classification, crop yield forecasting, flood segmentation, building footprint extraction).

---

## 2. Prominent Model Architectures
1. **Prithvi (IBM / NASA):**
   * Pre-trained on Harmonized Landsat-Sentinel-2 (HLS) multi-spectral data.
   * Utilizes 3D spatial-temporal Masked Autoencoders to model Earth dynamics.
2. **Scale-MAE:**
   * Pre-trained on multi-resolution aerial and satellite imagery.
   * Explicitly incorporates GSD (Ground Sample Distance) scale embeddings to handle resolution shifts between drones ($5\text{cm}$) and satellites ($10\text{m}$).
3. **Clay Foundation Model:**
   * Open-source multi-modal earth observation foundation model incorporating Sentinel-2, Sentinel-1 SAR, and DEM height datasets.

---

## 3. Pre-training Strategies
* **Multi-Modal Pre-training:** Jointly encoding optical multispectral channels, radar backscatter ($\sigma_0$), and elevation data.
* **Spatial-Temporal Embeddings:** Injecting geographic coordinate embeddings (latitude, longitude) and day-of-year sin/cos encodings directly into transformer self-attention layers.
