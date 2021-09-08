from bs4 import BeautifulSoup
from urllib import request

url = "https://www.cgv.co.kr/movies/"
target = request.urlopen(url)
soup = BeautifulSoup(target, "html.parser")
print(soup.title.string)
news = soup.select('ol > li > div > a > strong.title')
rank = 1

for article in news:
    print("[{0:2d}]{1}".format(rank, article.get_text()))
    rank += 1


import sys
print(sys.executable)