```
i [1, N+1]: i番目までで
w [0, W+1]: 幅wの
k [0, K+1]: k枚
```

```
dp[番号i][幅w][枚数k]

dp[番号i-1][幅w][枚数k]
dp[番号i-1][幅w-幅i番目][枚数k-1] + value[i-1]
```

```python
dp[i][w][k] = max([
	dp[i-1][w][k],
	dp[i-1][w-width[i-1]][k-1] + value[i-1]
])
```

