# Lecture 38: Multi-Modal Data Fusion (Optical + SAR + Thermal) (Detailed Notes)

This lecture explores **Multi-Modal Sensor Fusion**, combining complementary signals from Optical, Synthetic Aperture Radar (SAR), Thermal, and Digital Elevation Models (DEM).

---

## 1. Modality Synergies
| Modality | Advantages | Limitations |
| :--- | :--- | :--- |
| **Optical (RGB/NIR/SWIR)** | High semantic detail, intuitive vegetation indices (NDVI) | Blocked by cloud cover, night limitations |
| **SAR (Radar C/L/X band)** | Cloud-penetrating, day/night sensing, structural/moisture sensitivity | Speckle noise, geometric layover/foreshortening |
| **Thermal (TIR)** | Land surface temperature (LST) estimation | Low spatial resolution |
| **DEM (Elevation)** | Topographic height, slope, aspect information | Static, doesn't capture temporal dynamics |

---

## 2. Fusion Architectures
1. **Early Fusion (Pixel-level):** Stacks multi-modal rasters along the channel dimension prior to network input ($C = C_{\text{optical}} + C_{\text{SAR}}$).
2. **Intermediate Fusion (Feature-level):** Independent encoder backbones extract feature maps from each sensor, which are aligned and fused using Cross-Attention modules.
3. **Late Fusion (Decision-level):** Independent streams make standalone predictions, which are ensembled via weighted averaging or gating.

```
Optical Image ──► ResNet Stream ──┐
                                 ├──► Cross-Attention Feature Fusion ──► Unified Task Head
SAR Image     ──► ResNet Stream ──┘
```
