# Week 7 : Assignment 7

### Question 1
When dealing with geographic context in Earth observation, why can models that rely purely on visual image appearance often fail to generalize across different parts of the world?
- [ ] Similar land-cover classes always show exactly same visual properties across different regions.
- [x] **Similar land-cover classes often manifest with highly distinct visual properties across different regions.** (Correct)
- [ ] Land-cover classes are guaranteed to have identical spectral signatures regardless of climate or geography, however novel classes may appear in different places.
- [ ] Images from different locations come with different number of bands even if the acquisition sensor is same.

---

### Question 2
In an Early Fusion strategy combining satellite imagery with meteorological data, weather variables are appended directly to pixel-level features. What major data-engineering bottleneck or challenge does this specific approach present?
- [ ] Complete representation collapse inside the image encoder backbone.
- [ ] Weather variables cannot be propagated through convolutional layers.
- [ ] Early Fusion eliminates spatial information from satellite images.
- [x] **Severe spatial and temporal resolution mismatches between broad-scale weather models and localized, high-resolution satellite rasters.** (Correct)

---

### Question 3
What is a major structural advantage of using an Intermediate or Late Fusion strategy over an Early Fusion layer when building deep models to ingest heterogeneous multi-modal inputs (like images and weather data)?
- [ ] It removes the requirement to compute individual loss functions.
- [x] **It allows for modality-specific feature extraction, easier handling of heterogeneous structural data types, and significantly improved interpretability.** (Correct)
- [ ] It guarantees higher accuracy because modalities are fused only after independent optimization.
- [ ] It prevents overfitting by forcing all modalities to share identical network parameters.

---

### Question 4
In transfer learning vocabulary, what core problem is Unsupervised Domain Adaptation (UDA) specifically designed to solve?
- [ ] A severe shortage of images in the source dataset during initial network pre-training.
- [ ] The breakdown of backpropagation gradients caused by an excessively high learning rate.
- [ ] A severe shortage of labelled images in the source dataset during initial network pre-training.
- [x] **A distribution shift between the labeled source domain training data and the unlabeled target domain deployment data.** (Correct)

---

### Question 5
How does Test-Time Domain Adaptation (TTDA) differ fundamentally from traditional Unsupervised Domain Adaptation (UDA) workflows?
- [ ] It completely eliminates the use of convolutional layers during inference.
- [ ] It forces the model to execute a k-means clustering loop on the entire source asset first.
- [x] **It adapts the model directly during inference using only the target test-time data, without requiring access to the original source training dataset.** (Correct)
- [ ] It relies strictly on manual, pixel-level corrections provided in real-time by a human operator or a third model.

---

### Question 6
When performing Test-Time Adaptation using Test-Time Batch Normalization (BN), what specific modification is made to the network's normalization layers when a batch of target data arrives?
- [ ] The source-domain running mean and variance are completely frozen and never altered.
- [x] **The source-domain tracking statistics are replaced or updated using the empirical mean and variance calculated directly from the current target test batch.** (Correct)
- [ ] All batch normalization parameters (gamma and beta) are reset to zero.
- [ ] The layer switches from normalizing channels to randomly masking out some of the neurons.

---

### Question 7
In a Domain Adversarial Neural Network (DANN) framework, what are the three interconnected sub-networks that form the core architecture?
- [x] **A Feature Extractor, a Label Predictor (Classifier), and a Domain Discriminator.** (Correct)
- [ ] A Forward Encoder, a Reverse Diffusion Decoder, and a Softmax Normalizer.
- [ ] A Spatial Transformer, a Channel Squeezer, and a Spatial Inpainter.
- [ ] An Online Momentum Encoder, a Target Predictor, and a k-Means clustering.

---

### Question 8
What unique component is inserted between the Feature Extractor and the Domain Discriminator in a DANN model to enable joint adversarial optimization?
- [ ] A Batch Normalization layer to normalize feature distributions before domain classification.
- [ ] A Fully Connected classification layer that predicts the target class labels.
- [ ] A Global Average Pooling layer that converts feature maps into feature vectors.
- [x] **A Gradient Reversal Layer (GRL)** (Correct)

---

### Question 9
From an optimization standpoint, what is the ultimate structural goal of the Feature Extractor in a fully converged Domain Adversarial Neural Network (DANN)?
- [ ] To compress spatial information.
- [x] **To extract features that are highly discriminative for the main classification task, yet completely invariant to the domain distribution shift.** (Correct)
- [ ] To maximize the domain classification accuracy of the Domain Discriminator.
- [ ] To completely eliminate the need to calculate cross-entropy loss terms.

---

### Question 10
Why is relying purely on the maximum Softmax Probability Score considered an unreliable baseline technique for detecting OOD samples?
- [ ] The Softmax function automatically converts all out-of-distribution feature coordinates to negative infinity.
- [x] **Deep neural networks suffer from overconfidence, meaning they regularly assign exceptionally high Softmax confidence scores to anomalous inputs that lie far away from the true decision boundaries.** (Correct)
- [ ] Softmax probabilities are strictly restricted to processing 3-channel RGB images.
- [ ] Softmax confidence depends only on the number of output classes and not on the input features.
