# Week 5 : Assignment 5

### Question 1
Why does the direct transfer of deep convolutional networks pre-trained on optical datasets (such as ImageNet) often fall short or underperform when applied directly to SAR images?
- [ ] Optical networks only focus on textual features, which is not sufficient for SAR images.
- [ ] Optical images are dominated by high-frequency features, whereas SAR images contain low-frequency features.
- [x] **SAR images lack intuitive visual semantic information, exhibit entirely different scattering mechanisms, and are inherently degraded by multiplicative speckle noise.** (Correct)
- [ ] Optical networks automatically restrict the input tensor size to single-channel panchromatic strips.

---

### Question 2
In a Supervised Despeckling training framework using deep learning, what major data-engineering bottleneck presents the greatest challenge for optimizing the network?
- [ ] The inability of standard GPUs to process multi-channel complex inputs.
- [x] **The severe real-world lack of true clean, noiseless "ground-truth" SAR images for supervised training.** (Correct)
- [ ] The absolute requirement to modify all input images to 3-channel format.
- [ ] Variability in speckle characteristics across images.

---

### Question 3
Why are standard pixel-wise regression losses like Mean Squared Error often considered insufficient or flawed when used alone for training deep SAR despeckling networks?
- [ ] They completely ignore the phase angle vectors of the complex input.
- [x] **They encourage the network to produce over-smoothed, blurry outputs that erase critical structural components like edges and high-frequency textures.** (Correct)
- [ ] Such losses can be applied to grayscale SAR images only, i.e., cannot process more than one channel, e.g., two polarizations.
- [ ] They prevent convolutional layers from learning spatial context.

---

### Question 4
When building neural networks that explicitly process Single Look Complex (SLC) SAR data, why are standard real-valued architectures structurally limited?
- [ ] Real-valued networks completely ignore the amplitude maps of the SAR backscatter.
- [ ] They require converting the entire dataset into binary data.
- [ ] They force the model to drop their convolutional filters.
- [x] **They discard or decouple the critical phase information, which is essential for mapping phase-sensitive scattering mechanisms.** (Correct)

---

### Question 5
What severe operational limitation occurs when attempting to solve a SAR segmentation or classification task using standard Supervised Learning models in data-scarce remote sensing domains?
- [ ] The performance is primarily limited because SAR images always have lower spatial resolution than optical images.
- [x] **High annotation costs, limited human expertise in interpreting radar signatures, and a scarcity of labeled training data cause deep networks to overfit or fail to generalize to new regions.** (Correct)
- [ ] Supervised models require SAR images from exactly the same acquisition geometry and season as the training data.
- [ ] Increasing the depth of the network alone is generally sufficient to overcome the lack of labeled SAR data.

---

### Question 6
Why is a U-Net architecture with skip-connections often favored when designing deep networks for pixel-wise SAR image analysis tasks such as despeckling or semantic segmentation?
- [ ] It reduces the number of trainable parameters by eliminating redundant convolutional layers.
- [ ] It completely removes the need to calculate backpropagation loss gradients.
- [ ] It ensures that the receptive field remains constant throughout the network.
- [x] **The skip-connections pass low-level high-resolution spatial features directly from the encoder to the decoder, preserving fine structural boundaries and details that are otherwise lost during downsampling.** (Correct)

---

### Question 7
What is the primary operational bottleneck that makes the original R-CNN pipeline exceptionally slow during both training and inference?
- [x] **It extracts approximately 2,000 region proposals per image and forces each proposal through a deep Convolutional Neural Network independently, leading to massive redundant feature computations.** (Correct)
- [ ] It uses a single recurrent layer to process all pixels simultaneously.
- [ ] It uses an ensemble of 10 methods to detect the region proposals.
- [ ] It relies entirely on unsupervised clustering to update the network's convolutional weights.

---

### Question 8
How does the original R-CNN framework bridge the geometric gap between arbitrarily shaped region proposals and the rigid square input size required by standard fully-connected classification layers?
- [ ] It dynamically expands the convolutional kernel dimensions at runtime.
- [x] **It applies a warping operation to hard-resize every extracted image patch into a fixed target resolution.** (Correct)
- [ ] It crops each region proposal to a fixed size without any geometric transformation.
- [ ] It skips the classification step entirely and outputs raw feature map indices.

---

### Question 9
How does Fast R-CNN fundamentally solve the massive feature computation redundancy found in the original R-CNN framework?
- [ ] It completely eliminates the need to look at region proposals or bounding boxes altogether.
- [ ] It forces the model to only use single-channel panchromatic images to speed up convolutions.
- [x] **It processes the entire single image through the deep CNN backbone exactly once to generate a global feature map, and then projects the region proposals directly onto this shared feature map.** (Correct)
- [ ] It completely replaces the convolutional backbone with an array of independent multi-layer perceptrons.

---

### Question 10
Fast R-CNN optimizes its classification and bounding box regression branches jointly. What type of loss function enables this end-to-end training?
- [x] **A Multi-Task Loss function combining classification loss (cross-entropy) and a variant of L1 loss for bounding box regression.** (Correct)
- [ ] Within-Cluster Sum of Squares (WCSS)
- [ ] Unsupervised Contrastive Loss
- [ ] Unsupervised Contrastive Loss using adversarial domain discrimination.
