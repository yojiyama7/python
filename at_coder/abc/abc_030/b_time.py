# 時間にそろえて*30、分は*6 で 360 に合わせる
n, m = map(int, input().split())

ans = abs((n%12 + m/60)*30-m*6)
print(min(ans, 360-ans))