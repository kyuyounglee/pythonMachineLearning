score = int(input('점수를 입력하세요. '))

if score >= 60:	        # 60점 이상이면 'D' 출력
    print('D')
elif score >= 80:	       # 80점 이상이면 ‘B’ 출력
    print('B')
elif score >= 70:           # 70점 이상이면 ‘C’ 출력
    print('C')
elif score >= 90:	        # 90점 이상이면 ‘A’ 출력
    print('A')
else:		        # 그렇지 않으면 ‘F’ 출력
    print('F')
