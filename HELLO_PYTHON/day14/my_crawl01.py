# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://127.0.0.1:5000/")
#
# bsObject = BeautifulSoup(html, "html.parser")
#
#
# print(bsObject)

import requests
from bs4 import BeautifulSoup as bs

resp = requests.get("http://127.0.0.1:5000/")
# print(resp.text)

soup = bs(resp.text, "html.parser")
# print(soup)

table = soup.select('table')[0]

trs = table.select('tr')

# print(trs)

for idx, p in enumerate(trs):
    # print(idx)
    if(idx == 0):
        continue
    # print(p.get_text())
    e_id = p.select("td")[0].text
    e_name = p.select("td")[1].text
    gen = p.select("td")[2].text
    addr = p.select("td")[3].text
    
    print(e_id,e_name,gen,addr)
    # print(e_name,end="\t")
    
    

