from bs4 import BeautifulSoup
from urllib import request

url = "https://news.daum.net/ranking/popular"
target = request.urlopen(url)
soup = BeautifulSoup(target, "html.parser")
print(soup.title.string)
news = soup.select('div > strong > a')
rank = 1

for article in news:
    print("[{0:2d}]{1}".format(rank,article.get_text()))
    rank += 1
