class Member:
    def __init__(self, mid, psw):
        self.__mid = mid
        self.__psw = psw

    def getPwd(self):
        return self.__psw

    def setPwd(self, psw):
        self.__psw = psw

    def getId(self):
        return self.__mid


