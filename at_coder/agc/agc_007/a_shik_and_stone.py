# 最短ルートでいける、左上開始、右上終了ゆえに#の数数えればいけるぞ
# やられた、、、

H, W = map(int, input().split(" "))
A = [input() for _ in range(H)]

print(["Impossible", "Possible"]["".join(A).count("#")==H+W-1])

################################

# # WA
# h,w=map(int,input().split());print("P"*(open(0).read().count("#")==h+w-1)or"Imp"+"ossible")