# http://asq.kr/xgjDn
import re
from urllib import request
url = "http://asq.kr/xgjDn"
html = request.urlopen(url)
html_contents = str(html.read())
#print(html.read())
id_results = re.findall(r"[A-Za-z0-9]+\*\*\*", html_contents)
for i in id_results:
    print(i)
