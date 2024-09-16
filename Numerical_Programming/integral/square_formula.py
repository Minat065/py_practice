#矩形公式（方形公式）の計算

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)**2

x_low = 0.0
x_high = 5.0
N = 32
dx = (x_high - x_low) / N
x = np.linspace(x_low, x_high, N)
y = f(x)

S = np.sum(y) * dx
print(S)
