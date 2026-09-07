# Week 8 : Assignment 8

### Question 1
Why do traditional post-classification change detection approaches—where a pre-trained semantic segmentation model is run independently on pre-change and post-change images and the outputs are compared—usually fail to provide satisfactory results?
- [ ] They are completely restricted to processing single-channel grayscale arrays.
- [x] **They amplify individual classification errors and fail to perform direct temporal reasoning to distinguish true changes from environmental noise.** (Correct)
- [ ] They force the output maps to completely delete spatial resolution parameters.
- [ ] They require both input satellite images to be captured at the exact same minute of the day.

---

### Question 2
When applying a supervised change detection model trained on a specific geographic region (e.g., European cities) to a completely different geographic region (e.g., Asian cities), what major challenge typically causes a drop in model performance?
- [ ] There is generally no such drop in model performance.
- [x] **Geographic variation and domain shifts in urban architecture and land cover characteristics.** (Correct)
- [ ] A strict requirement that forces Asian satellite tiles to use fewer spectral bands.
- [ ] Change detection models can only be applied to regions containing the same land-cover classes as the training data.

---

### Question 3
What core structural motivation justifies using a Siamese Network architecture instead of a single-stream fully convolutional network for change detection tasks?
- [ ] It eliminates the need for computing backpropagation gradients during training.
- [ ] It forces the model to use hand-crafted SVM classifiers at the end of every block.
- [ ] It automatically restricts the network depth to a maximum of two layers.
- [x] **It allows the network to process two temporal images using weight-sharing twin branches to extract highly consistent, shared feature representations.** (Correct)

---

### Question 4
What are the two primary objectives of the Unsupervised Deep Change Vector Analysis (DCVA) framework when processing bi-temporal Very High Resolution (VHR) images?
- [x] **To distinguish changed pixels from unchanged ones (binary CD) and further segregate those changed pixels into different types of changes (multiple CD).** (Correct)
- [ ] To distinguish changed pixels from unchanged ones (binary CD) and further segregate those changed pixels into permanent and temporary change (multiple CD).
- [ ] To distinguish changed pixels from unchanged ones (binary CD) and further compress the changed pixels by using a binary encoding.
- [ ] To completely eliminate the need for convolutional layers by using linear regression.

---

### Question 5
To preserve high-resolution spatial boundaries and object details in a Siamese change detection network, from which path do the decoder blocks pull "Skip Connections" (resembling a U-Net style layout)?
- [ ] Directly from input images.
- [x] **From the intermediate layers of the Siamese encoder branches.** (Correct)
- [ ] From an external, pre-calculated texture feature matrix.
- [ ] From a single fixed-size fully connected linear layer.

---

### Question 6
Consider an advanced remote sensing scenario where you must detect structural changes using three input layers: a Pre-change Optical image, a Pre-change SAR image, and a Post-change SAR image. How many encoder branches should your Siamese network design ideally feature?
- [ ] One branch total, processing all data sequentially.
- [x] **Three encoder branches.** (Correct)
- [ ] Exactly five parallel streams.
- [ ] Two branches, completely removing the optical stream.

---

### Question 7
In the asymmetrical multi-modal setup described (Pre-change Optical + SAR and Post-change SAR), should all active encoder branches share the exact same weights?
- [ ] Yes, all three branches must share weights to compress disk space.
- [ ] Yes, weight sharing is mandatory across different modalities to prevent gradients from exploding.
- [ ] No, weight sharing must be avoided because the images were taken on different days of the week.
- [x] **No, because optical and SAR images capture completely different physical properties, meaning their corresponding encoder branches preferably should not share weights.** (Correct)

---

### Question 8
What fundamental assumption does the Unsupervised Deep Change Vector Analysis (DCVA) technique make regarding the availability of a neural network (considering change detection of VHR optical images)?
- [x] **It assumes a network has already been trained on VHR optical images for a proxy task like classification or segmentation, providing a strong feature extractor.** (Correct)
- [ ] It assumes the network has completely frozen all layers except for the final linear layer.
- [ ] It requires a network that has never processed an optical or multi-spectral image tile.
- [ ] It relies on a network that computes operations entirely without utilizing matrix multiplications.

---

### Question 9
In dual-task constrained Siamese frameworks, what is the primary benefit of co-training the model on both change detection and semantic segmentation tasks simultaneously?
- [ ] It allows the model to completely ignore the post-change image stream during backpropagation.
- [ ] It guarantees that the training process completely bypasses the need for validation loops.
- [ ] It cuts the training data footprint in half.
- [x] **The joint task constraints act as regularizers, forcing the network to learn richer, more semantically meaningful features that improve overall change detection.** (Correct)

---

### Question 10
In the Deep Change Vector Analysis (DCVA) pipeline, from which layers of a pre-trained CNN are the deep feature vectors typically extracted for temporal comparison?
- [ ] Exclusively from the final fully connected classification layer.
- [x] **From selected intermediate convolutional layers that capture both fine structural and abstract semantic details.** (Correct)
- [ ] Only from the raw input pixel matrix before any convolution occurs.
- [ ] From the first layer and the final layer.
