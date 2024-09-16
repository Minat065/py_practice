
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x ** 2 - 2

def bisection(f, a, b, epsilon, max_loop):
	n = 0
	while True:
		c = (a + b) / 2
		if f(a) * f(c) > 0:
			a = c
		else:
			b = c
		n += 1
		if abs(b - a) < epsilon or n > max_loop:
			break
	return c, n

a = 1
b = 2
epsilon = 1e-5
max_loop = 100

c, n = bisection(f, a, b, epsilon, max_loop)
print(c)
print(n)
print(f(c))

#この解法の良いところは、厳密な解が求められなくても、解の近似値が求められること。
#また、関数が連続であることが前提となるが、それ以外の制約は少ない。
#しかし、収束が遅いという欠点がある。
#また、scipy.optimizeモジュールには、bisection関数が用意されているので、それを使うこともできる。

#scipy.optimize.bisect(f, a, b, xtol=1e-5, maxiter=100)

