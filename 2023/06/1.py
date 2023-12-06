
import math

t = [62, 64, 91, 90]
d = [553, 1010, 1473, 1074]

p = 1
for i in range(len(t)):
    mi = math.ceil(((-1 * t[i]) + math.sqrt(t[i] ** 2 - (4 * d[i]))) / -2)
    ma = math.floor(((-1 * t[i]) - math.sqrt(t[i] ** 2 - (4 * d[i]))) / -2)

    p *= (ma - mi + 1)

print(p)
