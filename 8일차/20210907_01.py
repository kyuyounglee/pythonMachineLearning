import csv
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# f = None
# try:
#     f = open("d:/한국도로공사_교통사고통계_20201231.csv")
# except Exception as e:
#     print(e)
# finally:
#     if f:
#         f.close()

with open("d:/한국도로공사_교통사고통계_20201231.csv") as f:
    data = csv.reader(f)
    next(data)
    x = []
    y = []
    for row in data:
        x.append(row[0])
        y.append(int(row[1]))

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(12,5), facecolor='lightyellow')
plt.bar(x, y, color = "darkgreen")
plt.show()







