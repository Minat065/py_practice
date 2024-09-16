#テント写像のふるまいを調べるプログラム

import numpy as np
import matplotlib.pyplot as plt

# パラメタaを変えることで、振る舞いが大きく変わります。

a = 3.8
x = 0.8
x_list = []
n_list = []
num = 50

for i in range(num):
	x = a * min(x, 1 - x)
	x_list.append(x)
	n_list.append(i)

plt.plot(n_list, x_list)
plt.xlabel('n')
plt.ylabel('x')
plt.show()
