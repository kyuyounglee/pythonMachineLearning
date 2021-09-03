text = input("파일에 저장할 내용을 입력하세요")
f = None
try:
    f = open("c:/Temp/myData.txt", 'w', encoding='utf-8')
    f.write(text)
except Exception as e:
    print(e)
finally:
    if f:
        f.close()


