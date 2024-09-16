#前進差分と中心差分の比較

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return -2 * x * np.exp(-x**2)

def forward_diff(x):
	return (f(x + h) - f(x)) / h

def central_diff(x):
	return (f(x + h) - f(x - h)) / (2 * h)

x = np.arange(0.0, 5, 0.01)
h = 0.1

plt.plot(x, forward_diff(x), label="forward diff")
plt.plot(x, central_diff(x), label="central diff")
plt.legend()
plt.show()
