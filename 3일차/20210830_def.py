# 함수
# 입력된값 으로 어떤 기능을 실행 한 후 결과값을 리턴하는 것
# 입력된값 / 결과값을 리턴 : 필수가 아님
def func_print():
    print("함수연습")
    print("입력된값이 없고 결과값도 없는 함수")


def fun_01(n):
    for i in range(1, 6):
        print(i*n)

# 함수 를 만들고 그 함수를 호출하면
# 3
# 6
# 9
# 12
# 15
# or
# 2
# 4
# 6
# 8
# 10

# 가변 매개변수  - 파이썬은 method overload 지원 하지 않습니다.
# fun_sum(1,2,3,4)   10
# fun_sum(1,2,3,4,5,6,7,8,9,10)   55

# 가변 매개변수
def fun_sum(* numbers):
    _sum = 0
    for i in numbers:
        _sum += i
    print(_sum)

fun_sum(1, 2, 3, 4, 5)

# 디폴트 매개변수
def fun_print(str, n=1):
    for i in range(n):
        print(i, str)

fun_print("안녕")
fun_print("안녕", 2)








