
from math import sin, pi, e
# --example--
# print(sin(0))
# >>> 0
# -----------

def f_1(x):
    return sin(x)

def f_2(x):
    return 4 / (1 + (x)**2)

def f_3(x):
    return pi ** (1/2) * e ** (-1*(x)**2)


def daikei(f, a = 0, b = 1, n = 100):
    h = (b - a) / n

    s = 0
    for k in range (1, n + 1):
        s += h * (f(a + (k-1) * h) + f(a + k*h)) / 2
    return s



print('(1)', daikei(f_1, 0, pi / 2, 50))
print('(2)', daikei(f_2, 0, 1, 100))
print('(3)', daikei(f_3, -100, 100, 1000))
