
import numpy as np
import matplotlib.pyplot as plt

def Euler(dfx, dfv, t, x, v, h):
    return x + dfx(t, x, v) * h, v + dfv(t, x, v) * h

def dfx(t, x, v):
    return v

def dfv(t, x, v):
    return -1

h = 0.01
t0 = 0.0
x0 = 6.0
v0 = 2.0
t_end = 6.0

t_list = np.arange(t0, t_end, h)
x_list = []
v_list = []
x = x0
v = v0

for t in t_list:
    x_list.append(x)
    v_list.append(v)
    x, v = Euler(dfx, dfv, t, x, v, h)

x_exact = -(1 / 2)*t_list**2 + 2*t_list + 6

plt.plot(t_list, x_list, t_list, x_exact)
plt.show()
