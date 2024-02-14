import requests
from bs4 import BeautifulSoup as bs
import datetime


now = datetime.datetime.now()

resp = requests.get("https://map.kakao.com/")

soup = bs(resp.text, "html.parser")
print(soup)

# lis = soup.select('li .row_sty')
# print(lis)

# for idx, li in enumerate(lis):
#     # print(idx, li)
#
#     # print(idx, li.select('div.st_name')[0].text.strip())
#     s_name = li.select('div.st_name')[0].text.strip()
#
#     # print(idx, li.select('a')[0]['href'].split('/')[3])
#     s_id = li.select('a')[0]['href'].split('/')[3]
#
#     # print(idx, li.select('div.st_price')[0].text.strip())
#     # print(idx, li.select('span.price')[0].text)
#     price = li.select('div.st_price')[0].text.strip()
#
#     print(idx, s_name, s_id, price, ymd)
#
#
#     cnt = ls.insert(s_id, s_name, price, ymd)
#     print("cnt", cnt)

# name = soup.select('li div span a')
# print(name)
#
# href = name.split('">')
# print(href)