import pandas as pd
import numpy as np
filePath = './data/chipotle.tsv'
chipo = pd.read_csv(filePath, sep='\t')

# DataFrame 복사
chipCopy = chipo.copy()

print(chipCopy.head())
# item_price 컬럼의 모든 값
# print(chipCopy['item_price'])
# item_price 컬럼의 첫번째 값
# print(chipCopy['item_price'][0])

# 값을 변경
# chipCopy['item_price'][0] = '$5.39'
# print(chipCopy.loc[0]['item_price'])
# print(chipCopy.loc[0, 'item_price'])
chipCopy.loc[0, 'item_price'] = '$5.39'
print(chipCopy.loc[0, 'item_price'])
print(chipo.loc[0, 'item_price'])

print(chipCopy['item_name'].head())

# item_name이  Chicken Bowl인 row들을 출력
print(chipCopy[chipCopy['item_name'] == 'Chicken Bowl'])
selectChickenBowl = chipCopy[chipCopy['item_name'] == 'Chicken Bowl']
print(selectChickenBowl[['order_id', 'quantity', 'item_name', 'item_price']])





# print(chipo['item_price'])
# print(chipo['item_price'].str.findall('\d*\.?\d+'))
# chipo['int_item_price'] = chipo['item_price'].str.findall('\d*\.?\d+')
# chipCopy = chipo.copy()
#
# data = chipCopy[chipCopy['item_name'] == 'Chicken Bowl']
#
# print(data[['item_name','item_price']])

