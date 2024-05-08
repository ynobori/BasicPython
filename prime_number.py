n = input("nの値を入力: ")
n = float(n)


# TODO

def prime(n):
    if int(n) != n:
        return False
    if n <= 1:
        return False

    for i in range(2,int(n)):
        if n % i == 0:
            return False
    return True
print(prime(n))
