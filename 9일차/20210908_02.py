import pandas as pd
names = ['a', 'b', 'c', 'd', 'e']
birth = [123, 587, 247, 415, 555]
custom = [1, 5, 25, 13, 23232]

# zip  두개의 리스트를 각각 묶어서 튜플의 객체로 만들고 list로 씌워야 튜플로 사용 할수 있다
# 리스트의 요소로 튜플을 사용
dataSet = list(zip(names, birth))
print(dataSet)

# 2차원 행열구조
list_a = ([x, y] for x, y in zip(names, birth))
print(list(list_a))

# dataFrame 구조로 만들기
df = pd.DataFrame(data=dataSet, columns=['Names', 'Birth'])
print(df)

print(df.dtypes)
print(df.index)
print(df.columns)

print(df[df.columns[0]])
print(df[df['Birth'] > 300])
print(df[0:3])

import numpy as np
print(np.arange(15))
arr1 = np.arange(15).reshape(3, 5)
print(arr1.shape)

arr2 = np.array([6, 7, 8])
print(type(arr2))

arr3 = np.zeros((3, 4))
print(arr3)
arr4 = np.ones((3, 4))
print(arr4)

