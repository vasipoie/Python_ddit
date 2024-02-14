import requests
from bs4 import BeautifulSoup as bs
# from day15.lite_naver import LiteNaver

# ln = LiteNaver()

file = open('dummy.xml', "r") #xml 파일을 읽어서
Soup = bs(file, "lxml") #BeautifulSoup을 생성할 때 전달한다.

names_list = Soup.find_all("item") # bs 객체를 통해 찾고 싶은 Tag를 전부 찾을 수 있다.
for name in names_list: # 메뉴명을 하나씩 출력한다
    print(name)


# for idx, p in enumerate(trs):
#     if(idx == 0):
#         continue
#     title = p.select("td")[0].text
#
#     print(title)
    
    # link = p.select("td")[1].text
    # description = p.select("td")[2].text
    # bloggername = p.select("td")[3].text
    # bloggerlink= p.select("td")[3].text
    # postdate = p.select("td")[3].text
    
    
    # cnt = ln.insert(title, link, description, bloggername, bloggerlink, postdate)
    # print(cnt)
    # print(idx, title, link, description, bloggername, bloggerlink, postdate)

