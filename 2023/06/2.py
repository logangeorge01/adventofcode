
import math

t = int(''.join([str(n) for n in [62, 64, 91, 90]]))
d = int(''.join([str(n) for n in [553, 1010, 1473, 1074]]))

mi = math.ceil(((-1 * t) + math.sqrt(t ** 2 - (4 * d))) / -2)
ma = math.floor(((-1 * t) - math.sqrt(t ** 2 - (4 * d))) / -2)

p = (ma - mi + 1)

print(p)
