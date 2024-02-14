import requests
from bs4 import BeautifulSoup as bs
from day14.lite_emp import LiteEmp

le = LiteEmp()

resp = requests.get("http://127.0.0.1:5000/")

soup = bs(resp.text, "html.parser")

table = soup.select('table')[0]

trs = table.select('tr')


for idx, p in enumerate(trs):
    if(idx == 0):
        continue
    e_id = p.select("td")[0].text
    e_name = p.select("td")[1].text
    gen = p.select("td")[2].text
    addr = p.select("td")[3].text
    
    
    cnt = le.insert(e_id, e_name, gen, addr)
    print(idx, e_id,e_name,gen,addr)

