# def add(x, y):
#     return x + y

# lamda 매개변수: 리턴할 수식    -> 한줄로 표현

def strAdd(str, x,y, func):
    return "{} : {}".format(str, func(x, y))

str1 = "두변수의 합"
print(strAdd(str1, 10, 20, lambda x, y: x+y))

import pandas as pd
import numpy as np
filePath = './data/chipotle.tsv'
chipo = pd.read_csv(filePath, sep='\t')

print(chipo.shape)
print(chipo.info())
print(chipo.head())
print(chipo.columns)
print(chipo.index)

print(chipo.describe())
print(chipo['order_id'].head())

chipo['order_id'] = chipo['order_id'].astype(str)
print(chipo.describe())

# 갯수 확인하기
print(chipo['order_id'].unique())
print(chipo['item_name'].unique())

# 가장 많이 주문한 상품은 상위 10?
print(chipo['item_name'].value_counts()[:10])

# 가장 많이 팔린 제품과 가장 안팔린 제품은
print("--------------------------------------------")
print(chipo['item_name'].value_counts().index[0])
print(chipo['item_name'].value_counts().index[-1])
print(chipo['item_name'].value_counts().head(1).index[0])
print(chipo['item_name'].value_counts().tail(1).index[0])
print(chipo['item_name'].value_counts().index)
print(chipo['item_name'].value_counts().index.tolist())

# 아이템당 주문 개수와 총량 구하기
print("--------------------------------------------")
print(chipo.groupby('item_name')['order_id'].sum())
print("--------------------------------------------")
print(chipo.groupby('item_name')['quantity'].sum())

# 아이템당 평균 가격( 제품가격)
print("--------------------------------------------")
# print(chipo.columns)
# print(chipo.groupby('item_name')['item_price'].sum())
# print("--------------------------------------------")
# print(chipo['item_price'].str.len()-1)
# print(chipo['item_price'])
# print(chipo['item_price'].str.slice(start=1, stop=list(chipo['item_price'].str.len()[1] )

print(chipo['item_price'].str[1:])
chipo['item_price_float'] = chipo['item_price'].str[1:]
chipo['item_price_float'] = chipo['item_price_float'].astype(float)
print(chipo.info())
# 아이템당 가격이 얼마인지..
print(chipo.groupby('item_name')['item_price_float'].mean())


# 아이템당 가격을 구해보자
print(chipo[['item_name', 'item_price_float']])

chipo2 = chipo[['item_name', 'item_price_float']]
print("-----------------------------------------------------------")
print(np.round(chipo2.groupby('item_name')['item_price_float'].mean()), 3)
print("-----------------------------------------------------------")

import matplotlib.pyplot as plt
item_quantity = chipo.groupby('item_name')['quantity'].sum()
print(item_quantity)
# x 축
print("---------------------------------------")
item_name_list = item_quantity.index.tolist()
print(item_name_list)
print(len(item_name_list))
x_pos = np.array(len(item_name_list))
print(x_pos)
order_cnt = item_quantity.values.tolist()

plt.bar(item_name_list, order_cnt, align='center')
plt.show()
