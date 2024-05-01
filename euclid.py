a = input("a の値を入力: ")
b = input("b の値を入力: ")
a = int(a)
b = int(b)

# TODO
"""
if a < b:
    c = a
    a = b
    b = c
"""
while True:
    d = a % b
    if d == 0:
        print('最大公約数は',b)
        break
    else:    
        a = b
        b = d