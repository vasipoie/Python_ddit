# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs
from day15.lite_naver import LiteNaver

ln = LiteNaver()

client_id = "z2V_KnAXM8iDmqVpXzRc"
client_secret = "RsrhWeNNqs"
encText = urllib.parse.quote("오류동")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    soup = bs(response_body.decode('utf-8'), "xml")
    
    items = soup.select("item")
    
    for idx, i in enumerate(items):
        title = i.select_one('title').text
        link = i.select_one('link').text
        description = i.select_one('description').text
        bloggername = i.select_one('bloggername').text
        bloggerlink = i.select_one('bloggerlink').text
        postdate = i.select_one('postdate').text
        
        cnt = ln.insert(title, link, description, bloggername, bloggerlink, postdate)
        print(idx)
        print(title)
        print(link)
        print(description)
        print(bloggername)
        print(bloggerlink)
        print(postdate)
        print("")
    
    