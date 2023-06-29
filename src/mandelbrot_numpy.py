import numpy as np
import matplotlib.pyplot as plt
import os

PIXEL_DENSITY = 3000


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return np.abs(z) < 2


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=PIXEL_DENSITY)
colormap = np.random.choice(plt.colormaps())
plt.imshow(is_stable(c, num_iterations=20), cmap=colormap)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()

name = f"imgs/mandelbrot_{str(colormap)}_{PIXEL_DENSITY}"
name = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), name
)
plt.savefig(name, dpi=400)
