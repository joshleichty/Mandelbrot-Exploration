import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(x, y):
    c = complex(x, y)
    z = 0
    n = 0
    while abs(z) <= 2 and n < 255:
        z = z * z + c
        n += 1
    return n

def mandelbrot_grid(x_min, x_max, y_min, y_max, N=1000, M=1000):
    x = np.linspace(x_min, x_max, N)
    y = np.linspace(y_min, y_max, M)
    return [[mandelbrot(x[i], y[j]) for i in range(N)] for j in range(M)]

mandelbrot_set = mandelbrot_grid(-2, 2, -2, 2)
plt.imshow(mandelbrot_set)
plt.show()