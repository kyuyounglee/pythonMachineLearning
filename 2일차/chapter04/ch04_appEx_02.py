print('내일 날씨 정보를 입력하세요.')
dayData = input('요일:')
dateData = input('날짜: ')
lowestTemp = input('아침 최저기온: ')
highestTemp = input('낮 최고기온: ')
rainingPercent = input('비올 확률: ')
fineDustStatus = input('미세먼지: ') 
sunriseTime = input('일출 시간: ')
sunsetTime = input('일몰 시간: ')
southOceanWave = input('남해 물결 높이: ')
eastOceanWave = input('동해 물결 높이: ')
westOceanWave = input('서해 물결 높이: ')

print('-------------------------------------------------------------------------------------------')
print('내일 날씨 예보입니다.')
print(dayData + '요일인 ' + dateData + '의 ' + '아침 최저 기온은 ' + lowestTemp + '도, 낮 최고 기온은 ' + highestTemp + '도로 예보됐습니다.')
print('비올 확률은 ' +  rainingPercent + '%이고, 미세먼지는 ' + fineDustStatus + ' 수준일 것으로 예상됩니다.')
print('일출 시간은 ' + sunriseTime + '이고, 일몰 시간은 ' + sunsetTime + '입니다.')
print('바다의 물결은 남해 앞바다 ' + southOceanWave + 'm, 동해 앞바다 ' + eastOceanWave + 'm, 서해 앞바다 ' + westOceanWave + 'm 높이로 일겠습니다.')
print('지금까지 ' + dateData + ' ' + dayData + '요일 날씨 예보였습니다.')
print('-------------------------------------------------------------------------------------------')
