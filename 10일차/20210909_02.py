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
# 동일 아이템이 여러개 있으므로 groupby로 묶어준다.
chipo_per_item = chipo_one_item.groupby('item_name').min()
chipo_per_item_sort_descend = chipo_per_item.sort_values(by='item_price', ascending=False)
print(chipo_per_item_sort_descend.head())

# 시각화
item_name_list = chipo_per_item.index.tolist()
x_pos = np.arange(len(item_name_list))
item_prices = chipo_per_item['item_price'].tolist()

import matplotlib.pyplot as plt
plt.bar(x_pos, item_prices)
plt.show()

plt.hist(item_prices)
plt.show()

# 주문들 중에서 가장 비싼 주문이 top 5
# 주문을 기준으로 gropuby sum
print("---------- 가장 비싼 주문 top 5-----------")
expensive_top5 = chipo.groupby('order_id').sum().sort_values(by = 'item_price', ascending=False)[:5]
print(expensive_top5)


# 아이템중에 한가지 선택해서 그 아이템이 몇번 주문되었는지  Barbacoa Bowl
print("아이템 리스트")
# Barbacoa Bowl 이 아이템을 구매한 row을 골라낸다
bb = chipo[chipo['item_name'] == 'Barbacoa Bowl']
# bb를 order id 순으로 정렬
bb = bb.sort_values(by='order_id')
print(bb[['order_id', 'item_name']])
# orderid 기준으로 groupby 하고 count해서 결과를 보자
# 1. groupby 를 이용하는 것과
print(bb.groupby('order_id').count())
# 2. 중복을 제거하는 함수가 있다.
print(bb.drop_duplicates(['order_id', 'item_name']))

#
