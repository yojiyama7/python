# 必要な知識・単語(not in python)
# 配列
	# スカラー
	# スカラー倍
	# 配列同士の積
# 正規分布 (https://atarimae.biz/archives/9850)
# 統計
	# 標準偏差

import numpy as np

# 1次元配列
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr, arr.shape)

# 要素が全て0の配列
arr = np.zeros((2, 5))
print(arr, arr.shape)
# 要素が全て1の配列
arr = np.ones((2, 5))
print(arr, arr.shape)
# 要素が0-1の範囲でランダムな配列
arr = np.random.rand(2, 5)
print(arr, arr.shape)
# 要素が正規分布に則ったランダムな配列(ランダムであってる？)
arr = np.random.randn(2, 5)
print(arr, arr.shape)