# Lecture 4: Multispectral Imaging & Satellite Platforms (Detailed Notes)

This lecture introduces **Multispectral Imaging** in remote sensing, detailing how capturing electromagnetic wavelengths beyond standard red, green, and blue (RGB) bands allows for deeper Earth observation. Key topics cover spectral bands, spectral indices, the Sentinel-2 mission, and comparisons with the Landsat series.

---

## 1. Core Concepts: Spectral Bands Beyond RGB (4:09 - 5:08)
Standard human vision (and conventional digital cameras) captures only the visible spectrum (RGB: Red, Green, Blue). Remote sensing sensors detect wavelengths beyond this range to identify specific material properties:

*   **Near-Infrared (NIR) (4:09 - 4:45):**
    *   **Application:** Crucial for vegetation analysis.
    *   **Mechanism:** Healthy green leaves have a high reflectance in the NIR spectrum due to their internal cellular structure (mesophyll cells). By contrast, they absorb visible light (especially Red) for photosynthesis. This sharp difference is known as the **"Red Edge"**.
*   **Shortwave Infrared (SWIR) (4:45 - 5:08):**
    *   **Application:** Soil moisture estimation, crop drought studies, and mapping burnt areas.
    *   **Mechanism:** Water molecules absorb SWIR radiation. Dry soil or moisture-stressed vegetation reflects more SWIR light, whereas wet soil and healthy, hydrated plants absorb it, showing up darker.

---

## 2. Spectral Indices (9:18 - 12:08)
Spectral indices simplify high-dimensional multi-band imagery by applying mathematical ratios to highlight specific land-cover classes:

*   **Normalized Difference Vegetation Index (NDVI):**
    *   **Formula:** $$\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$$
    *   **Range:** -1.0 to 1.0 (Dense vegetation is close to 1.0, water/clouds/barren land are near or below 0).
*   **Normalized Difference Water Index (NDWI):**
    *   **Formula:** $$\text{NDWI} = \frac{\text{Green} - \text{NIR}}{\text{Green} + \text{NIR}}$$ (or using SWIR to emphasize leaf water content).
    *   **Application:** Emphasizes open water bodies and maps surface water extent.
*   **Normalized Difference Built-up Index (NDBI):**
    *   **Formula:** $$\text{NDBI} = \frac{\text{SWIR} - \text{NIR}}{\text{SWIR} + \text{NIR}}$$
    *   **Application:** Pinpoints urban developments, concrete, and built-up areas.

---

## 3. The Sentinel-2 Satellite Mission (17:42 - 20:33)
Managed by the European Space Agency (ESA) under the Copernicus program, Sentinel-2 is a cornerstone of modern Earth Observation.

### Key Specifications
*   **Spectral Bands:** Captures **13 spectral bands** spanning the visible, NIR, Red Edge, and SWIR wavelengths.
*   **Spatial Resolutions:** The bands are captured at three different spatial scales depending on application needs:
    *   **10 meters:** Visible (B2, B3, B4) and one NIR band (B8). Good for mapping infrastructure and basic vegetation.
    *   **20 meters:** Red Edge bands (B5, B6, B7), narrow NIR (B8a), and SWIR bands (B11, B12). Ideal for agricultural crop classification.
    *   **60 meters:** Atmospheric correction bands (B1, B9, B10). Used to estimate water vapor, aerosols, and cirrus clouds.
*   **Orbit Design:** Uses a **sun-synchronous polar orbit**. This ensures that the satellite passes over any given point on Earth at roughly the same local solar time, maintaining consistent solar illumination and shadow angles across temporal revisits.

---

## 4. Comparison: Sentinel-2 vs. Landsat Series (26:27 - 28:42)
The lecture compares Sentinel-2 with USGS/NASA's Landsat 7 and Landsat 8 missions:

| Feature / Metric | Sentinel-2 (A & B constellation) | Landsat 8 (OLI & TIRS) |
| :--- | :--- | :--- |
| **Launch Timeline** | Launched starting 2015 (Sentinel-2A) | Launched in 2013 |
| **Spatial Resolution** | Up to **10m** (Visible/NIR) | Up to **30m** (Visible/NIR/SWIR) |
| **Temporal Resolution** | **5 days** (at the equator) | **16 days** (single satellite) |
| **Thermal Sensing** | No thermal bands | **Yes**, TIRS sensor provides thermal infrared bands at 100m (resampled to 30m) |

---

## 5. Practical Implementation (15:04 - 16:00)
*   The instructor prompts students to practice these multi-band and ratio concepts using **Google Earth Engine (GEE)**.
*   By writing JavaScript in the GEE Code Editor, students can access the public Sentinel-2 archive, compute NDVI/NDWI on-the-fly, and visualize changes over large regional areas without downloading massive raw datasets.
