import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
	return 1 + np.cos(x + a)

x = np.arange(-1*np.pi, 1*np.pi, 0.1)
y = f(x, 0)

plt.plot(x, y)

y = f(x, np.pi/2)
plt.plot(x, y)

plt.show()
