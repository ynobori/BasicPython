from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# ----------

n = 100
a = 0
b = math.pi / 2
h = (b - a) / n

s = 0
for k in range (1, n + 1):
    s += h * (sin(a + (k-1) * h) + sin(a + k*h)) / 2
print(s)