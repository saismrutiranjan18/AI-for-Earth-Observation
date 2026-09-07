# Lecture 26: Faster R-CNN Architecture & Region Proposal Networks (RPN) in Remote Sensing (Detailed Notes)

This lecture covers the **Faster R-CNN** architecture and the **Region Proposal Network (RPN)**, explaining how object detection evolved from slow CPU-bound heuristic proposals (Selective Search) to an end-to-end trainable deep learning framework suitable for high-resolution satellite imagery.

---

## 1. Limitations of Previous Detection Pipelines (Fast R-CNN)
* **Selective Search Bottleneck:** Fast R-CNN shared convolutional feature maps for classification and bounding box regression, but relied on **Selective Search** (an external CPU-based algorithm) to extract ~2,000 region proposals per image.
* **Inference Speed Barrier:** Selective Search took ~2 seconds per image, preventing real-time or scalable planetary-scale satellite object detection.
* **Goal of Faster R-CNN:** Replace CPU-bound proposal algorithms with a deep neural network that generates region proposals directly on GPU features.

---

## 2. Faster R-CNN Architecture Overview
Faster R-CNN combines two modules into a single unified network:
1. **Region Proposal Network (RPN):** A deep fully convolutional network that proposes candidate regions.
2. **Fast R-CNN Detector:** Uses RoI Pooling / RoI Align to extract features from proposed regions and classify objects while refining bounding boxes.

```
Input Image ──► Backbone (ResNet / VGG) ──► Shared Feature Map ──┬──► RPN ──► Bounding Box Proposals
                                                                └──► RoI Pooling / Align ──► Classification & Regression
```

---

## 3. The Region Proposal Network (RPN)
* **Sliding Window mechanism:** A $3 \times 3$ convolutional kernel slides over the shared feature map.
* **Anchor Boxes:** At each sliding position, $k$ reference anchor boxes are evaluated across multiple scales (e.g., $128^2, 256^2, 512^2$) and aspect ratios (e.g., $1:1, 1:2, 2:1$).
* **Dual Output Heads:**
  * **Classification Head ($2k$ outputs):** Estimates objectness probability (object vs. background).
  * **Regression Head ($4k$ outputs):** Predicts bounding box adjustments $(\Delta x, \Delta y, \Delta w, \Delta h)$ relative to anchor templates.

---

## 4. Relevance to Earth Observation
* **Small Target Detection:** Satellites capture objects like vehicles, solar panels, and buildings that span only a few pixels. Tailoring anchor box scales in RPN is critical for EO datasets.
* **Dense Layouts:** High spatial resolution imagery contains hundreds of objects per tile. RPN handles dense proposal generation efficiently on GPU.
