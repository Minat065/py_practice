#前進差分と中心差分の誤差を比較する
#前進差分 O(h)
#中心差分 O(h^2)

import numpy as np
import matplotlib.pyplot as plt

# 関数
def f(x):
	return np.exp(-x**2)

def forward_diff(f, x, h):
	return (f(x + h) - f(x)) / h

def central_diff(f, x, h):
	return (f(x + h) - f(x - h)) / (2 * h)

def exact_diff(x):
	return -2 * x * np.exp(-x**2)

dx = 0.01
x = np.arange(0.0, 4.0, dx)
h = 0.1

# y_forward = forward_diff(x, h)
# y_exact = exact_diff(x)

# diff_y_forword_error = np.abs(y_forward - y_exact)

#これは前進差分の誤差
# plt.plot(x, diff_y_forword_error, label="forward diff error")
# plt.legend()
# plt.show()

#厳密解と前進差分の誤差を方形公式で積分
#print(np.sum(diff_y_forword_error) * dx)

#上の誤差がhに比例していることを確認
#同様のことを中心差分で行う

def error_forward_diff(f, h, dx, low_x, high_x):
	x = np.arange(low_x, high_x, dx)
	y_forward = forward_diff(f, x, h)
	y_exact = exact_diff(x)
	diff_y_forword_error = np.abs(y_forward - y_exact)
	return np.sum(diff_y_forword_error) * dx

def error_central_diff(f, h, dx, low_x, high_x):
	x = np.arange(low_x, high_x, dx)
	y_central = central_diff(f, x, h)
	y_exact = exact_diff(x)
	diff_y_central_error = np.abs(y_central - y_exact)
	return np.sum(diff_y_central_error) * dx

low_x = 0.0
high_x = 100

h_list = np.linspace(0.01, 10, 100)
error_list_forword = [error_forward_diff(f, h, dx, low_x, high_x) for h in h_list]
error_list_central = [error_central_diff(f, h, dx, low_x, high_x) for h in h_list]

plt.plot(h_list, error_list_forword, 'bo', label="forward diff error")
plt.plot(h_list, error_list_central, 'ro', label="central diff error")
plt.xlabel("h")
plt.ylabel("error")
plt.show()
