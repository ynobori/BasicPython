a = input("a の値を入力: ")
b = input("b の値を入力: ")
a = int(a)
b = int(b)

# TODO
def euclid(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd = euclid(a, b)
print('最大公約数は',gcd)


def multiple_prime(a, b):
    gcd = euclid(a, b)
    if gcd == 1:
        return True
    else:
        return False

print(multiple_prime(a, b))
