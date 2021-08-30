import numpy as np
# 175 177 179 181 183
# 평균 : 변량의 합 / 인원수    179
# 편차 : 변량 - 평균
# 편차제곱 :
# 분산 : 편차제곱의 평균    8
# 표준편차 : 분산에 루트를 씌운것  2.828

# 10 10 10 10 10
# 분산 0
# 표준편차 0

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
)

print("합", np.sum(matrix))
print("합", matrix.sum())

print("평균", np.mean(matrix))
print("평균", matrix.mean())

print("분산", np.var(matrix))
print("분산", matrix.var())

print("표준편차", np.std(matrix))
print("표준편차", matrix.std())

print("최소", np.min(matrix))
print("최소", matrix.min())

print("열에서 최대값", np.max(matrix, axis=0))
print("행에서 최대값", np.max(matrix, axis=1))






