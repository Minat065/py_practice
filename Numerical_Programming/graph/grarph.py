import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.exp(-t*t)*np.cos(2*np.pi*t)

x=np.arange(0.0,4.0,0.05)
y=f(x)

plt.plot(x,y)
plt.show()
