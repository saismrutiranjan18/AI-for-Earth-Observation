# Lecture 28: One-Stage Object Detectors (YOLO & SSD) for Real-Time Earth Observation (Detailed Notes)

This lecture covers **One-Stage Object Detection** architectures, focusing on **YOLO (You Only Look Once)** and **SSD (Single Shot MultiBox Detector)** for high-speed, real-time satellite and drone video streams.

---

## 1. Two-Stage vs. One-Stage Detectors
* **Two-Stage (Faster R-CNN):** Proposal generation (RPN) followed by region classification. High precision, lower speed (~10-20 FPS).
* **One-Stage (YOLO/SSD):** Directly predicts class probabilities and bounding box coordinates in a single pass. High speed (~60-150 FPS), ideal for onboard UAV/drone processing.

---

## 2. YOLO Architecture Principles
* **Grid Cell Assignment:** Divides the input image into an $S \times S$ grid. If an object's center falls inside a grid cell, that cell is responsible for detecting that object.
* **Direct Prediction:** Each grid cell predicts $B$ bounding boxes, confidence scores, and $C$ class probabilities simultaneously.
* **Unified Loss Function:** Combines localization loss (coordinate offsets), confidence loss (objectness), and classification loss (cross-entropy).

---

## 3. SSD (Single Shot MultiBox Detector)
* **Multi-Scale Feature Maps:** Uses feature maps from multiple convolutional layers (at different depths) to detect objects of varying sizes without a separate feature pyramid.
* **Default Boxes:** Similar to anchor boxes, predefined default boxes with varied aspect ratios are evaluated across different layer outputs.

---

## 4. Earth Observation Trade-offs
* **Onboard Edge Inference:** Drones and microsatellites with limited power budgets benefit from lightweight YOLO models (YOLOv8-nano/small) for real-time monitoring of wildfires or oil spills.
* **Small Object Challenge:** Standard YOLO models historically struggled with tiny satellite targets due to aggressive downsampling. Modern variants incorporate FPN and high-resolution detection heads to mitigate this issue.
