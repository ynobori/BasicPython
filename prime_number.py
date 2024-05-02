n = input("nの値を入力: ")
n = float(n)


# TODO

def prime(n):
    if int(n) != n:
        return False
    elif n <= 1:
        return False
    else:
        i = 2
        while n > i:
            if n % i == 0:
                return False
                break
            elif i > n/2:
                return True
                break
            else:
                i += 1


print(prime(n))
