from functools import reduce


def apply(list_1, _func):
    _result = _func(list_1)
    return _result


list_a = list(range(1, 10))  # 1,2,3,4,5,6,7,8,9
print(reduce(lambda x, y: x+y, list_a))
print(reduce(lambda x, y: x*y, list_a))

list_a.reverse()

list_a.sort(reverse=True)
print(list_a)

list_b = [(1, 2), (0, 3), (5, 1), (3, 0)]
print(list_b)

def customSort(x):
    return x[1]

print(sorted(list_b, key=lambda x: x[0]))
# print(sorted(list_b, key=lambda x: x[1]))
print(sorted(list_b, key=customSort))



# lamda 인자 : 표현식
def add(x,y):
    return x+y

(lambda x,y : x+y)(10,20)

#reduce(함수, 시퀀스)

print(reduce(lambda x,y : x+y, list_a))

#filter(함수, 시퀀스) -->
a = list(filter(lambda x: x % 2 == 0, list_a))
print(sorted(a))

# def add(x,y):
#     return x+y

add = lambda x, y: x+y
ret = add(1, 3)
print(ret)  # 4


funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1 = funcs[0]("intro")
ret2 = funcs[1]("Report")
print(ret1, ret2)

names = {
    'Mary':25,
    'Sams':35,
    'Aimy':27
}
# 이름순으로 정렬
# 나이순으로 정렬
# sorted
print(names.items())
result = sorted(names.items(), key=lambda x: x[1])
print(result)


# map    java map 과 다름       java map == dictionary
# 람다의 매개변수를 시퀀스의 요소를 전달해서 반복 수행하고 결과를 리스트형태로 반환-->리스트로 변환해야함
result = map(lambda x: x**x, [1, 2, 3, 4, 5])
print(list(result))

# reduce, filter, map  -->  lamda 사용하는 case





