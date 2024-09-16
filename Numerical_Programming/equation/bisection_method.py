#二分法による方程式の解法手順
# 1. 関数f(x)を定義する
# 2. 関数f(x)のグラフを描画する
# 3. 区間[a, b]を設定する
# 4. 区間[a, b]の中点cを求める
# 5. f(c)を計算する
# 6. f(c) = 0 ならば、cが解である
# 7. f(c) > 0 ならば、解は区間[a, c]にある
# 8. f(c) < 0 ならば、解は区間[c, b]にある
# 9. 区間[a, b]を[c, b]または[a, c]に更新する
# 10. 区間[a, b]の幅が十分狭くなるまで、ステップ4-9を繰り返す

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2 -2

#まずは関数の形を見てみる

# x = np.arange(-2, 2, 0.01)
# z = np.zeros(len(x))
# y = f(x)

# plt.plot(x, y, x, z)
# plt.show()

#次に二分法を実装する

a = -1
b = -1.5
n = 0

epsilon = 1e-5

while True:
	c = (a + b) / 2
	if f(a) * f(c) > 0:
		a = c
	else:
		b = c
	n += 1
	if abs(b - a) < epsilon:
		break

print(c)
print(n)
print(f(c))
