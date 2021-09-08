import numpy as np
import pandas as pd

# numpy 가 csv 파일을 읽어오면 DataFrame 형태로 반환한다
df = pd.read_csv("./data/ch2_scores_em.csv", index_col = 'student number')

print(np.array(df['english']))
scores = np.array(df['english'])
scores = scores[:10]
print(scores.shape)
names = ['A','B','C','D','E','F','G','H','I','J']
new_df = pd.DataFrame(
     {'score': scores},
    index=pd.Index(names, name='Student')
 )
print(new_df)

print(np.mean(scores))
print(new_df.mean())

# 중앙값
#  n -- >홀수  (n+1)/2    1 5 8                           5
#  n -- >짝수  n/2 와 n/2+1번째 데이터의 평균    1 5 8 10    6.5

print(scores)
print(np.sort(scores))

# 절사평균
# 10%절사평균
# 데이터가 20 양쪽에서 하나씩 제거해서 18

scores =  np.array(df['english'])[:15]
print("오리지널",scores)
# scores = scores[1:]
# scores = scores[:-1]
# print(int(len(scores)*0.2/2))
number = int(np.ceil(len(scores)*0.2/2))
print(number)
print("20%절사", scores[number:-number])


# 20%절사평균
# 데이터가 20 양쪽에서 두개씩 제거해서 16

#다이빙 점수
# 7명의 심판중에 최고와 최저점을 제외하고 5명의 평균....에 난이도를 고려



#최빈값 : 가장많이 나타나는 값

print(type([1, 1, 1, 2, 2, 3]))
print(type(scores))
print(pd.Series(scores).mode())

# 편차  n - mean
# score의 편차를 구해봅시다
print(np.mean(scores))
pencha = np.round(scores - np.mean(scores), 2)
print(pencha)
# numpy
# 평균 : mean
# 편차 :  각 요소를 평균으로 뺀거
# 편차 제곱 ( 편차*편차)
# 분산 var : 편차제곱의 평균
# 표준편차 std : 분산에다가 root를 씌운것


