# Week 2 : Assignment 2

### Question 1
What is the primary geometric objective of a Linear Support Vector Machine (SVM) when separating a two-class, linearly separable dataset?
- [ ] To find a curved boundary that wraps tightly around the majority class.
- [ ] To calculate the global average coordinate of all data points combined.
- [x] **To find the optimal hyper-plane that maximizes the margin (the distance between the boundary and the closest data points of any class).** (Correct)
- [ ] To find the optimal hyper-plane that minimizes the margin.

---

### Question 2
In a linear SVM formulation, how does the regularization parameter C control the trade-off in a soft-margin optimization?
- [ ] A very large value of C prioritizes a wide margin while ignoring all misclassifications.
- [x] **A very large value of C heavily penalizes misclassifications, forcing the model to choose a narrower margin to keep the training data as clean as possible.** (Correct)
- [ ] A small value of C heavily penalizes misclassifications.
- [ ] C has as such no effect on soft-margin optimization.

---

### Question 3
k-Means is categorized under which learning paradigm, and what is its primary objective?
- [ ] Supervised Learning ; it maps input vectors to categorical class labels using cross-entropy.
- [x] **Unsupervised Learning ; it groups unlabeled data points into k distinct clusters based on feature similarity.** (Correct)
- [ ] Reinforcement Learning ; it optimizes an agent's policy using a sparse reward function.
- [ ] Self-Supervised Learning ; it shuffles and predicts the original sequence order of channels.

---

### Question 4
What mathematical metric does the k-Means objective function seek to minimize?
- [x] **The Within-Cluster Sum of Squares (WCSS), which measures the sum of squared Euclidean distances between each data point and its assigned cluster centroid.** (Correct)
- [ ] The maximum margin distance between support vector groups.
- [ ] The negative log-likelihood of a multinomial softmax output distribution.
- [ ] The structural reconstruction error of a convolutional autoencoder mask.

---

### Question 5
How does the initial placement of centroids affect the final output of a standard k-Means algorithm?
- [ ] Centroid initialization has no impact because the optimization space is perfectly convex.
- [x] **Poor initial centroid placement can cause the algorithm to get stuck in a poor local minimum, resulting in sub-optimal clustering layouts.** (Correct)
- [ ] Centroid initialization has no impact because the algorithm will get stuck in a poor local minimum, no matter what.
- [ ] Centroid initialization may or may not have impact, depending on some other parameters.

---

### Question 6
What are the three structural layer classifications that define the standard feedforward architecture of a Multi-Layer Perceptron (MLP)?
- [ ] A Convolutional Layer, a Squeeze Layer, and an Excitation Layer.
- [ ] An Input Layer, exactly one Hidden Layer, and an Output Layer. *(Incorrect choice made during attempt)*
- [ ] A Source Layer, a Domain Discriminator Layer, and a Gradient Reversal Layer.
- [x] **An Input Layer, one or more Hidden Layers, and an Output Layer.** (Correct)

---

### Question 7
How does Hyperspectral Anomaly Detection (HAD) differ fundamentally from traditional Target Detection?
- [ ] HAD requires prior knowledge of target spectral signatures, whereas target detection assumes completely unknown threats.
- [x] **HAD assumes unknown targets and focuses entirely on identifying spectrally rare objects that differ from the surrounding background, requiring no prior signatures.** (Correct)
