import random
# 0	    1	-1
# -1	0	1
# 1	    -1	0
list_a = [0, 1, -1]
list_b = [-1, 0, 1]
list_c = [1, -1, 0]
twoList = [list_a, list_b, list_c]

compNumber = random.randrange(0, 2)
userNumber = int(input("가위(0) 바위(1) 보(2)"))
result = twoList[compNumber][userNumber]
list_a = ["가위", "바위", "보"]
print("compNumber", list_a[compNumber]
      , "\tuserNumber", list_a[userNumber])
if result == 0:
    print("비김")
elif result > 0:
    print("유저 승")
else:
    print("컴퓨터 승")

