# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:20:47 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Création dossier figures
os.makedirs("figures", exist_ok=True)

# Paramètres
size = 200
w0 = 30
noise_level = 0.1

x = np.linspace(-100, 100, size)
y = np.linspace(-100, 100, size)
X, Y = np.meshgrid(x, y)

# Faisceau gaussien
def gaussian_beam(x0, y0):
    return np.exp(-2 * ((X - x0)**2 + (Y - y0)**2) / w0**2)

# Ajout bruit
def add_noise(I, level):
    noise = level * np.random.randn(*I.shape)
    return I + noise

# Centre de masse
def compute_centroid(I):
    I = np.abs(I)
    total = np.sum(I)
    cx = np.sum(X * I) / total
    cy = np.sum(Y * I) / total
    return cx, cy

# =====================
# FIGURE 1
# =====================
I = gaussian_beam(0,0)
plt.imshow(I, extent=[-100,100,-100,100])
plt.title("Faisceau centré")
plt.colorbar()
plt.savefig("figures/fig1_beam_centered.png")
plt.show()

# =====================
# FIGURE 2
# =====================
I_shift = gaussian_beam(40,-30)
plt.imshow(I_shift, extent=[-100,100,-100,100])
plt.title("Faisceau désaligné")
plt.colorbar()
plt.savefig("figures/fig2_misaligned.png")
plt.show()

# =====================
# FIGURE 3
# =====================
I_noise = add_noise(I_shift, noise_level)
plt.imshow(I_noise, extent=[-100,100,-100,100])
plt.title("Faisceau bruité")
plt.colorbar()
plt.savefig("figures/fig3_noisy.png")
plt.show()

# =====================
# FIGURE 4
# =====================
cx, cy = compute_centroid(I_noise)

plt.imshow(I_noise, extent=[-100,100,-100,100])
plt.scatter(cx, cy, color='red')
plt.title("Détection du centre")
plt.savefig("figures/fig4_detection.png")
plt.show()

# =====================
# FIGURE 5
# =====================
x0, y0 = 40, -30
positions = []

for i in range(20):
    I = gaussian_beam(x0, y0)
    I_noise = add_noise(I, noise_level)

    cx, cy = compute_centroid(I_noise)
    positions.append((x0, y0))

    gain = 0.5
    x0 -= gain * cx
    y0 -= gain * cy

positions = np.array(positions)

plt.plot(positions[:,0], positions[:,1], 'o-')
plt.title("Convergence")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("figures/fig5_convergence.png")
plt.show()

# =====================
# FIGURE 6
# =====================
noise_levels = np.linspace(0,0.5,20)
errors = []

for n in noise_levels:
    I = gaussian_beam(20,20)
    I_noise = add_noise(I, n)

    cx, cy = compute_centroid(I_noise)
    error = np.sqrt(cx**2 + cy**2)
    errors.append(error)

plt.plot(noise_levels, errors)
plt.title("Effet du bruit")
plt.xlabel("Bruit")
plt.ylabel("Erreur")
plt.grid()
plt.savefig("figures/fig6_noise_effect.png")
plt.show()