#中心差分による微分の計算

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2 + 50*x

def df(x):
	return (f(x + h) - f(x - h)) / (2 * h)

x = np.arange(0.0, 50, 0.1)
h = 1e-5

plt.plot(x, df(x))
plt.show()
