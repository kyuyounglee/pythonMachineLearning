import numpy as np
#ndarray  dtype

vec_dtype = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print(vec_dtype)

vec_dtype_float = np.array([1.3, 2.5, 3.2, 4.5, 5.2], dtype=np.float64)
# astype : 배열의 자료형을 변경
print(vec_dtype_float)
new_float = vec_dtype_float.astype(np.int64)
print(new_float)

# 인덱싱
# axis = 0    / axis = 1

# 슬라이싱
vector = np.array([1, 2, 3, 4, 5])
print(vector[:3])
print(vector[3:])
print(vector[1])
print(vector[-1])
print(vector[2:4])
print(vector[2:-1])  # 3 4
print(vector[-1])
print(vector[1])
print(vector[-2])
print(vector[2])




