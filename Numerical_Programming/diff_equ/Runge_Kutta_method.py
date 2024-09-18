import numpy as np
import matplotlib.pyplot as plt

#k1~k4に前もってhをかけておくと、結果が異なる。
#k1~k4にhをかけるのは、returnのところで行ったが手計算との比較で決定した。
#ちがいが起こるのは、前もってかけることで値の切り捨てが行われるため、誤差が生じる？

def RK4(df, x, y, h):
    k1 = df(x, y)
    k2 = df(x + h / 2, y + k1 / 2)
    k3 = df(x + h / 2, y + k2 / 2)
    k4 = df(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6

def df(x, y):
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
    y = RK4(df, x, y, h)

y_exact = (x_list ** 3) / 3 + 2 / 3

plt.plot(x_list, y_list, x_list, y_exact)
plt.show()

error = np.sum(abs(y_list - y_exact)*h)
print(error)
