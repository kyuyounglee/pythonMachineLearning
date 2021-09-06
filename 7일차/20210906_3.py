#import urllib.request as re
from urllib import request
import re

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

result = re.findall("(\<dl class=\"bind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)


