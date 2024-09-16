
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(x) - 4 * x

def df(x):
	return np.exp(x) - 4

#まずは関数の形を見てみる(1)

# x = np.arange(-2, 4, 0.01)
# z = np.zeros(len(x))
# y = f(x)

# plt.plot(x, y, x, z)
# plt.show()

#次にニュートン法を実装する(2)

# x = 4
# epsilon = 1e-5

# print("n\t x\t f(x)")
# n = 1
# while True:
# 	x = x - f(x) / df(x)
# 	print("{}\t{:.6f}\t{:.6f}".format(n, x, f(x)))
# 	n += 1
# 	if abs(f(x)) < epsilon:
# 		break

# print("x = %f" % x)

#次にニュートン法を関数化する(3)

# x = 4
# epsilon = 1e-5
# h = 1e-4

# def Newton_next(f, x, h):
# 	fdx = (f(x + h) - f(x)) / h
# 	return x - f(x) / fdx

# print("n\t x\t f(x)")
# n = 1
# while True:
# 	x = Newton_next(f, x, h)
# 	print("{}\t{:.6f}\t{:.6f}".format(n, x, f(x)))
# 	n += 1
# 	if abs(f(x)) < epsilon:
# 		break

# print("x = %f" % x)

#次にニュートン法全体を関数化する(4)

def Newton_next(f, x, h):
	fdx = (f(x + h) - f(x)) / h
	return x - f(x) / fdx

def Newton_method(f, x, epsilon, h):
	n = 0
	while True:
		x = Newton_next(f, x, h)
		n += 1
		if abs(f(x)) < epsilon:
			break
	return x, n

def g(x):
	return np.exp(x) - 4 * x

x = -2
epsilon = 1e-5
h = 1e-4

x, n = Newton_method(g, x, epsilon, h)
print("x = %f" % x)




