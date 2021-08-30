# 숫자 맞추기 게임
# 컴퓨터가 선택한 숫자를 맞추는 게임
# 총 시도 횟수가 5번을 넘어가면 out
# 컴퓨터는 1 ~ 100 사이의 숫자를 선택  사용자의 값이 크면 크다  작으면 작다
import random as rd
# 컴퓨터가 선택한 숫자
comNumber = rd.randrange(1, 101)
# tryCount = 0
# while tryCount < 6:
#     tryCount += 1
for i in range(0, 6):
    # 사용자가 선택한 숫자
    userNumber = int(input("숫자입력>>"))
    # 두 숫자를 비교
    if comNumber == userNumber:
        print("정답")
        break
    elif comNumber > userNumber:
        print("작다")
    else:
        print("크다")

print("computer = ", comNumber)




