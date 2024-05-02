a = input("a の値を入力: ")
b = input("b の値を入力: ")
a = int(a)
b = int(b)

# TODO
def euclid(a, b):
    while True:
        d = a % b
        if d == 0:
            return b
            break
        else:    
            a = b
            b = d

gcd = euclid(a, b)
print('最大公約数は',gcd)