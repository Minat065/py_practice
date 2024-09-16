#関数化して厳密解と比較する
#終わってから気が付いたけど、squareだと正方形になるから、rectangle_formulaとかにした方がいいかも

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)**2

def square_formula(f, x_low, x_high, N):
	dx = (x_high - x_low) / N
	x = np.linspace(x_low, x_high, N)
	y = f(x)
	S = np.sum(y) * dx
	return S

x_low = 0.0
x_high = 5.0
exact = 5.0 / 2.0 - np.sin(10.0) / 4.0

for N in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
	S = square_formula(f, x_low, x_high, N)
	print("N = %4d, S = %.10f, error = %.10f" % (N, S, np.abs(S - exact)))
