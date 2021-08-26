import Gawibawibo

money = 500
isStop = False
while not isStop:
    money = Gawibawibo.gameGawibawibo(money)
    if money <= 0 or input("계속하시겠습니까?(y/n)") != 'y':
        isStop = True

print(money)





