# 데이터 전처리
import pandas as pd
import numpy as np
filePath = './data/chipotle.tsv'
chipo = pd.read_csv(filePath, sep='\t')

# 문자형 실수값을 실수로 변환
# print(chipo['item_price'].apply(lambda x: float(x[1:])))
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
print(chipo['item_price'].head())

# 주문당 평균 금액
total_orderid_mean = chipo.groupby('order_id')['item_price'].sum()
print(total_orderid_mean)
# 기술통계량
print(total_orderid_mean.describe())

# 한주문에 10달러 이상 사용한 아이디를 출력
# print(chipo.info())
orderid_sum = chipo.groupby('order_id').sum()

# result = orderid_sum[orderid_sum['item_price'] >= 10]
result = orderid_sum[orderid_sum.item_price >= 10]
print(result.head())
print(result.index.values)

# 각 아이템의 가격  quantity 가 1일때의 row을 출력
print("--------------------------------")
print(chipo.head())

chipo_one_item = chipo[chipo['quantity'] == 1]
