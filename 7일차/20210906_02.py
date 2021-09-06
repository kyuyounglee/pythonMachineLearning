from urllib import request
import re

url = "https://c11.kr/rxy1"
html = request.urlopen(url)
html_contents = str(html.read().decode("utf8"))
url_list = re.findall(r"(http)(.+)(zip)", html_contents)

# 이중에 10개만 가져와 봅시다
full_url = "".join(url_list[0])
list_a = full_url.split("/")
print(list_a[-1])

for i in range(0, 10):
    try:
        full_url = "".join(url_list[i])
        request.urlretrieve(full_url, full_url.split("/")[-1])
    except Exception as e:
        print(e)
    finally:
        print(full_url.split("/")[-1])




