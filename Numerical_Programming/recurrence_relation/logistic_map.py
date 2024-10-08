# ロジスティック写像は、次のような再帰的な式で定義される数列です。

# xn+1 = a * xn * (1 - xn)

# パラメタaを変えることで、振る舞いが大きく変わります。

# 0≤a≤1のとき：xnはnの増加とともに単調減少して0に収束する
# 1<a≤2のとき：xnはnについて単調に変化しながら1−1/aに収束する。
# 2<a≤3のとき：xnは1−1/aに収束するが、途中経過は単調ではない
# 3<a≤3.4494897⋯のとき：xnは1つの値には収束せず、ある2つの値を交互にとるような周期的な変化(２周期軌道)を示すようになる。
# 3.4494897<a≤3.5699456⋯のとき:aを増やすにつれて、4周期, 8周期, 16周期と周期が増えていく
# 3.5699456⋯<a<4のとき：カオスが発生し、収束もせず周期性もない複雑な挙動を示す

# このように、aの値によっては、単純な振る舞いを示す場合もあれば、カオスを示す場合もあります。

import matplotlib.pyplot as plt

# パラメタaを変えることで、振る舞いが大きく変わります。
a = 1.5
x = 0.8
x_list = []
n_list = []
num = 50

for i in range(num):
	x = a * x * (1 - x)
	x_list.append(x)
	n_list.append(i)

plt.plot(n_list, x_list)
plt.xlabel('n')
plt.ylabel('x')
plt.show()
