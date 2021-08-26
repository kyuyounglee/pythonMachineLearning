import random
def gameGawibawibo(money):
    # 사용자가 stop 하면 끝  또는 -금액이 나오면 중지
    list_a = [0, 1, -1]
    list_b = [-1, 0, 1]
    list_c = [1, -1, 0]
    twolist = [list_a, list_b, list_c]
    compnumber = random.randrange(0, 3)
    usernumber = int(input("가위(0) 바위(1) 보(2)"))
    result = twolist[compnumber][usernumber]
    list_d = ["가위", "바위", "보"]
    print("compNumber", list_d[compnumber]
          , "\tuserNumber", list_d[usernumber])
    if result == 0:
        print("비김")
    elif result > 0:
        money = money * 0.3 + money
        print("승리")
    else:
        money = money - money * 0.5
        print("패배")
    return money