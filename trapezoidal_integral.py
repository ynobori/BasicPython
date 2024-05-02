from math import sin, pi, e
# --example--
# print(sin(0))
# >>> 0
# -----------

n = 100
a = 0
b = 1

def f_1(x):
    return sin(x)

def f_2(x):
    return 4 / (1 + (x)**2)

def f_3(x):
    return pi ** (1/2) * e ** (-1*(x)**2)


def daikei(a, b, n, f):
    h = (b - a) / n

    s = 0
    for k in range (1, n + 1):
        s += h * (f(a + (k-1) * h) + f(a + k*h)) / 2
    return s



print('(1)', daikei(0, pi / 2, 50, f_1))
print('(2)', daikei(0, 1, 100, f_2))
print('(3)', daikei(-100, 100, 1000, f_3))