a = input("aの値を入力: ")
b = input("bの値を入力: ")
a = int(a)
b = int(b)

# TODO
i = 2
while a > i:
    if a % i == 0:
        print('aは素数ではありません')
        break
    elif i > a/2:
        print('aは素数です')
        break
    else:
        i += 1


j = 2
while b > j:
    if b % j == 0:
        print('bは素数ではありません')
        break
    elif j > b/2:
        print('bは素数です')
        break
    else:
        j += 1