# Week 4 : Assignment 4

### Question 1
In the classic counterfeit currency analogy used to introduce Generative Adversarial Networks (GANs), what real-world roles do the "generative model" and the "discriminative model" respectively represent?
- [ ] The law enforcement agent detecting fake bills, the central bank printing legal tender.
- [x] **The counterfeiter creating fake currency, the law enforcement agent trying to identify the fake notes.** (Correct)
- [ ] The merchant accepting all payments blindly, the bank auditor balancing accounts.
- [ ] The central bank printing legal tender, the counterfeiter creating fake currency.

---

### Question 2
From a game theory perspective, what optimal condition or stability state does the competitive training framework of a basic GAN seek to reach?
- [ ] Pareto Optimality
- [ ] Stackelberg Leadership Model
- [x] **Nash Equilibrium** (Correct)
- [ ] Prisoner's Dilemma

---

### Question 3
What specific problem occurs during GAN optimization when the generator learns to produce samples from a few repetitive patterns, failing to capture the full variety of the real data distribution?
- [ ] Gradient Explosion
- [x] **Mode Collapse** (Correct)
- [ ] Latent Space Decoupling
- [ ] Mode Doubling

---

### Question 4
What is the primary operational strategy behind the "Progressive Growing of GANs" strategy?
- [ ] Training the model exclusively on low-resolution thumbnails.
- [x] **Starting from a low resolution, model increasingly fine details as training progresses.** (Correct)
- [ ] Alternating the training cycle so the generator runs for some epochs while the discriminator is frozen.
- [ ] Dropping the learning rate by exactly half after every epoch.

---

### Question 5
If an LSGAN is configured with the parameter choices a = 0 (fake data target) and b = 1 (real data target), what value must the parameter c (the value the generator wants the discriminator to believe for fake data) be set to?
- [ ] c = -1
- [ ] c = 0
- [ ] c = 0.5
- [x] **c = 1** (Correct)

---

### Question 6
How does Semantic Segmentation fundamentally differ from traditional Image Classification?
- [ ] Semantic segmentation handles only single-channel grayscale images.
- [ ] Semantic segmentation predicts one dominant object category label for the entire image area.
- [x] **Semantic segmentation assigns a semantic label to every single pixel in an image, producing a dense prediction map.** (Correct)
- [ ] Semantic segmentation completely skips using convolutional features during inference steps.

---

### Question 7
Why are standard classification CNN architectures (which use fully connected layers at their tail end) structurally unsuitable for executing pixel-wise semantic segmentation tasks?
- [ ] They increase the feature map resolution.
- [ ] Convolution operations in standard classification architectures cannot model neighboring pixel relationships.
- [x] **They compress spatial features into low resolutions and lose final spatial layout information through fully connected layers.** (Correct)
- [ ] They require much larger batch sizes than what standard GPUs can allocate.

---

### Question 8
What helps reduce classification confusion and improve segmentation accuracy across complex urban setups (e.g., distinguishing a gray roof from a gray road)?
- [ ] Preprocessing input image to retain one channel while discarding the others.
- [ ] Restricting the network's depth to bare minimum.
- [x] **Multi-scale and global spatial context.** (Correct)
- [ ] Evaluating pixels entirely in isolation without surrounding dependencies.

---

### Question 9
In Earth observation and remote sensing workflows, why is semantic segmentation often chosen over standard image classification?
- [ ] It processes scenes significantly faster by avoiding pooling.
- [x] **Earth observation applications often require pixel-level precision to map exact object shapes, boundaries, and land-cover classes.** (Correct)
- [ ] Classification models are physically incapable of reading imagery coming from Sentinel-2 or Landsat.
- [ ] It limits the output map to containing only one active ground feature type per satellite tile.

---

### Question 10
What operation is commonly utilized within the decoder block of an FCN or U-Net to upscale low-resolution, abstract feature maps back to full spatial dimensions?
- [ ] Max Pooling
- [ ] Principal Component Analysis (PCA)
- [ ] Channel Concatenation
- [x] **Transposed Convolution / Upsampling** (Correct)
