a = input("aの値を入力: ")
b = input("bの値を入力: ")
a = int(a)
b = int(b)

# TODO
if a == 1:
    print(a,'は素数ではありません')
else:
    i = 2
    while a > i:

        if a % i == 0:
            print(a,'は素数ではありません')
            break
        elif i > a/2:
            print(a,'は素数です')
            break
        else:
            i += 1

if b == 1:
    print(b,'は素数ではありません')
else:
    j = 2
    while b > j:
        if b % j == 0:
            print(b,'は素数ではありません')
            break
        elif j > b/2:
            print(b,'は素数です')
            break
        else:
            j += 1