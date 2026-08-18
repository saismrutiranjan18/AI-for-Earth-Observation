# Lecture 7: Traditional Machine Learning Pipelines & Support Vector Machines (Detailed Notes)

This lecture provides a detailed overview of machine learning techniques in Earth Observation and remote sensing, focusing primarily on the era before deep learning (roughly 2000-2010), with a deep dive into **Support Vector Machines (SVMs)**.

---

## 1. Historical Context (0:36 - 4:48)
*   **The Pre-DL Era:** Before deep learning (CNNs and Vision Transformers) became dominant, remote sensing image classification relied on classical statistical methods and machine learning.
*   **Dominant Algorithms:** **Support Vector Machines (SVMs)** and **Random Forests / Decision Trees** were the state-of-the-art tools for mapping land cover, identifying crop types, and analyzing satellite imagery.

---

## 2. The Traditional ML Pipeline (8:04 - 9:41)
Unlike modern deep learning, where feature extraction and classification are optimized end-to-end, traditional workflows are strictly decoupled:

```
[ Raw Satellite Image ] 
        │
        ▼ (Manual / Classical Feature Extraction)
[ Hand-crafted Features ]  <-- (e.g., Haralick Texture, NDVI, Edge Features)
        │
        ▼
[ Classifier / Model ]     <-- (e.g., SVM, Random Forest, Naive Bayes)
        │
        ▼
[ Land-Cover Map ]
```

### Key Properties
*   **Hand-crafted Features:** Human domain experts designed algorithms to extract mathematical descriptors.
    *   *Spectral Features:* Ratios like NDVI.
    *   *Texture Features:* Haralick texture features computed using Gray-Level Co-occurrence Matrices (GLCM) to capture spatial patterns.
*   **Separate Optimization:** The feature extractor was independent of the classifier. If the features missed key details, the classifier could not compensate.

---

## 3. Support Vector Machines (SVM) Mechanics (16:45 - 20:00)

### A. Core Objective (16:45 - 18:00)
*   SVM is a supervised learning model used primarily for binary classification (which can be extended to multi-class using One-vs-One or One-vs-All strategies).
*   **Separating Hyperplane:** The goal is to find a decision boundary (a hyperplane) that separates the data points of two classes.
    *   In 2D, the hyperplane is a line.
    *   In 3D, it is a plane.
    *   In higher dimensions, it is a $(d-1)$-dimensional flat subspace.

### B. Maximum Margin Concept (18:04 - 20:00)
*   There can be many valid separating hyperplanes. SVM specifically searches for the **optimal hyperplane** that maximizes the **margin**—the perpendicular distance between the decision boundary and the closest data points from either class.
*   **Support Vectors:** The data points that lie directly on the margins. These are critical because they define the boundary location; moving any other data points has no effect on the model.

---

## 4. Soft Margin SVM & Regularization (32:08 - 35:33)

### A. Non-Linear Separability & Noise
*   In real-world remote sensing datasets, data points from different classes (e.g., urban asphalt vs. dark soil) are rarely perfectly separable by a straight line due to noise and spectral overlap.

### B. The Parameter $C$
*   To handle non-separable data, the **Soft Margin SVM** formulation introduces slack variables ($\xi_i$) and a regularization parameter $C$:
*   **The Trade-off:** The parameter $C$ acts as a penalty weight for misclassifications:
    *   **Large $C$ (High Penalty):** Forces the model to prioritize classifying all training points correctly, resulting in a **narrower margin**. This can lead to overfitting if the data is noisy.
    *   **Small $C$ (Low Penalty):** Prioritizes finding a **wider margin**, even if it means allowing some data points to be misclassified or violate the margin boundaries. This increases model generalization and robustness to noise.
