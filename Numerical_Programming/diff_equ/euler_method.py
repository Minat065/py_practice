import numpy as np
import matplotlib.pylab as plt

def	Euler(df, x, y, h):
	return y + df(x) * h

def	df(x):
	return x * x

h = 0.01
x0 = 1.0
y0 = 1.0
x_end = 2.0

x_list = np.arange(x0, x_end, h)

y_list = []
y = y0

for x in x_list:
	y_list.append(y)
	y = Euler(df, x, y, h)

y_exact = x_list ** 3/3 + 2/3

plt.plot(x_list, y_list, x_list, y_exact)
plt.show()
