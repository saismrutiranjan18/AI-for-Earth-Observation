# Lecture 33: Masked Autoencoders (MAE) & Vision Transformers (ViT) (SatMAE) (Detailed Notes)

This lecture explores **Vision Transformers (ViT)** and **Masked Autoencoders (MAE)** adapted for satellite image analysis (e.g., SatMAE).

---

## 1. Vision Transformers (ViT) in Remote Sensing
Unlike CNNs which rely on inductive spatial biases (local convolutions), Vision Transformers process global relationships using self-attention:
1. An input patch $X \in \mathbb{R}^{H \times W \times C}$ is split into $N = (H \cdot W)/P^2$ non-overlapping patches of size $P \times P$.
2. Patches are projected into linear embeddings, combined with positional encodings, and fed into Transformer encoder blocks.

---

## 2. Masked Autoencoder (MAE) Architecture
MAE is an asymmetric encoder-decoder self-supervised model:
* **High Masking Ratio:** Randomly masks a large percentage (e.g., $75\% - 85\%$) of spatial patches.
* **Encoder:** Processes **only the visible (unmasked) patches**, drastically lowering compute and memory costs.
* **Decoder:** Lightweight network that receives encoded visible patches plus learnable `[mask]` tokens at missing positions, reconstructing target pixel values.

```
Satellite Tile ──► Patchify & Mask 75% ──► Visible Patches ──► Encoder ──► Latent Code ──► Add Mask Tokens ──► Decoder ──► Reconstructed Pixels
```

---

## 3. SatMAE (MAE for Satellite Imagery)
* **Temporal Masking:** Masks patches across multi-temporal acquisition dates, teaching the model to predict seasonal changes.
* **Spectral Masking:** Masks individual spectral channels (e.g., masking RedEdge or SWIR while keeping RGB), enabling cross-spectral reconstruction.
