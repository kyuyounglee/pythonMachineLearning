import pandas as pd

df = pd.read_csv("./data/ch1_sport_test.csv", encoding="UTF-8", index_col='학생번호')
# print(df)

print(df['악력'])
print(type(df['악력']))
print(df.shape)
print(df)

#양적 변수 : 양을 표현하는 변수
#질적 변수 : 선택이 필요한 변수, 종류를 구별하는 변수
# 1. 좋은 2. 나쁨
# A형 B형    / 남 여여

# 범주형 변수 : 카테고리를 가지고 있는 변수
# 연속형 변수 : 계산이 가능한 변수
    # 이산형 변수 : 인접한 숫자 사이에 값이 존재하지 않는경우
