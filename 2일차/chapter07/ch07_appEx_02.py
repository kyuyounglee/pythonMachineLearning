trainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0:
        print(9+n//60, end='')
        print('시 ', end='')
        print(n%60, end='')
        print('분')
    elif n % trainB == 0 and n % trainC == 0:
        print(9+n//60, end='')
        print('시 ', end='')
        print(n%60, end='')
        print('분')
    elif n % trainC == 0 and n % trainA == 0:
        print(9+n//60, end='')
        print('시 ', end='')
        print(n%60, end='')
        print('분')
