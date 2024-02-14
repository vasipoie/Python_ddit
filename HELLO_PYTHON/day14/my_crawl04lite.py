import requests
from bs4 import BeautifulSoup as bs
from day14.lite_emp import LiteEmp

le = LiteEmp()

resp = requests.get("http://127.0.0.1:5000/")

soup = bs(resp.text, "html.parser")

table = soup.find_all('table')
trs = table[0].find_all('tr')
print(trs)

print("-----------------------")

for idx, p in enumerate(trs):
    if(idx == 0):
        continue
    tds = p.find_all('td')
    e_id = tds[0].text
    e_name = tds[1].text
    gen = tds[2].text
    addr = tds[3].text
    
    cnt = le.insert(e_id, e_name, gen, addr)
    print(e_id,e_name,gen,addr)