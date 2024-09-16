#hの大きさを段階的に変えて厳密な値に近づける

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x * np.exp(-x**2)

def central_diff(x, h):
	return (f(x + h) - f(x - h)) / (2 * h)

x = np.arange(0.0, 5, 0.01)
h1 = 0.5
h2 = 0.25
h3 = 0.1
h4 = 0.05

plt.plot(x, central_diff(x, h1), label="h=0.5")
plt.plot(x, central_diff(x, h2), label="h=0.25")
plt.plot(x, central_diff(x, h3), label="h=0.1")
plt.plot(x, central_diff(x, h4), label="h=0.05")
plt.legend()
plt.show()
