# Week 3 : Assignment 3

### Question 1
In the four essential components of supervised learning, which component corresponds specifically to the model's parameters?
- [ ] The Training Data
- [x] **The Learner** (Correct)
- [ ] The Learning Algorithm
- [ ] The Performance Metric

---

### Question 2
In the LeNet architecture, the C3 convolution layer introduces a specific connectivity design. What type of connectivity pattern is explicitly featured in this layer?
- [ ] Fully Global Connectivity
- [ ] Residual Identity Skipping
- [x] **Partial Connectivity** (Correct)
- [ ] Max Pooling

---

### Question 3
What common pipeline approach was predominantly used by the top performing teams during the ImageNet Large Scale Visual Recognition Challenge in 2010 (ILSVRC2010)?
- [ ] End-to-end deep residual learning networks
- [x] **Hand-crafted feature extraction combined with a Support Vector Machine (SVM)** (Correct)
- [ ] Fully automated Inception modules with parallel convolutions
- [ ] Multi-GPU split vision transformer blocks

---

### Question 4
AlexNet used an exceptionally large filter size in its very first convolutional layer to capture broad structural features from its high-resolution input. What spatial size did these initial kernels have?
- [ ] 3 * 3
- [ ] 5 * 5
- [ ] 7 * 7
- [x] **11 * 11** (Correct)

---

### Question 5
During training, AlexNet implemented a technique called Dropout. What is the fundamental mechanism and purpose of using Dropout?
- [x] **It forces hidden units to create robust features independently without relying on other units to correct mistakes.** (Correct)
- [ ] It mathematically collapses spatial dimensions down to a single scalar value.
- [ ] It dynamically rescales input channel values to maintain zero mean and unit variance.
- [ ] It permanently removes weak parameter connections after an epoch ends.

---

### Question 6
What paradigm shift did VGGNet introduce regarding filter size selection compared to its predecessor AlexNet?
- [ ] It advocated for progressively larger filter grids as the network gets deeper.
- [x] **It promoted a uniform, consistent use of small 3 * 3 filters across all layers while scaling network depth.** (Correct)
- [ ] It entirely replaced spatial convolution filters with purely dense linear projection arrays.
- [ ] It suggested avoiding uniform filter dimensions to keep feature representations asymmetric.

---

### Question 7
In theory, adding extra layers that implement simple identity mappings to a shallower network should guarantee that a deeper model achieves no worse training error. Why was the Residual Block introduced in ResNet?
- [ ] Because in practice, adding extra layers always improves the model performance.
- [ ] Because in practice, we need to account for the limitations related to memory consumption on standard GPUs.
- [x] **Because in practice, standard deeper networks experience performance degradation where training error often worsens.** (Correct)
- [ ] To guarantee that the model uses only hand-crafted features at the end of training pipelines.

---

### Question 8
When using a pre-trained convolutional neural network strictly as a "Feature Extractor" for a new target task, which of the following statements is true regarding the network's weights?
- [ ] Only the early convolutional layers are modified during backpropagation.
- [ ] The entire network is trained from scratch using a low learning rate.
- [x] **The features are extracted from particular layers without any parameter tuning or updates.** (Correct)
- [ ] All layers are frozen except for the input layer, which is dynamically adapted.

---

### Question 9
How does Self-Supervised Learning (SSL) fundamentally differ from traditional Unsupervised Learning?
- [ ] SSL relies strictly on human-annotated regression values instead of discrete classes.
- [x] **SSL derives its labels automatically from a co-occurring modality or from a property of the data sample itself.** (Correct)
- [ ] SSL completely avoids using any form of loss function or optimization step.
- [ ] SSL uses an annotated dataset in addition to an unlabeled dataset.

---

### Question 10
What term is used to describe the self-supervised task (such as predicting the rotation angle of an image) that is solved specifically to help a network learn meaningful visual representations?
- [ ] Downstream Task
- [ ] Principal Component Task
- [x] **Pre-text Task** (Correct)
- [ ] Linear Evaluation Task
