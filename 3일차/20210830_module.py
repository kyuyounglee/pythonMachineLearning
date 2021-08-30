# 행렬/성형대수/통계    Numpy 넘파이
#   행렬 기반의 데이터 처리, 데이터 분석
# 데이터 프로세싱 : Pandas 판다스
#   2차원데이터 처리에 효율적인 라이브러리
# 시각화 : 맷플립 Matplotlib / 시본(Seaborn) 2차원과 3차원 데이터 그래프
# 머신러닝 : 사이킷런 Scikit-Lean
import numpy as np

data_1 = [1, 2, 3, 4, 5]  # 백터 (Vector)
print(data_1)
data_2 = [[1, 2, 3], [4, 5, 6]]  # 행렬(Matrix)
print(data_2)

vector_1 = np.array(data_1)
print(vector_1)
matrix_1 = np.array(data_2)
print(matrix_1)

print(np.zeros((2, 5)))
print(np.ones(5))
print(np.arange(5))
print(np.full((3, 3), 5))

#dtype : 타입을 알려준다
#ndim : 차원을 알려준다
#shape : 행렬의 크기를 알려준다
#size : 행렬의 개수를 알려준다

print(vector_1.dtype)
print(matrix_1.ndim)
print(matrix_1.shape)
print(matrix_1.size)


