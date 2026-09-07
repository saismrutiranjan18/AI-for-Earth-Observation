# Week 6 : Assignment 6

### Question 1
In the Masked Spectral Modeling pretext task, how is the network trained to understand complex spectral dependencies?
- [ ] The network is forced to guess the geographic location of the patch.
- [x] **Random spectral bands are masked out during training, and the network is tasked to predict the missing spectral values.** (Correct)
- [ ] Some bands are randomly selected and appended to the end of the original bands.
- [ ] It applies a hard threshold to convert all multi-channel vectors into binary masks.

---

### Question 2
Why are Graph Neural Networks (GNNs) often used for hyperspectral image classification over standard pixel-wise classifiers?
- [ ] GNNs treat every pixel as an isolated 1D array, ignoring the spatial arrangement entirely.
- [ ] GNNs scale down the dimensionality of hyperspectral cubes.
- [ ] They remove the necessity of utilizing multi-head self-attention projection layers.
- [x] **Hyperspectral pixels exhibit strong spatial relationships where nearby pixels share similar properties, which GNNs naturally model as connected nodes.** (Correct)

---

### Question 3
What specific domain challenge arises when a hyperspectral classification model trained on a specific sensor dataset (like Indian Pines) is deployed to a different sensor dataset (like Pavia University)?
- [x] **Sensor Shift, which prevents models from being easily portable across different hyperspectral sensors** (Correct)
- [ ] Increased spatial resolution always guarantees better classification performance across datasets.
- [ ] Models trained on one hyperspectral dataset can only process images with exactly the same spatial dimensions.
- [ ] Models trained on one sensor can ingest another sensor, however only if the images belong to the same geographic location.

---

### Question 4
What is the primary operational objective of Hyperspectral Anomaly Detection (HAD)?
- [ ] To classify every single pixel in a scene into a pre-defined set of land-cover categories.
- [x] **To identify spectrally rare targets that differ significantly from the surrounding background without prior knowledge of their signatures.** (Correct)
- [ ] To identify targets similar to a few pre-defined spectral signatures.
- [ ] To identify spectrally common targets.

---

### Question 5
What is the primary distinction between Feature Selection and Feature Extraction in dimensionality reduction workflows?
- [ ] Feature selection modifies neural network weights via backpropagation, while feature extraction operates strictly without any model training.
- [x] **Feature selection preserves the original physical meaning of bands by choosing a subset of them, whereas feature extraction transforms bands into a new, usually compact feature space.** (Correct)
- [ ] Feature extraction is restricted to 3-channel RGB data, whereas feature selection handles hyperspectral pipelines.
- [ ] Feature selection completely deletes raw metadata, whereas feature extraction preserves them.

---

### Question 6
What fundamental physical constraint necessitates the use of Hyperspectral Unmixing algorithms?
- [ ] The sensor measures only one material at a time, but the output is stored as overlapping bands.
- [ ] Every pixel contains completely random, synthetic noise.
- [ ] The sensor is restricted to mapping terrains that lie exactly at sea level.
- [x] **The ground spatial resolution is often coarse enough that a single pixel covers a mixture of multiple distinct materials.** (Correct)

---

### Question 7
In the training strategy of the 1D convolutional hyperspectral unmixing model, why are pure endmember spectra used as training samples?
- [ ] To provide continuous abundance fractions for every material in each training sample.
- [x] **Because abundance fractions are difficult to obtain for training; instead, pure spectra are labeled using one-hot vectors, allowing the network outputs (appropriately processed) to approximate abundance fractions during inference.** (Correct)
- [ ] Because abundance fractions are easy to obtain for training.
- [ ] To force every training sample to contain an equal mixture of all endmembers.

---

### Question 8
Under the Linear Mixing Model paradigm, how is the total measured spectrum of a mixed pixel mathematically approximated?
- [ ] As a linear mixture of pure endmember spectra, weighted by the inverse of their fractional abundances.
- [ ] As the most dominant endmember spectrum.
- [ ] As a nonlinear interaction among neighboring pixels through spatial convolution.
- [x] **As a linear mixture of pure endmember spectra, weighted by their corresponding fractional abundances.** (Correct)

---

### Question 9
When framing hyperspectral image inpainting as a Self-Supervised Learning (SSL) task, how is the loss function typically formulated to optimize the network weights?
- [ ] By evaluating a contrastive language loss against scraped web sentences.
- [x] **By computing a reconstruction error (such as Mean Squared Error) exclusively over the pixels that were intentionally masked out during training.** (Correct)
- [ ] By running a simple clustering.
- [ ] By using a supervised loss in addition to a reconstruction error.

---

### Question 10
Which statement is incorrect?
- [x] **Airport-Beach-Urban (ABU) anomaly dataset mainly consists of scenes captured using Hydice sensor.** (Correct)
- [ ] GANs (with appropriate architecture design) can be possibly used for hyperspectral anomaly detection.
- [ ] 3D CNN (with appropriate architecture design) can be possibly used for hyperspectral anomaly detection.
- [ ] Indian Pines dataset was captured using AVIRIS sensor.
