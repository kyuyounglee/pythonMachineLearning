# 클래스명 : calculator
# 속성(변수) : num1 num2
# 함수 : add, subtract
class Calculator:
    # 생성자(Default 생성자) - 없어도 아래와 같이 자동으로 제공(hidden)
    def __init__(self, n1=0, n2=0):
        print("생성자 호출")
        self.n1 = n1
        self._n2 = n2


# c1 객체 생성  기본생성자 호출을 통해서
print("객체생성전")
c1 = Calculator(10, 20)
c2 = Calculator()
c1.n1 = 100
c1._n2 = 200
print("객체생성후")

