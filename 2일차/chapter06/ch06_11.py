score = int(input('점수를 입력하세요. '))
 
if score >= 60 and score < 70 :		# 60 이상 70 미만이면 ‘D' 출력
    print('D')
elif score >= 80 and score < 90 :		# 80 이상 90 미만이면 ‘B' 출력
    print('B')
elif score >= 70 and score < 80 :		# 70 이상 80 미만이면 ‘C' 출력
    print('C')
elif score >= 90 :	                		# 90 이상이면 ‘A’ 출력
    print('A')
else:			               	# 60 미만이면 'F' 출력
    print('F')
