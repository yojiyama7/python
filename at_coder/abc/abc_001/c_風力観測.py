from decimal import Decimal, ROUND_HALF_UP
from bisect import bisect_right

DEG, DIS = map(int, input().split(" "))

power_data = [0.3, 1.6, 3.4, 5.5, 8.0, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]
# print(bisect_right(power_data, 32.6), DIS/60)
# print(Decimal(str(DIS/60)).quantize(Decimal("1.0"), rounding=ROUND_HALF_UP))
speed = float(Decimal(str(DIS/60)).quantize(Decimal("1.0"), rounding=ROUND_HALF_UP))
# print(speed)
power = bisect_right(power_data, speed)

direction_data = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
if power == 0:
    direction = "C"
else:
    # print((DEG/10+11.25)%360//22.5)
    direction = direction_data[int((DEG/10+11.25)%360//22.5)]
# print(speed)

print(direction, power)