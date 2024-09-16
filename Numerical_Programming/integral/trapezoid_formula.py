#台形公式による積分計算
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)**2

def trapezoid(f, x, dx):
	return (f(x) + f(x + dx)) * dx / 2.0

def integral_trapezoid(f, x_low, x_high, N):
	dx = (x_high - x_low) / N
	x_list = np.linspace(x_low, x_high - dx, N)
	y_list = [trapezoid(f, x, dx) for x in x_list]
	S = np.sum(y_list)
	return S

x_low = 0.0
x_high = 5.0
exact = 5.0 / 2.0 - np.sin(10.0) / 4.0

for N in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
	S = integral_trapezoid(f, x_low, x_high, N)
	print("N = %4d, S = %.10f, error = %.10f" % (N, S, np.abs(S - exact)))
