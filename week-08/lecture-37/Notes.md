# Lecture 37: Satellite Time-Series Analysis (LSTMs & Spatial-Temporal Transformers) (Detailed Notes)

This lecture covers **Satellite Time-Series (STS)** processing for crop phenology mapping, vegetation health monitoring, and land-use trajectory modeling.

---

## 1. Nature of Satellite Time Series Data
* **Dense Revisit Stacks:** Satellites like Sentinel-2 acquire images every 5 days over the same location, producing a temporal sequence $\{X_{t_1}, X_{t_2}, \dots, X_{t_T}\}$.
* **Irregular Sampling & Cloud Gaps:** Cloud cover and orbital overlaps lead to missing observations and non-uniform time gaps $\Delta t_i = t_{i+1} - t_i$.

---

## 2. Recurrent vs. Transformer Models
* **Recurrent Neural Networks (ConvLSTM / Bi-GRU):**
  * Maintains hidden states updated sequentially over time.
  * Suffers from vanishing gradients over long temporal stacks ($>30$ dates) and struggles with irregular sampling.
* **Spatial-Temporal Transformers (ST-Former):**
  * Applies **Temporal Self-Attention** across date tokens and **Spatial Self-Attention** across image patches.
  * Incorporates **Continuous Fourier Positional Encodings** based on real acquisition timestamps (Day of Year).

---

## 3. Key Applications
* **Crop Type Mapping:** Distinguishing crops with similar single-date spectral signatures (e.g., wheat vs. barley) by tracking their unique phenological growth curves across months.
