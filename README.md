# 🎯 Automatic Optical Beam Alignment System

This project focuses on the numerical simulation and automation of a laser beam alignment system. It demonstrates the implementation of a feedback control loop to maintain precise optical alignment, simulating real-world conditions found in high-energy laser facilities (e.g., CEA Laser Mégajoule).

## 🔬 Project Overview
In precision optics, misalignment leads to signal degradation and measurement errors. This system automates the alignment process by:
1. **Detecting** the beam position (Centroid).
2. **Calculating** the error relative to the target center.
3. **Correcting** the alignment through a simulated feedback loop.

This project covers the full engineering cycle:  
**Physical Modeling → Image Processing → Noise Analysis → Automated Correction**

---

## 🛠️ Key Technical Features

### 1. Beam Modeling & Simulation
* **Gaussian Profile:** Generation of 2D intensity profiles $I(x,y)$ with adjustable width and position.
* **Realistic Noise:** Integration of Gaussian noise to test the robustness of the detection algorithm under experimental conditions.

### 2. Intelligent Detection (Centroide Analysis)
* **Barycenter Calculation:** Implementation of a centroid algorithm to locate the beam center with sub-pixel precision:
    $$C_x = \frac{\sum x \cdot I(x,y)}{\sum I(x,y)} , \quad C_y = \frac{\sum y \cdot I(x,y)}{\sum I(x,y)}$$
* **Image Processing:** Matrix manipulation using NumPy to handle 2D intensity maps.

### 3. Automated Alignment Loop
* **Error Evaluation:** Real-time calculation of the displacement vector.
* **Feedback Control:** Simulated correction to bring the beam back to the optical axis $(0,0)$.

---

## 📊 Visualized Results
The simulation provides several analytical views:
1. **Reference Beam:** The ideal aligned state.
2. **Misaligned & Noisy Input:** Simulation of raw data from a CMOS/CCD sensor.
3. **Centroid Mapping:** Visual confirmation of the detected center (Red Cross).
4. **Correction Path:** Visualization of the beam returning to its target position.

---

## 🚀 Professional & Industrial Relevance
This project demonstrates skills essential for:
* **Laser Instrumentation (CEA/Safran):** Automated alignment of high-power laser chains.
* **Adaptive Optics:** Real-time correction of wavefront or beam pointing.
* **Vision Systems:** Use of CMOS sensors for metrology and industrial inspection.

---

## 💻 Skills Demonstrated
* **Computation:** Python (NumPy, Matplotlib, SciPy).
* **Control Theory:** Feedback loops and error correction.
* **Image Processing:** Spatial filtering and centroid detection.
* **Optics:** Beam propagation and Gaussian optics.

---

## 📄 Project Resources
* 📄 **Scientific Report:** [Download PDF](/Automatic_Optical_Beam_Align_System_Using_Numerical_Simulation.pdf)
* 💻 **Source Code:** [Python Script](/beam_alignment_sim.py)

---
**Babacar NDIAYE** | *Master 2 Applied Physics – Nanophysics & Optics* | *Université du Mans*
