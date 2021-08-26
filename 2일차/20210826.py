# 가위 바위 보
# 가위:1  바위:2  보:3
# random--> 객체를 이용해서 random 함수를 호출
import random
compNumber = random.randrange(1, 3)
userNumber = int(input("가위:1  바위:2  보:3 >>>"))
# 컴      사용자
# 가위 vs 가위  : 비김
# 가위 vs 바위  : 사용자가 이김
# 가위 vs 보  : 사용자가 짐
if (compNumber == 1) & (userNumber == 1):
    print("비김")
elif (compNumber == 1) & (userNumber == 2):
    print("사용자가 이김")
elif (compNumber == 1) & (userNumber == 3):
    print("사용자가 짐")
# 바위 vs 가위  : 사용자가 짐
# 바위 vs 바위  : 비김
# 바위 vs 보  : 사용자가 이김
elif (compNumber == 2) & (userNumber == 1):
    print("사용자가 짐")
elif (compNumber == 2) & (userNumber == 2):
    print("비김")
elif (compNumber == 2) & (userNumber == 3):
    print("사용자가 이김")
# 보 vs 가위  : 사용자가 이김
# 보 vs 바위  : 사용자가 짐
# 보 vs 보  : 비김
elif (compNumber == 3) & (userNumber == 1):
    print("사용자가 이김")
elif (compNumber == 3) & (userNumber == 2):
    print("사용자가 짐")
else:
    print("비김")

list_a = ["", "가위", "바위", "보"]
print("compNumber", list_a[compNumber]
      , "\tuserNumber", list_a[userNumber])


# 2차원 리스트를 사용해서 표현








