number1 = int(input("입력1>>"))
number2 = int(input("입력2>>"))

list_a = list(range(5))
print(list_a)

print(number1+number2)
print(number1-number2)
# print(list_a[5])
# print(number1/number2)
try:
    print(number1/number2)   # die
    print(list_a[5])
except Exception as e:
    print(e)


print(number1*number2+100)
print(number1**number2+100)


#10 0