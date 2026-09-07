# Lecture 35: Transfer Learning, Fine-Tuning & Downstream Task Adaptation (Detailed Notes)

This lecture addresses **Transfer Learning** and **Fine-Tuning strategies** for adapting foundation models and SSL backbones to data-scarce Earth Observation tasks.

---

## 1. Fine-Tuning Protocols
* **Linear Probing:** Freeze the pre-trained encoder weights completely and train only a linear classification layer on top. Used to benchmark SSL representation quality.
* **Full Fine-Tuning:** Unfreeze all encoder layers and update weights end-to-end with a smaller learning rate (e.g., $10^{-4} - 10^{-5}$).
* **Parameter-Efficient Fine-Tuning (PEFT / LoRA):** Inject low-rank trainable matrices into Transformer attention projection weights ($W_q, W_v$), updating $<1\%$ of total parameters.

---

## 2. Adapting Pre-trained Backbones to EO Tasks
```
Pre-trained Foundation Backbone (Frozen / LoRA) ──┬──► Task Head: Segmentation (UperNet / Segmenter)
                                                 ├──► Task Head: Bounding Box (RoI Head)
                                                 └──► Task Head: Time Series Regression
```

---

## 3. Evaluation and Benchmark Suites
* **GEO-BENCH:** Standardized evaluation suite for geospatial foundation models across diverse tasks (change detection, segmentation, classification).
* **Domain Shift Challenges:** Fine-tuning must mitigate sensor domain shifts (e.g., models pre-trained on Sentinel-2 $10\text{m}$ imagery applied to WorldView $0.3\text{m}$ imagery).
