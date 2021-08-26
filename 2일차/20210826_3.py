import random
# 순환문
# for while
# 조건문
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list(range(1, 10)):
#     print(" 2 x ", i, " = ", 2 * i)

# while 조건을 가지고 순환하는 문장
_sum = 0
# for i in range(0, 5):
#     _sum += random.randrange(0, 100)
# print(_sum)
countN = 0
while _sum < 250:
    countN += 1
    _sum += random.randrange(0, 100)

print(_sum)
print(countN)











