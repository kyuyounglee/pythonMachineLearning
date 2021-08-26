adminPw = 'hanbitac'
count = 1

while True:
    if count > 5:
        print('로그인 실패!! 횟수 초과!!!')
        break

    inputPw = input('관리자 암호를 입력하세요. ')
    
    if inputPw != adminPw:
        print('암호를 다시 확인하세요!')
        count += 1
    elif inputPw == adminPw:
        print('로그인 됐습니다.')
        break
