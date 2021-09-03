f = None
try:
    f = open("c:/Temp/test.txt", 'r', encoding="utf-8")
    data = f.read()
    print(data)
    f.close()
except Exception as e:
    if f:
        f.close()
    print(e)
print("#################")
try:
    f = open("c:/Temp/test.txt", 'r', encoding="utf-8")
    line = 1
    while line:
        line = f.readline()
        print(line, end='')
except Exception as e:
    print(e)
finally:
    if f:
        f.close()
    print()


