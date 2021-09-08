import pandas as pd
import numpy as np
df = pd.read_csv("./data/ch2_scores_em.csv", index_col = 'student number')
# print(df)

print(df['english'])
df_english = df['english']
# 기술통계량
print(df_english.describe())
print("irq", 65.000000 - 54.000000)

q1 = np.percentile(df_english, 25)
q3 = np.percentile(df_english, 75)
irq = q3 - q1
print("irq", irq)

print(df_english.head())

scores = np.array(df['english'])[:10]
print(scores)

