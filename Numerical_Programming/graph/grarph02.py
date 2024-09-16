import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 1 + np.cos(x)

x = np.arange(-1*np.pi, 1*np.pi, 0.1)
y = f(x)

plt.plot(x, y)
plt.show()
