lifeTime = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요. '))

if lifeTime <= 60:
    print('생존율 : 85%')
elif lifeTime <= 120:
    print('생존율 : 76%')
elif lifeTime <= 180:
    print('생존율 : 66%')
elif lifeTime <= 240:
    print('생존율 : 57%')
elif lifeTime <= 300:
    print('생존율 : 47%')
elif lifeTime <= 360:
    print('생존율 : 37%')
else:
    print('생존율 : 25% 미만')
