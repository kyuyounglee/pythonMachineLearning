incoming = int(input('수입 : '))
outgoing = int(input('지출 : '))
result = '흑자' if incoming > outgoing else '적자'
print(result)
